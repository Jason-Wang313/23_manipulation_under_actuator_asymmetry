# Experiment Rigor Checklist

- [x] Main simulator is deterministic from recorded seeds.
- [x] Directional asymmetry ratio sweep is included.
- [x] Baselines separate nominal branch selection, mean-gain compensation, symmetric derating, signed fixed branch, and signed-cone primitive selection.
- [x] V2 calibration-error stress attacks the known-asymmetry assumption.
- [x] Negative v2 result is included in the paper and docs.
- [ ] No real robot or high-fidelity physics validation.
- [ ] No online identification baseline.
- [ ] No full constrained MPC / control-allocation baseline.

Decision: rigorous enough for workshop-only / strong-revise positioning; not enough for full submission claims.
