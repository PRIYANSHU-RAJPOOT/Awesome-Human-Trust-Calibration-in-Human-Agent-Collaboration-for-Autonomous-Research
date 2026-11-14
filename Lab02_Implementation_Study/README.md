# Lab Assignment 02 — From Review to Research

**Topic:** Human Trust Calibration in Human–Agent Collaboration for Autonomous Research  
**Candidate study:** Retrieval-error propagation and evidence-recovery checkpoints in scientific claim verification  
**Benchmark candidate:** SciFact  
**Status:** Research design and repository scaffold prepared; environment, baseline and experimental evidence remain pending.

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