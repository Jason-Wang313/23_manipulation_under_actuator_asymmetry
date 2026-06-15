# Hostile Reviewer Response

## Main Concern

The strongest objection is that SCMP assumes the signed actuator cone is correct. If the sign profile is wrong, the policy can choose a systematically bad primitive.

## V3 Response

The v3 paper does not hide this. It runs a 69,480-row full-scale suite with explicit calibration-budget, bias, drift, noise, ablation, and negative-control families. In the wrong-sign negative control, estimated SCMP reaches only 0.150 success and guarded SCMP reaches 0.200, while true-cone SCMP reaches 0.933. That is a failure case and a deployment guardrail, not a success claim.

## Revised Claim

SCMP is a policy representation for calibrated signed actuator authority. It is useful when primitives induce different signed actuator demands and the signed cone is correct enough to rank those primitives. It is not a method for unknown sign conventions, uncalibrated faults, or rapidly drifting actuator profiles without identification.

## Positive Evidence

Family A shows that the mechanism matters when the assumptions hold: true-cone SCMP reaches 0.940 success and guarded SCMP reaches 0.939, versus signed fixed branch 0.891, symmetric derating 0.785, and nominal branch 0.771. At ratio 5.0, guarded SCMP reaches 0.854 while symmetric derating reaches 0.298.

## Remaining Weakness

Online identification, real hardware validation, high-fidelity contact simulation, and a full signed-bound MPC/control-allocation baseline remain necessary for a stronger empirical submission.
