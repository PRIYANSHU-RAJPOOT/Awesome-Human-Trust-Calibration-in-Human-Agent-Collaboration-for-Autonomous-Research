# Contribution pathway decision

## A. Reproduce under a justified new condition
Question: does an existing approach retain behavior under a justified new condition? Code: preserve baseline, add condition/configuration. Compute: low–moderate. Advantage: clean reproduction/adaptation distinction. Risk: arbitrary split/domain slice may be weak or underpowered. Evidence: faithful baseline audit, condition rationale, sample counts, split, metrics and uncertainty. Current assessment: no sufficiently justified extra condition selected.

## B. Controlled comparative robustness study
Question: how does retrieval corruption degrade evidence selection and final verification, and does a predefined checkpoint mitigate it? Code: separate corruption, checkpoint, runner and evaluator modules; baseline remains immutable. Compute: low–moderate with sparse retrieval. Advantage: directly tests the selected question and isolates intervention. Risks: unrealistic corruption, extra candidate budget, small dataset and limited external validity. Evidence: validated baseline, label-blind corruption, matched C1/C2 inputs, budget accounting, paired uncertainty and error analysis. **Recommended provisionally.**

## C. Targeted theoretical extension
Question: does a specific mechanism, such as uncertainty-aware checkpoint triggering, improve recovery? Code: one isolated extension. Compute: low–moderate for a rule, higher for learned mechanisms. Advantages: mechanism-level contribution if theoretically grounded. Risks: post-hoc threshold tuning, extra-compute confounding, complexity. Evidence: frozen rule, validation-only tuning, budget-matched control and ablation. Premature until B establishes a stable failure mode.

## Decision
Choose B provisionally. Do not claim novelty or gains. Main experiments are blocked until the baseline is audited and actually run.