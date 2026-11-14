# Frozen comparison protocol — pre-experiment draft

## Conditions
- C0: clean retrieval, no checkpoint.
- C1: corrupted retrieval, no checkpoint.
- C2: exact same corrupted candidates as C1, with checkpoint/recovery.
- C3 optional: clean retrieval with checkpoint.

## Controls
1. Same claim IDs, split, corpus snapshot, tokenizer, retrieval implementation, top-k and evaluator.
2. C1 and C2 receive identical corrupted candidate IDs for each claim and seed.
3. Distractor selection must not inspect gold evidence IDs, labels or rationales.
4. Checkpoint is label-blind and frozen before the main evaluation.
5. Record candidates, retrieval calls and runtime. Add budget-matched control if C2 gets more retrieval budget.
6. Never tune on hidden test labels. Development-set outcomes must be described as dev-set evidence.
7. Confirm official SciFact treatment of SUPPORT, CONTRADICT and NOT ENOUGH INFO before metric code is frozen.

## Seeds and analysis
Planned seeds: 13, 37, 73, 101, 137. Pair by claim ID. Repeated seeds are perturbation replicates, not independent claims. Planned primary outcome is macro-F1; primary contrast C2−C1. Use paired bootstrap intervals only after confirming per-claim paired outputs and appropriate resampling assumptions. No significance claim without a valid test.

## Corruption
Candidate pilot policy: replace/demote one top-ranked abstract with a lexical-similarity-band distractor selected from text-only signals. Exact pool, band and rules remain unset until pilot. The implementation must not access gold fields.

## Checkpoint
A label-blind validation rule followed by expanded retrieval is considered. If no defensible adaptive trigger is available, use a fixed expanded-retrieval recovery pass and do not call it adaptive. Thresholds, if any, are pilot/validation-only and frozen before main results.

## Planned error taxonomy
Retrieval unchanged; relevant evidence displaced; distractor selected; correct evidence/wrong label; checkpoint missed trigger; unnecessary trigger; evidence recovered/final label wrong; checkpoint regression.

## Gate
No main comparison before clean baseline, official evaluator and data split are validated.