# AI assistance and debugging provenance

| Case | Assistance | Verification/state |
|---|---|---|
| Gap mapping | Organized gaps stated in supplied literature review | Candidate mapping; novelty not verified |
| Baseline choice | Suggested SciFact and official TF-IDF baseline | Source, code, license, dependencies and evaluator audit pending |
| Environment | Proposed dependencies and Colab diagnostics | Must run in actual Colab |
| Retrieval utility | Generic shared-vocabulary TF-IDF smoke module | Not claimed as official SciFact reproduction |
| DBG-001 | Synthetic example of independently fitted TF-IDF vocabularies | Teaching case, not a real user failure |
| Study design | Proposed C0/C1/C2/C3 paired conditions | Protocol must be frozen before main run |
| Evaluation | Generated claim-label validation/metric scaffold | Must run on real per-claim predictions; evidence metrics require evidence traces |

Human accountability: student must understand, run, inspect and explain submitted code. AI-generated code/text are drafts, not evidence. No synthetic data, fabricated results or imagined execution logs are to be reported as real experiments.