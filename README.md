# Noncommutative projective plane recognition (degree 9)

Current research sources (2026-11-17, v10). The six intrinsic axioms and the existence of a heart-exact cube root of the inverse Serre twist are studied as a proposed characterization of standard noncommutative projective planes. **The unrestricted recognition statement remains open.** Conditional theorems, proof dependencies, counterexamples and open gaps are documented in the paper and notes.

## Start here

1. `research_plan.tex`: current goals, established results, unresolved central questions, research policy and next steps.
2. `nc_dp9_recognition.tex`: publication-oriented paper with proofs and references.
3. `research_notes.tex`: auxiliary computations, examples, obstructions, and literature audits.
4. `README.txt`: detailed self-contained continuation and reproduction instructions from the research bundle.

## Build

Requires LuaLaTeX, latexmk, `luatexja-fontspec`, `Noto Serif CJK JP`, and `Noto Sans CJK JP`. Run from the repository root:

```sh
latexmk nc_dp9_recognition.tex
latexmk research_plan.tex
latexmk research_notes.tex
```

To reproduce exact finite computations (Python 3 with dependencies described in `README.txt`):

```sh
python3 verify_identities.py
python3 verify_toric.py
```

The Git repository tracks **source only**: generated PDFs, TeX intermediates, caches, and historical ZIP bundles are excluded. GitHub Actions is not used. Commit directly to `main` after coherent research steps; preserve proofs and separate proved, conditional, conjectural and computational statements.
