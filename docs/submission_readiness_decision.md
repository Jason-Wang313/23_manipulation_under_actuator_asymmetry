# Submission Readiness Decision

Decision: ready as a final full-scale synthetic mechanism paper under the stated scope.

## Why It Is Ready For The Batch Standard

- The final manuscript is 25 pages and exported to `C:/Users/wangz/Downloads/23.pdf`.
- The final PDF is verified: 25 pages, 360,190 bytes, SHA256 `84342525B234DFCBF4F1D23DD11349BDF2D179953A42A0110D60078403247519`.
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
