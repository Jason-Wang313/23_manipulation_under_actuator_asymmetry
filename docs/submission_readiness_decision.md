# Submission Readiness Decision

Decision: workshop-only / strong-revise.

## Why Not Submit-Ready

- Evidence is a simplified planar proxy.
- No hardware or high-fidelity contact simulation is included.
- V2 shows SCMP collapses when the signed actuator cone is badly misestimated.
- Full constrained MPC or control allocation with signed bounds is not implemented as a strongest baseline.

## Why Not Kill

- The signed-cone action interface is crisp and falsifiable.
- The main ratio sweep shows a clear policy-level primitive-selection effect.
- The v2 stress makes the calibration boundary honest rather than hiding it.

## Required Next Work For Main-Track Strength

- Add online signed-authority identification.
- Compare against full constrained MPC/control allocation with the same signed bounds.
- Validate on hardware or high-fidelity contact simulation.
- Test smooth primitive transitions and safety under switching.
