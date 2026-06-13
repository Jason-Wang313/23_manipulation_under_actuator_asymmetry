# Hostile Reviewer Response

## Main Concern

The strongest objection is that SCMP assumes known sign-dependent gains and limits. If the signed cone is wrong, the policy may choose the wrong primitive or command infeasible motion.

## V2 Response

We added a calibration-error stress with true asymmetry ratio fixed at 4.0. SCMP reaches 0.863 success with correct calibration, remains 0.844 or better down to estimated ratio 2.0, but falls to 0.281 when the policy assumes symmetry.

## Revised Claim

SCMP is a policy representation for calibrated signed actuator authority. The paper no longer implies robustness to unknown or badly misestimated actuator asymmetry.

## Remaining Weakness

Online identification, real hardware validation, and a full signed-bound MPC baseline remain necessary for a main-track submission.
