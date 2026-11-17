#!/usr/bin/env python3
"""Exact finite checks for root_artin_lifting.tex, 2026-11-17 / v16.
Checks algebraic identities and character counts, NOT categorical existence,
formal smoothness, or algebraization. Requires Python 3 and SymPy.
"""
from itertools import product
import sympy as sp


def assert_zero(matrix: sp.MatrixBase) -> None:
    assert all(sp.simplify(v) == 0 for v in matrix)


def check_affine_averaging() -> None:
    for order in range(1, 9):
        permutation = sp.zeros(order)
        for i in range(order):
            permutation[(i + 1) % order, i] = 1
        identity = sp.eye(order)
        norm = sum((permutation ** j for j in range(order)), sp.zeros(order))
        projector = norm / order
        assert_zero(projector ** 2 - projector)
        assert projector.rank() == 1
        assert_zero(permutation * projector - projector)
        # All translations satisfying N c=0 are covered over Q by c=(1-A)b.
        b = sp.Matrix(sp.symbols(f'b0:{order}'))
        x = sp.Matrix(sp.symbols(f'x0:{order}'))
        c = (identity - permutation) * b
        assert_zero(norm * c)
        orbit = []
        y = x
        for _ in range(order):
            orbit.append(y)
            y = permutation * y + c
        assert_zero(y - x)
        average = sum(orbit, sp.zeros(order, 1)) / order
        assert_zero(permutation * average + c - average)
        assert_zero(average - (b + projector * (x - b)))
    print('PASS affine finite-order averaging, cyclic torsors, orders 1..8')


def check_cubic_characters() -> None:
    # Fermat Jacobian ring C[x,y,z,w]/(x^2,y^2,z^2,w^2), degree 3.
    monomials = [e for e in product(range(2), repeat=4) if sum(e) == 3]
    assert len(monomials) == 4
    weights_u = [e[3] % 3 for e in monomials]
    # Natural anticanonical action is det(f)^(-1) times linear coordinates.
    weights_p = [(w - 1) % 3 for w in [0, 0, 0, 1]]
    assert [weights_u.count(j) for j in range(3)] == [1, 3, 0]
    assert [weights_p.count(j) for j in range(3)] == [1, 0, 3]
    assert [(weights_u + weights_p).count(j) for j in range(3)] == [2, 3, 3]
    # With our pullback convention, the product of the three lines in a plane.
    z, w = sp.symbols('z w')
    t = sp.symbols('t')
    resultant = sp.resultant(t ** 3 - 1, z + t*w, t)
    assert sp.expand(resultant - (z**3+w**3)) == 0
    print('PASS Fermat cubic HH characters (2,3,3), and tritangent norm')


def check_formal_fixed_loci() -> None:
    x, y = sp.symbols('x y')
    a = sp.Matrix([x, -y])
    b = sp.Matrix([x, 2*x*x-y])
    def compose(f, g):
        return f.subs({x:g[0], y:g[1]}, simultaneous=True).applyfunc(sp.expand)
    point = sp.Matrix([x, y])
    assert_zero(compose(a, a)-point)
    assert_zero(compose(b, b)-point)
    assert a.jacobian(point).subs({x:0, y:0}) == b.jacobian(point).subs({x:0, y:0})
    assert_zero(compose(b, a)-sp.Matrix([x,y+2*x*x]))
    for n in range(1, 7):
        iterated = point
        for _ in range(n):
            iterated = compose(compose(b,a),iterated)
        assert_zero(iterated-sp.Matrix([x,y+2*n*x*x]))
    assert sp.expand((b-point)[1]) == -2*(y-x*x)
    print('PASS nonlinear fixed-locus warning: identical tangents, distinct formal loci')


def check_nilpotent_power_correction() -> None:
    t, c = sp.symbols('t c')
    for degree in (2, 3, 4, 5, 6):
        for precision in (2, 3, 5, 7):
            # Unique scalar correction on 1+(t) modulo t^precision.
            correction = sum(sp.binomial(sp.Rational(-1,degree), k)*(c*t)**k
                             for k in range(precision))
            error = sp.series(correction**degree*(1+c*t)-1,t,0,precision).removeO()
            assert sp.expand(error) == 0
    print('PASS nilpotent scalar corrections of root-isomorphism choices')


if __name__ == '__main__':
    check_affine_averaging()
    check_cubic_characters()
    check_formal_fixed_loci()
    check_nilpotent_power_correction()
    print('All finite exact checks passed; categorical theorems require the written proofs.')
