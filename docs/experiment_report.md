# V3 Full-Scale Experiment Report

## Execution

- Runner: `experiments/full_scale_signed_cone.py`.
- Seed: 23023.
- Rows: 69,480 policy rows.
- Cases: 6,690 task cases.
- Plot failures: 0.
- Output root: `results/full_scale/`.
- Figure root: `figures/full_scale/`.
- Table root: `results/full_scale/tex/`.

The suite was run sequentially and wrote family-level rows/summaries to disk to keep RAM use modest. The final manuscript consumes generated tables and figures directly from the full-scale output folders.

## Families

- Family A: ratio/task sweep, 40,320 rows over 3,360 cases.
- Family B: asymmetry-source sweep, 7,560 rows over 630 cases.
- Family C: calibration budget and bias, 12,800 rows over 1,600 cases.
- Family D: drift, 2,400 rows over 300 cases.
- Family E: noise, 2,400 rows over 300 cases.
- Family F: ablations, 1,120 rows over 140 cases.
- Family G: negative controls, 2,880 rows over 360 cases.

## Main Interpretation

Family A supports the core mechanism. True-cone SCMP reaches 0.940 success and guarded SCMP reaches 0.939, while signed fixed branch reaches 0.891, symmetric derating 0.785, and nominal branch 0.771. Mean-gain compensation is strong at 0.932, so the paper should not claim that any signed information is enough; the specific contribution is signed-cone primitive selection under branch/sign contrast.

The result is regime-dependent. At ratio 1.0, nearly all sensible methods are near ceiling. At ratio 5.0, guarded SCMP reaches 0.854 and true-cone SCMP 0.838, while symmetric derating reaches 0.298 and nominal branch reaches 0.442. The strongest evidence is therefore not a universal aggregate win; it is the high-asymmetry, branch-contrast failure of symmetric or nominal action interfaces.

## Calibration And Failure

Calibration is the main deployment boundary. In Family C, estimated SCMP improves with calibration budget but is not monotone, reflecting estimator variance and task mix. In Family G, wrong-sign calibration is catastrophic: estimated SCMP reaches 0.150 success and guarded SCMP reaches 0.200, while true-cone SCMP reaches 0.933. This belongs in the paper as a first-class result.

## Negative Controls

Negative controls prevent overclaiming. With symmetric actuation or no branch contrast, the SCMP advantage shrinks or disappears. With shared weak signs or wrong sign estimates, estimated signed-cone policies can be worse than random branch selection. These controls narrow the claim to calibrated signed actuator authority with meaningful primitive-sign diversity.

## Final Artifact

The final PDF exported to `C:/Users/wangz/Downloads/23.pdf` is 25 pages, 360,190 bytes, SHA256 `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`. Text extraction confirms the v3 marker, row/case counts, headline results, wrong-sign failure, no-real-robot limitation, and final audit marker. The VLA-style link-box audit has 53 green citation/URL boxes, 3 red internal-reference boxes, no cyan boxes, and one-point borders on all 56 link annotations.
