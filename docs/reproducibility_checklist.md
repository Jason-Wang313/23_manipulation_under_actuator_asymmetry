# Reproducibility Checklist

- [x] Dependencies are listed in `requirements.txt`.
- [x] Main simulator source is `src/asym_manip/simulator.py`.
- [x] Legacy experiment runner is `scripts/run_experiments.py`.
- [x] V3 full-scale runner is `experiments/full_scale_signed_cone.py`.
- [x] V3 outputs are under `results/full_scale/`.
- [x] V3 figures are under `figures/full_scale/`.
- [x] Generated V3 TeX tables are under `results/full_scale/tex/`.
- [x] Paper source is `paper/main.tex`.
- [x] Canonical batch PDF path is `C:/Users/wangz/Downloads/23.pdf`.
- [x] Canonical PDF is verified at 25 pages, 360,190 bytes, SHA256 `84342525B234DFCBF4F1D23DD11349BDF2D179953A42A0110D60078403247519`.
- [x] Local `paper/main.pdf` is deleted after copying the canonical PDF to Downloads.
- [x] The full-scale runner compiles with `python -m py_compile`.

Recommended verification commands:

```powershell
python .\experiments\full_scale_signed_cone.py
python -m py_compile .\experiments\full_scale_signed_cone.py
cd .\paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdfinfo .\main.pdf
pdftotext .\main.pdf - | Select-String -Pattern 'v3 final full-scale|69,480|6,690|0.940|0.939|0.891|0.785|0.771|0.150|wrong-sign|no real robot|Final Audit'
```
