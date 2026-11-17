# Lab Assignment 02 — From Review to Research

**Topic:** Human Trust Calibration in Human–Agent Collaboration for Autonomous Research  
**Candidate study:** Retrieval-error propagation and evidence-recovery checkpoints in scientific claim verification  
**Benchmark candidate:** SciFact  
**Status:** Corrected four-condition retrieval experiment completed on the labelled SciFact development split; paper and multi-seed/baseline validation work remain in progress.

## Research question
How does controlled retrieval corruption affect evidence selection and final scientific claim verification, and does a predefined evidence-validation/recovery checkpoint reduce that impact?

## Review-derived motivation
The supplied literature review identifies multi-step error propagation, adaptive human checkpoints, provenance, calibrated explanations, dynamic trust measurement, and long-term human-agent interaction as open directions. This project focuses on multi-step error propagation and checkpoints. This is a candidate gap, not a verified novelty claim.

## Provisional contribution
Pathway B: a controlled comparative robustness study:
- C0: clean retrieval, no checkpoint.
- C1: corrupted retrieval, no checkpoint.
- C2: same corrupted retrieval realization as C1, with checkpoint/recovery.
- C3 (optional): clean retrieval with checkpoint.

Primary planned comparison: C2 versus C1, paired by claim ID. Primary planned metric: macro-F1 after confirming official evaluator conventions. Secondary measures: official evidence/rationale F1, error rate, recovery/regression rates, candidates examined, and runtime.

## Integrity and status
This branch does not claim a successful Colab run, dataset download, baseline reproduction, empirical improvement, or statistical significance. These are blocked until actual logs and predictions exist. Do not use gold labels/evidence to choose distractors. Do not treat benchmark label metrics as direct measures of human trust.

## Suggested reading order
1. `docs/research_brief.md`
2. `docs/gap_map.md`
3. `docs/contribution_pathway.md`
4. `docs/experiment_protocol.md`
5. `docs/baseline_validation_status.md`
6. `docs/remaining_work.md`

## Official benchmark references
- [SciFact repository](https://github.com/allenai/scifact)
- [SciFact paper](https://aclanthology.org/2020.emnlp-main.609/)
- [Data schema](https://github.com/allenai/scifact/blob/master/doc/data.md)
- [Model documentation](https://github.com/allenai/scifact/blob/master/doc/model.md)

## Reproducibility
Master seed 13; planned seeds 13, 37, 73, 101, 137. Record Python/package versions, runtime/hardware, code and dataset commits, file checksums, config, exact commands, and raw per-claim outputs.

## Latest experimental progress
The corrected experiment has now been run. See [corrected results report](docs/corrected_results_report.md), [primary metrics for 188 evidence-bearing claims](results/primary_metrics_evidence_bearing.csv), and [secondary metrics for all 300 claims](results/secondary_metrics_all_300.csv).

Primary comparison (188 evidence-bearing claims): C0 clean TF-IDF macro-F1 0.3786; C1 corrupted TF-IDF 0.0938; C2 independent BM25+RRF recovery 0.1603; C3 clean BM25 0.4212. C2 improves over C1 by 0.06649 (paired claim-bootstrap 95% interval [0.04255, 0.09043]), but recovery is partial. C3 is strongest in this run.

Important: this is evidence-document retrieval, not end-to-end SciFact claim classification and not a human trust/reliance study. The BM25 recovery condition uses additional retrieval computation and is not compute-budget matched. Only seed 37 has been run so far.


## Updated full manuscript (17 November 2026)
The previous short protocol draft has been replaced with a corrected experimental manuscript:
- [Open updated LaTeX source](paper/main.tex)
- [Manuscript compilation instructions](paper/README.md)
- [Primary metrics: 188 evidence-bearing claims](results/primary_metrics_evidence_bearing.csv)
- [Secondary metrics: all 300 development claims](results/secondary_metrics_all_300.csv)

The LaTeX source contains the corrected C0-C3 results, equations, a TikZ workflow diagram, tables, paired bootstrap analysis, discussion, limitations and references. It is self-contained with respect to figures and can be compiled using pdfLaTeX from the `paper/` directory.
