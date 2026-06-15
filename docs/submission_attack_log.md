# Submission Attack Log

Updated: 2026-06-15 02:31 +01:00

## V3 Attack Rounds

1. **"The paper is too small."** Replaced the narrow 4,800-row v2 study with a 69,480-row full-scale suite over 6,690 task cases.
2. **"SCMP assumes the signed actuator cone is known."** Added calibration-budget, calibration-bias, wrong-sign, drift, and guarded/robust policy variants.
3. **"The method may collapse if calibration is wrong."** Confirmed and foregrounded. Wrong-sign calibration drives estimated SCMP to 0.150 and guarded SCMP to 0.200.
4. **"Signed-cone primitive selection may just be generic compensation."** Added mean-gain, signed fixed, robust, guarded, oracle, random, and ablation comparisons. Mean gain is strong at 0.932, so the claim is narrowed to primitive selection under signed branch contrast.
5. **"Symmetric derating is a weak baseline."** Kept derating but no longer relies on it alone; V3 compares against multiple compensation and oracle-like policies.
6. **"The result will vanish in irrelevant regimes."** Added negative controls for symmetric actuation, no branch contrast, shared weak signs, and wrong sign estimates.
7. **"No hardware validation."** Still unresolved and stated clearly in the paper, audit, and reproducibility docs.
8. **"Full constrained MPC remains a stronger baseline."** Still unresolved and listed as required next work.

## Terminal Assessment

The artifact is now final for the batch standard: 25-page PDF, full-scale synthetic evidence, explicit positive and negative findings, and verified export to Downloads. The research claim remains scoped: calibrated signed-cone primitive selection improves a synthetic manipulation proxy in regimes with meaningful signed-authority contrast. Hardware readiness and universal control dominance are not claimed.
