# nc-dp9: normalized Fano index and recognition

Current self-contained research state: **2026-11-17 / v12**. General intrinsic recognition is open. Elementary consequences and existing lattice classifications are not asserted to be new results.

## Start here

Read `research_plan.tex` first. `normalized_fano_index.tex` treats the index/coindex problem; its Introduction now explicitly explains why an automorphism-twisted Serre root gives a **norm equation**, not divisibility by a line bundle. `nc_dp9_recognition.tex` retains the full existing recognition framework and proofs. `research_notes.tex` retains current auxiliary proofs, examples, counterexamples, and qualifications. No old bundle or conversation is required to resume.

## Current mathematical results and boundaries

The index paper distinguishes numerical normalization on the whole numerical Grothendieck group from normalization only along the chosen structure-object orbit. On a smooth complex Fano variety they yield the same set of root degrees (the divisors of the classical index), but different sets of roots. Weak normalization can depend on the chosen structure object. For a fixed automorphism, the norm equation modulo line-bundle conjugacy is described by cyclic `H^1(Pic)`; this uses the standard cyclic-cohomology formula.

Within the existing theory of unimodular surface-like pseudolattices, with a point-like class, a rank-one exceptional class, and characteristic canonical class, a unipotent integral numerical root exists exactly when `-K` is divisible by its degree in the Neron–Severi lattice. For positive `K^2` and nonpositive defect, the index is at most three. The projective-plane and quadric **lattice** classifications are existing results of Kuznetsov, not a new classification of categories. Lifting numerical roots, deriving the lattice hypotheses from the weak heart axioms, and proving fullness remain open.

The previous Euler-polynomial divisibility and cubic-normal-boundary vanishing results are preserved. A Hilbert function alone is not an Euler polynomial: the asymptotic higher-Ext hypothesis remains explicit. The positive-defect numerical models are not realized categories. Under an ordinary genus-one boundary triple, or the existing smooth-high-Veronese reconstruction theorem, the previous recognition result applies.

## Literature comparison

The Introduction records exact comparisons with Kuznetsov–Smirnov (categorical polarizations), Bondal–Orlov (autoequivalences), Keeler (sigma-ampleness), de Thanhoffer de Volcsey–Van den Bergh and Kuznetsov (surface-like lattices and defect), Mori–Ueyama **v4** (the corrected recognition theorem), Hanihara (root pairs and cyclic invariance), and Loginov–Orlov's 2026 Fano/minifold definitions. Bibliographic identifiers and theorem locations are in the paper. Selected primary definitions/statements and proof passages were checked; exhaustive novelty certification and an audit of every proof in all references were not performed. Loginov–Orlov was read in primary arXiv HTML. Older qualifications on unavailable Artin–Zhang/Artin–Stafford originals remain in the research notes.

## Reproduce

Use LuaLaTeX, latexmk, and TeX Live packages `luatexja`, `fontspec`, and Harano Aji fonts. Fonts are not included. PDFs are generated next to the sources and SyncTeX is enabled.

```sh
latexmk research_plan.tex
latexmk normalized_fano_index.tex
latexmk nc_dp9_recognition.tex
latexmk research_notes.tex
python3 verify_normalized_index.py
python3 verify_identities.py
python3 verify_toric.py
```

The scripts require Python 3 and SymPy. They verify exact polynomial, matrix, Hilbert, and finite explicit-model calculations, not categorical existence or formal proof certificates.

## Verification performed

All four documents compiled: plan **5 pages**, index paper **13 pages**, recognition paper **101 pages**, notes **60 pages**. Final logs contain no undefined references/citations, overfull boxes, missing-character warnings, or LaTeX errors. The index paper and plan were visually inspected, together with representative pages of the inherited long documents. All three calculation scripts passed. New checks include symbolic numerical-tensor group laws, Serre matrices, roots, integral Gram bases, the positive-defect model, and the distinction between the two normalizations.

The mathematical sources of `nc_dp9_recognition.tex` and `research_notes.tex` are unchanged. Their full proofs were not independently re-audited in this step. The new index results state their dependence on the existing normal-element vanishing and boundary-recognition results. Internal labels, companion labels, and required input files were checked.

## Repository and bundle workflow

`uedakazushi/nc-dp9` `main` is the source of truth. Reflect coherent work directly on `main`, without pull requests or GitHub Actions. Track sources and checks, not PDFs, ZIPs, logs, or caches. Keep proved, conditional, incomplete, conjectural, and computational statements distinct. The standing authorization to save current bundles to Library is recorded separately from project-specific strategy in `research_plan.tex`. Existing Library files are not deleted without explicit permission.
