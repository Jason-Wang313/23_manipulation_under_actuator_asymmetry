from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"
PAPER = ROOT / "paper"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/23.pdf")
DESKTOP_PDF = Path("C:/Users/wangz/OneDrive/Desktop/23.pdf")


def count_matrix() -> int:
    matrix = DOCS / "related_work_matrix.csv"
    if not matrix.exists():
        return 0
    with matrix.open(newline="", encoding="utf-8") as f:
        return max(0, sum(1 for _ in csv.DictReader(f)))


def best_result_line() -> str:
    path = RESULTS / "summary.json"
    if not path.exists():
        return "Experiments were not run; no strongest evidence available."
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("summary", [])
    def get(method: str, ratio: float):
        for row in rows:
            if row.get("method") == method and abs(float(row.get("ratio", 0.0)) - ratio) < 1e-6:
                return row
        return {}
    scmp = get("signed_cone_policy", 4.0)
    nominal = get("nominal_branch", 4.0)
    fixed = get("signed_fixed", 4.0)
    return (
        "At asymmetry ratio 4.0, SCMP reached success "
        f"{float(scmp.get('success_rate', 0.0)):.3f} and final error "
        f"{float(scmp.get('final_error_mean', 0.0)):.3f}; nominal branch reached success "
        f"{float(nominal.get('success_rate', 0.0)):.3f} and final error "
        f"{float(nominal.get('final_error_mean', 0.0)):.3f}; signed fixed branch reached success "
        f"{float(fixed.get('success_rate', 0.0)):.3f} and final error "
        f"{float(fixed.get('final_error_mean', 0.0)):.3f}."
    )


def calibration_result_line() -> str:
    path = RESULTS / "summary.json"
    if not path.exists():
        return "V2 calibration stress was not run."
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("calibration_stress", [])

    def get(method: str, estimated_ratio: float):
        for row in rows:
            if row.get("method") == method and abs(float(row.get("estimated_ratio", 0.0)) - estimated_ratio) < 1e-6:
                return row
        return {}

    exact = get("signed_cone_policy", 4.0)
    symmetric = get("signed_cone_policy", 1.0)
    mean_exact = get("mean_gain", 4.0)
    return (
        "V2 calibration stress with true ratio 4.0: SCMP success "
        f"{float(exact.get('success_rate', 0.0)):.3f} under correct calibration versus "
        f"{float(mean_exact.get('success_rate', 0.0)):.3f} for mean-gain compensation; "
        "when the policy assumes symmetry, SCMP falls to "
        f"{float(symmetric.get('success_rate', 0.0)):.3f}."
    )


def read_optional(path: Path, default: str) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return default


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    github_status = read_optional(DOCS / "github_status.md", "GitHub push not attempted yet.")
    build_status = read_optional(PAPER / "build_status.txt", "Paper build not attempted yet.")
    pdf_status = f"present, {DOWNLOADS_PDF.stat().st_size} bytes" if DOWNLOADS_PDF.exists() else "missing"
    local_pdf_status = "present" if (PAPER / "main.pdf").exists() else "absent after canonical copy"
    desktop_status = str(DESKTOP_PDF) if DESKTOP_PDF.exists() else "absent under v2 hardening"
    matrix_count = count_matrix()
    audit = [
        "# Final Audit",
        "",
        "1. Chosen thesis: Manipulation policies should expose signed actuator cones and choose contact/IK primitives by signed projected object-motion feasibility rather than hiding actuator asymmetry inside generic robustness.",
        "",
        "2. Field assumption broken: The policy action space can remain a symmetric command vector while low-level control, uncertainty, or randomization absorbs actuator mismatch.",
        "",
        "3. New central mechanism: Signed-Cone Manipulation Policy (SCMP), which factors each actuator into positive and negative channels, projects desired local object motion through each candidate primitive's signed cone, and selects the primitive with low projected error plus high remaining directional margin.",
        "",
        "4. Genuine novelty: The novelty is policy-level primitive selection in signed actuator-feasibility coordinates. Actuator limits, fault tolerance, robust control, and projection alone are not claimed as new.",
        "",
        "5. Closest hostile prior work: Fault-tolerant/adaptive manipulator control, actuator-saturation and constrained MPC/control allocation, sim-to-real dynamics randomization, and contact-mode/nonprehensile manipulation. The hostile set is documented in `docs/hostile_prior_work.md`.",
        "",
        f"6. Literature coverage: `docs/related_work_matrix.csv` contains {matrix_count} entries; the intended tiers are 1000-paper landscape, 300-paper serious skim, 240-paper deep read, and 100-paper hostile prior-work set. Synthesis documents are in `docs/literature_map.md`, `docs/novelty_boundary_map.md`, and `docs/novelty_decision.md`.",
        "",
        "7. Proof/formal-claim status: Two local propositions are argued in the paper. The fixed-primitive projection claim is a convex projection statement. The symmetric-derating loss claim is an existence/counterexample statement. No global optimality, real-robot theorem, or unknown-fault identification guarantee is claimed.",
        "",
        f"8. Strongest evidence: {best_result_line()} {calibration_result_line()}",
        "",
        "9. Biggest weaknesses: The evidence is a simplified two-link manipulation proxy; no hardware validation; actuator asymmetry is assumed known; v2 shows SCMP collapses when the signed cone is badly miscalibrated; primitive switching is local and not globally planned; full signed-bound MPC is not implemented as a strongest possible baseline.",
        "",
        "10. Paper-readiness judgment: workshop-only / strong-revise. The mechanism is crisp and runnable, but a main-conference submission would need real-robot or higher-fidelity evidence, online calibration, and a stronger constrained-MPC comparison.",
        "",
        f"11. Exact Downloads PDF path: {DOWNLOADS_PDF} ({pdf_status}).",
        "",
        f"12. GitHub URL/status: {github_status}",
        "",
        f"13. Visible Desktop PDF copy status: {desktop_status}",
        "",
        f"14. Local build PDF status: `paper/main.pdf` is {local_pdf_status}.",
        "",
        "## Build Status Excerpt",
        "```",
        build_status[-3000:],
        "```",
    ]
    (DOCS / "final_audit.md").write_text("\n".join(audit) + "\n", encoding="utf-8")
    print("wrote docs/final_audit.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
