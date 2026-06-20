# Final Audit

1. Chosen thesis: manipulation policies should expose signed actuator cones and choose contact/IK primitives by signed projected object-motion feasibility rather than hiding actuator asymmetry inside generic robustness.

2. Field assumption broken: the policy action space can remain a symmetric command vector while low-level control, uncertainty, or randomization absorbs actuator mismatch.

3. New central mechanism: Signed-Cone Manipulation Policy (SCMP), which factors each actuator into positive and negative channels, projects desired local object motion through each candidate primitive's signed cone, and selects the primitive with low projected error plus high remaining directional margin.

4. Genuine novelty: the novelty is policy-level primitive selection in signed actuator-feasibility coordinates. Actuator limits, fault tolerance, robust control, and projection alone are not claimed as new.

5. Closest hostile prior work: fault-tolerant/adaptive manipulator control, actuator-saturation and constrained MPC/control allocation, sim-to-real dynamics randomization, and contact-mode/nonprehensile manipulation. The hostile set is documented in `docs/hostile_prior_work.md`.

6. Literature coverage: `docs/related_work_matrix.csv` contains 1000 entries; the intended tiers are 1000-paper landscape, 300-paper serious skim, 240-paper deep read, and 100-paper hostile prior-work set. Synthesis documents are in `docs/literature_map.md`, `docs/novelty_boundary_map.md`, and `docs/novelty_decision.md`.

7. Proof/formal-claim status: two local propositions are argued in the paper. The fixed-primitive projection claim is a convex projection statement. The symmetric-derating loss claim is an existence/counterexample statement. No global optimality, real-robot theorem, or unknown-fault identification guarantee is claimed.

8. Strongest v3 evidence: the full-scale suite produced 69,480 policy rows over 6,690 task cases with seed 23023 and zero plot failures. In Family A, true-cone SCMP reaches 0.940 success and guarded SCMP reaches 0.939, compared with signed fixed branch 0.891, symmetric derating 0.785, and nominal branch 0.771. At ratio 5.0, guarded SCMP reaches 0.854 and true-cone SCMP 0.838, compared with symmetric derating 0.298 and nominal branch 0.442.

9. Strongest negative evidence: wrong-sign calibration is catastrophic. In Family G, estimated SCMP reaches 0.150 and guarded SCMP reaches 0.200, while true-cone SCMP reaches 0.933. This means calibration and sign-convention validation are required assumptions, not incidental details.

10. Biggest weaknesses: the evidence is a simplified planar manipulation proxy; no hardware validation; no high-fidelity contact simulation; primitive switching is local and not globally planned; full signed-bound MPC/control allocation is not implemented as the strongest possible baseline.

11. Paper-readiness judgment: final batch artifact and submission-ready synthetic mechanism paper under the stated scope. It should not be marketed as a real-robot result or as dominance over full constrained MPC. A main-track empirical submission would still need hardware/high-fidelity validation, online calibration, and stronger MPC/control-allocation baselines.

12. Exact Downloads PDF path: `C:/Users/wangz/Downloads/23.pdf`.

13. Downloads PDF verification: 25 pages, 360,190 bytes, SHA256 `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`.

14. GitHub URL/status: `https://github.com/Jason-Wang313/23_manipulation_under_actuator_asymmetry`.

15. Visible Desktop PDF copy status: absent; canonical batch artifact is in Downloads.

16. Local build PDF status: `paper/main.pdf` is absent after canonical copy.

17. VLA-style link-box audit: all 56 link annotations use one-point borders;
    citation and URL boxes are green, internal-reference boxes are red, no cyan
    boxes are present, and rendered affected pages were visually inspected.

## Final Build And Verification

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex -> 0
bibtex main -> 0
pdflatex -interaction=nonstopmode -halt-on-error main.tex -> 0
pdflatex -interaction=nonstopmode -halt-on-error main.tex -> 0
pdfinfo C:/Users/wangz/Downloads/23.pdf -> 25 pages
Get-FileHash -Algorithm SHA256 C:/Users/wangz/Downloads/23.pdf -> 2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B
pdftotext marker check -> v3 marker, row/case counts, headline metrics, wrong-sign failure, no-real-robot limitation, and final audit marker found
```
