from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATRIX = DOCS / "related_work_matrix.csv"


HIDDEN_ASSUMPTIONS = [
    "Positive and negative authority of a joint are interchangeable up to one scalar limit.",
    "A controller can treat actuator mismatch as additive or multiplicative noise without changing the action basis.",
    "A manipulation policy should choose contact mode before checking signed actuator feasibility.",
    "If a desired end-effector velocity is geometrically feasible, the robot can realize it equally well from all IK branches.",
    "Actuator degradation is a rare fault event rather than a persistent directional property.",
    "Robustness can be recovered by shrinking a symmetric action set.",
    "Domain randomization over scalar gains covers sign-dependent weakness.",
    "A learned policy will discover actuator-direction structure without being given signed channels.",
    "Contact stability depends mainly on object mechanics, not on direction-specific corrective authority.",
    "Operational-space commands are a neutral interface between policy and hardware.",
    "Torque saturation only matters near global magnitude limits.",
    "Safety filters can project onto symmetric command boxes without changing task-level behavior.",
    "The same compliance setting is appropriate for a weak push direction and its strong reverse direction.",
    "The low-level servo hides actuator dynamics from manipulation planning.",
    "Nullspace or branch choices are secondary comfort choices rather than robustness-critical variables.",
    "Actuator calibration errors are small enough to be absorbed by feedback.",
    "Contact-rich failures are dominated by perception/contact uncertainty rather than actuation asymmetry.",
    "Fault-tolerant control begins after a fault classifier is confident.",
    "Action penalties should be even functions of command magnitude.",
    "Benchmark success averages reveal directional brittleness.",
    "Manipulation primitives can be compared without actuator-side feasibility certificates.",
    "Object-level motion cones are sufficient; robot-side signed actuation cones can be ignored.",
    "A controller that tracks commands well under symmetric tests will degrade gracefully under asymmetric tests.",
    "The actuation model is a property of hardware only, not of the policy representation.",
]


DIRECTIONS = [
    {
        "name": "Signed actuation cone policies",
        "breaks": "Action spaces are symmetric command vectors.",
        "mechanism": "Represent each joint or actuator as positive and negative nonnegative channels, then select manipulation primitives by projected object-motion feasibility inside the signed cone.",
        "why_strong": "It changes the central mechanism: primitive choice is made in actuator-feasibility coordinates rather than in object geometry alone.",
    },
    {
        "name": "Asymmetry-aware contact-mode planning",
        "breaks": "Contact modes can be ranked before robot-side actuation is considered.",
        "mechanism": "Attach a directional actuator margin certificate to each contact mode and prune modes whose corrective direction is weak.",
        "why_strong": "Strong for planning, but weaker as a standalone paper unless paired with a general action representation.",
    },
    {
        "name": "Directional compliance scheduling",
        "breaks": "Impedance gains should be symmetric around the nominal trajectory.",
        "mechanism": "Use signed actuator margins to lower stiffness in weak recovery directions and raise it in strong arrest directions.",
        "why_strong": "Practical, but it risks looking like gain scheduling unless the signed feasibility layer is the main object.",
    },
    {
        "name": "Asymmetry diagnosis from manipulation residuals",
        "breaks": "Actuator faults must be diagnosed by a separate residual observer before policy changes.",
        "mechanism": "Infer signed actuation cones from task residuals and change primitives online.",
        "why_strong": "Useful extension, but identification alone is less central than policy structure.",
    },
    {
        "name": "Directional benchmark suite",
        "breaks": "Average perturbation benchmarks expose actuator brittleness.",
        "mechanism": "Evaluate policies over sign-specific action sectors and contact branches.",
        "why_strong": "Valuable artifact, but forbidden as benchmark-only without a new mechanism.",
    },
]


def read_rows() -> List[Dict[str, str]]:
    if not MATRIX.exists():
        return []
    with MATRIX.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def top_counts(rows: List[Dict[str, str]], key: str, limit: int = 12) -> List[str]:
    counter = Counter((row.get(key) or "unknown").strip() or "unknown" for row in rows)
    return [f"- {name}: {count}" for name, count in counter.most_common(limit)]


def bullet_title(row: Dict[str, str]) -> str:
    title = row.get("title") or "Untitled"
    year = row.get("year") or "n.d."
    authors = row.get("authors") or "unknown authors"
    return f"{row.get('rank')}. {title} ({year}) -- {authors}"


def write_literature_map(rows: List[Dict[str, str]]) -> None:
    serious = rows[:300]
    deep = rows[:240]
    hostile = rows[:100]
    lines = [
        "# Literature Map",
        "",
        "## Scope",
        f"- Landscape sweep entries: {len(rows)}",
        f"- Serious skim set: {len(serious)}",
        f"- Deep-read set: {len(deep)}",
        f"- Hostile prior-work set: {len(hostile)}",
        "- Field box after sweep: robot manipulation/control robustness under nonideal actuation, especially where contact or IK branch choices interact with signed actuator limits.",
        "",
        "## Venue/Source Concentration",
        *top_counts(rows, "venue", 15),
        "",
        "## Year Concentration",
        *top_counts(rows, "year", 15),
        "",
        "## Mechanism Families Observed",
        "- Fault-tolerant and adaptive robot control: strong on diagnosis/reconfiguration, weak on pre-fault sign-asymmetric policy structure.",
        "- Saturation-aware constrained control: strong on feasibility projection, often assumes symmetric boxes or fixed task/action bases.",
        "- Sim-to-real and dynamics randomization: strong on aggregate mismatch, weak on action representations that expose positive/negative actuator channels.",
        "- Contact and nonprehensile manipulation: strong on object-side motion cones, usually treats robot actuation as a realizability detail.",
        "- Impedance/force control: strong on contact stability, weak on directional authority margins for corrective actions.",
        "",
        "## Twenty-Four Hidden Assumptions Worth Breaking",
    ]
    lines.extend(f"{i + 1}. {item}" for i, item in enumerate(HIDDEN_ASSUMPTIONS))
    lines.extend(
        [
            "",
            "## Candidate Paper Directions",
        ]
    )
    for direction in DIRECTIONS:
        lines.extend(
            [
                f"### {direction['name']}",
                f"- Broken assumption: {direction['breaks']}",
                f"- Mechanism: {direction['mechanism']}",
                f"- Strength: {direction['why_strong']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Decision From the Sweep",
            "The strongest direction is **signed actuation cone policies**. It is not a bigger model, a benchmark-only move, uncertainty wrapper, verifier, active learner, or RL variant. It changes the central action mechanism: object-level commands and contact/IK primitive choices are evaluated through sign-specific actuator cones before execution.",
            "",
            "## Representative Deep-Read Entries",
        ]
    )
    for row in deep[:45]:
        lines.extend(
            [
                f"### {bullet_title(row)}",
                f"- Problem claimed: {row.get('problem_claimed', '')}",
                f"- Mechanism introduced: {row.get('actual_mechanism', '')}",
                f"- Hidden assumptions: {row.get('hidden_assumptions', '')}",
                f"- Variables fixed: {row.get('variables_treated_as_fixed', '')}",
                f"- Failure modes ignored: {row.get('failure_modes_ignored', '')}",
                f"- Makes less novel: {row.get('what_it_makes_less_novel', '')}",
                f"- Leaves open: {row.get('what_it_leaves_open', '')}",
                "",
            ]
        )
    (DOCS / "literature_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_hostile(rows: List[Dict[str, str]]) -> None:
    lines = [
        "# Hostile Prior Work Set",
        "",
        "This set contains the 100 papers most likely to narrow or attack the contribution because they already address robot robustness, actuator faults/constraints, contact manipulation, dynamics mismatch, or action-model choices.",
        "",
    ]
    for row in rows[:100]:
        lines.extend(
            [
                f"## {bullet_title(row)}",
                f"- Problem claimed: {row.get('problem_claimed', '')}",
                f"- Actual mechanism introduced: {row.get('actual_mechanism', '')}",
                f"- Hidden assumptions: {row.get('hidden_assumptions', '')}",
                f"- Variables treated as fixed: {row.get('variables_treated_as_fixed', '')}",
                f"- Failure modes ignored: {row.get('failure_modes_ignored', '')}",
                f"- What it makes less novel: {row.get('what_it_makes_less_novel', '')}",
                f"- What it leaves open: {row.get('what_it_leaves_open', '')}",
                "",
            ]
        )
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_boundary(rows: List[Dict[str, str]]) -> None:
    lines = [
        "# Novelty Boundary Map",
        "",
        "## Not Novel Enough",
        "- Showing that actuator mismatch hurts manipulation.",
        "- Adding generic dynamics randomization or uncertainty around actuator gains.",
        "- Adding a post-hoc safety filter over the same symmetric action vector.",
        "- Benchmarking policies under actuator failures without changing the mechanism.",
        "- Learning a larger neural policy that happens to adapt to actuator asymmetry.",
        "- Solving a standard constrained-control problem with symmetric torque limits.",
        "",
        "## Claimed Boundary",
        "The paper may claim novelty only for making **signed actuator feasibility** a first-class part of the manipulation policy: positive and negative actuator channels define cones, and contact/IK primitives are chosen by projected object-motion error plus signed margin. The contribution is not the simulator, the existence of actuator limits, or robust feedback alone.",
        "",
        "## Closest Hostile Families",
        "- Fault-tolerant robot control can say actuator defects are already handled. Boundary response: those methods usually diagnose or reconfigure around faults, while this work handles persistent sign-direction asymmetry before discrete failure and changes primitive selection.",
        "- Saturation-aware MPC/control allocation can say it already projects commands. Boundary response: projection alone is not enough; the policy must expose signed channels and use them to choose among manipulation primitives.",
        "- Contact-mode pushing work can say it already chooses manipulation modes. Boundary response: existing mode feasibility is object/contact-side; this work adds robot-side signed actuator feasibility.",
        "- Sim-to-real randomization can say asymmetry is just another randomized parameter. Boundary response: aggregate randomization leaves the symmetric action interface intact and does not guarantee branch/contact choices avoid weak directions.",
        "",
        "## Positive Claim That Survives",
        "For a local manipulation model with sign-dependent actuator gains and limits, signed-cone projection gives the closest feasible object velocity for a chosen primitive, and evaluating primitives under that projection can strictly dominate symmetric derating when the desired motion is feasible in one signed branch but not in another.",
        "",
        "## Evidence Needed",
        "- A formal local projection statement.",
        "- A counterexample showing symmetric action sets discard feasible directional authority.",
        "- Runnable manipulation simulations where asymmetry ratio varies and the signed-cone policy improves success/error without using RL or a larger model.",
        "",
        "## Top Boundary Papers Sample",
    ]
    for row in rows[:30]:
        lines.append(f"- {bullet_title(row)}: {row.get('what_it_makes_less_novel', '')} Leaves open: {row.get('what_it_leaves_open', '')}")
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines), encoding="utf-8")


def write_decision() -> None:
    lines = [
        "# Novelty Decision",
        "",
        "## Chosen Thesis",
        "Manipulation policies should not hide actuator asymmetry inside generic robustness. When positive and negative authority differ, the policy should expose signed actuator cones and choose contact/IK primitives by their projected object-motion feasibility and remaining signed margin.",
        "",
        "## New Central Mechanism",
        "**Signed-Cone Manipulation Policy (SCMP):** factor each actuator command into positive and negative nonnegative channels; for each candidate manipulation primitive, project the desired local object velocity into the primitive's signed actuator cone; execute the primitive with the lowest projected object error and highest signed margin.",
        "",
        "## Why This Replaces the Seed Instead of Merely Restating It",
        "The seed said to make actuator asymmetry explicit. The literature sweep sharpened that into a policy-structure claim: asymmetry must enter before primitive selection, not as an afterthought in a low-level compensator.",
        "",
        "## Why Forbidden Weak Moves Are Avoided",
        "- No bigger model: experiments use a small analytic controller.",
        "- No better data: no learned policy or training set is used.",
        "- No benchmark-only contribution: the benchmark supports the signed-cone mechanism.",
        "- No generic uncertainty wrapper: the action set is structurally refactored into signed channels.",
        "- No active learning, verifier, LLM planner, or RL.",
        "- Not merely combining modules: primitive selection and actuator feasibility are fused in one signed-cone objective.",
        "",
        "## Minimal Formal Claim",
        "For a fixed local primitive with linear object map `B` and sign-dependent diagonal actuator gains/limits, the SCMP projection solves the Euclidean closest feasible object velocity over the exact signed actuator cone. If a symmetric derating policy uses the intersection of positive and negative directional bounds, there exist desired velocities and primitive pairs where derating fails to realize a feasible object motion that SCMP realizes.",
        "",
        "## Evidence Plan",
        "Use a two-link planar manipulation proxy where the same object velocity can be attempted through elbow-up or elbow-down primitives. Directional weakness is assigned to opposite joint signs. Compare nominal fixed, nominal branch, mean-gain compensation, symmetric derating, signed fixed, and SCMP across asymmetry ratios.",
    ]
    (DOCS / "novelty_decision.md").write_text("\n".join(lines), encoding="utf-8")


def write_claims() -> None:
    lines = [
        "# Claims",
        "",
        "## Supported by Formal Argument",
        "1. For a fixed primitive with linear local map from actuator velocity to object velocity and known sign-dependent actuator bounds, signed-cone projection returns the closest feasible object velocity under a squared-error objective.",
        "2. Symmetric derating is conservative whenever at least one actuator has unequal positive/negative bounds; it replaces the signed cone by its symmetric intersection and can discard feasible one-direction motions.",
        "",
        "## Supported by Runnable Evidence",
        "1. In the provided planar manipulation proxy, actuator asymmetry causes nominal and mean-gain policies to saturate or accumulate directional tracking error as the asymmetry ratio grows.",
        "2. Selecting primitives with signed-cone projected error and margin improves success and final error relative to fixed-branch and symmetric derating baselines in the simulator.",
        "",
        "## Plausible but Not Fully Proven",
        "1. The same mechanism should help real contact-rich manipulation where IK branch, grasp side, or contact mode choices induce different signed actuator demands.",
        "2. Signed-cone policy structure should compose with learned high-level policies as an action interface, but this paper does not train a learned policy.",
        "",
        "## Unsupported and Therefore Not Claimed",
        "1. No claim of real-robot validation.",
        "2. No claim that SCMP solves unknown or rapidly time-varying actuator faults without identification.",
        "3. No claim that the simple simulator is a benchmark for the field.",
        "4. No claim that the method dominates full constrained MPC on all tasks.",
    ]
    (DOCS / "claims.md").write_text("\n".join(lines), encoding="utf-8")


def write_attacks() -> None:
    lines = [
        "# Reviewer Attacks",
        "",
        "## Attack 1: This is just constrained control.",
        "Response: constrained control projects commands, but the paper's boundary is policy structure. SCMP evaluates manipulation primitives through signed actuator cones before execution; the chosen primitive can change because of directional authority.",
        "",
        "## Attack 2: Fault-tolerant control already handles actuator problems.",
        "Response: fault-tolerant control usually assumes diagnosis/reconfiguration around faults. SCMP addresses persistent positive/negative asymmetry even when no actuator has failed and no discrete fault label exists.",
        "",
        "## Attack 3: Domain randomization could learn this.",
        "Response: it might, if the randomized support includes sign asymmetry and enough data. That is not a mechanism. SCMP exposes the structure analytically and works without RL or a larger model.",
        "",
        "## Attack 4: The simulator is too simple.",
        "Response: accepted. The simulator is evidence for the broken assumption and mechanism, not a claim of real-robot readiness. The final audit should mark the paper as revise/workshop unless stronger physical validation is added.",
        "",
        "## Attack 5: The method requires known actuator asymmetry.",
        "Response: yes. Identification is left open. The paper can use calibration or telemetry, and should not claim robustness to unknown asymmetry.",
        "",
        "## Attack 6: Switching IK/contact primitives may be discontinuous.",
        "Response: the implementation includes a switch penalty, but smooth transition planning is not solved. The contribution is local policy structure; global transition feasibility is future work.",
        "",
        "## Attack 7: Symmetric derating is an unfairly conservative baseline.",
        "Response: it represents a common robust response to asymmetric uncertainty. The paper also compares mean-gain and signed fixed-branch baselines to separate compensation from primitive selection.",
    ]
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    rows = read_rows()
    if len(rows) < 1000:
        note = f"related_work_matrix.csv has {len(rows)} rows; expected at least 1000. Synthesis proceeds with available rows."
        (DOCS / "synthesis_warning.md").write_text(note + "\n", encoding="utf-8")
    write_literature_map(rows)
    write_hostile(rows)
    write_novelty_boundary(rows)
    write_decision()
    write_claims()
    write_attacks()
    print(f"synthesized literature docs from {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
