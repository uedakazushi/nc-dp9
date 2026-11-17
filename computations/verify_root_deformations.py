#!/usr/bin/env python3
"""Exact character checks for fano_root_deformations.tex (2026-11-17/v15).

These checks do NOT prove Toda's theorem, existence of categories, relative
Serre duality, or higher/coherent root lifting. Only the finite linear algebra,
monomial arrangement, and square-zero norm identities are checked here.
"""
from __future__ import annotations

from itertools import combinations, product
from math import comb, prod
import sympy as sp


def check_degree_four() -> None:
    # G = signs in five coordinates / simultaneous negation; unique |S|<=2 rep.
    reps = [frozenset(s) for k in range(3) for s in combinations(range(5), k)]
    assert len(reps) == 16
    positive_spaces: dict[frozenset[int], frozenset[int]] = {}
    for support in reps:
        signs = tuple(-1 if i in support else 1 for i in range(5))
        determinant = prod(signs)
        character = tuple(determinant * a for a in signs)
        # In odd ambient dimension the sign quotient is well-defined.
        opposite = tuple(-a for a in signs)
        assert tuple(prod(opposite) * a for a in opposite) == character
        plus = frozenset(i for i, a in enumerate(character) if a == 1)
        positive_spaces[support] = plus
        if not support:
            assert len(plus) == 5
            continue
        assert len(plus) == (1 if len(support) == 1 else 3)
        # A rank-4 pencil quadric whose two rulings are swapped.
        j = next(i for i in range(5) if (i not in support if len(support) == 1 else i in support))
        assert prod(signs[i] for i in range(5) if i != j) == -1
        matrix = sp.diag(*([1, 1] + list(character)))
        assert matrix**2 == sp.eye(7)
        reynolds = (sp.eye(7) + matrix) / 2
        assert reynolds**2 == reynolds
        assert reynolds.rank() == 2 + len(plus)

    maximal = {p for s, p in positive_spaces.items() if len(s) == 2}
    assert maximal == {frozenset(t) for t in combinations(range(5), 3)}
    assert all(any(p <= m for m in maximal) for s, p in positive_spaces.items() if len(s) == 1)
    # Check every support, including 0; no sample numerical coordinates needed.
    for mask in product((0, 1), repeat=5):
        support = frozenset(i for i, bit in enumerate(mask) if bit)
        lies_in_union = any(support <= p for p in maximal)
        degree4_monomials_vanish = all(not set(indices) <= support for indices in combinations(range(5), 4))
        assert lies_in_union == degree4_monomials_vanish == (len(support) <= 3)

    t = sp.symbols('t')
    series = sum(comb(5, j) * (t / (1 - t))**j for j in range(4))
    assert sp.factor(series - (1 + 2*t + 3*t**2 + 4*t**3) / (1-t)**3) == 0
    for degree in range(1, 10):
        coefficient = sum(comb(5, j) * comb(degree-1, j-1) for j in range(1, min(3, degree)+1))
        enumerated = sum(1 for exponents in product(range(degree+1), repeat=5)
                         if sum(exponents) == degree and sum(a > 0 for a in exponents) <= 3)
        assert coefficient == enumerated
    print('PASS dP4: all 16 characters, 15 ruling tests, 32 supports, ten maximal planes, Hilbert series')


def check_plane_and_geiser() -> None:
    monomials = [(a, b, 3-a-b) for a in range(4) for b in range(4-a)]
    counts = [sum((b + 2*c) % 3 == weight for a, b, c in monomials) for weight in range(3)]
    assert counts == [4, 3, 3]
    fixed = {e for e in monomials if (e[1] + 2*e[2]) % 3 == 0}
    assert fixed == {(3,0,0), (0,3,0), (0,0,3), (1,1,1)}
    # C3 characters can be handled in Q[zeta] without numerical complex arithmetic.
    z = sp.symbols('z')
    phi3 = sp.Poly(z*z+z+1, z)
    for exponent in range(3):
        avg = sp.Rational(1,3) * sum(z**(j*exponent) for j in range(3))
        rem = sp.rem(sp.Poly(avg, z), phi3).as_expr()
        assert rem == (1 if exponent == 0 else 0)
    geiser = sp.diag(*([1]*6 + [-1]*3))
    assert geiser**2 == sp.eye(9)
    assert ((sp.eye(9)+geiser)/2).rank() == 6
    print('PASS P2 weights (4,3,3), invariant monomials, C3 projector; Geiser invariant dimension 6')


def check_norm_repair_and_triangular() -> None:
    for order in range(1, 9):
        action = sp.zeros(order)
        for i in range(order):
            action[(i+1) % order, i] = 1
        norm = sum((action**j for j in range(order)), sp.zeros(order))
        defect = sp.ones(order, 1) * (order + 2)
        correction = -defect / order
        assert action * defect == defect
        assert norm * correction + defect == sp.zeros(order, 1)
        reynolds = norm / order
        assert reynolds**2 == reynolds
    # The off-diagonal action need not vanish on negative eigenspaces.
    b1, b2 = sp.symbols('b1 b2')
    triangular = sp.Matrix([[1, 0, b1], [0, 1, b2], [0, 0, -1]])
    assert triangular**2 == sp.eye(3)
    assert (triangular-sp.eye(3)).rank() == 1
    # Finite order kills mixing FROM a trivial quotient when U is trivial.
    c = sp.symbols('c')
    bad = sp.Matrix([[1, c], [0, 1]])
    assert bad**2-sp.eye(2) == sp.Matrix([[0,2*c],[0,0]])
    print('PASS square-zero cyclic norm repair (orders 1..8) and triangular finite-order identities')


def main() -> None:
    check_degree_four()
    check_plane_and_geiser()
    check_norm_repair_and_triangular()
    print('All exact checks passed; categorical lifting and higher coherence are not certified.')


if __name__ == '__main__':
    main()
