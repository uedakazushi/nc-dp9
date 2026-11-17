#!/usr/bin/env python3
"""Exact checks for normalized_fano_index.tex (2026-11-17, v11).

These checks certify polynomial/matrix identities, not existence of categories.
Run with Python 3 and SymPy: python3 verify_normalized_index.py
"""
from __future__ import annotations

import sympy as sp


def zero_matrix(matrix: sp.MatrixBase) -> bool:
    return all(sp.simplify(x) == 0 for x in matrix)


def main() -> None:
    k, m, r, a, d, x = sp.symbols("k m r a d x")
    q = 1 + a * k * (k + r) / 2
    assert sp.expand(q.subs(k, k + 2) - 2 * q.subs(k, k + 1) + q) == a
    assert sp.expand(q - (1 + a * k * (k - 1) / 2 + a * (r + 1) * k / 2)) == 0
    assert sp.expand(q.subs(k, -k - r) - q) == 0
    assert sp.simplify(q.subs({a: d / r**2, k: r * m}) - (1 + d * m * (m + 1) / 2)) == 0
    candidates = [(degree, root) for degree in range(1, 10) for root in range(2, 10)
                  if degree % (root * root) == 0
                  and (degree // (root * root)) * (root + 1) % 2 == 0]
    assert candidates == [(8, 2), (9, 3)]
    print("PASS integer-valued Euler polynomial and degree 1..9 obstruction:", candidates)

    T = sp.Matrix([[0, 0, 1], [1, 0, -3], [0, 1, 3]])
    I = sp.eye(3)
    N = T - I
    assert N**3 == sp.zeros(3)
    G = sp.Matrix([[1, (r + 3) / 2, r + 3],
                   [(3 - r) / 2, 1, (r + 3) / 2],
                   [3 - r, (3 - r) / 2, 1]])
    assert sp.factor(G.det()) == 1
    assert zero_matrix(T.T * G * T - G)
    inverse_power = I - r * N + r * (r + 1) * N**2 / 2
    assert zero_matrix(G * inverse_power - G.T)
    e = sp.Matrix([1, 0, 0])
    power = I + k * N + k * (k - 1) * N**2 / 2
    assert sp.simplify((e.T * G * power * e)[0] - (1 + k * (k + r) / 2)) == 0
    assert G.subs(r, 5) == sp.Matrix([[1, 4, 8], [-1, 1, 4], [-2, -1, 1]])
    print("PASS symbolic Serre-compatible unimodular lattice for every odd r")

    U = T**3
    M = U - I
    root = I + M / r + (1 - r) * M**2 / (2 * r**2)
    D = root - I
    assert zero_matrix(D**3)
    assert zero_matrix(I + r * D + r * (r - 1) * D**2 / 2 - U)
    assert root.subs(r, 3) == T
    print("PASS unique unipotent root formula when (U-I)^3=0")

    j = sp.symbols("j", integer=True)
    P = lambda v: (v + 1) * (v + 2) / 2
    assert sp.simplify(sp.summation(3 * (3 * j + 1), (j, 0, m)) - P(3 * m + 1)) == 0
    assert sp.simplify(sp.summation(3 * (3 * j + 2), (j, 0, m)) - P(3 * m + 2)) == 0
    assert sp.simplify(1 + 9 * m * (m + 1) / 2 - P(3 * m)) == 0
    assert P(-1) == 0 and P(-2) == 0
    print("PASS cubic boundary cumulative bounds and negative-window zeros")

    def tensor_action(intersection: sp.Matrix, divisor: sp.Matrix) -> sp.Matrix:
        """Chern coordinates (rank, c1-coordinates, ch2) on a surface."""
        rho = len(divisor)
        out = sp.eye(rho + 2)
        for i in range(rho):
            out[i + 1, 0] = divisor[i]
        out[-1, 0] = (divisor.T * intersection * divisor)[0] / 2
        for i in range(rho):
            out[-1, i + 1] = (divisor.T * intersection)[i]
        return out

    intersection = sp.diag(1, -1, -1, -1)
    permutation = sp.eye(6)
    permutation[2:5, 2:5] = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    S6 = tensor_action(intersection, sp.Matrix([1, -1, 0, 0])) * permutation
    assert S6**3 == tensor_action(intersection, sp.Matrix([3, -1, -1, -1]))
    assert sp.factor(S6.charpoly(x).as_expr()) == (x - 1)**4 * (x*x + x + 1)

    intersection2 = sp.Matrix([[0, 1], [1, 0]])
    swap = sp.eye(4)
    swap[1:3, 1:3] = sp.Matrix([[0, 1], [1, 0]])
    S8 = tensor_action(intersection2, sp.Matrix([1, 0])) * swap
    assert S8**4 == tensor_action(intersection2, sp.Matrix([2, 2]))
    assert sp.factor(S8.charpoly(x).as_expr()) == (x - 1)**3 * (x + 1)
    print("PASS unnormalized geometric roots: degree 6 cube and quadric fourth root")
    print("All exact checks passed. No categorical realization is asserted by this script.")


if __name__ == "__main__":
    main()
