# Final Audit

1. Chosen thesis: Manipulation policies should expose signed actuator cones and choose contact/IK primitives by signed projected object-motion feasibility rather than hiding actuator asymmetry inside generic robustness.

2. Field assumption broken: The policy action space can remain a symmetric command vector while low-level control, uncertainty, or randomization absorbs actuator mismatch.

3. New central mechanism: Signed-Cone Manipulation Policy (SCMP), which factors each actuator into positive and negative channels, projects desired local object motion through each candidate primitive's signed cone, and selects the primitive with low projected error plus high remaining directional margin.

4. Genuine novelty: The novelty is policy-level primitive selection in signed actuator-feasibility coordinates. Actuator limits, fault tolerance, robust control, and projection alone are not claimed as new.

5. Closest hostile prior work: Fault-tolerant/adaptive manipulator control, actuator-saturation and constrained MPC/control allocation, sim-to-real dynamics randomization, and contact-mode/nonprehensile manipulation. The hostile set is documented in `docs/hostile_prior_work.md`.

6. Literature coverage: `docs/related_work_matrix.csv` contains 1000 entries; the intended tiers are 1000-paper landscape, 300-paper serious skim, 240-paper deep read, and 100-paper hostile prior-work set. Synthesis documents are in `docs/literature_map.md`, `docs/novelty_boundary_map.md`, and `docs/novelty_decision.md`.

7. Proof/formal-claim status: Two local propositions are argued in the paper. The fixed-primitive projection claim is a convex projection statement. The symmetric-derating loss claim is an existence/counterexample statement. No global optimality, real-robot theorem, or unknown-fault identification guarantee is claimed.

8. Strongest evidence: At asymmetry ratio 4.0, SCMP reached success 0.906 and final error 0.055; nominal branch reached success 0.500 and final error 0.100; signed fixed branch reached success 0.613 and final error 0.092.

9. Biggest weaknesses: The evidence is a simplified two-link manipulation proxy; no hardware validation; actuator asymmetry is assumed known; primitive switching is local and not globally planned; full signed-bound MPC is not implemented as a strongest possible baseline.

10. Paper-readiness judgment: workshop. The mechanism is crisp and runnable, but a main-conference submission would need real-robot or higher-fidelity evidence and a stronger constrained-MPC comparison.

11. Exact Downloads PDF path: C:\Users\wangz\Downloads\23.pdf (present).

12. GitHub URL/status: https://github.com/Jason-Wang313/23_manipulation_under_actuator_asymmetry

13. Visible Desktop PDF copy status: pending orchestrator copy

## Build Status Excerpt
```
Build started at 2026-06-11T18:51:32.4660155+01:00
RUN pdflatex1: pdflatex -interaction=nonstopmode -halt-on-error main.tex
EXIT pdflatex1: 0
RUN bibtex: bibtex main
EXIT bibtex: 0
RUN pdflatex2: pdflatex -interaction=nonstopmode -halt-on-error main.tex
EXIT pdflatex2: 0
RUN pdflatex3: pdflatex -interaction=nonstopmode -halt-on-error main.tex
EXIT pdflatex3: 0
PDF copied to C:\Users\wangz\Downloads\23.pdf
Build finished at 2026-06-11T18:51:41.5336309+01:00
```

## Orchestrator Desktop Copy

Checked: 2026-06-11 19:00:05 +01:00
Downloads PDF: C:/Users/wangz/Downloads/23.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_23_20260611_190001.log
