# Novelty Decision

## Chosen Thesis
Manipulation policies should not hide actuator asymmetry inside generic robustness. When positive and negative authority differ, the policy should expose signed actuator cones and choose contact/IK primitives by their projected object-motion feasibility and remaining signed margin.

## New Central Mechanism
**Signed-Cone Manipulation Policy (SCMP):** factor each actuator command into positive and negative nonnegative channels; for each candidate manipulation primitive, project the desired local object velocity into the primitive's signed actuator cone; execute the primitive with the lowest projected object error and highest signed margin.

## Why This Replaces the Seed Instead of Merely Restating It
The seed said to make actuator asymmetry explicit. The literature sweep sharpened that into a policy-structure claim: asymmetry must enter before primitive selection, not as an afterthought in a low-level compensator.

## Why Forbidden Weak Moves Are Avoided
- No bigger model: experiments use a small analytic controller.
- No better data: no learned policy or training set is used.
- No benchmark-only contribution: the benchmark supports the signed-cone mechanism.
- No generic uncertainty wrapper: the action set is structurally refactored into signed channels.
- No active learning, verifier, LLM planner, or RL.
- Not merely combining modules: primitive selection and actuator feasibility are fused in one signed-cone objective.

## Minimal Formal Claim
For a fixed local primitive with linear object map `B` and sign-dependent diagonal actuator gains/limits, the SCMP projection solves the Euclidean closest feasible object velocity over the exact signed actuator cone. If a symmetric derating policy uses the intersection of positive and negative directional bounds, there exist desired velocities and primitive pairs where derating fails to realize a feasible object motion that SCMP realizes.

## Evidence Plan
Use a two-link planar manipulation proxy where the same object velocity can be attempted through elbow-up or elbow-down primitives. Directional weakness is assigned to opposite joint signs. Compare nominal fixed, nominal branch, mean-gain compensation, symmetric derating, signed fixed, and SCMP across asymmetry ratios.