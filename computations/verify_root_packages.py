#!/usr/bin/env python3
"""Exact checks for simultaneous Serre roots, 2026-11-17 / v17.

Checks D5 lattice identities, all 1024 labelled simple graphs on five vertices,
finite quotients for compatible bipartite choices, quantum PBW identities and
Hesse characters. Does not certify abstract categories or formal-lifting proofs.
Requires Python 3 and SymPy. No external input files.
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
import sympy as sp

VERTICES = tuple(range(5))
EDGES = tuple(combinations(VERTICES, 2))


def lattice_checks() -> None:
    basis = sp.eye(6)
    h = basis[:, 0]
    es = [basis[:, i+1] for i in VERTICES]
    form = sp.diag(1, -1, -1, -1, -1, -1)
    K = -3*h + sum(es, sp.zeros(6, 1))
    conics = [h-e for e in es]
    vs = [a + K/2 for a in conics]
    transform = sp.Matrix.hstack(K, *vs)
    assert transform.det() != 0
    assert transform.T*form*transform == sp.diag(4, -1, -1, -1, -1, -1)
    actions = {}
    a, b, c, d = sp.symbols('a b c d')
    for i, j in EDGES:
        signs = [1] + [-1 if t in (i,j) else 1 for t in VERTICES]
        F = transform*sp.diag(*signs)*transform.inv()
        assert all(x.is_Integer for x in F)
        assert F**2 == basis and F.T*form*F == form and F*K == K
        D = -K/2 + a*vs[i] + b*vs[j]
        assert D + F*D == -K
        assert D[0] == sp.Rational(3,2) - (a+b)/2
        for aa, bb in product(range(-5,6), repeat=2):
            DD = D.subs({a:sp.Rational(aa,2), b:sp.Rational(bb,2)})
            integral = all(x.is_Integer for x in DD)
            assert integral == (aa%2 == bb%2 == 0 and ((aa+bb)//2)%2 == 1)
        actions[(i,j)] = F
    for e, f in combinations(EDGES, 2):
        D = -K/2 + a*vs[e[0]] + b*vs[e[1]]
        J = -K/2 + c*vs[f[0]] + d*vs[f[1]]
        comm = (basis-actions[f])*D - (basis-actions[e])*J
        shared = set(e)&set(f)
        expected = sp.zeros(6,1)
        if shared:
            i = next(iter(shared))
            expected = 2*((a,b)[e.index(i)]-(c,d)[f.index(i)])*vs[i]
        assert all(sp.expand(x) == 0 for x in comm-expected)
        assert sp.expand((K.T*form*comm)[0]) == 0
    print('PASS D5 rational basis, ten integral sign actions, all norm parity tests and 45 commutators')


def two_coloring(edges):
    adjacency = {i:[] for i in VERTICES}
    for i,j in edges:
        adjacency[i].append(j)
        adjacency[j].append(i)
    colors, components = {}, 0
    for seed in VERTICES:
        if not adjacency[seed] or seed in colors:
            continue
        components += 1
        colors[seed] = 0
        stack = [seed]
        while stack:
            i = stack.pop()
            for j in adjacency[i]:
                if j in colors:
                    if colors[j] == colors[i]:
                        return None, components
                else:
                    colors[j] = 1-colors[i]
                    stack.append(j)
    return colors, components


def multiply(a, b):
    # Quotient by tau: parity of total -K/2 coefficient, v-translation, sign mask.
    m,u,F = a
    n,v,G = b
    return ((m+n)%2, tuple(u[i] + (-1 if F>>i&1 else 1)*v[i]
                           for i in VERTICES), F^G)


def graph_checks() -> None:
    counts = Counter()
    for graph_mask in range(1 << len(EDGES)):
        edges = [edge for n,edge in enumerate(EDGES) if graph_mask>>n&1]
        vertices = set(i for e in edges for i in e)
        color, components = two_coloring(edges)
        # Independent exhaustive solution of the parity equations.
        solutions = [v for v in product((0,1), repeat=5)
                     if all((v[i]+v[j])%2 == 1 for i,j in edges)]
        assert bool(solutions) == (color is not None)
        counts['graphs'] += 1
        if color is None:
            continue
        counts['bipartite'] += 1
        if not edges:
            continue
        # An integral choice different from the {0,1} conic choice tests signs too.
        coeffs = [color.get(i,0) + 2*(i-2) for i in VERTICES]
        generators = [(1,tuple(coeffs[i] if i in e else 0 for i in VERTICES),
                       sum(1<<i for i in e)) for e in edges]
        identity = (0,(0,)*5,0)
        assert all(multiply(g,g) == identity for g in generators)
        assert all(multiply(g,h) == multiply(h,g) for g,h in combinations(generators,2))
        group, frontier = {identity}, [identity]
        while frontier:
            g = frontier.pop()
            for h in generators:
                gh = multiply(g,h)
                if gh not in group:
                    group.add(gh); frontier.append(gh)
                    assert len(group) <= 16
        assert len(group) == 2**(len(vertices)-components)
        assert len({g[2] for g in group}) == len(group)
        fixed_coords = [i for i in VERTICES if all(i not in e for e in edges)]
        assert len(fixed_coords) + 2 == 7-len(vertices)
        counts['nonempty'] += 1
        counts[f'formal_dimension_{7-len(vertices)}'] += 1
    assert counts['graphs'] == 1024
    assert counts['bipartite'] == 376 and counts['nonempty'] == 375
    assert counts['formal_dimension_5'] == 10
    for m in range(1,5):
        v = set(i for j in range(1,m+1) for i in (0,j))
        assert 7-len(v) == 6-m
    assert set(i for e in [(0,1),(1,2),(3,4)] for i in e) == set(VERTICES)
    print('PASS all 1024 labelled graphs:',dict(sorted(counts.items())))


def reduce_word(word, from_right=False):
    word = list(word)
    exponent = 0
    weights = {(1,0):-1, (2,0):1, (2,1):-1}
    while True:
        indices = [i for i in range(len(word)-1) if word[i]>word[i+1]]
        if not indices:
            return tuple(word), exponent
        i = indices[-1] if from_right else indices[0]
        exponent += weights[(word[i],word[i+1])]
        word[i],word[i+1] = word[i+1],word[i]


def quantum_checks() -> None:
    # Every word of lengths 0..7: two different reduction strategies agree.
    for length in range(8):
        for word in product(range(3), repeat=length):
            assert reduce_word(word) == reduce_word(word,from_right=True)
    p12,p13,p23 = -1,1,-1  # exponents of q in RRZ's convention
    assert [-p12-p13, p12-p23, p13+p23] == [0,0,0]
    # The multiplication exponent is a bilinear integer cocycle.
    a = sp.symbols('a0:3'); b = sp.symbols('b0:3'); c = sp.symbols('c0:3')
    add = lambda v,w:tuple(v[i]+w[i] for i in range(3))
    phi = lambda v,w: -v[1]*w[0]+v[2]*w[0]-v[2]*w[1]
    assert sp.expand(phi(a,b)+phi(add(a,b),c)-phi(b,c)-phi(a,add(b,c))) == 0
    cyclic = lambda w:tuple((i+1)%3 for i in w)
    for u,v in [((1,2),(2,1)),((2,0),(0,2)),((0,1),(1,0))]:
        # left word equals q times right word; still true after cyclic permutation.
        for transform in (lambda w:w, cyclic):
            lw,le = reduce_word(transform(u)); rw,re = reduce_word(transform(v))
            assert lw==rw and le==re+1
    cubic = [p for p in product(range(4),repeat=3) if sum(p)==3]
    fixed_d = [p for p in cubic if (p[1]+2*p[2])%3 == 0]
    assert len(fixed_d)==4
    orbits=[]; remain=set(fixed_d)
    while remain:
        p=min(remain); orb={p,(p[2],p[0],p[1]),(p[1],p[2],p[0])}
        assert orb<=set(fixed_d)
        orbits.append(orb);remain-=orb
    assert sorted(map(len,orbits)) == [1,3]
    # Projectivized log-canonical bracket: {y/x,z/x}=3 yz/x^2.
    x,y,z=sp.symbols('x y z', nonzero=True)
    pi=sp.Matrix([[0,x*y,-z*x],[-x*y,0,y*z],[z*x,-y*z,0]])
    grad=lambda f:sp.Matrix([sp.diff(f,t) for t in (x,y,z)])
    assert sp.simplify((grad(y/x).T*pi*grad(z/x))[0]-3*y*z/x**2)==0
    print('PASS quantum PBW (3280 words), cyclic symmetries, Nakayama, 2D Hesse invariants and projective bracket')


if __name__ == '__main__':
    lattice_checks()
    graph_checks()
    quantum_checks()
    print('All exact checks passed. Abstract formal and categorical claims use the written proofs.')
