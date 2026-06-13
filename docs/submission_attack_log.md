# Submission Attack Log

Updated: 2026-06-13 03:23:00 +01:00

## V2 Attack Rounds

1. **"SCMP assumes the signed actuator cone is known."** Added a calibration-error stress with true asymmetry ratio fixed at 4.0 and estimated ratios from 4.0 down to 1.0.
2. **"The method may collapse if calibration is wrong."** Confirmed. SCMP reaches 0.863 success with correct calibration and 0.281 when it assumes symmetry.
3. **"Signed-cone primitive selection may just be compensation."** The stress still separates SCMP from signed fixed branch under moderate calibration, but the claim is conditional.
4. **"Full constrained MPC remains a stronger baseline."** Still unresolved; listed as required next work.
5. **"No hardware validation."** Still unresolved; decision remains workshop-only / strong-revise.

## Terminal Assessment

The recoverable overclaim was addressed by adding a calibration stress and narrowing the claim. Remaining weaknesses require real hardware or high-fidelity simulation, online identification, and a full signed-bound MPC comparison.
