# Paper 23 Full-Scale Execution Plan

## 2026-06-20 Visual-Hardening Addendum

The final v3 manuscript was rebuilt with the explicit VLA role-model hyperref
policy for boxed links. The Downloads artifact remains 25 pages and is now:

- Path: `C:/Users/wangz/Downloads/23.pdf`
- Size: 360,190 bytes
- SHA256: `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`
- Link-box inventory: green = 53, red = 3, cyan = 0, with one-point borders on
  all 56 link annotations.

## Current Claim

The current v2 paper argues that manipulation policies should expose signed actuator authority. When positive and negative actuator directions have different gains or limits, a manipulation policy should choose IK/contact primitives by feasibility inside signed actuator cones rather than by nominal object-space geometry or symmetric derating.

The current evidence is a small two-link planar manipulation proxy:

- Main suite: 4,800 episode rows.
- Methods: nominal fixed, nominal branch, mean gain, symmetric derating, signed fixed, signed cone policy.
- Ratios: 1.0, 1.5, 2.0, 3.0, 4.0.
- Key v2 result: at ratio 4.0, signed cone policy reaches 0.906 success versus nominal branch 0.500, signed fixed 0.613, and symmetric derating 0.544.
- Calibration stress: true ratio 4.0, estimated ratio swept from 4.0 to 1.0. SCMP reaches 0.863 when calibrated correctly and falls to 0.281 when it assumes symmetry.

The paper is currently too short and too narrow for the user's full-scale standard. The v3 goal is not to inflate the same result. It is to turn the paper into a final 25+ page synthetic mechanism paper with larger evidence, stronger baselines, explicit failure cases, and a clear nonclaim boundary.

## Main Gaps To Close

1. **Scale gap:** 4,800 rows is not enough for the requested final version. The v3 suite should be at least an order of magnitude larger while remaining RAM-light.
2. **Regime gap:** The current simulator varies only asymmetry ratio and calibration error. It needs actuator-limit asymmetry, gain asymmetry, mixed sign patterns, drift, partial faults, command noise, observation noise, and branch/contact contrast levels.
3. **Baseline gap:** Current baselines do not include a constrained-MPC-like oracle, learned classifier/regressor, robust min-max branch choice, adaptive online identification, or randomized policy selection.
4. **Ablation gap:** The current method mixes signed projection, primitive switching, margin reward, and switching penalty. These need to be separated.
5. **Calibration gap:** V2 shows collapse under bad calibration. V3 should measure sample-budget identification, drift, biased calibration, and confidence-gated fallback.
6. **Failure gap:** The paper must state when signed cones do not help: symmetric actuation, no branch contrast, incorrect signed profile, high noise, rapidly drifting faults, or tasks where all primitives share the same weak direction.
7. **Writing gap:** The manuscript needs deeper related work, full method specification, formal boundary propositions, experiment details, result ledgers, limitations, deployment guardrails, falsification criteria, and reproducibility artifacts.

## V3 Method Upgrade

Keep the core Signed-Cone Manipulation Policy (SCMP), but add a calibrated and guarded variant:

- **SCMP:** known signed actuator cone, primitive selection by signed projection error, effort, margin, and switching cost.
- **Adaptive SCMP:** estimates positive/negative gains from a small calibration budget and updates them online.
- **Guarded SCMP:** uses signed-cone policy only when estimated cone uncertainty is low enough; otherwise falls back to symmetric derating or robust min-max.
- **Robust signed cone:** selects the primitive whose projected error is best under lower-confidence signed authority bounds.

The paper should not pretend these variants are mature robot controllers. They are diagnostic policies for testing how actuator-asymmetry information should enter primitive selection.

## Experiment Families

### Family A: Full-Scale Ratio And Topology Sweep

Purpose: reproduce and scale the original result across task families.

Variables:

- Ratios: 1.0, 1.25, 1.5, 2.0, 3.0, 4.0, 5.0.
- Task families: reach-push, lateral carry, corner approach, near-singular approach, high-branch-contrast, low-branch-contrast.
- Seeds per condition selected to produce a large but RAM-light run.

Metrics:

- Success rate.
- Final error.
- Tracking error.
- Saturations.
- Effort.
- Signed margin.
- Branch switches.
- Regret to feasible oracle.

Expected honest outcome:

- SCMP should help most at high asymmetry and high branch contrast.
- Gains should be small when ratio is near 1 or branch contrast is low.

### Family B: Actuator Asymmetry Source Sweep

Purpose: separate gain asymmetry, limit asymmetry, mixed gain/limit asymmetry, deadband, backlash-like weak regions, and sign-pattern flips.

Variables:

- Gain-only asymmetry.
- Limit-only asymmetry.
- Gain-plus-limit asymmetry.
- Joint-1 weak-positive/joint-2 weak-negative pattern.
- Same-sign weak directions.
- Random sign pattern.
- Actuator deadband/no-response zone.

Expected honest outcome:

- SCMP should help when primitive choice changes the sign pattern.
- It may not help when every primitive requires the same weak signs.

### Family C: Calibration Budget And Bias

Purpose: expand the v2 calibration stress into a full sample-budget study.

Variables:

- Calibration samples: 0, 4, 8, 16, 32, 64, 128, 256.
- Bias cases: assume symmetry, underestimate ratio, overestimate ratio, wrong weak sign, noisy gains.
- Policies: SCMP with true cone, estimated SCMP, adaptive SCMP, guarded SCMP, robust signed cone, symmetric derating.

Expected honest outcome:

- True-cone SCMP should be an upper mechanism reference.
- Estimated SCMP should fail with wrong sign or tiny sample budget.
- Guarded/robust variants should trade peak performance for safer degradation.

### Family D: Drift And Online Identification

Purpose: test whether signed-cone policy survives actuator profiles that change during a task.

Variables:

- No drift.
- Slow monotone gain loss.
- Sudden weak-direction fault.
- Thermal-like recovery.
- Alternating drift across joints.

Metrics:

- Success before and after drift.
- Identification error.
- Saturation bursts.
- Recovery time.

Expected honest outcome:

- Fixed SCMP can fail under drift.
- Adaptive/guarded variants should reduce catastrophic collapse but may add tracking error.

### Family E: Noise And Disturbance Robustness

Purpose: ensure the result is not only a deterministic simulator artifact.

Variables:

- Command noise.
- Object motion noise.
- Sensor noise on end-effector/object position.
- Jacobian/model noise.
- Contact-slip disturbance.

Expected honest outcome:

- Signed cones should still help under moderate noise.
- Under severe noise, all methods degrade and learned/adaptive baselines may be competitive.

### Family F: Ablations

Purpose: isolate SCMP components.

Ablations:

- No margin term.
- No effort term.
- No switching penalty.
- Signed projection but no primitive switching.
- Primitive switching with symmetric derating.
- Oracle primitive choice with true post-execution error.
- Wrong branch-contrast sampler disabled.

Expected honest outcome:

- Primitive switching and signed projection should both matter.
- Margin may mainly reduce saturation and effort rather than maximize success.

### Family G: Negative Controls

Purpose: prevent overclaiming.

Controls:

- Perfectly symmetric actuators.
- No branch contrast.
- Goals where both branches share weak signs.
- Random primitive labels.
- Unreachable or near-singular tasks.
- Wrong sign calibration.

Expected honest outcome:

- SCMP advantage should disappear or reverse when signed authority is irrelevant or misestimated.

## Baselines

Minimum v3 policy set:

- Nominal fixed branch.
- Nominal branch by joint-speed norm.
- Mean-gain compensation.
- Symmetric derating.
- Signed fixed branch.
- SCMP true cone.
- Estimated SCMP.
- Adaptive SCMP.
- Guarded SCMP.
- Robust lower-bound signed cone.
- Oracle primitive choice using true one-step tracking error.
- Constrained-QP/MPC-like local oracle with true signed bounds and no switching penalty.
- Random branch policy as a sanity check.

## RAM-Light Execution Strategy

- Run one family at a time.
- Stream rows to CSV instead of holding all rows in memory.
- Use compact per-row dictionaries and aggregate summaries after each family.
- Save progress JSON after each family.
- Generate figures after summaries are written.
- Avoid multiprocessing unless necessary; sequential execution is acceptable.
- Keep episode horizon modest but increase condition/seed coverage.
- Use deterministic seeds and family-specific seed offsets.

## Figures And Tables

Required figures:

- Main success/error by ratio and task family.
- Asymmetry-source sweep.
- Calibration-budget/bias curves.
- Drift and online-identification curves.
- Noise robustness.
- Ablation success/regret/margin.

Required tables:

- Main full-scale benchmark.
- Asymmetry-source summary.
- Calibration-budget summary.
- Drift summary.
- Noise summary.
- Ablation summary.
- Negative-control summary.
- Claim-to-evidence map.

## Manuscript Expansion Strategy

The final manuscript must reach at least 25 pages from real content:

- Core paper: abstract, introduction, related work, problem setup, method, formal propositions, simulator, policies, results, discussion, limitations.
- Appendices: full execution protocol, simulator details, policy pseudocode, metric definitions, family-by-family result ledgers, calibration failure analysis, drift/noise analysis, ablations, negative controls, deployment guardrails, falsification criteria, reproducibility statement, artifact manifest, final audit.

No padding. Length should come from experiment breadth, exact result interpretation, tables/figures, and explicit failure cases.

## Final Acceptance Checklist

Before exporting to Downloads:

- `paper/main.pdf` builds locally.
- PDF is at least 25 pages.
- PDF text contains `v3 final full-scale`.
- PDF text contains final row/case counts and headline metrics.
- Manuscript states no real-robot validation.
- Manuscript states calibration and drift failure cases.
- Manuscript states when SCMP does not help.
- `docs/evidence_summary.md` exists and matches the final numbers.
- `docs/experiment_report.md`, `docs/final_audit.md`, and reproducibility docs are updated.
- Final PDF copied to `C:/Users/wangz/Downloads/23.pdf`.
- Local `paper/main.pdf` removed after export.
- Final PDF page count, bytes, and SHA256 recorded.
- Repo committed, pushed, clean, and `HEAD == @{u}` before moving to Paper 24.
