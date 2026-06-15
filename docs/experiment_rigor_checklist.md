# Experiment Rigor Checklist

- [x] Main simulator is deterministic from recorded seeds.
- [x] V3 full-scale runner records seed 23023 and family-level progress.
- [x] Directional asymmetry ratio sweep is included through ratio 5.0.
- [x] Task topology/branch-contrast sweep is included.
- [x] Baselines separate nominal fixed, nominal branch, mean-gain compensation, symmetric derating, signed fixed branch, true-cone SCMP, estimated SCMP, adaptive SCMP, guarded SCMP, robust SCMP, oracle one-step choice, and random branch selection.
- [x] Asymmetry-source sweep separates gain-only, limit-only, mixed gain/limit, same-sign weakness, flipped signs, and deadband-like profiles.
- [x] Calibration-budget and calibration-bias studies are included.
- [x] Drift and noise stress families are included.
- [x] Ablations separate margin, effort, switching, signed projection, and symmetric switching components.
- [x] Negative controls include symmetric actuation, no branch contrast, wrong-sign calibration, and shared weak positive profiles.
- [x] Plot generation recorded zero failures.
- [x] Final PDF text was checked for v3 marker, row/case counts, headline values, wrong-sign limitation, and no-real-robot limitation.
- [ ] No real robot or high-fidelity physics validation.
- [ ] No online identification baseline with real actuator data.
- [ ] No full constrained MPC/control-allocation baseline with the same signed bounds.

Decision: rigorous enough for a final synthetic mechanism paper under the scoped claims; not enough to claim hardware readiness or universal control dominance.
