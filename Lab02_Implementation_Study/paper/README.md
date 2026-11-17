# Corrected manuscript

The current `main.tex` is the updated experimental manuscript, not the earlier protocol-only draft.

## Compile
Run from this directory with TeX Live / MiKTeX installed:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All diagrams are generated with TikZ inside `main.tex`; no external figure files are required to compile this source.

## Included
Corrected C0-C3 results; primary metrics on 188 evidence-bearing claims; secondary metrics on all 300 claims; paired bootstrap interval; workflow diagram; methodology; equations; results tables; discussion; limitations; references.

## Scope
Evidence-document retrieval only; not the complete official SciFact claim-verification pipeline and not a human trust/reliance study. One corruption seed (37) has been run. BM25+RRF recovery uses extra retrieval computation and is not compute-budget matched.
