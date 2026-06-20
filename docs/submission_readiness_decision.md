# Submission Readiness Decision

Decision: ready as a final full-scale synthetic mechanism paper under the stated scope.

## Why It Is Ready For The Batch Standard

- The final manuscript is 25 pages and exported to `C:/Users/wangz/Downloads/23.pdf`.
- The final PDF is verified: 25 pages, 360,190 bytes, SHA256 `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`.
- VLA-style link boxes are verified: green citations/URLs, red internal
  references, no cyan boxes, one-point borders.
- The v3 suite contains 69,480 policy rows over 6,690 task cases with zero plot failures.
- The paper includes ratio/task, asymmetry-source, calibration, drift, noise, ablation, and negative-control families.
- The manuscript includes positive findings and failure cases rather than padding.
- The text states no real-robot validation, calibration limitations, and non-universal regimes.

## Why The Scientific Claim Is Still Scoped

- Evidence is a simplified planar proxy.
- No hardware or high-fidelity contact simulation is included.
- Wrong-sign calibration can be catastrophic.
- Full constrained MPC/control allocation with signed bounds is not implemented as a strongest baseline.

## Required Next Work For Main-Track Empirical Strength

- Add online signed-authority identification.
- Compare against full constrained MPC/control allocation with the same signed bounds.
- Validate on hardware or high-fidelity contact simulation.
- Test smooth primitive transitions and safety under switching.
