# Child Status

Stage: v3 final full-scale complete; VLA link-box hardening exported and
verified.

Current facts:
- V1/V2 repository was already published at `https://github.com/Jason-Wang313/23_manipulation_under_actuator_asymmetry`.
- V2 added calibration-error stress: true ratio 4.0, SCMP 0.863 success with correct calibration and 0.281 when assuming symmetry.
- V3 full-scale plan was written first in `docs/full_scale_execution_plan.md`.
- V3 full-scale runner `experiments/full_scale_signed_cone.py` completed with seed 23023.
- V3 suite produced 69,480 policy rows over 6,690 task cases with zero plot failures.
- Family coverage: ratio/task sweep, asymmetry-source sweep, calibration budget and bias, drift, noise, ablations, and negative controls.
- Final manuscript source is `paper/main.tex` and contains the marker `v3 final full-scale`.
- Final LaTeX build completed with pdflatex, bibtex, pdflatex, pdflatex all exiting 0.
- Final PDF was exported to `C:/Users/wangz/Downloads/23.pdf`.
- Verified final PDF: 25 pages, 360,190 bytes, SHA256 `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`.
- Final PDF link boxes: green citation/URL boxes = 53, red internal references
  = 3, cyan = 0, with one-point borders on all 56 link annotations.
- Final PDF text check found the v3 marker, 69,480 rows, 6,690 cases, headline success values, wrong-sign calibration failure, no-real-robot limitation, and final audit marker.
- Local `paper/main.pdf` was removed after export.

Key v3 results:
- Family A aggregate: SCMP true-cone 0.940 success, guarded SCMP 0.939, signed fixed branch 0.891, symmetric derating 0.785, nominal branch 0.771.
- High asymmetry remains the core positive result: at ratio 5.0, guarded SCMP reaches 0.854 and true-cone SCMP 0.838, versus symmetric derating 0.298 and nominal branch 0.442.
- Calibration is a real boundary: wrong-sign calibration drives estimated SCMP to 0.150 and guarded SCMP to 0.200 while true-cone SCMP reaches 0.933.
- Negative controls are explicit: gains disappear or become irrelevant under symmetric actuation, no branch contrast, and misestimated sign profiles.

Remaining limitations:
- No real robot or high-fidelity contact simulation.
- No full constrained-MPC/control-allocation baseline with identical signed bounds.
- Calibration, sign conventions, and actuator drift remain deployment-critical.
- The paper should be read as a full-scale synthetic mechanism paper, not a hardware performance claim.
