# Corrected SciFact experiment — progress update

**Execution status:** corrected four-condition retrieval experiment completed on the labelled SciFact development split.

## Dataset and runtime facts
- Corpus abstracts: 5,183
- Labelled development claims: 300
- Test claims: 300; the downloaded test file has no public evidence annotations
- Claims with at least one annotated evidence document: 188
- Claims with an empty evidence mapping: 112
- Python: 3.13.18
- scikit-learn: 1.6.1
- Random seed: 37
- Top-k: 3
- Corruption: replace TF-IDF rank 1 with a randomly selected document from original ranks 4–20
- Recovery: independent BM25 top-50 retrieval plus reciprocal-rank fusion (RRF), k=60
- Bootstrap: 5,000 paired claim-level resamples

Dataset archive SHA-256:
`11c621288d41ac144d29b13b0f8503b3820b7d6e8b1f6ff24dff335c196d76be`

## Primary results: evidence-bearing subset (188 claims)

| Condition | Macro precision | Macro recall | Macro-F1 | Hit@3 |
|---|---:|---:|---:|---:|
| C0 clean TF-IDF | 0.2571 | 0.7438 | 0.3786 | 0.7553 |
| C1 corrupted TF-IDF | 0.0656 | 0.1791 | 0.0938 | 0.1968 |
| C2 BM25 + RRF recovery | 0.1099 | 0.3121 | 0.1603 | 0.3298 |
| C3 clean BM25 | 0.2872 | 0.8236 | 0.4212 | 0.8404 |

## Secondary results: all 300 claims

| Condition | Macro precision | Macro recall | Macro-F1 | Hit@3 |
|---|---:|---:|---:|---:|
| C0 clean TF-IDF | 0.1611 | 0.4661 | 0.2373 | 0.4733 |
| C1 corrupted TF-IDF | 0.0411 | 0.1122 | 0.0588 | 0.1233 |
| C2 BM25 + RRF recovery | 0.0689 | 0.1956 | 0.1005 | 0.2067 |
| C3 clean BM25 | 0.1800 | 0.5161 | 0.2639 | 0.5267 |

The 188-claim evidence-bearing subset is the primary retrieval analysis. The all-300 table is retained as a secondary descriptive view; empty-evidence claims are assigned zero by the evaluation code.

## Paired recovery analysis
- C2 minus C1 macro-F1: 0.06649
- Paired bootstrap 95% percentile interval: [0.04255, 0.09043]
- Corrupted C1 misses on evidence-bearing claims: 151
- Misses converted to hit@3 by C2: 25
- Hit@3 regressions: 0
- Recovery rate among C1 misses: 16.56%

## Interpretation
The independent BM25+RRF recovery condition improves over corrupted TF-IDF retrieval, but recovery is partial and does not restore clean TF-IDF performance. Clean BM25 is strongest among these four conditions on this development subset.

## Limitations and claims not supported
1. The BM25 recovery pass adds a full-corpus retrieval operation; the comparison is not compute-budget matched.
2. Only one corruption seed (37) has been run; the planned multi-seed analysis remains outstanding.
3. This evaluates evidence-document retrieval, not sentence-level rationale quality or final SUPPORT/CONTRADICT/NOT ENOUGH INFO classification.
4. No human participants, trust scales, or reliance behavior were measured. The results do not demonstrate improved human trust calibration.
5. The TF-IDF/BM25 implementation is a retrieval experiment, not a verified exact reproduction of the complete official SciFact pipeline.

## Next steps
- Add a compute-budget-matched comparator.
- Run multiple corruption seeds and summarize variation across perturbations.
- Audit and reproduce the official end-to-end SciFact baseline/evaluator.
- Add sentence-level rationale evaluation.
- Update the paper after these validations; keep the human-trust claims appropriately scoped.
