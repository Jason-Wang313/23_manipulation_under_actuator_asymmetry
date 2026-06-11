# Claims

## Supported by Formal Argument
1. For a fixed primitive with linear local map from actuator velocity to object velocity and known sign-dependent actuator bounds, signed-cone projection returns the closest feasible object velocity under a squared-error objective.
2. Symmetric derating is conservative whenever at least one actuator has unequal positive/negative bounds; it replaces the signed cone by its symmetric intersection and can discard feasible one-direction motions.

## Supported by Runnable Evidence
1. In the provided planar manipulation proxy, actuator asymmetry causes nominal and mean-gain policies to saturate or accumulate directional tracking error as the asymmetry ratio grows.
2. Selecting primitives with signed-cone projected error and margin improves success and final error relative to fixed-branch and symmetric derating baselines in the simulator.

## Plausible but Not Fully Proven
1. The same mechanism should help real contact-rich manipulation where IK branch, grasp side, or contact mode choices induce different signed actuator demands.
2. Signed-cone policy structure should compose with learned high-level policies as an action interface, but this paper does not train a learned policy.

## Unsupported and Therefore Not Claimed
1. No claim of real-robot validation.
2. No claim that SCMP solves unknown or rapidly time-varying actuator faults without identification.
3. No claim that the simple simulator is a benchmark for the field.
4. No claim that the method dominates full constrained MPC on all tasks.