# One-page research brief

## Topic and source basis
The supplied review, *Human Trust Calibration in Human–Agent Collaboration for Autonomous Research* (Priyanshu, 2026), synthesizes trust in automation, trust in AI, algorithm aversion/appreciation, explanations, uncertainty communication, source provenance, expertise, and human oversight. Its cited foundation includes Lee & See (2004), Hoff & Bashir (2015), Dietvorst et al. (2015), Logg et al. (2019), Glikson & Woolley (2020), Amershi et al. (2019), Bansal et al. (2021), Tenhundfeld et al., and Shneiderman (2022).

## Research gap
The review identifies multi-step error propagation and adaptive human checkpoints as future research directions. An early source-retrieval error in an autonomous research chain can affect evidence selection and downstream synthesis/verification. This project makes a bounded computational study of that failure pathway. Novelty remains unverified pending a targeted search of neighboring work.

## Research question
How does controlled retrieval corruption affect evidence selection and final scientific claim verification, and does a predefined evidence-validation/recovery checkpoint reduce that impact?

## Pathway
B — controlled comparative robustness study. Preserve a validated baseline and compare clean retrieval, corrupted retrieval, and corrupted retrieval with a checkpoint.

## Dataset and baseline
Candidate dataset: SciFact (Wadden et al., EMNLP 2020), using official labelled splits and evaluator conventions. Candidate baseline: official SciFact TF-IDF pipeline, subject to source-code, dependency, evaluator, and license audit. An independent generic TF-IDF implementation must be called an adapted baseline, not an exact reproduction.

## Conditions and outcomes
C0 clean/no checkpoint; C1 corrupted/no checkpoint; C2 same corruption as C1/with checkpoint; optional C3 clean/with checkpoint. Primary metric: macro-F1 for final claim labels, after validating official class conventions. Primary comparison: paired C2−C1. Secondary: official evidence/rationale F1, error/recovery/regression rates, candidates examined, and runtime.

## Risks
Unrealistic corruption, extra retrieval budget confounding, small dev partition, leakage through gold evidence/labels, and limited external validity. The computational benchmark does not directly measure human trust or reliance.

## First executable milestone
Verify the Colab environment, then inspect the official SciFact schema, split, evaluator and licenses. Reproduce the clean baseline before introducing any corruption or checkpoint.