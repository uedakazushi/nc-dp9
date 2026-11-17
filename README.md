# nc-dp9: normalized Fano index and recognition

Current self-contained research state: **2026-11-17 / v14**. General intrinsic recognition is open. The categorical Fano index and its realization by genuine exact roots are the top priority. Elementary consequences and existing lattice classifications are not asserted to be new results.

## Start here

Read `research_plan.tex` first. `normalized_fano_index.tex` treats the index/coindex problem; its Introduction now explicitly explains why an automorphism-twisted Serre root gives a **norm equation**, not divisibility by a line bundle. `nc_dp9_recognition.tex` retains the full existing recognition framework and proofs. `research_notes.tex` retains current auxiliary proofs, examples, counterexamples, and qualifications. No old bundle or conversation is required to resume.

## Current mathematical results and boundaries

The index paper distinguishes numerical normalization on the whole numerical Grothendieck group from normalization only along the chosen structure-object orbit. On a smooth complex Fano variety they yield the same set of root degrees (the divisors of the classical index), but different sets of roots.

**Numerical-root theorem.** For a unimodular surface-like lattice with rank-one exceptional vector, characteristic canonical class and positive-rank root action, every (possibly unnormalized) Serre root is uniquely a numerical translation `t_H` composed with a canonical-class-preserving isometry `F` of NS. Its root equation is `F^r=I`, `N_r(F)H=-K`; in particular `r | K^2`. Under geometric signature the Euler-orbit error relative to the normalized quadratic polynomial is a nonpositive, r-periodic norm-square on `K^perp`. Exact unnormalized roots are automatically numerically normalized when the numerical lattice has rank three. The fixed-F conjugacy classes of numerical solutions form a torsor under cyclic `H^1(NS)`. These statements are numerical except for the explicit geometric example below.

**Geometric exact index across del Pezzo degrees.** The exact heart-auto-equivalence root degree always divides the anticanonical degree `d=K^2`. Across smooth degree `d=1,...,9`, the maximum realizable exact indices are `1,2,3,4,5,6,1,4,3`. Exact roots attaining degrees 2 through 6 are constructed geometrically by Geiser, Fermat cubic, a 4-cycle blow-up of P1xP1, the order-five symmetry of the degree-five del Pezzo, and the toric hexagon. The degree-2 statement is valid for every smooth degree-2 del Pezzo; degree-3 and degree-4 claims are existential rather than universal. The F1 degree-eight surface has index 1 whereas P1xP1 has index 4. The required Weyl and Picard identities are checked by `verify_del_pezzo_roots.py`, while existence of automorphisms is justified geometrically. On every smooth degree-four del Pezzo surface an exact square root exists, while a general one (automorphism group (Z/2)^4) has exact index exactly 2. Nevertheless their common integral numerical Euler lattice admits a fourth root, transported from the special cyclic four-root surface: **an explicit numerical root that cannot lift to any exact autoequivalence**. The individual del Pezzo surfaces and their symmetries are classical, and novelty of packaging them as a categorical exact-index table is not yet certified.

**Genuine exact geometric example.** On the toric degree-six del Pezzo surface, the 6-cycle on the boundary hexagon gives a heart-exact, AZ-ample sixth root of anticanonical tensor. The classical Fano index is 1 but the unnormalized exact categorical index is exactly 6, by the numerical degree bound. The periodic Euler defect is `(0,-7/12,-1/3,-1/4,-1/3,-7/12)` modulo 6. The toric fan, Picard lattice, Serre matrix and exact rational defects are reproduced by `verify_normalized_index.py`.

**Dimension-three arithmetic.** If an exceptional marked object has a cubic anticanonical Euler polynomial with leading coefficient `d/6` and an orbit-normalized r-th root, Serre symmetry forces `F(m)=(2m+1)(1+d*m*(m+1)/12)`. Integrality of the full root orbit yields three explicit Newton-coefficient congruences. For `1<=d<=72`, all nontrivial numerical candidates are `r=2,d=8,16,...,72`, `r=3,d=54`, `r=4,d=64`. A possible comparison with Loginov–Orlov’s five Euler degrees remains conditional until conventions and root hypotheses are matched; no existence statement for the noncommutative `M_72` is made.

**Orbit-generation criterion.** The two normalization notions coincide whenever the chosen structure object’s orbit spans the full numerical Grothendieck space. This does not assert that a numerically full orbit produces a full derived exceptional collection.

Weak normalization can depend on the chosen structure object. For a fixed automorphism, the norm equation modulo line-bundle conjugacy is described by cyclic `H^1(Pic)`; this uses the standard cyclic-cohomology formula.

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
python3 verify_del_pezzo_roots.py
python3 verify_identities.py
python3 verify_toric.py
```

The scripts require Python 3 and SymPy. They verify exact polynomial, matrix, Hilbert, and finite explicit-model calculations, not categorical existence or formal proof certificates.

## Verification performed

All four documents compiled in v14: plan **6 pages**, normalized index paper **21 pages**, recognition paper **101 pages**, notes **61 pages**. Final LaTeX logs have no undefined references or missing-character warnings. The plan was recompiled after a line-break adjustment for long script filenames. All **four** calculation scripts (`verify_del_pezzo_roots.py`, `verify_normalized_index.py`, `verify_identities.py`, `verify_toric.py`) passed in exact arithmetic. Final logs contain no undefined references/citations, overfull boxes, missing-character warnings, or LaTeX errors. Pages of the index paper (including the present main theorems) were visually inspected; inherited long documents have a successful compile, but their entire proofs were not independently re-audited. PDF integrity was validated. The exact divisor and numerical scripts were rerun for v14; the checks do not prove existence of categorical autoequivalences or furnish a formal proof certificate. The index script checks the full sixth-root toric fan and NS action, Euler isometry and Serre power, exact periodic defect, the dimension-three polynomial symmetry and Newton-coefficient integrality table. These checks do not certify the general categorical existence assumptions.

The recognition manuscript preserves its complete conditional-recognition arguments; the notes preserve auxiliary calculations and remaining obstructions. The index results state their dependence on the normal-element vanishing and boundary-recognition results. Internal labels, companion labels, and required input files were checked.

## Repository and bundle workflow

`uedakazushi/nc-dp9` `main` is the source of truth. Reflect coherent work directly on `main`, without pull requests or GitHub Actions. Track sources and checks, not PDFs, ZIPs, logs, or caches. Keep proved, conditional, incomplete, conjectural, and computational statements distinct. The standing authorization to save current bundles to Library is recorded separately from project-specific strategy in `research_plan.tex`. Existing Library files are not deleted without explicit permission.
