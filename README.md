# Manipulation Under Actuator Asymmetry

Anonymous ICLR-style paper artifact for paper 23 in the robotics/embodied-intelligence batch.

## Thesis

Robot manipulation policies should expose signed actuator authority. When positive and negative actuator directions have different gains or limits, a policy should choose contact/IK primitives by projected feasibility inside signed actuator cones, not only by nominal object-space geometry.

## Reproduce

From the repository root:

```powershell
python scripts/collect_literature.py
python scripts/synthesize_literature.py
python scripts/run_experiments.py
python scripts/fetch_iclr_template.py
python scripts/write_paper.py
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
python scripts/write_final_audit.py
```

The final PDF target is:

```text
C:/Users/wangz/Downloads/23.pdf
```

## Main Artifacts

- `docs/related_work_matrix.csv`: 1000-paper literature matrix when OpenAlex retrieval succeeds.
- `docs/literature_map.md`: landscape, serious skim, deep-read synthesis.
- `docs/hostile_prior_work.md`: hostile 100-paper prior-work set.
- `docs/novelty_boundary_map.md`: novelty boundaries and closest attacks.
- `docs/novelty_decision.md`: chosen thesis and mechanism.
- `docs/claims.md`: supported, plausible, and unsupported claims.
- `docs/reviewer_attacks.md`: adversarial review risks.
- `src/asym_manip/simulator.py`: signed-actuator manipulation simulator.
- `results/summary.csv`: aggregate experiment results.
- `paper/main.tex`: anonymous ICLR-style manuscript.
- `docs/final_audit.md`: required final audit.
