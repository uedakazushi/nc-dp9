# nc-dp9: normalized Fano index and recognition

Current research bundle: **2026-11-17 / v11**. The general intrinsic recognition problem is open; no novelty claim is made without further literature comparison.

## Start here

Read `research_plan.tex` first. Then read the short paper `normalized_fano_index.tex` for the current index/coindex direction, and `nc_dp9_recognition.tex` for the full recognition framework. `research_notes.tex` retains the current auxiliary proofs, examples, counterexamples, and literature qualifications. The two papers have different mathematical scopes; the existing recognition proofs have not been shortened or replaced by summaries.

## Current results and limits

The new paper defines normalization by unipotence on the numerical Grothendieck group, and separates it from the weaker orbit condition. For a smooth complex Fano variety, normalized root degrees are precisely the positive divisors of the ordinary Fano index. Under an eventual anticanonical **Euler** polynomial and orbit unipotence, a surface root of degree `r` satisfies `r^2 | d`, and `2*r^2 | d` when `r` is even. For `1 <= d <= 9`, the nontrivial possibilities are `(d,r)=(8,2),(9,3)`.

The hypothesis on the Euler polynomial must not be silently replaced by a Hilbert function: asymptotic higher-Ext vanishing is a separate input. Neither a general noncommutative degree bound `d <= 9` nor a general index bound is proved. A family of integral unimodular Euler lattices demonstrates the limitation of purely numerical arguments; it is not a family of actual categories.

For a degree-nine candidate with an orbit-normalized cube root and an integral cubic normal quotient, all orbit `Ext^1` groups vanish. Standard Hilbert functions and boundary saturation follow directly. Recognition further uses an ordinary genus-one boundary triple (or the existing smooth-high-Veronese reconstruction theorem). Fullness for a general singular boundary is still open.

## Reproduce

Use LuaLaTeX, latexmk, and TeX Live's `luatexja`, `fontspec`, and Harano Aji fonts. Font files are not distributed. PDFs are generated next to their sources; SyncTeX is enabled.

```sh
latexmk research_plan.tex
latexmk normalized_fano_index.tex
latexmk nc_dp9_recognition.tex
latexmk research_notes.tex
python3 verify_normalized_index.py
python3 verify_identities.py
python3 verify_toric.py
```

The Python scripts require SymPy. They check exact polynomial, matrix, Hilbert, and explicit finite-model calculations, not categorical existence or a formal verification of the recognition theorems.

## Verification of this bundle

All four documents compiled successfully: research plan 5 pages, normalized-index paper 7 pages, recognition paper 101 pages, research notes 60 pages. All three calculation scripts passed. The new index paper and current plan were visually inspected; representative pages of the inherited long documents were checked after font portability changes. Internal labels and cited companion theorem labels were checked. The existing recognition paper and research-notes mathematical sources are unchanged from the imported v10 research state. Their full proofs were not independently re-audited in this step; the normal-element vanishing argument used by the new paper was re-examined.

The bundle contains only current documents, sources, PDFs, build settings, and necessary checks. Compilation logs, caches, prior ZIPs, and external literature PDFs are excluded.

## Repository workflow

`uedakazushi/nc-dp9` `main` is the source of truth. Commit coherent research stages directly to `main`; do not use pull requests or GitHub Actions. Track sources and reproducibility code, not PDFs, ZIPs, or TeX intermediates. Preserve valid results and proofs. Distinguish proved statements, extra-hypothesis results, incomplete arguments, conjectures, and computational observations. The standing authorization to save current research bundles to Library is recorded separately from the project-specific strategy in `research_plan.tex`.
