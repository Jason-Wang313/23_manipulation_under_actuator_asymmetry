# Reviewer Attacks

## Attack 1: This is just constrained control.

Response: constrained control projects commands, but the paper's boundary is policy structure. SCMP evaluates manipulation primitives through signed actuator cones before execution; the chosen primitive can change because of directional authority.

## Attack 2: Fault-tolerant control already handles actuator problems.

Response: fault-tolerant control usually assumes diagnosis/reconfiguration around faults. SCMP addresses persistent positive/negative asymmetry even when no actuator has failed and no discrete fault label exists.

## Attack 3: Domain randomization could learn this.

Response: it might, if the randomized support includes sign asymmetry and enough data. That is not a mechanism. SCMP exposes the structure analytically and works without RL or a larger model.

## Attack 4: The simulator is too simple.

Response: accepted. V3 expands the synthetic evidence to 69,480 rows and seven experiment families, but it is still a planar proxy. The paper must not claim real-robot performance.

## Attack 5: The method requires known actuator asymmetry.

Response: yes. V3 makes this central. Estimated SCMP improves with calibration in some settings, but wrong-sign calibration drops estimated SCMP to 0.150 and guarded SCMP to 0.200. Identification is an assumption and a future-work requirement.

## Attack 6: Switching IK/contact primitives may be discontinuous.

Response: the implementation includes a switch penalty, but smooth transition planning is not solved. The contribution is local policy structure; global transition feasibility is future work.

## Attack 7: Symmetric derating is an unfairly conservative baseline.

Response: it represents a common robust response to asymmetric uncertainty. V3 also compares mean-gain compensation, signed fixed branch, robust signed cones, guarded SCMP, adaptive SCMP, oracle one-step choice, and random branch selection.

## Attack 8: Mean-gain compensation is already strong.

Response: correct. Mean gain reaches 0.932 in Family A, close to SCMP true-cone at 0.940. The paper should frame the contribution around high-ratio, high-branch-contrast regimes, negative controls, and interpretability rather than pretending a large aggregate win over every compensation baseline.

## Attack 9: Wrong calibration makes the method unsafe.

Response: correct. Wrong-sign calibration is a first-class failure result. Deployment needs sign-convention tests, confidence gates, low-force calibration, and fallback behavior before signed-cone primitive selection is trusted.
