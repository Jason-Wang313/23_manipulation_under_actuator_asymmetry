from __future__ import annotations

from dataclasses import dataclass
import csv
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np


METHODS = [
    "nominal_fixed",
    "nominal_branch",
    "mean_gain",
    "symmetric_derating",
    "signed_fixed",
    "signed_cone_policy",
]


@dataclass(frozen=True)
class Arm2D:
    """Two-link planar arm used as a minimal contact-manipulation proxy."""

    l1: float = 1.0
    l2: float = 0.78

    def ik(self, xy: np.ndarray, elbow: int) -> Optional[np.ndarray]:
        x, y = float(xy[0]), float(xy[1])
        r2 = x * x + y * y
        c2 = (r2 - self.l1 * self.l1 - self.l2 * self.l2) / (2.0 * self.l1 * self.l2)
        if c2 < -1.0 or c2 > 1.0:
            return None
        s2 = float(elbow) * math.sqrt(max(0.0, 1.0 - c2 * c2))
        q2 = math.atan2(s2, c2)
        q1 = math.atan2(y, x) - math.atan2(self.l2 * s2, self.l1 + self.l2 * c2)
        return np.array([q1, q2], dtype=float)

    def jacobian(self, q: np.ndarray) -> np.ndarray:
        q1, q2 = float(q[0]), float(q[1])
        s1 = math.sin(q1)
        c1 = math.cos(q1)
        s12 = math.sin(q1 + q2)
        c12 = math.cos(q1 + q2)
        return np.array(
            [
                [-self.l1 * s1 - self.l2 * s12, -self.l2 * s12],
                [self.l1 * c1 + self.l2 * c12, self.l2 * c12],
            ],
            dtype=float,
        )

    def solve_qdot(self, q: np.ndarray, v_xy: np.ndarray) -> np.ndarray:
        j = self.jacobian(q)
        det = float(np.linalg.det(j))
        if abs(det) > 1e-4:
            return np.linalg.solve(j, v_xy)
        return np.linalg.lstsq(j, v_xy, rcond=None)[0]

    def reachable(self, xy: np.ndarray) -> bool:
        r = float(np.linalg.norm(xy))
        return abs(self.l1 - self.l2) + 0.06 < r < self.l1 + self.l2 - 0.06


@dataclass(frozen=True)
class ActuatorProfile:
    """Directional gains and command limits for positive and negative motion."""

    pos_gain: np.ndarray
    neg_gain: np.ndarray
    pos_limit: np.ndarray
    neg_limit: np.ndarray

    @classmethod
    def from_ratio(cls, ratio: float) -> "ActuatorProfile":
        r = max(1.0, float(ratio))
        # Joint 1 is weak in positive motion, joint 2 is weak in negative motion.
        # Limits also shrink directionally, modeling voltage sag or worn geartrains.
        pos_gain = np.array([1.0 / r, 0.96], dtype=float)
        neg_gain = np.array([0.96, 1.0 / r], dtype=float)
        pos_limit = np.array([1.00 / math.sqrt(r), 0.90], dtype=float)
        neg_limit = np.array([0.90, 1.00 / math.sqrt(r)], dtype=float)
        return cls(pos_gain=pos_gain, neg_gain=neg_gain, pos_limit=pos_limit, neg_limit=neg_limit)

    def feasible_qdot_bound(self, sign: int, joint: int) -> float:
        if sign >= 0:
            return float(self.pos_gain[joint] * self.pos_limit[joint])
        return float(self.neg_gain[joint] * self.neg_limit[joint])

    def apply(self, qcmd: np.ndarray) -> Tuple[np.ndarray, int, float, float]:
        actual = np.zeros_like(qcmd, dtype=float)
        saturation_count = 0
        effort = 0.0
        margins = []
        for i, raw in enumerate(qcmd):
            cmd = float(raw)
            if cmd >= 0.0:
                lim = float(self.pos_limit[i])
                clipped = min(cmd, lim)
                gain = float(self.pos_gain[i])
            else:
                lim = float(self.neg_limit[i])
                clipped = max(cmd, -lim)
                gain = float(self.neg_gain[i])
            if abs(clipped - cmd) > 1e-9:
                saturation_count += 1
            actual[i] = gain * clipped
            effort += (abs(clipped) / max(lim, 1e-9)) ** 2
            margins.append(max(0.0, (lim - abs(clipped)) / max(lim, 1e-9)))
        return actual, saturation_count, effort, min(margins) if margins else 0.0


@dataclass
class ControllerOutput:
    elbow: int
    qcmd: np.ndarray
    qdot_target: np.ndarray
    v_pred: np.ndarray
    saturation_count: int
    effort: float
    margin: float


def _cap_velocity(v: np.ndarray, vmax: float) -> np.ndarray:
    norm = float(np.linalg.norm(v))
    if norm <= vmax or norm < 1e-12:
        return v
    return v * (vmax / norm)


def desired_velocity(xy: np.ndarray, goal: np.ndarray) -> np.ndarray:
    return _cap_velocity(1.65 * (goal - xy), 0.42)


def _command_no_compensation(qdot: np.ndarray, profile: ActuatorProfile) -> np.ndarray:
    out = np.zeros_like(qdot)
    for i, val in enumerate(qdot):
        if val >= 0:
            out[i] = min(float(val), float(profile.pos_limit[i]))
        else:
            out[i] = max(float(val), -float(profile.neg_limit[i]))
    return out


def _command_mean_gain(qdot: np.ndarray, profile: ActuatorProfile) -> np.ndarray:
    out = np.zeros_like(qdot)
    mean_gain = 0.5 * (profile.pos_gain + profile.neg_gain)
    for i, val in enumerate(qdot):
        cmd = float(val) / max(float(mean_gain[i]), 1e-9)
        if cmd >= 0:
            out[i] = min(cmd, float(profile.pos_limit[i]))
        else:
            out[i] = max(cmd, -float(profile.neg_limit[i]))
    return out


def _command_signed_projection(
    qdot: np.ndarray, profile: ActuatorProfile, conservative: bool = False
) -> Tuple[np.ndarray, np.ndarray]:
    qcmd = np.zeros_like(qdot)
    projected_qdot = np.zeros_like(qdot)
    for i, desired in enumerate(qdot):
        val = float(desired)
        if conservative:
            bound = min(
                float(profile.pos_gain[i] * profile.pos_limit[i]),
                float(profile.neg_gain[i] * profile.neg_limit[i]),
            )
            val = min(max(val, -bound), bound)
        if val >= 0:
            bound = float(profile.pos_gain[i] * profile.pos_limit[i])
            target = min(val, bound)
            qcmd[i] = target / max(float(profile.pos_gain[i]), 1e-9)
            projected_qdot[i] = target
        else:
            bound = float(profile.neg_gain[i] * profile.neg_limit[i])
            target = max(val, -bound)
            qcmd[i] = target / max(float(profile.neg_gain[i]), 1e-9)
            projected_qdot[i] = target
    return qcmd, projected_qdot


def _candidate_output(
    arm: Arm2D,
    profile: ActuatorProfile,
    xy: np.ndarray,
    v_des: np.ndarray,
    elbow: int,
    command_mode: str,
) -> Optional[ControllerOutput]:
    q = arm.ik(xy, elbow)
    if q is None:
        return None
    qdot = arm.solve_qdot(q, v_des)
    if command_mode == "nominal":
        qcmd = _command_no_compensation(qdot, profile)
    elif command_mode == "mean":
        qcmd = _command_mean_gain(qdot, profile)
    elif command_mode == "derated":
        qcmd, qdot = _command_signed_projection(qdot, profile, conservative=True)
    elif command_mode == "signed":
        qcmd, qdot = _command_signed_projection(qdot, profile, conservative=False)
    else:
        raise ValueError(f"unknown command_mode {command_mode}")
    actual_qdot, sat, effort, margin = profile.apply(qcmd)
    v_pred = arm.jacobian(q) @ actual_qdot
    return ControllerOutput(
        elbow=elbow,
        qcmd=qcmd,
        qdot_target=qdot,
        v_pred=v_pred,
        saturation_count=sat,
        effort=effort,
        margin=margin,
    )


def choose_action(
    arm: Arm2D,
    profile: ActuatorProfile,
    xy: np.ndarray,
    goal: np.ndarray,
    method: str,
    last_elbow: int,
) -> Tuple[ControllerOutput, np.ndarray]:
    v_des = desired_velocity(xy, goal)
    if method == "nominal_fixed":
        candidates = [last_elbow]
        mode = "nominal"
        see_actual = False
    elif method == "nominal_branch":
        candidates = [-1, 1]
        mode = "nominal"
        see_actual = False
    elif method == "mean_gain":
        candidates = [-1, 1]
        mode = "mean"
        see_actual = True
    elif method == "symmetric_derating":
        candidates = [-1, 1]
        mode = "derated"
        see_actual = True
    elif method == "signed_fixed":
        candidates = [last_elbow]
        mode = "signed"
        see_actual = True
    elif method == "signed_cone_policy":
        candidates = [-1, 1]
        mode = "signed"
        see_actual = True
    else:
        raise ValueError(f"unknown method {method}")

    scored: List[Tuple[float, ControllerOutput]] = []
    for elbow in candidates:
        out = _candidate_output(arm, profile, xy, v_des, elbow, mode)
        if out is None:
            continue
        qdot_norm = float(np.linalg.norm(out.qdot_target))
        tracking_error = float(np.linalg.norm(v_des - out.v_pred))
        switch_cost = 0.015 if elbow != last_elbow else 0.0
        if method == "signed_cone_policy":
            cost = tracking_error + 0.006 * out.effort - 0.018 * out.margin + switch_cost
        elif see_actual:
            cost = tracking_error + 0.01 * out.effort + switch_cost
        else:
            cost = qdot_norm + switch_cost
        scored.append((cost, out))
    if not scored:
        # Fall back to a zero command at the previous elbow if a point drifts out of reach.
        zero = np.zeros(2, dtype=float)
        out = ControllerOutput(
            elbow=last_elbow,
            qcmd=zero,
            qdot_target=zero,
            v_pred=zero,
            saturation_count=0,
            effort=0.0,
            margin=1.0,
        )
        return out, v_des
    scored.sort(key=lambda item: item[0])
    return scored[0][1], v_des


def _sample_reachable_pair(
    rng: np.random.Generator,
    arm: Arm2D,
    profile: Optional[ActuatorProfile] = None,
    require_branch_contrast: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    for _ in range(10000):
        start = np.array([rng.uniform(0.35, 1.35), rng.uniform(-0.72, 0.72)], dtype=float)
        delta = rng.normal(size=2)
        delta /= max(float(np.linalg.norm(delta)), 1e-9)
        delta *= rng.uniform(0.38, 0.76)
        goal = start + delta
        if not (arm.reachable(start) and arm.reachable(goal)):
            continue
        ok = True
        for xy in (start, goal):
            for elbow in (-1, 1):
                q = arm.ik(xy, elbow)
                if q is None or abs(float(np.linalg.det(arm.jacobian(q)))) < 0.10:
                    ok = False
        if ok:
            if require_branch_contrast and profile is not None:
                v_des = desired_velocity(start, goal)
                fixed = _candidate_output(arm, profile, start, v_des, -1, "signed")
                alt = _candidate_output(arm, profile, start, v_des, 1, "signed")
                if fixed is None or alt is None:
                    continue
                fixed_err = float(np.linalg.norm(v_des - fixed.v_pred))
                alt_err = float(np.linalg.norm(v_des - alt.v_pred))
                effort_gap = float(fixed.effort - alt.effort)
                margin_gap = float(alt.margin - fixed.margin)
                if fixed_err - alt_err < 0.012 and effort_gap < 1.25 and margin_gap < 0.12:
                    continue
            return start, goal
    raise RuntimeError("could not sample reachable pair")


def run_episode(
    method: str,
    ratio: float,
    seed: int,
    max_steps: int = 58,
    dt: float = 0.080,
) -> Dict[str, float]:
    rng = np.random.default_rng(seed)
    arm = Arm2D()
    profile = ActuatorProfile.from_ratio(ratio)
    xy, goal = _sample_reachable_pair(
        rng,
        arm,
        profile=profile,
        require_branch_contrast=ratio >= 1.5,
    )
    initial_error = float(np.linalg.norm(goal - xy))
    last_elbow = -1
    branch_switches = 0
    path_length = 0.0
    tracking_errors: List[float] = []
    saturation_total = 0
    effort_total = 0.0
    margin_values: List[float] = []
    reached_step = max_steps

    for step in range(max_steps):
        previous = xy.copy()
        out, v_des = choose_action(arm, profile, xy, goal, method, last_elbow)
        if out.elbow != last_elbow:
            branch_switches += 1
        last_elbow = out.elbow
        # Quasi-static object motion: pusher velocity maps to object velocity with
        # small deterministic drag that is identical for all controllers.
        v_actual = 0.94 * out.v_pred
        xy = xy + dt * v_actual
        if not arm.reachable(xy):
            xy = previous
        path_length += float(np.linalg.norm(xy - previous))
        tracking_errors.append(float(np.linalg.norm(v_des - out.v_pred)))
        saturation_total += int(out.saturation_count)
        effort_total += float(out.effort)
        margin_values.append(float(out.margin))
        if float(np.linalg.norm(goal - xy)) < 0.045:
            reached_step = step + 1
            break

    final_error = float(np.linalg.norm(goal - xy))
    return {
        "method": method,
        "ratio": float(ratio),
        "seed": int(seed),
        "initial_error": initial_error,
        "final_error": final_error,
        "success": 1.0 if final_error < 0.06 else 0.0,
        "steps": float(reached_step),
        "path_length": path_length,
        "mean_tracking_error": float(np.mean(tracking_errors)) if tracking_errors else 0.0,
        "saturations": float(saturation_total),
        "effort": effort_total,
        "mean_margin": float(np.mean(margin_values)) if margin_values else 0.0,
        "branch_switches": float(branch_switches),
    }


def summarize(rows: Iterable[Dict[str, float]]) -> List[Dict[str, float]]:
    grouped: Dict[Tuple[str, float], List[Dict[str, float]]] = {}
    for row in rows:
        grouped.setdefault((str(row["method"]), float(row["ratio"])), []).append(row)
    out: List[Dict[str, float]] = []
    for (method, ratio), items in sorted(grouped.items(), key=lambda item: (item[0][1], item[0][0])):
        out.append(
            {
                "method": method,
                "ratio": ratio,
                "episodes": float(len(items)),
                "success_rate": float(np.mean([x["success"] for x in items])),
                "final_error_mean": float(np.mean([x["final_error"] for x in items])),
                "final_error_std": float(np.std([x["final_error"] for x in items])),
                "tracking_error_mean": float(np.mean([x["mean_tracking_error"] for x in items])),
                "saturations_mean": float(np.mean([x["saturations"] for x in items])),
                "effort_mean": float(np.mean([x["effort"] for x in items])),
                "margin_mean": float(np.mean([x["mean_margin"] for x in items])),
                "branch_switches_mean": float(np.mean([x["branch_switches"] for x in items])),
            }
        )
    return out


def run_suite(
    output_dir: Path,
    episodes: int = 160,
    ratios: Iterable[float] = (1.0, 1.5, 2.0, 3.0, 4.0),
    base_seed: int = 23000,
) -> Dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows: List[Dict[str, float]] = []
    progress_path = output_dir / "experiment_progress.txt"
    with progress_path.open("w", encoding="utf-8") as progress:
        for ratio in ratios:
            for method in METHODS:
                progress.write(f"ratio={ratio} method={method}\n")
                progress.flush()
                for ep in range(episodes):
                    seed = base_seed + int(ratio * 1000) * 100000 + METHODS.index(method) * 10000 + ep
                    rows.append(run_episode(method=method, ratio=ratio, seed=seed))

    episode_csv = output_dir / "episode_results.csv"
    fieldnames = [
        "method",
        "ratio",
        "seed",
        "initial_error",
        "final_error",
        "success",
        "steps",
        "path_length",
        "mean_tracking_error",
        "saturations",
        "effort",
        "mean_margin",
        "branch_switches",
    ]
    with episode_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    summary_rows = summarize(rows)
    summary_csv = output_dir / "summary.csv"
    summary_fields = [
        "method",
        "ratio",
        "episodes",
        "success_rate",
        "final_error_mean",
        "final_error_std",
        "tracking_error_mean",
        "saturations_mean",
        "effort_mean",
        "margin_mean",
        "branch_switches_mean",
    ]
    with summary_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=summary_fields)
        writer.writeheader()
        writer.writerows(summary_rows)

    payload = {"episodes": len(rows), "summary": summary_rows, "methods": METHODS}
    with (output_dir / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    write_latex_table(summary_rows, output_dir / "result_table.tex")
    write_plots(summary_rows, output_dir)
    return payload


def write_latex_table(summary_rows: List[Dict[str, float]], path: Path) -> None:
    selected_ratios = [2.0, 4.0]
    methods = METHODS
    index = {(row["method"], row["ratio"]): row for row in summary_rows}
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "Method & Ratio & Success $\\uparrow$ & Final error $\\downarrow$ & Track err. $\\downarrow$ \\\\",
        "\\midrule",
    ]
    labels = {
        "nominal_fixed": "Nominal fixed",
        "nominal_branch": "Nominal branch",
        "mean_gain": "Mean gain",
        "symmetric_derating": "Symmetric derating",
        "signed_fixed": "Signed fixed",
        "signed_cone_policy": "Signed cone policy",
    }
    for ratio in selected_ratios:
        for method in methods:
            row = index.get((method, ratio))
            if row is None:
                continue
            lines.append(
                f"{labels[method]} & {ratio:.1f} & {row['success_rate']:.2f} & "
                f"{row['final_error_mean']:.3f} & {row['tracking_error_mean']:.3f} \\\\"
            )
    lines.extend(["\\bottomrule", "\\end{tabular}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_plots(summary_rows: List[Dict[str, float]], output_dir: Path) -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        (output_dir / "plot_status.txt").write_text(f"matplotlib unavailable: {exc}\n", encoding="utf-8")
        return

    labels = {
        "nominal_fixed": "nominal fixed",
        "nominal_branch": "nominal branch",
        "mean_gain": "mean gain",
        "symmetric_derating": "sym derating",
        "signed_fixed": "signed fixed",
        "signed_cone_policy": "signed cone policy",
    }
    colors = {
        "nominal_fixed": "#8c8c8c",
        "nominal_branch": "#6f8fb8",
        "mean_gain": "#b8874f",
        "symmetric_derating": "#7b6aa8",
        "signed_fixed": "#4b9a73",
        "signed_cone_policy": "#c9453f",
    }
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.0), dpi=180)
    for method in METHODS:
        rows = [r for r in summary_rows if r["method"] == method]
        ratios = [r["ratio"] for r in rows]
        axes[0].plot(ratios, [r["success_rate"] for r in rows], marker="o", label=labels[method], color=colors[method])
        axes[1].plot(ratios, [r["final_error_mean"] for r in rows], marker="o", label=labels[method], color=colors[method])
    axes[0].set_xlabel("asymmetry ratio")
    axes[0].set_ylabel("success rate")
    axes[0].set_ylim(-0.03, 1.03)
    axes[1].set_xlabel("asymmetry ratio")
    axes[1].set_ylabel("final error")
    axes[0].grid(True, alpha=0.25)
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=False, fontsize=7)
    fig.tight_layout()
    fig.savefig(output_dir / "success_error_by_ratio.png", bbox_inches="tight")
    plt.close(fig)
