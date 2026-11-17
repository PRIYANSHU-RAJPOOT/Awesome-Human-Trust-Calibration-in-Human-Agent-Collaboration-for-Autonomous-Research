# Baseline validation status

**Candidate official baseline:** SciFact TF-IDF retrieval/verification pipeline.  
**Current implemented experiment:** custom TF-IDF and BM25 evidence-document retrieval comparison with controlled corruption and BM25+RRF recovery.  
**Status:** Custom retrieval experiment executed on 300 labelled development claims. Exact reproduction of the official end-to-end SciFact pipeline remains unverified.

## VERIFIED FROM THE CORRECTED COLAB OUTPUT
- SciFact corpus: 5,183 abstracts.
- Labelled development claims: 300; test claims: 300, with no public evidence annotations in the downloaded test file.
- Python 3.13.18; scikit-learn 1.6.1.
- Dataset archive SHA-256: `11c621288d41ac144d29b13b0f8503b3820b7d6e8b1f6ff24dff335c196d76be`.
- Four conditions executed: clean TF-IDF, corrupted TF-IDF, BM25+RRF recovery, and clean BM25.
- Primary evidence-bearing subset: 188 claims; 112 claims had empty evidence mappings.
- Primary macro-F1: C0 0.3786; C1 0.0938; C2 0.1603; C3 0.4212.
- C2−C1 macro-F1 difference: 0.06649; paired claim-bootstrap 95% interval [0.04255, 0.09043].

## IMPORTANT SCOPE LIMITS
- The implementation is an adapted retrieval experiment, not a verified exact reproduction of the official SciFact end-to-end baseline/evaluator.
- Metrics are evidence-document retrieval metrics, not final SUPPORT/CONTRADICT/NOT ENOUGH INFO classification metrics.
- The BM25 recovery pass adds a full-corpus retrieval operation; comparison is not compute-budget matched.
- Only one corruption seed (37) has been executed.
- No human trust or reliance data were collected.

## STILL REQUIRED FOR OFFICIAL BASELINE VALIDATION
1. Inspect the official SciFact repository revision, code, model docs, evaluator and dependencies.
2. Compare tokenizer, text construction, vocabulary, ranking, split, label conventions and evaluation code against this experiment.
3. Run the official clean baseline and preserve its exact command, logs and predictions.
4. Record licenses for code, data and any model weights separately.
5. Do not call this exact reproduction until these checks are complete.
