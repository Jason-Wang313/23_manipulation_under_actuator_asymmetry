# Reviewer Attacks

## Attack 1: This is just constrained control.
Response: constrained control projects commands, but the paper's boundary is policy structure. SCMP evaluates manipulation primitives through signed actuator cones before execution; the chosen primitive can change because of directional authority.

## Attack 2: Fault-tolerant control already handles actuator problems.
Response: fault-tolerant control usually assumes diagnosis/reconfiguration around faults. SCMP addresses persistent positive/negative asymmetry even when no actuator has failed and no discrete fault label exists.

## Attack 3: Domain randomization could learn this.
Response: it might, if the randomized support includes sign asymmetry and enough data. That is not a mechanism. SCMP exposes the structure analytically and works without RL or a larger model.

## Attack 4: The simulator is too simple.
Response: accepted. The simulator is evidence for the broken assumption and mechanism, not a claim of real-robot readiness. The final audit should mark the paper as revise/workshop unless stronger physical validation is added.

## Attack 5: The method requires known actuator asymmetry.
Response: yes. Identification is left open. The paper can use calibration or telemetry, and should not claim robustness to unknown asymmetry.

## Attack 6: Switching IK/contact primitives may be discontinuous.
Response: the implementation includes a switch penalty, but smooth transition planning is not solved. The contribution is local policy structure; global transition feasibility is future work.

## Attack 7: Symmetric derating is an unfairly conservative baseline.
Response: it represents a common robust response to asymmetric uncertainty. The paper also compares mean-gain and signed fixed-branch baselines to separate compensation from primitive selection.