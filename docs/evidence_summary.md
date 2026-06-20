# Full-Scale Evidence Summary

- Stage: v3 final full-scale complete.
- Seed: 23023.
- Rows: 69,480 policy rows.
- Cases: 6,690 task cases.
- Plot failures: 0.
- Runner: `experiments/full_scale_signed_cone.py`.
- Final PDF: `C:/Users/wangz/Downloads/23.pdf`.
- Final PDF verification: 25 pages, 360,190 bytes, SHA256 `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`.
- Final PDF link boxes: green citation/URL boxes = 53, red internal references
  = 3, cyan = 0, with one-point borders on all 56 link annotations.

## Headline Numbers

- Family A SCMP true-cone success: 0.940.
- Family A guarded SCMP success: 0.939.
- Family A estimated SCMP success: 0.938.
- Family A adaptive SCMP success: 0.938.
- Family A robust SCMP success: 0.937.
- Family A mean-gain compensation success: 0.932.
- Family A signed-fixed success: 0.891.
- Family A symmetric-derating success: 0.785.
- Family A nominal-branch success: 0.771.
- Family C SCMP-estimated success at calibration budget 0: 0.550; at budget 256: 0.830.
- Family G wrong-sign calibration SCMP-estimated success: 0.150; guarded SCMP: 0.200; true-cone SCMP: 0.933.

## Family Counts

- Family A ratio/task sweep: 40,320 rows over 3,360 cases.
- Family B asymmetry sources: 7,560 rows over 630 cases.
- Family C calibration budget and bias: 12,800 rows over 1,600 cases.
- Family D drift: 2,400 rows over 300 cases.
- Family E noise: 2,400 rows over 300 cases.
- Family F ablations: 1,120 rows over 140 cases.
- Family G negative controls: 2,880 rows over 360 cases.

## Claim Boundary

These results support a synthetic signed-actuator mechanism and policy-interface diagnostic. They do not establish real-robot manipulation performance, do not show universal superiority over full signed-bound MPC, and do not remove the need for correct calibration. The wrong-sign and shared-weak-sign controls are part of the evidence, not cleanup.
