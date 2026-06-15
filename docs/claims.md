# Claims

## Supported By Formal Argument

1. For a fixed primitive with a linear local map from actuator velocity to object velocity and known sign-dependent actuator bounds, signed-cone projection returns the closest feasible object velocity under a squared-error objective.
2. Symmetric derating is conservative whenever at least one actuator has unequal positive/negative bounds; it replaces the signed cone by its symmetric intersection and can discard feasible one-direction motions.
3. If candidate primitives induce different actuator-sign demands, signed feasibility can change primitive ranking even when nominal object-space geometry ranks them differently.

## Supported By Runnable V3 Evidence

1. In the full-scale planar manipulation proxy, SCMP true-cone reaches 0.940 success and guarded SCMP reaches 0.939 across Family A, compared with signed fixed branch 0.891, symmetric derating 0.785, and nominal branch 0.771.
2. The advantage is strongest when asymmetry and branch contrast are meaningful. At ratio 5.0, guarded SCMP reaches 0.854 and true-cone SCMP 0.838, compared with symmetric derating 0.298 and nominal branch 0.442.
3. V3 separates gain/limit sources, calibration budget, bias, drift, noise, ablations, and negative controls over 69,480 policy rows and 6,690 task cases.
4. Calibration is required. In the wrong-sign negative control, estimated SCMP reaches 0.150 and guarded SCMP reaches 0.200, while true-cone SCMP reaches 0.933.
5. Primitive switching and signed projection both matter: ablations reduce success relative to true-cone SCMP, and symmetric switching remains weak.

## Plausible But Not Fully Proven

1. The same mechanism should help real contact-rich manipulation where IK branch, grasp side, or contact mode choices induce different signed actuator demands.
2. Signed-cone policy structure should compose with learned high-level policies as an action interface, but this paper does not train a learned policy.
3. Guarded or robust signed cones may be useful deployment guardrails, but they require better online calibration and safety evaluation.

## Unsupported And Therefore Not Claimed

1. No claim of real-robot validation.
2. No claim that SCMP solves unknown, wrong-sign, or rapidly time-varying actuator faults without identification.
3. No claim that the simple simulator is a benchmark for the field.
4. No claim that the method dominates full constrained MPC or control allocation on all tasks.
5. No claim of robustness to badly misestimated signed cones.
6. No claim that SCMP helps when primitives have no signed-authority contrast.
