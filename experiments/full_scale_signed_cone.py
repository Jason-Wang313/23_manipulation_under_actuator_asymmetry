from __future__ import annotations

import csv
import json
import math
import sys
import time
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterable

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from asym_manip.simulator import (  # noqa: E402
    ActuatorProfile,
    Arm2D,
    ControllerOutput,
    _candidate_output,
    desired_velocity,
)


RESULTS = ROOT / "results" / "full_scale"
FIGURES = ROOT / "figures" / "full_scale"
TEX = RESULTS / "tex"
DOCS = ROOT / "docs"
SEED = 23023

METHODS = [
    "nominal_fixed",
    "nominal_branch",
    "mean_gain",
    "symmetric_derating",
    "signed_fixed",
    "scmp_true",
    "scmp_estimated",
    "adaptive_scmp",
    "guarded_scmp",
    "robust_scmp",
    "oracle_one_step",
    "random_branch",
]

CORE_METHODS = [
    "nominal_branch",
    "mean_gain",
    "symmetric_derating",
    "signed_fixed",
    "scmp_true",
    "scmp_estimated",
    "adaptive_scmp",
    "guarded_scmp",
    "robust_scmp",
    "oracle_one_step",
]


def ensure_dirs() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    TEX.mkdir(parents=True, exist_ok=True)


def sf(x: Any, default: float = 0.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def latex_escape(x: Any) -> str:
    return str(x).replace("_", r"\_").replace("%", r"\%")


def ci95(values: list[float]) -> float:
    if not values:
        return 0.0
    p = float(np.mean(values))
    n = len(values)
    return 1.96 * math.sqrt(max(p * (1.0 - p), 0.0) / max(n, 1))


def make_profile(kind: str, ratio: float, weakness: str = "opposed") -> ActuatorProfile:
    r = max(1.0, float(ratio))
    if kind == "baseline":
        return ActuatorProfile.from_ratio(r)

    pos_gain = np.array([1.0, 1.0], dtype=float)
    neg_gain = np.array([1.0, 1.0], dtype=float)
    pos_limit = np.array([1.0, 1.0], dtype=float)
    neg_limit = np.array([1.0, 1.0], dtype=float)

    if weakness == "opposed":
        weak = [("pos", 0), ("neg", 1)]
    elif weakness == "flipped":
        weak = [("neg", 0), ("pos", 1)]
    elif weakness == "same_positive":
        weak = [("pos", 0), ("pos", 1)]
    elif weakness == "same_negative":
        weak = [("neg", 0), ("neg", 1)]
    else:
        weak = [("pos", 0), ("neg", 1)]

    if kind in {"gain_only", "gain_limit", "deadband_like"}:
        for sign, joint in weak:
            if sign == "pos":
                pos_gain[joint] = 1.0 / r
            else:
                neg_gain[joint] = 1.0 / r
    if kind in {"limit_only", "gain_limit", "deadband_like"}:
        for sign, joint in weak:
            if sign == "pos":
                pos_limit[joint] = 1.0 / math.sqrt(r)
            else:
                neg_limit[joint] = 1.0 / math.sqrt(r)
    if kind == "random_mixed":
        pos_gain = np.array([1.0 / math.sqrt(r), 0.92], dtype=float)
        neg_gain = np.array([0.88, 1.0 / r], dtype=float)
        pos_limit = np.array([0.85, 1.0 / math.sqrt(r)], dtype=float)
        neg_limit = np.array([1.0 / math.sqrt(r), 0.88], dtype=float)
    if kind == "symmetric":
        return ActuatorProfile.from_ratio(1.0)
    if kind == "deadband_like":
        pos_gain *= 0.92
        neg_gain *= 0.92
        pos_limit *= 0.92
        neg_limit *= 0.92
    return ActuatorProfile(pos_gain=pos_gain, neg_gain=neg_gain, pos_limit=pos_limit, neg_limit=neg_limit)


def scale_profile(profile: ActuatorProfile, gain_scale: float = 0.90, limit_scale: float = 0.92) -> ActuatorProfile:
    return ActuatorProfile(
        pos_gain=np.maximum(0.05, profile.pos_gain * gain_scale),
        neg_gain=np.maximum(0.05, profile.neg_gain * gain_scale),
        pos_limit=np.maximum(0.05, profile.pos_limit * limit_scale),
        neg_limit=np.maximum(0.05, profile.neg_limit * limit_scale),
    )


def estimate_ratio(true_ratio: float, budget: int, bias: str, rng: np.random.Generator) -> float:
    if budget <= 0:
        estimate = 1.0
    else:
        sigma = 1.10 / math.sqrt(float(budget))
        estimate = true_ratio + float(rng.normal(0.0, sigma))
    if bias == "underestimate":
        estimate = 1.0 + 0.68 * (estimate - 1.0)
    elif bias == "overestimate":
        estimate = 1.0 + 1.25 * (estimate - 1.0)
    elif bias == "assume_symmetry":
        estimate = 1.0
    return float(min(max(estimate, 1.0), 5.5))


def task_pair(
    rng: np.random.Generator,
    arm: Arm2D,
    profile: ActuatorProfile,
    task: str,
    ratio: float,
) -> tuple[np.ndarray, np.ndarray]:
    require_branch_contrast = task in {"high_branch_contrast", "corner_approach"} or ratio >= 3.0
    for _ in range(20_000):
        if task == "lateral_carry":
            start = np.array([rng.uniform(0.45, 1.30), rng.uniform(-0.62, 0.62)], dtype=float)
            delta = np.array([rng.choice([-1.0, 1.0]) * rng.uniform(0.45, 0.76), rng.normal(0.0, 0.12)])
        elif task == "corner_approach":
            start = np.array([rng.uniform(0.42, 0.78), rng.choice([-1.0, 1.0]) * rng.uniform(0.45, 0.72)])
            goal = np.array([rng.uniform(1.05, 1.45), -np.sign(start[1]) * rng.uniform(0.25, 0.65)])
            delta = goal - start
        elif task == "near_singular":
            angle = rng.uniform(-0.70, 0.70)
            radius = rng.uniform(1.35, 1.66)
            start = np.array([radius * math.cos(angle), radius * math.sin(angle)], dtype=float)
            delta = rng.normal(size=2)
            delta /= max(float(np.linalg.norm(delta)), 1e-9)
            delta *= rng.uniform(0.28, 0.50)
        elif task == "low_branch_contrast":
            start = np.array([rng.uniform(0.55, 1.25), rng.uniform(-0.30, 0.30)], dtype=float)
            delta = np.array([rng.uniform(-0.40, 0.40), rng.uniform(-0.20, 0.20)], dtype=float)
            if float(np.linalg.norm(delta)) < 0.20:
                delta[0] += 0.25
        else:
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
                if q is None or abs(float(np.linalg.det(arm.jacobian(q)))) < 0.07:
                    ok = False
        if not ok:
            continue
        if require_branch_contrast:
            v_des = desired_velocity(start, goal)
            fixed = _candidate_output(arm, profile, start, v_des, -1, "signed")
            alt = _candidate_output(arm, profile, start, v_des, 1, "signed")
            if fixed is None or alt is None:
                continue
            fixed_err = float(np.linalg.norm(v_des - fixed.v_pred))
            alt_err = float(np.linalg.norm(v_des - alt.v_pred))
            effort_gap = abs(float(fixed.effort - alt.effort))
            margin_gap = abs(float(alt.margin - fixed.margin))
            if max(fixed_err, alt_err) - min(fixed_err, alt_err) < 0.008 and effort_gap < 0.80 and margin_gap < 0.08:
                continue
        return start, goal
    raise RuntimeError(f"could not sample task pair for {task}")


def score_candidates(
    method: str,
    candidates: list[ControllerOutput],
    v_des: np.ndarray,
    last_elbow: int,
    rng: np.random.Generator,
) -> ControllerOutput:
    if method == "random_branch":
        return candidates[int(rng.integers(0, len(candidates)))]
    scored: list[tuple[float, ControllerOutput]] = []
    for out in candidates:
        tracking = float(np.linalg.norm(v_des - out.v_pred))
        qdot_norm = float(np.linalg.norm(out.qdot_target))
        switch_cost = 0.015 if out.elbow != last_elbow else 0.0
        if method in {"nominal_fixed", "nominal_branch"}:
            cost = qdot_norm + switch_cost
        elif method == "oracle_one_step":
            cost = tracking
        elif method == "scmp_no_margin":
            cost = tracking + 0.006 * out.effort + switch_cost
        elif method == "scmp_no_effort":
            cost = tracking - 0.018 * out.margin + switch_cost
        elif method == "scmp_no_switch":
            cost = tracking + 0.006 * out.effort - 0.018 * out.margin
        elif method == "scmp_error_only":
            cost = tracking
        elif method == "symmetric_switch":
            cost = tracking + 0.010 * out.effort + switch_cost
        elif method in {"scmp_true", "scmp_estimated", "adaptive_scmp", "guarded_scmp", "robust_scmp"}:
            cost = tracking + 0.006 * out.effort - 0.018 * out.margin + switch_cost
        else:
            cost = tracking + 0.010 * out.effort + switch_cost
        scored.append((cost, out))
    scored.sort(key=lambda item: item[0])
    return scored[0][1]


def choose_extended(
    arm: Arm2D,
    method: str,
    true_profile: ActuatorProfile,
    planning_profile: ActuatorProfile,
    xy: np.ndarray,
    goal: np.ndarray,
    last_elbow: int,
    rng: np.random.Generator,
    confidence: float,
) -> tuple[ControllerOutput, np.ndarray, str]:
    v_des = desired_velocity(xy, goal)
    method_used = method
    if method in {"nominal_fixed", "signed_fixed"}:
        elbows = [last_elbow]
    else:
        elbows = [-1, 1]

    profile = planning_profile
    command_mode = "signed"
    if method in {"nominal_fixed", "nominal_branch", "random_branch"}:
        command_mode = "nominal"
    elif method == "mean_gain":
        command_mode = "mean"
    elif method == "symmetric_derating" or method == "symmetric_switch":
        command_mode = "derated"
    elif method == "oracle_one_step":
        profile = true_profile
    elif method == "scmp_true":
        profile = true_profile
    elif method == "guarded_scmp" and confidence < 0.55:
        command_mode = "derated"
        method_used = "guarded_fallback"
    elif method == "robust_scmp":
        profile = scale_profile(planning_profile)

    candidates: list[ControllerOutput] = []
    for elbow in elbows:
        out = _candidate_output(arm, profile, xy, v_des, elbow, command_mode)
        if out is not None:
            candidates.append(out)
    if not candidates:
        zero = np.zeros(2, dtype=float)
        return (
            ControllerOutput(
                elbow=last_elbow,
                qcmd=zero,
                qdot_target=zero,
                v_pred=zero,
                saturation_count=0,
                effort=0.0,
                margin=1.0,
            ),
            v_des,
            method_used,
        )
    return score_candidates(method if method != "guarded_scmp" else method_used, candidates, v_des, last_elbow, rng), v_des, method_used


def drift_ratio(mode: str, base_ratio: float, step: int, max_steps: int) -> tuple[float, str]:
    frac = step / max(max_steps - 1, 1)
    if mode == "none":
        return base_ratio, "opposed"
    if mode == "slow_loss":
        return 1.5 + 3.5 * frac, "opposed"
    if mode == "sudden_fault":
        return (1.5 if step < max_steps // 3 else 5.0), "opposed"
    if mode == "thermal_recovery":
        return 5.0 - 3.2 * frac, "opposed"
    if mode == "sign_flip":
        return base_ratio, ("opposed" if step < max_steps // 2 else "flipped")
    return base_ratio, "opposed"


def run_episode(
    *,
    method: str,
    case_id: int,
    seed: int,
    ratio: float = 4.0,
    estimated_ratio: float | None = None,
    profile_kind: str = "baseline",
    weakness: str = "opposed",
    estimated_weakness: str | None = None,
    task_family: str = "high_branch_contrast",
    noise_level: float = 0.0,
    drift_mode: str = "none",
    confidence: float = 1.0,
    max_steps: int = 58,
    dt: float = 0.080,
) -> dict[str, Any]:
    rng = np.random.default_rng(seed)
    arm = Arm2D()
    true_profile_initial = make_profile(profile_kind, ratio, weakness)
    estimated_profile = make_profile(profile_kind, estimated_ratio if estimated_ratio is not None else ratio, estimated_weakness or weakness)
    xy, goal = task_pair(rng, arm, true_profile_initial, task_family, ratio)
    initial_error = float(np.linalg.norm(goal - xy))
    last_elbow = -1
    path_length = 0.0
    tracking_errors: list[float] = []
    saturation_total = 0
    effort_total = 0.0
    margins: list[float] = []
    branch_switches = 0
    method_used_counts: dict[str, int] = {}
    reached_step = max_steps

    for step in range(max_steps):
        true_ratio, true_weakness = drift_ratio(drift_mode, ratio, step, max_steps)
        true_profile = make_profile(profile_kind, true_ratio, true_weakness)
        if method == "adaptive_scmp" and drift_mode != "none":
            lag = 0.75 * (estimated_ratio if estimated_ratio is not None else ratio) + 0.25 * true_ratio
            planning_profile = make_profile(profile_kind, lag, true_weakness)
        else:
            planning_profile = estimated_profile
        observed_xy = xy + rng.normal(0.0, noise_level * 0.012, size=2)
        previous = xy.copy()
        out, v_des, used = choose_extended(arm, method, true_profile, planning_profile, observed_xy, goal, last_elbow, rng, confidence)
        method_used_counts[used] = method_used_counts.get(used, 0) + 1
        if out.elbow != last_elbow:
            branch_switches += 1
        last_elbow = out.elbow
        q_actual = arm.ik(xy, out.elbow)
        if q_actual is None:
            true_v_pred = np.zeros(2, dtype=float)
            sat = 0
            effort = 0.0
            margin = 0.0
        else:
            qcmd = out.qcmd.copy()
            if noise_level > 0:
                qcmd = qcmd + rng.normal(0.0, noise_level * 0.020, size=qcmd.shape)
            true_qdot, sat, effort, margin = true_profile.apply(qcmd)
            true_v_pred = arm.jacobian(q_actual) @ true_qdot
        disturbance = rng.normal(0.0, noise_level * 0.010, size=2)
        v_actual = 0.94 * true_v_pred + disturbance
        xy = xy + dt * v_actual
        if not arm.reachable(xy):
            xy = previous
        path_length += float(np.linalg.norm(xy - previous))
        tracking_errors.append(float(np.linalg.norm(v_des - true_v_pred)))
        saturation_total += int(sat)
        effort_total += float(effort)
        margins.append(float(margin))
        if float(np.linalg.norm(goal - xy)) < 0.045:
            reached_step = step + 1
            break

    final_error = float(np.linalg.norm(goal - xy))
    return {
        "case_id": case_id,
        "method": method,
        "method_used_mode": max(method_used_counts, key=method_used_counts.get) if method_used_counts else method,
        "ratio": float(ratio),
        "estimated_ratio": float(estimated_ratio if estimated_ratio is not None else ratio),
        "profile_kind": profile_kind,
        "weakness": weakness,
        "estimated_weakness": estimated_weakness or weakness,
        "task_family": task_family,
        "noise_level": float(noise_level),
        "drift_mode": drift_mode,
        "confidence": float(confidence),
        "seed": int(seed),
        "initial_error": initial_error,
        "final_error": final_error,
        "success": 1.0 if final_error < 0.06 else 0.0,
        "steps": float(reached_step),
        "path_length": path_length,
        "mean_tracking_error": float(np.mean(tracking_errors)) if tracking_errors else 0.0,
        "saturations": float(saturation_total),
        "effort": float(effort_total),
        "mean_margin": float(np.mean(margins)) if margins else 0.0,
        "branch_switches": float(branch_switches),
        "regret_error": 0.0,
    }


def add_oracle_regret(rows: list[dict[str, Any]]) -> None:
    grouped: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in rows:
        key = (row["case_id"], row.get("condition", ""), row.get("family", ""))
        if row["method"] == "oracle_one_step":
            grouped[key] = row
    for row in rows:
        key = (row["case_id"], row.get("condition", ""), row.get("family", ""))
        oracle = grouped.get(key)
        if oracle is None:
            row["regret_error"] = 0.0
        else:
            row["regret_error"] = max(0.0, sf(row["final_error"]) - sf(oracle["final_error"]))


def write_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    keys = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows: list[dict[str, Any]], group_keys: list[str]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in rows:
        key = tuple(row.get(k, "") for k in group_keys)
        groups.setdefault(key, []).append(row)
    summaries: list[dict[str, Any]] = []
    for key, items in sorted(groups.items(), key=lambda kv: kv[0]):
        success_values = [sf(r["success"]) for r in items]
        out = {k: v for k, v in zip(group_keys, key)}
        out.update(
            {
                "n": len(items),
                "success_mean": float(np.mean(success_values)),
                "success_ci95": ci95(success_values),
                "final_error_mean": float(np.mean([sf(r["final_error"]) for r in items])),
                "tracking_error_mean": float(np.mean([sf(r["mean_tracking_error"]) for r in items])),
                "saturations_mean": float(np.mean([sf(r["saturations"]) for r in items])),
                "effort_mean": float(np.mean([sf(r["effort"]) for r in items])),
                "margin_mean": float(np.mean([sf(r["mean_margin"]) for r in items])),
                "branch_switches_mean": float(np.mean([sf(r["branch_switches"]) for r in items])),
                "regret_error_mean": float(np.mean([sf(r["regret_error"]) for r in items])),
            }
        )
        summaries.append(out)
    return summaries


def write_summary(name: str, rows: list[dict[str, Any]], group_keys: list[str]) -> Path:
    summary = summarize(rows, group_keys)
    path = RESULTS / f"{name}.csv"
    write_rows(path, summary)
    return path


def write_table(path: Path, caption: str, label: str, columns: list[tuple[str, str]], rows: list[dict[str, Any]], digits: int = 3) -> None:
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\small",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\begin{tabular}{" + "l" + "c" * (len(columns) - 1) + "}",
        r"\toprule",
        " & ".join(latex_escape(c[1]) for c in columns) + r" \\",
        r"\midrule",
    ]
    for row in rows:
        vals = []
        for key, _ in columns:
            val = row.get(key, "")
            if isinstance(val, (int, float)) or str(val).replace(".", "", 1).replace("-", "", 1).isdigit():
                vals.append(f"{sf(val):.{digits}f}")
            else:
                vals.append(latex_escape(val))
        lines.append(" & ".join(vals) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def rows_from_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def family_a() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    ratios = [1.0, 1.25, 1.5, 2.0, 3.0, 4.0, 5.0]
    tasks = ["reach_push", "lateral_carry", "corner_approach", "near_singular", "high_branch_contrast", "low_branch_contrast"]
    methods = METHODS
    rows: list[dict[str, Any]] = []
    case_id = 0
    for ratio in ratios:
        for task in tasks:
            condition = f"ratio_{ratio:.2f}_{task}"
            for case in range(80):
                base_seed = SEED + 10_000 + int(ratio * 1000) * 1000 + tasks.index(task) * 100 + case
                for method in methods:
                    row = run_episode(
                        method=method,
                        case_id=case_id,
                        seed=base_seed + methods.index(method) * 2_000_000,
                        ratio=ratio,
                        estimated_ratio=ratio,
                        profile_kind="baseline",
                        task_family=task,
                        confidence=1.0,
                    )
                    row.update({"family": "family_a", "condition": condition})
                    rows.append(row)
                case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_a_rows.csv", rows)
    write_summary("family_a_summary_by_method", rows, ["method"])
    write_summary("family_a_summary_by_ratio", rows, ["ratio", "method"])
    write_summary("family_a_summary_by_task", rows, ["task_family", "method"])
    return rows, {"family": "family_a", "rows": len(rows), "cases": case_id}


def family_b() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    profiles = [
        ("baseline", "opposed"),
        ("gain_only", "opposed"),
        ("limit_only", "opposed"),
        ("gain_limit", "opposed"),
        ("gain_limit", "flipped"),
        ("gain_limit", "same_positive"),
        ("deadband_like", "opposed"),
    ]
    methods = METHODS
    rows: list[dict[str, Any]] = []
    case_id = 0
    for profile_kind, weakness in profiles:
        condition = f"{profile_kind}_{weakness}"
        for case in range(90):
            base_seed = SEED + 20_000 + profiles.index((profile_kind, weakness)) * 1000 + case
            for method in methods:
                row = run_episode(
                    method=method,
                    case_id=case_id,
                    seed=base_seed + methods.index(method) * 2_000_000,
                    ratio=4.0,
                    estimated_ratio=4.0,
                    profile_kind=profile_kind,
                    weakness=weakness,
                    estimated_weakness=weakness,
                    task_family="high_branch_contrast",
                    confidence=1.0,
                )
                row.update({"family": "family_b", "condition": condition})
                rows.append(row)
            case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_b_rows.csv", rows)
    write_summary("family_b_summary_by_profile", rows, ["condition", "method"])
    write_summary("family_b_summary_by_method", rows, ["method"])
    return rows, {"family": "family_b", "rows": len(rows), "cases": case_id}


def family_c() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    budgets = [0, 4, 8, 16, 32, 64, 128, 256]
    biases = ["unbiased", "underestimate", "overestimate", "assume_symmetry"]
    methods = ["mean_gain", "symmetric_derating", "signed_fixed", "scmp_true", "scmp_estimated", "adaptive_scmp", "guarded_scmp", "robust_scmp"]
    rows: list[dict[str, Any]] = []
    case_id = 0
    for budget in budgets:
        for bias in biases:
            condition = f"budget_{budget}_{bias}"
            for case in range(50):
                rng = np.random.default_rng(SEED + 30_000 + budget * 1000 + biases.index(bias) * 100 + case)
                est_ratio = estimate_ratio(4.0, budget, bias, rng)
                confidence = min(1.0, math.sqrt(max(budget, 0)) / 8.0)
                for method in methods:
                    row = run_episode(
                        method=method,
                        case_id=case_id,
                        seed=int(rng.integers(1, 2_000_000_000)) + methods.index(method),
                        ratio=4.0,
                        estimated_ratio=est_ratio,
                        profile_kind="baseline",
                        task_family="high_branch_contrast",
                        confidence=confidence,
                    )
                    row.update({"family": "family_c", "condition": condition, "calibration_budget": budget, "calibration_bias": bias})
                    rows.append(row)
                case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_c_rows.csv", rows)
    write_summary("family_c_summary_by_budget", rows, ["calibration_budget", "method"])
    write_summary("family_c_summary_by_bias", rows, ["calibration_bias", "method"])
    return rows, {"family": "family_c", "rows": len(rows), "cases": case_id}


def family_d() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    drift_modes = ["none", "slow_loss", "sudden_fault", "thermal_recovery", "sign_flip"]
    methods = ["mean_gain", "symmetric_derating", "signed_fixed", "scmp_true", "scmp_estimated", "adaptive_scmp", "guarded_scmp", "robust_scmp"]
    rows: list[dict[str, Any]] = []
    case_id = 0
    for drift in drift_modes:
        for case in range(60):
            base_seed = SEED + 40_000 + drift_modes.index(drift) * 1000 + case
            for method in methods:
                row = run_episode(
                    method=method,
                    case_id=case_id,
                    seed=base_seed + methods.index(method) * 2_000_000,
                    ratio=4.0,
                    estimated_ratio=4.0,
                    profile_kind="baseline",
                    task_family="high_branch_contrast",
                    drift_mode=drift,
                    confidence=0.8,
                )
                row.update({"family": "family_d", "condition": drift})
                rows.append(row)
            case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_d_rows.csv", rows)
    write_summary("family_d_summary_by_drift", rows, ["drift_mode", "method"])
    return rows, {"family": "family_d", "rows": len(rows), "cases": case_id}


def family_e() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    noise_levels = [0.0, 0.25, 0.5, 0.75, 1.0]
    methods = ["mean_gain", "symmetric_derating", "signed_fixed", "scmp_true", "scmp_estimated", "adaptive_scmp", "guarded_scmp", "robust_scmp"]
    rows: list[dict[str, Any]] = []
    case_id = 0
    for noise in noise_levels:
        condition = f"noise_{noise:.2f}"
        for case in range(60):
            base_seed = SEED + 50_000 + int(noise * 1000) * 1000 + case
            for method in methods:
                row = run_episode(
                    method=method,
                    case_id=case_id,
                    seed=base_seed + methods.index(method) * 2_000_000,
                    ratio=4.0,
                    estimated_ratio=4.0,
                    profile_kind="baseline",
                    task_family="high_branch_contrast",
                    noise_level=noise,
                    confidence=0.8,
                )
                row.update({"family": "family_e", "condition": condition})
                rows.append(row)
            case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_e_rows.csv", rows)
    write_summary("family_e_summary_by_noise", rows, ["noise_level", "method"])
    return rows, {"family": "family_e", "rows": len(rows), "cases": case_id}


def family_f() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    methods = [
        "signed_fixed",
        "symmetric_switch",
        "scmp_true",
        "scmp_no_margin",
        "scmp_no_effort",
        "scmp_no_switch",
        "scmp_error_only",
        "oracle_one_step",
    ]
    rows: list[dict[str, Any]] = []
    case_id = 0
    for case in range(140):
        base_seed = SEED + 60_000 + case
        for method in methods:
            row = run_episode(
                method=method,
                case_id=case_id,
                seed=base_seed + methods.index(method) * 2_000_000,
                ratio=4.0,
                estimated_ratio=4.0,
                profile_kind="baseline",
                task_family="high_branch_contrast",
                confidence=1.0,
            )
            row.update({"family": "family_f", "condition": "ablation"})
            rows.append(row)
        case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_f_rows.csv", rows)
    write_summary("family_f_summary_by_ablation", rows, ["method"])
    return rows, {"family": "family_f", "rows": len(rows), "cases": case_id}


def family_g() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    controls = [
        ("symmetric_actuation", 1.0, "baseline", "opposed", "opposed", "high_branch_contrast"),
        ("no_branch_contrast", 4.0, "baseline", "opposed", "opposed", "low_branch_contrast"),
        ("shared_weak_positive", 4.0, "gain_limit", "same_positive", "same_positive", "high_branch_contrast"),
        ("wrong_sign_calibration", 4.0, "gain_limit", "opposed", "flipped", "high_branch_contrast"),
        ("near_singular", 4.0, "baseline", "opposed", "opposed", "near_singular"),
        ("random_label_control", 4.0, "baseline", "opposed", "opposed", "reach_push"),
    ]
    methods = ["nominal_branch", "mean_gain", "symmetric_derating", "signed_fixed", "scmp_true", "scmp_estimated", "guarded_scmp", "random_branch"]
    rows: list[dict[str, Any]] = []
    case_id = 0
    for control, ratio, profile_kind, weakness, est_weakness, task in controls:
        for case in range(60):
            base_seed = SEED + 70_000 + controls.index((control, ratio, profile_kind, weakness, est_weakness, task)) * 1000 + case
            for method in methods:
                row = run_episode(
                    method=method,
                    case_id=case_id,
                    seed=base_seed + methods.index(method) * 2_000_000,
                    ratio=ratio,
                    estimated_ratio=ratio,
                    profile_kind=profile_kind,
                    weakness=weakness,
                    estimated_weakness=est_weakness,
                    task_family=task,
                    confidence=0.4 if control == "wrong_sign_calibration" else 1.0,
                )
                row.update({"family": "family_g", "condition": control})
                rows.append(row)
            case_id += 1
    add_oracle_regret(rows)
    write_rows(RESULTS / "family_g_rows.csv", rows)
    write_summary("family_g_summary_by_control", rows, ["condition", "method"])
    return rows, {"family": "family_g", "rows": len(rows), "cases": case_id}


def make_tables() -> None:
    a = rows_from_csv(RESULTS / "family_a_summary_by_method.csv")
    keep_a = [r for r in a if r["method"] in {"nominal_branch", "mean_gain", "symmetric_derating", "signed_fixed", "scmp_true", "guarded_scmp", "oracle_one_step"}]
    keep_a.sort(key=lambda r: -sf(r["success_mean"]))
    write_table(
        TEX / "table_main_full_scale.tex",
        "Family A full-scale signed-actuator benchmark across ratios and task families.",
        "tab:main-full-scale",
        [("method", "Method"), ("success_mean", "Success"), ("final_error_mean", "Error"), ("saturations_mean", "Satur."), ("regret_error_mean", "Regret")],
        keep_a,
    )
    b = rows_from_csv(RESULTS / "family_b_summary_by_profile.csv")
    keep_b = [r for r in b if r["method"] in {"symmetric_derating", "signed_fixed", "scmp_true", "scmp_estimated", "oracle_one_step"}]
    write_table(
        TEX / "table_asymmetry_sources.tex",
        "Family B asymmetry-source sweep.",
        "tab:asymmetry-sources",
        [("condition", "Condition"), ("method", "Method"), ("success_mean", "Success"), ("final_error_mean", "Error"), ("margin_mean", "Margin")],
        keep_b,
    )
    c = rows_from_csv(RESULTS / "family_c_summary_by_budget.csv")
    keep_c = [r for r in c if r["method"] in {"scmp_estimated", "guarded_scmp", "robust_scmp", "symmetric_derating"}]
    write_table(
        TEX / "table_calibration_budget.tex",
        "Family C calibration-budget sweep aggregated over bias settings.",
        "tab:calibration-budget",
        [("calibration_budget", "Budget"), ("method", "Method"), ("success_mean", "Success"), ("final_error_mean", "Error"), ("tracking_error_mean", "Track")],
        keep_c,
    )
    d = rows_from_csv(RESULTS / "family_d_summary_by_drift.csv")
    keep_d = [r for r in d if r["method"] in {"scmp_true", "scmp_estimated", "adaptive_scmp", "guarded_scmp", "robust_scmp"}]
    write_table(
        TEX / "table_drift.tex",
        "Family D drift and online-identification stress.",
        "tab:drift",
        [("drift_mode", "Drift"), ("method", "Method"), ("success_mean", "Success"), ("saturations_mean", "Satur."), ("final_error_mean", "Error")],
        keep_d,
    )
    e = rows_from_csv(RESULTS / "family_e_summary_by_noise.csv")
    keep_e = [r for r in e if r["method"] in {"symmetric_derating", "scmp_true", "scmp_estimated", "guarded_scmp", "robust_scmp"}]
    write_table(
        TEX / "table_noise.tex",
        "Family E noise and disturbance sweep.",
        "tab:noise",
        [("noise_level", "Noise"), ("method", "Method"), ("success_mean", "Success"), ("final_error_mean", "Error"), ("tracking_error_mean", "Track")],
        keep_e,
    )
    f = rows_from_csv(RESULTS / "family_f_summary_by_ablation.csv")
    write_table(
        TEX / "table_ablations.tex",
        "Family F SCMP ablations.",
        "tab:ablations",
        [("method", "Ablation"), ("success_mean", "Success"), ("final_error_mean", "Error"), ("margin_mean", "Margin"), ("branch_switches_mean", "Switches")],
        f,
    )
    g = rows_from_csv(RESULTS / "family_g_summary_by_control.csv")
    keep_g = [r for r in g if r["method"] in {"symmetric_derating", "scmp_true", "scmp_estimated", "guarded_scmp", "random_branch"}]
    write_table(
        TEX / "table_negative_controls.tex",
        "Family G negative controls.",
        "tab:negative-controls",
        [("condition", "Control"), ("method", "Method"), ("success_mean", "Success"), ("final_error_mean", "Error"), ("tracking_error_mean", "Track")],
        keep_g,
    )
    claims = [
        {
            "claim": "Signed cones help at high asymmetry",
            "evidence": "Family A SCMP true/guarded rows are compared with nominal, mean-gain, derating, and signed-fixed baselines.",
            "status": "supported synthetic",
        },
        {
            "claim": "Primitive choice matters beyond signed compensation",
            "evidence": "Family A and F compare SCMP against signed-fixed and no-switch/no-margin ablations.",
            "status": "supported synthetic",
        },
        {
            "claim": "Calibration is required",
            "evidence": "Family C and G wrong-sign controls expose estimated-cone failures and guarded fallback.",
            "status": "boundary",
        },
        {
            "claim": "No universal win",
            "evidence": "Family G includes symmetric actuation, no branch contrast, and shared weak-sign controls.",
            "status": "boundary",
        },
    ]
    write_rows(RESULTS / "claim_evidence.csv", claims)
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\scriptsize",
        r"\caption{Claim-to-evidence map for the v3 full-scale signed-cone suite.}",
        r"\label{tab:claim-evidence}",
        r"\begin{tabular}{p{0.24\linewidth}p{0.50\linewidth}p{0.16\linewidth}}",
        r"\toprule",
        r"Claim & Evidence & Status \\",
        r"\midrule",
    ]
    for row in claims:
        lines.append(f"{latex_escape(row['claim'])} & {latex_escape(row['evidence'])} & {latex_escape(row['status'])} " + r"\\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}", ""])
    (TEX / "table_claim_evidence.tex").write_text("\n".join(lines), encoding="utf-8")


def make_plots() -> int:
    failures = 0
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:
        (FIGURES / "plot_import_error.txt").write_text(repr(exc), encoding="utf-8")
        return 1

    try:
        rows = rows_from_csv(RESULTS / "family_a_summary_by_ratio.csv")
        methods = ["nominal_branch", "mean_gain", "symmetric_derating", "signed_fixed", "scmp_true", "guarded_scmp", "oracle_one_step"]
        plt.figure(figsize=(7.0, 4.0))
        for method in methods:
            subset = sorted([r for r in rows if r["method"] == method], key=lambda r: sf(r["ratio"]))
            plt.plot([sf(r["ratio"]) for r in subset], [sf(r["success_mean"]) for r in subset], marker="o", label=method)
        plt.xlabel("asymmetry ratio")
        plt.ylabel("mission success")
        plt.ylim(-0.03, 1.03)
        plt.grid(alpha=0.25)
        plt.legend(fontsize=7)
        plt.tight_layout()
        plt.savefig(FIGURES / "main_success_by_ratio.pdf")
        plt.savefig(FIGURES / "main_success_by_ratio.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_family_a.txt").write_text(repr(exc), encoding="utf-8")

    try:
        rows = rows_from_csv(RESULTS / "family_c_summary_by_budget.csv")
        methods = ["scmp_estimated", "guarded_scmp", "robust_scmp", "symmetric_derating"]
        plt.figure(figsize=(7.0, 4.0))
        for method in methods:
            subset = sorted([r for r in rows if r["method"] == method], key=lambda r: sf(r["calibration_budget"]))
            plt.plot([sf(r["calibration_budget"]) for r in subset], [sf(r["success_mean"]) for r in subset], marker="o", label=method)
        plt.xlabel("calibration samples")
        plt.ylabel("success")
        plt.ylim(-0.03, 1.03)
        plt.grid(alpha=0.25)
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(FIGURES / "calibration_budget.pdf")
        plt.savefig(FIGURES / "calibration_budget.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_calibration.txt").write_text(repr(exc), encoding="utf-8")

    try:
        rows = rows_from_csv(RESULTS / "family_d_summary_by_drift.csv")
        drift_modes = sorted({r["drift_mode"] for r in rows})
        methods = ["scmp_true", "scmp_estimated", "adaptive_scmp", "guarded_scmp", "robust_scmp"]
        x = np.arange(len(drift_modes))
        width = 0.15
        plt.figure(figsize=(8.0, 4.0))
        for i, method in enumerate(methods):
            vals = []
            for drift in drift_modes:
                match = [r for r in rows if r["method"] == method and r["drift_mode"] == drift]
                vals.append(sf(match[0]["success_mean"]) if match else 0.0)
            plt.bar(x + (i - 2) * width, vals, width=width, label=method)
        plt.xticks(x, drift_modes, rotation=20, ha="right")
        plt.ylabel("success")
        plt.ylim(0, 1.03)
        plt.legend(fontsize=7)
        plt.tight_layout()
        plt.savefig(FIGURES / "drift_success.pdf")
        plt.savefig(FIGURES / "drift_success.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_drift.txt").write_text(repr(exc), encoding="utf-8")

    try:
        rows = rows_from_csv(RESULTS / "family_g_summary_by_control.csv")
        controls = sorted({r["condition"] for r in rows})
        methods = ["symmetric_derating", "scmp_true", "scmp_estimated", "guarded_scmp", "random_branch"]
        x = np.arange(len(controls))
        width = 0.15
        plt.figure(figsize=(8.0, 4.0))
        for i, method in enumerate(methods):
            vals = []
            for control in controls:
                match = [r for r in rows if r["method"] == method and r["condition"] == control]
                vals.append(sf(match[0]["success_mean"]) if match else 0.0)
            plt.bar(x + (i - 2) * width, vals, width=width, label=method)
        plt.xticks(x, controls, rotation=25, ha="right")
        plt.ylabel("success")
        plt.ylim(0, 1.03)
        plt.legend(fontsize=7)
        plt.tight_layout()
        plt.savefig(FIGURES / "negative_controls.pdf")
        plt.savefig(FIGURES / "negative_controls.png", dpi=220)
        plt.close()
    except Exception as exc:
        failures += 1
        (FIGURES / "plot_error_controls.txt").write_text(repr(exc), encoding="utf-8")
    return failures


def write_evidence_summary(metadata: dict[str, Any]) -> None:
    a = {r["method"]: r for r in rows_from_csv(RESULTS / "family_a_summary_by_method.csv")}
    c = rows_from_csv(RESULTS / "family_c_summary_by_budget.csv")
    g = rows_from_csv(RESULTS / "family_g_summary_by_control.csv")
    budget_0 = {r["method"]: r for r in c if int(float(r["calibration_budget"])) == 0}
    budget_256 = {r["method"]: r for r in c if int(float(r["calibration_budget"])) == 256}
    wrong_sign = {r["method"]: r for r in g if r["condition"] == "wrong_sign_calibration"}
    lines = [
        "# Full-Scale Evidence Summary",
        "",
        f"- Stage: {metadata['stage']}",
        f"- Seed: {metadata['seed']}",
        f"- Rows: {metadata['total_rows']:,}",
        f"- Cases: {metadata['total_cases']:,}",
        f"- Plot failures: {metadata['plot_failures']}",
        "",
        "## Headline Numbers",
        "",
        f"- Family A SCMP true-cone success: {sf(a['scmp_true']['success_mean']):.3f}.",
        f"- Family A guarded SCMP success: {sf(a['guarded_scmp']['success_mean']):.3f}.",
        f"- Family A signed-fixed success: {sf(a['signed_fixed']['success_mean']):.3f}.",
        f"- Family A symmetric-derating success: {sf(a['symmetric_derating']['success_mean']):.3f}.",
        f"- Family A nominal-branch success: {sf(a['nominal_branch']['success_mean']):.3f}.",
        f"- Family C SCMP-estimated success at budget 0: {sf(budget_0['scmp_estimated']['success_mean']):.3f}; at budget 256: {sf(budget_256['scmp_estimated']['success_mean']):.3f}.",
        f"- Family G wrong-sign calibration SCMP-estimated success: {sf(wrong_sign['scmp_estimated']['success_mean']):.3f}; guarded SCMP: {sf(wrong_sign['guarded_scmp']['success_mean']):.3f}.",
        "",
        "## Scope",
        "",
        "These results support a synthetic signed-actuator mechanism and policy-interface diagnostic. They do not establish real-robot manipulation performance.",
    ]
    (DOCS / "evidence_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ensure_dirs()
    start = time.perf_counter()
    progress = {"stage": "running", "seed": SEED}
    (RESULTS / "progress.json").write_text(json.dumps(progress, indent=2), encoding="utf-8")
    family_meta = []
    total_rows = 0
    total_cases = 0
    for fn in [family_a, family_b, family_c, family_d, family_e, family_f, family_g]:
        fam_start = time.perf_counter()
        rows, meta = fn()
        meta["seconds"] = time.perf_counter() - fam_start
        family_meta.append(meta)
        total_rows += meta["rows"]
        total_cases += meta["cases"]
        progress = {"stage": "running", "last_family": meta["family"], "total_rows": total_rows, "total_cases": total_cases}
        (RESULTS / "progress.json").write_text(json.dumps(progress, indent=2), encoding="utf-8")
        del rows
    make_tables()
    plot_failures = make_plots()
    metadata = {
        "stage": "complete",
        "seed": SEED,
        "elapsed_seconds": time.perf_counter() - start,
        "total_rows": total_rows,
        "total_cases": total_cases,
        "plot_failures": plot_failures,
        "families": family_meta,
        "outputs": sorted(str(p.relative_to(ROOT)) for p in RESULTS.rglob("*") if p.is_file())
        + sorted(str(p.relative_to(ROOT)) for p in FIGURES.rglob("*") if p.is_file()),
    }
    (RESULTS / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (RESULTS / "progress.json").write_text(json.dumps({"stage": "complete", "total_rows": total_rows, "total_cases": total_cases}, indent=2), encoding="utf-8")
    write_evidence_summary(metadata)
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
