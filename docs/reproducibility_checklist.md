# Reproducibility Checklist

- [x] Dependencies are listed in `requirements.txt`.
- [x] Main simulator source is `src/asym_manip/simulator.py`.
- [x] Main experiment runner is `scripts/run_experiments.py`.
- [x] Paper generator is `scripts/write_paper.py`.
- [x] Main outputs are `results/episode_results.csv`, `results/summary.csv`, and `results/result_table.tex`.
- [x] V2 outputs are `results/calibration_stress_episodes.csv`, `results/calibration_stress_summary.csv`, `results/calibration_stress_table.tex`, and `results/calibration_stress.png`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical batch PDF path is `C:/Users/wangz/Downloads/23.pdf`.
- [x] Local `paper/main.pdf` is deleted after copying the canonical PDF to Downloads.

Recommended verification commands:

```powershell
python scripts\run_experiments.py
python scripts\write_paper.py
python scripts\validate_artifacts.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
