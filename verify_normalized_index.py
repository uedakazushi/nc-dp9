#!/usr/bin/env python3
"""Exact checks for normalized_fano_index.tex (2026-11-17, v12).

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
    # General surface-like numerical tensor formula, with a symbolic NS pairing.
    q11, q12, q22, k1, k2, h1, h2, j1, j2 = sp.symbols(
        "q11 q12 q22 k1 k2 h1 h2 j1 j2")
    Q = sp.Matrix([[q11, q12], [q12, q22]])
    K = sp.Matrix([k1, k2])
    H = sp.Matrix([h1, h2])
    J = sp.Matrix([j1, j2])

    def surface_euler(pairing: sp.Matrix, canonical: sp.Matrix) -> sp.Matrix:
        rho = pairing.rows
        form = sp.zeros(rho + 2)
        form[0, 0] = form[0, -1] = form[-1, 0] = 1
        form[1:rho + 1, 0] = pairing * canonical
        form[1:rho + 1, 1:rho + 1] = -pairing
        return form

    def numerical_tensor(pairing: sp.Matrix, canonical: sp.Matrix,
                         divisor: sp.Matrix) -> sp.Matrix:
        rho = pairing.rows
        action = sp.eye(rho + 2)
        action[1:rho + 1, 0] = divisor
        action[-1, 1:rho + 1] = (pairing * divisor).T
        action[-1, 0] = ((divisor.T * pairing * divisor)[0]
                         - (canonical.T * pairing * divisor)[0]) / 2
        return action

    form = surface_euler(Q, K)
    tH, tJ = numerical_tensor(Q, K, H), numerical_tensor(Q, K, J)
    assert zero_matrix(tH.T * form * tH - form)
    assert zero_matrix(tH * tJ - numerical_tensor(Q, K, H + J))
    assert zero_matrix((tH - sp.eye(4))**3)
    assert zero_matrix(form * numerical_tensor(Q, K, K) - form.T)
    # The unique unipotent root has H=-K/r; the r-th power is a finite polynomial.
    rootH = numerical_tensor(Q, K, -K / r)
    rootN = rootH - sp.eye(4)
    assert zero_matrix(sp.eye(4) + r * rootN + r * (r - 1) * rootN**2 / 2
                       - numerical_tensor(Q, K, -K))
    print("PASS symbolic surface-like tensor, group law, Serre action and root")

    qp, kp = sp.Matrix([[1]]), sp.Matrix([-3])
    gp = surface_euler(qp, kp)
    hp = numerical_tensor(qp, kp, sp.Matrix([1]))
    ep = sp.Matrix([1, 0, 0])
    bp = sp.Matrix.hstack(ep, hp * ep, hp**2 * ep)
    assert bp.T * gp * bp == sp.Matrix([[1, 3, 6], [0, 1, 3], [0, 0, 1]])
    assert abs(bp.det()) == 1
    qq, kq = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([-2, -2])
    gq = surface_euler(qq, kq)
    hq1 = numerical_tensor(qq, kq, sp.Matrix([1, 0]))
    hq2 = numerical_tensor(qq, kq, sp.Matrix([0, 1]))
    eq = sp.Matrix([1, 0, 0, 0])
    bq = sp.Matrix.hstack(eq, hq1 * eq, hq2 * eq, hq1 * hq2 * eq)
    assert bq.T * gq * bq == sp.Matrix([[1, 2, 2, 4], [0, 1, 0, 2],
                                      [0, 0, 1, 2], [0, 0, 0, 1]])
    assert abs(bq.det()) == 1
    point = sp.Matrix([1, -2, 1])
    divisor = sp.Matrix([-1, 1, 0])
    assert point.T * G == sp.Matrix([[1, 1, 1]])
    assert G * point == sp.Matrix([1, 1, 1])
    assert (point.T * G * point)[0] == 0
    assert sp.simplify(-(divisor.T * G * divisor)[0]) == 1
    assert sp.simplify((divisor.T * G * e - e.T * G * divisor)[0]) == -r
    assert sp.expand(r**2 + 3 - 12) == r**2 - 9
    print("PASS P2/quadric integral Gram bases and positive-defect lattice model")

    # Weak normalization does not imply full normalization, even on a quadric.
    weak = tensor_action(intersection2, sp.Matrix([1, 1])) * swap
    o = sp.Matrix([1, 0, 0, 0])
    assert weak**2 == tensor_action(intersection2, sp.Matrix([2, 2]))
    assert (weak - sp.eye(4))**3 * o == sp.zeros(4, 1)
    assert (weak - sp.eye(4))**3 != sp.zeros(4)
    marked = tensor_action(intersection2, sp.Matrix([1, 0])) * o
    assert (weak - sp.eye(4))**5 * marked != sp.zeros(4, 1)
    assert sp.factor(weak.charpoly(x).as_expr()) == (x - 1)**3 * (x + 1)
    print("PASS full/orbit normalization distinction and marking dependence")

    # Cyclic norm identity. These finite instances supplement the written proof.
    for degree in range(1, 9):
        F = sp.zeros(degree)
        for index in range(degree):
            F[(index + 1) % degree, index] = 1
        norm = sum((F**j for j in range(degree)), sp.zeros(degree))
        weighted = sum((j * F**j for j in range(degree)), sp.zeros(degree))
        assert (sp.eye(degree) - F) * weighted == norm - degree * sp.eye(degree)
    print("PASS finite cyclic-norm identity instances (orders 1..8)")
    print("All exact checks passed. No categorical realization is asserted by this script.")


if __name__ == "__main__":
    main()
