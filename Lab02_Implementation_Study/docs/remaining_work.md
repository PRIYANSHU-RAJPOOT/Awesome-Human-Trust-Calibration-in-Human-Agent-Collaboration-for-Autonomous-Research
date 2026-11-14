# Remaining work — submission gate checklist

## G1: Research brief
- [x] Review-derived gap map and candidate research question drafted.
- [ ] Verify key claims against original cited studies and perform a targeted novelty search.
- [ ] Confirm scope and benchmark with instructor/TA if required.

## G2: Baseline verification
- [ ] Run Google Colab environment notebook and save actual output.
- [ ] Clone SciFact; record commit, data manifest, checksums and license conditions.
- [ ] Audit official code, preprocessing, retrieval, split and evaluator.
- [ ] Run clean baseline and save actual console logs and per-claim predictions.
- [ ] Complete the validation report.

## G3: Experimental evidence
- [ ] Freeze corruption policy and checkpoint rule using separate pilot/validation evidence.
- [ ] Verify no use of gold evidence/labels in corruption selection.
- [ ] Run C0/C1/C2 with paired claim IDs and planned seeds.
- [ ] Add budget-matched control where needed.
- [ ] Export real metrics, uncertainty estimates, error tables and publication figures.
- [ ] Perform failure analysis and preserve raw outputs/configurations.

## G4: Paper and reproducibility
- [ ] Replace protocol-only manuscript sections with actual Results, Discussion and limitations.
- [ ] Recheck citations and bibliography metadata.
- [ ] Include reproducible commands, environment, checksums, data-access/license notes and deviations.
- [ ] Record AI assistance and meaningful human decisions.
- [ ] Run a five-minute technical demonstration using actual outputs.
- [ ] Confirm submission naming, visibility and required links with the handbook/instructor.

**Do not mark G2 or G3 complete until actual output files exist.**