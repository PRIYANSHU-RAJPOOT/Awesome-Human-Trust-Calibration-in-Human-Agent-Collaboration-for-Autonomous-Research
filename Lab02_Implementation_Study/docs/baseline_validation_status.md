# Baseline validation status

**Candidate:** official SciFact TF-IDF retrieval/verification baseline.  
**Dataset:** SciFact.  
**Status:** BLOCKED — actual source code, commit, run configuration, dataset partition, logs, predictions and measured results have not been supplied in the available evidence.

## VERIFIED
- SciFact is the proposed benchmark and official repository/paper are identified.
- The research question and candidate conditions have been scoped.

## UNCERTAIN
- Compatibility of official code with the current Colab runtime.
- Whether the run uses the official TF-IDF baseline/evaluator.
- Exact preprocessing, top-k, vocabulary fitting, split, labels and exclusions.
- Dataset commit, checksums and artifact-specific licenses.

## Required checks
1. Exact code/repository commit and run command.
2. Actual Colab environment output and pip check.
3. Dataset commit, schema, checksums, split and class/sample counts.
4. Preprocessing, retrieval, hyperparameters, seeds and metric conventions versus official source.
5. Evaluator sanity cases and manual prediction inspection.
6. Save per-claim predictions and full logs.
7. Record all adaptations; do not claim exact reproduction if the method differs.

A script running successfully is not enough to validate methodology. Exact numerical equality across environments is not required, but procedural fidelity must be established.