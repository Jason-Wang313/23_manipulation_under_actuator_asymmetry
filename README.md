# Manipulation Under Actuator Asymmetry

Anonymous ICLR-style paper artifact for paper 23 in the robotics/embodied-intelligence batch.

## Thesis

Robot manipulation policies should expose signed actuator authority. When positive and negative actuator directions have different gains or limits, a policy should choose contact/IK primitives by projected feasibility inside signed actuator cones, not only by nominal object-space geometry.

## V3 Full-Scale Status

- Stage: v3 final full-scale complete.
- Final PDF: `C:/Users/wangz/Downloads/23.pdf`.
- Final PDF verification: 25 pages, 360,190 bytes, SHA256 `84342525B234DFCBF4F1D23DD11349BDF2D179953A42A0110D60078403247519`.
- Full-scale runner: `experiments/full_scale_signed_cone.py`.
- Full-scale suite: 69,480 policy rows over 6,690 task cases, seed 23023, zero plot failures.
- Local build PDF policy: `paper/main.pdf` is removed after the canonical copy is exported to Downloads.

## Reproduce

From the repository root:

```powershell
python .\experiments\full_scale_signed_cone.py
cd .\paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The legacy v1/v2 pipeline remains available:

```powershell
python scripts/collect_literature.py
python scripts/synthesize_literature.py
python scripts/run_experiments.py
python scripts/fetch_iclr_template.py
python scripts/write_paper.py
powershell -ExecutionPolicy Bypass -File scripts/build_paper.ps1
python scripts/write_final_audit.py
```

## Main Artifacts

- `docs/full_scale_execution_plan.md`: paper-specific v3 plan written before the full-scale pass.
- `experiments/full_scale_signed_cone.py`: v3 RAM-light full-scale experiment runner.
- `results/full_scale/`: full-scale CSV rows, summaries, metadata, progress, and generated TeX tables.
- `figures/full_scale/`: full-scale PDF/PNG figures used by the manuscript.
- `docs/evidence_summary.md`: final full-scale evidence ledger.
- `docs/experiment_report.md`: v3 experiment report and interpretation.
- `docs/final_audit.md`: required final audit with Downloads artifact verification.
- `paper/main.tex`: anonymous v3 final full-scale manuscript source.
- `docs/related_work_matrix.csv`: 1000-paper literature matrix when OpenAlex retrieval succeeds.
- `docs/literature_map.md`: landscape, serious skim, deep-read synthesis.
- `docs/hostile_prior_work.md`: hostile 100-paper prior-work set.
- `docs/novelty_boundary_map.md`: novelty boundaries and closest attacks.
- `docs/claims.md`: supported, plausible, and unsupported claims.
- `docs/reviewer_attacks.md`: adversarial review risks and current responses.

## Headline Result

In the main full-scale aggregate, true-cone SCMP reaches 0.940 success and guarded SCMP reaches 0.939, compared with 0.891 for signed fixed branch, 0.785 for symmetric derating, and 0.771 for nominal branch selection. The result is conditional: wrong-sign calibration is catastrophic, no real robot is evaluated, and full signed-bound MPC remains a required future baseline.
