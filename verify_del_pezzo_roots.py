#!/usr/bin/env python3
"""Exact rational checks for normalized_fano_index.tex (2026-11-17 v14).

Verifies divisorial Picard actions, anticanonical orbit norms, degree-four
four-point general position, and finite Weyl matrix relations. This code
is not a proof that the prescribed Weyl matrices lift to automorphisms.
The geometric lift statements are proved separately in the manuscript.
Requires Python 3 and sympy.
"""
import sympy as sp


def check_degree_two_geiser():
    n = 7
    Q = sp.diag(1, *([-1]*n))
    K = sp.Matrix([-3]+[1]*n)
    E = sp.eye(n+1)[:, 1]
    I = sp.eye(n+1)
    # On Pic(X), Geiser acts as the identity on K and -1 on K^perp.
    F = K*(K.T*Q)-I
    assert K.dot(Q*K) == 2
    assert F*F == I
    assert F.T*Q*F == Q
    assert F*K == K
    assert E+F*E == -K
    print('PASS degree 2: Geiser involution and norm of an exceptional curve')


def check_degree_three_fermat():
    z, w, a = sp.symbols('z w a')
    polynomial = sp.expand((z+w)*(z+a*w)*(z-(1+a)*w))
    reduced = sp.rem(sp.Poly(polynomial-(z**3+w**3), a), sp.Poly(a*a+a+1,a)).as_expr()
    assert sp.expand(reduced) == 0
    print('PASS degree 3: Fermat hyperplane factors as three cyclic lines')


def check_degree_four_square():
    t = sp.symbols('t', nonzero=True)
    # rows of homogeneous evaluation of a*uv+b*u+c*v+d
    M = sp.Matrix([[0, 0, t, 1], [t, 0, 1, 0],
                   [1/t, 1, 0, 0], [0, 1/t, 0, 1]])
    determinant = sp.factor(M.det())
    assert sp.simplify(determinant - (t**4-1)/t**2) == 0
    assert determinant.subs(t, 2) != 0
    # Basis U,V,E0,...,E3, U.V=1, Ej^2=-1
    Q = sp.zeros(6)
    Q[0, 1] = Q[1, 0] = 1
    for i in range(2, 6):
        Q[i, i] = -1
    U, V = sp.eye(6)[:, 0], sp.eye(6)[:, 1]
    E = [sp.eye(6)[:, j] for j in range(2, 6)]
    antiK = 2*U+2*V-sum(E, sp.zeros(6, 1))
    D = [U-E[0], V-E[1], U-E[2], V-E[3]]
    F = sp.zeros(6)
    F[:, 0], F[:, 1] = V, U
    for j in range(4):
        F[:, 2+j] = E[(j-1) % 4]
    assert F**4 == sp.eye(6)
    assert F.T*Q*F == Q
    assert F*antiK == antiK
    assert (antiK.T*Q*antiK)[0] == 4
    assert sum((F**j*D[0] for j in range(4)),sp.zeros(6,1)) == antiK
    assert sum(D,sp.zeros(6,1)) == antiK
    assert all((x.T*Q*x)[0] == -1 for x in D)
    assert all((D[i].T*Q*D[j])[0] == (1 if (j-i)%4 in (1,3) else 0)
               for i in range(4) for j in range(4) if i != j)
    print('PASS degree 4: general-position determinant, four-cycle, norm and anticanonical square')


def check_degree_five_weyl():
    n=4
    Q=sp.diag(1,*([-1]*n))
    K=sp.Matrix([-3]+[1]*n)
    E=sp.eye(n+1)[:,1]
    alpha=[]
    for i in range(1,n):
        root=sp.zeros(n+1,1)
        root[i]=1
        root[i+1]=-1
        alpha.append(root)
    alpha.append(sp.Matrix([1,-1,-1,-1,0]))
    F=sp.eye(n+1)
    for a in alpha:
        assert (a.T*Q*a)[0]==-2
        F = F*(sp.eye(n+1)+a*(a.T*Q))
    assert F**5==sp.eye(n+1)
    assert F.T*Q*F==Q
    assert F*K==K
    assert (K.T*Q*K)[0] == 5
    orbit=[F**j*E for j in range(5)]
    assert sum(orbit,sp.zeros(n+1,1))==-K
    assert all((v.T*Q*v)[0]==-1 and (v.T*Q*K)[0]==-1 for v in orbit)
    assert all(v != w for i,v in enumerate(orbit) for w in orbit[i+1:])
    print('PASS degree 5: Weyl Coxeter order five and full anticanonical line orbit')


def check_degree_six_hexagon():
    H,E1,E2,E3 = sp.eye(4).columnspace()
    antiK=3*H-E1-E2-E3
    D=[E1,H-E1-E2,E2,H-E2-E3,E3,H-E3-E1]
    assert sum(D,sp.zeros(4,1))==antiK
    Q=sp.diag(1,-1,-1,-1)
    assert (antiK.T*Q*antiK)[0]==6
    print('PASS degree 6: toric hexagon anticanonical divisor')


def check_degree_eight():
    F=sp.Matrix([[0,1],[1,0]])
    L=sp.Matrix([1,0])
    norm4=sum((F**j*L for j in range(4)),sp.zeros(2,1))
    assert norm4==sp.Matrix([2,2])
    norm8=sp.eye(2)*4+F*4
    assert all((norm8*sp.Matrix([a,b])) != sp.Matrix([2,2]) for a in range(-2,3) for b in range(-2,3))
    print('PASS degree 8: quadric fourth root and eighth-root norm divisibility obstruction')


if __name__=='__main__':
    check_degree_two_geiser()
    check_degree_three_fermat()
    check_degree_four_square()
    check_degree_five_weyl()
    check_degree_six_hexagon()
    check_degree_eight()
    print('All exact Picard and divisor computations passed.')
