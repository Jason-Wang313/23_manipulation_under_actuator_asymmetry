# Plan

## Objective
Produce a complete, runnable robotics paper package for paper 23, beginning from the seed "Manipulation Under Actuator Asymmetry" but choosing the final thesis only after a broad prior-work audit.

## Execution Stages
1. Initialize run bookkeeping.
   - Maintain `child_status.md` with stage, commands, failures, and recovery.
   - Inspect existing artifacts from any previous attempt and reuse valid caches.
2. Build the literature landscape.
   - Collect at least 1000 robotics/control/manipulation papers into `docs/related_work_matrix.csv`.
   - Perform a 300-paper serious skim and a 200-250-paper deep-read subset using available metadata/abstracts.
   - Build a 100-paper hostile prior-work set.
   - Write `docs/literature_map.md`, `docs/hostile_prior_work.md`, and `docs/novelty_boundary_map.md`.
3. Decide the paper direction.
   - Define the field box.
   - Identify at least 20 hidden assumptions that may be false.
   - Generate candidate directions that break assumptions.
   - Choose the strongest central mechanism and document the decision in `docs/novelty_decision.md`.
4. Produce evidence.
   - Implement a small runnable manipulation/control simulation showing why actuator asymmetry matters.
   - Compare the proposed mechanism against symmetric or naive baselines.
   - Save code, results, plots, and reproducibility instructions.
5. Write the paper.
   - Use the latest official ICLR LaTeX template available at runtime.
   - Write an anonymous ICLR-style paper with honest claims.
   - Sanitize bibliography and LaTeX for pdfLaTeX.
6. Verify and package.
   - Run experiments and paper build with explicit timeouts.
   - Save final PDF only to `C:/Users/wangz/Downloads/23.pdf`.
   - Create/push public GitHub repo `23_manipulation_under_actuator_asymmetry`, or document failure.
   - Write `docs/final_audit.md` with the required audit answers.

## Safety Rules
- Use non-interactive commands only.
- Avoid bare probes that may abort on nonzero exit.
- Use explicit timeouts for long scripts and LaTeX builds.
- Do not delete useful existing artifacts unless they are demonstrably invalid.
