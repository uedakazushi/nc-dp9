#!/usr/bin/env python3
"""Exact, dependency-free checks for the current mathematical manuscript.

This verifies finite algebraic identities and explicit inequality
certificates, not categorical existence or the recognition theorem.
Polynomials are tuples of Fraction coefficients in ascending order.
The determinant checks are symbolic in the parameter e. The four-case
enumeration uses bounds derived from the stated inequalities; the period-6
exclusion is a symbolic certificate, not a bounded parameter search.
The degenerate Beilinson example is checked independently using the
K-relative normalized bar complex and exact rational matrix ranks.
"""
from fractions import Fraction as F
from itertools import permutations, product


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p or [F(0)])


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c * x for x in p])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def power(p, n):
    out = (F(1),)
    for _ in range(n):
        out = mul(out, p)
    return out


def det(matrix):
    size = len(matrix)
    out = (F(0),)
    for sigma in permutations(range(size)):
        inversions = sum(sigma[i] > sigma[j]
                         for i in range(size) for j in range(i + 1, size))
        term = (F((-1) ** inversions),)
        for i in range(size):
            term = mul(term, matrix[i][sigma[i]])
        out = add(out, term)
    return out


def p2(n):
    return F((n + 1) * (n + 2), 2)


def qmodel(n, kind):
    coeff = (-int(n % 3 != 0) if kind == 3
             else (0, 1, 1, 0, -1, -1)[n % 6])
    return trim((p2(n), coeff))


def check_series(coeff, denominator, numerator, count=36):
    for n in range(count):
        actual = sum(denominator[j] * coeff(n - j)
                     for j in range(min(n, len(denominator) - 1) + 1))
        expected = numerator[n] if n < len(numerator) else 0
        assert actual == expected, (n, actual, expected)


def check_low_degree_constraints():
    # For q=P, put x=e_1>=0 and y=e_2>=0. The three affine
    # inequalities are x<=1, x+y<=2, y>=2*x-1.
    # Here vectors have coefficients (constant, x, y); only add/scale
    # are used, so no polynomial multiplication of these vectors occurs.
    h1, h2 = tuple(map(F, (3, 1, 0))), tuple(map(F, (6, 0, 1)))
    assert add((4,), scale(h1, -1)) == tuple(map(F, (1, -1)))
    assert add((11,), scale(add(h1, h2), -1)) == tuple(map(F, (2, -1, -1)))
    assert add(add(h2, scale(h1, -2)), (1,)) == tuple(map(F, (1, -2, 1)))
    # These bounds exhaust all nonnegative integer solutions:
    # x in {0,1}, and 0<=y<=2-x. This is not an arbitrary cutoff.
    cases = tuple((x, y) for x in range(2) for y in range(3 - x)
                  if y >= 2 * x - 1)
    assert cases == ((0, 0), (0, 1), (0, 2), (1, 1))
    assert tuple((3 + x, 6 + y) for x, y in cases) == (
        (3, 6), (3, 7), (3, 8), (4, 7))

    # The case h1=4 gives 2*h1-1=11-h1=7; equality also
    # gives the product-space dimension bounds 2*4-1=7 and 4+7-1=10.
    assert 2 * 4 - 1 == 11 - 4 == 7
    assert 4 + 7 - 1 == 10

    # Period 6: h1=3+e+x, h2=6+e+y, with e>=1 and x,y>=0.
    # If e>=2, write e=2+d (d>=0). Then
    # h1-4=1+d+x, whose strictly positive constant and nonnegative
    # coefficients contradict h1<=4 for every d,x>=0.
    # Coefficients here are (constant, d, x).
    q1, q2 = qmodel(1, 6), qmodel(2, 6)
    e_equals_2_plus_d = tuple(map(F, (2, 1, 0)))
    x_form = tuple(map(F, (0, 0, 1)))
    h1_for_e_ge_2 = add(add((q1[0],),
                           scale(e_equals_2_plus_d, q1[1])), x_form)
    contradiction_certificate = add(h1_for_e_ge_2, (-4,))
    assert contradiction_certificate == tuple(map(F, (1, 1, 1)))
    assert contradiction_certificate[0] > 0
    assert all(c >= 0 for c in contradiction_certificate[1:])

    # Thus e=1. Now h1-4=x, so x=0, and h1+h2-1-10=y,
    # so y=0. These two polynomial identities use x and y separately.
    h1_at_e1_x0, h2_at_e1_y0 = sum(q1), sum(q2)
    assert add((h1_at_e1_x0, 1), (-4,)) == tuple(map(F, (0, 1)))
    assert add(add((h2_at_e1_y0, 1), (h1_at_e1_x0 - 1,)),
               (-10,)) == tuple(map(F, (0, 1)))
    assert (h1_at_e1_x0, h2_at_e1_y0, F(10)) == tuple(map(F, (4, 7, 10)))
    print("PASS: q=P gives exactly four low-degree integer candidates;")
    print("      symbolic period-6 certificates force e=1 and e_1=e_2=0")


def check_weighted_fiber():
    # K_0 coefficients are ordered L_0,L_1,L_2,L_3. Starting with L_3,
    # apply the numerical left-mutation formula at L_2,L_1,L_0.
    # The Euler entries are P(j-i), as established for this example
    # in the manuscript; their geometric validity is not tested here.
    residual = [F(0), F(0), F(0), F(1)]
    for i in (2, 1, 0):
        pairing = sum(residual[j] * p2(j - i) for j in range(4))
        residual[i] -= pairing
    assert tuple(residual) == tuple(map(F, (-1, 3, -3, 1)))

    # R(mu_4) is represented in its free basis 1,eta,eta^2,eta^3.
    # epsilon=eta^2 and the fiber of L_i has character eta^(2*i).
    fiber = [F(0)] * 4
    for i, coefficient in enumerate(residual):
        fiber[(2 * i) % 4] += coefficient
    assert tuple(fiber) == tuple(map(F, (-4, 0, 4, 0)))
    assert any(fiber) and sum(fiber) == 0
    print("PASS: weighted-stack mutation class (-1,3,-3,1) has")
    print("      fiber 4*epsilon-4*1 != 0 in the character basis of mu_4")


def c_ex_dimension(n):
    """Normal-form count for R[u,v]/(uv-F), deg(u)=deg(v)=6.

    R_n has dimension 3*n+1. Normal forms have either u^j or v^j;
    the j=0 contribution is counted once, and every j>=1 twice.
    This count is used only after the algebraic normal-form proof
    given in the research notes, not as a test of the domain property.
    """
    if n < 0:
        return F(0)
    return F(3 * n + 1 + 2 * sum(3 * (n - 6 * j) + 1
                               for j in range(1, n // 6 + 1)))


def check_c_ex_series():
    one_minus_t = tuple(map(F, (1, -1)))
    one_minus_t6 = tuple(map(F, (1, 0, 0, 0, 0, 0, -1)))
    one_plus_t6 = tuple(map(F, (1, 0, 0, 0, 0, 0, 1)))
    one_minus_t12 = tuple(map(F, (1,) + (0,) * 11 + (-1,)))
    # Exact cancellation of the degree-12 regular-relation factor.
    assert mul(one_minus_t6, one_plus_t6) == one_minus_t12
    numerator = mul((1, 2), one_plus_t6)
    denominator = mul(power(one_minus_t, 2), one_minus_t6)
    check_series(c_ex_dimension, denominator, numerator)
    assert tuple(c_ex_dimension(n) for n in (1, 2, 3, 6)) == (
        F(4), F(7), F(10), F(21))
    # At t=1 the remaining factor 1+t+...+t^5 has value 6.
    assert sum(numerator) / F(6) == 1
    print("PASS: C_ex Hilbert factorization and normal-form coefficients")
    print("      h_1=4, h_2=7, h_3=10, h_6=21 (not the required 28)")


def check_conic_boundary():
    """Exact polynomial and matrix certificates used in the conic proof.

    These checks do not prove primeness, the change-of-rings argument, or
    categorical recognition; those arguments are written in the manuscript.
    Gaussian rationals are stored as pairs, so no floating point is used.
    """
    minus, plus = (F(1), F(-1)), (F(1), F(1))
    assert mul(minus, plus) == (F(1), F(0), F(-1))
    assert mul((1, 0, -1), power(plus, 2)) == mul(minus, power(plus, 3))
    # P(2m)=(m+1)(2m+1), P(2m+1)=(m+1)(2m+3).
    assert mul((1, 1), (1, 2)) == tuple(map(F, (1, 3, 2)))
    assert mul((1, 1), (3, 2)) == tuple(map(F, (3, 5, 2)))
    check_series(lambda n: (1 if n == 0 else 3 if n == 1 else 4),
                 (1, 0, -1), power(plus, 3))

    def g(a=0, b=0):
        return F(a), F(b)

    def ga(a, b):
        return a[0] + b[0], a[1] + b[1]

    def gm(a, b):
        return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]

    def ma(a, b):
        return tuple(tuple(ga(a[i][j], b[i][j]) for j in range(2)) for i in range(2))

    def ms(a, c):
        return tuple(tuple(gm(a[i][j], c) for j in range(2)) for i in range(2))

    def mm(a, b):
        return tuple(tuple(ga(gm(a[i][0], b[0][j]), gm(a[i][1], b[1][j]))
                           for j in range(2)) for i in range(2))

    ident = ((g(1), g()), (g(), g(1)))
    zero = ((g(), g()), (g(), g()))
    matrices = (
        ((g(), g(1)), (g(1), g())),
        ((g(), g(0, -1)), (g(0, 1), g())),
        ((g(1), g()), (g(), g(-1))),
    )
    for i, p in enumerate(matrices):
        assert mm(p, p) == ident
        for q in matrices[i + 1:]:
            assert ma(mm(p, q), mm(q, p)) == zero
    p1, p2m, p3 = matrices
    assert mm(p1, p2m) == ms(p3, g(0, 1))
    assert mm(p2m, p3) == ms(p1, g(0, 1))
    assert mm(p3, p1) == ms(p2m, g(0, 1))
    assert ms(ma(ident, p3), g(F(1, 2))) == ((g(1), g()), (g(), g()))
    assert ms(ma(ident, ms(p3, g(-1))), g(F(1, 2))) == ((g(), g()), (g(), g(1)))
    assert ms(ma(p1, ms(p2m, g(0, 1))), g(F(1, 2))) == ((g(), g(1)), (g(), g()))
    assert ms(ma(p1, ms(p2m, g(0, -1))), g(F(1, 2))) == ((g(), g()), (g(1), g()))
    print("PASS: conic Hilbert and Yoneda polynomial identities;")
    print("      exact Pauli relations and all four matrix-unit certificates")


def check_cubic_boundary_obstacles():
    """Exact finite checks for the two nongenerated cubic-boundary models.

    Binary forms of a fixed total degree are represented by setting s=1;
    their coefficient of t^j still records s^(total_degree-j)*t^j.
    All span ranks below use Fraction elimination, not numerical tolerances.
    These checks do not prove domain, saturation, ampleness, or any
    categorical realization; those assertions require the written proofs.
    """
    minus = (F(1), F(-1))
    one_minus_t2, one_minus_t3 = (1, 0, -1), (1, 0, 0, -1)
    # The complete-intersection expression for weights (1,1,1,2)
    # and relation degrees (2,3) equals (1+t+t^2)/(1-t)^2.
    ci_numerator = mul(one_minus_t2, one_minus_t3)
    ci_denominator = mul(power(minus, 3), one_minus_t2)
    assert mul(ci_numerator, power(minus, 2)) == mul(
        (1, 1, 1), ci_denominator)
    check_series(lambda n: 1 if n == 0 else 3 * n,
                 ci_denominator, ci_numerator)

    def monomial(exponent):
        return (F(0),) * exponent + (F(1),)

    def rational_rank(polynomials, width):
        pivots = {}
        for polynomial in polynomials:
            assert len(polynomial) <= width
            row = list(map(F, polynomial)) + [F(0)] * (width - len(polynomial))
            for column in sorted(pivots):
                factor = row[column]
                if factor:
                    basis_row = pivots[column]
                    for j in range(column, width):
                        row[j] -= factor * basis_row[j]
            column = next((j for j, value in enumerate(row) if value), None)
            if column is not None:
                leading = row[column]
                pivots[column] = tuple(value / leading for value in row)
        return len(pivots)

    # u=s^5*t, v=s^3*t^3, w=s*t^5, z=s^12+t^12.
    # Their binary degrees are 6,6,6,12 and their ring weights 1,1,1,2.
    u, v, w = (monomial(j) for j in (1, 3, 5))
    z = add((1,), monomial(12))
    assert mul(u, w) == power(v, 2)
    assert mul(v, z) == add(power(u, 3), power(w, 3))

    max_degree = 12
    z_powers = [power(z, d) for d in range(max_degree // 2 + 1)]
    ranks = []
    for n in range(max_degree + 1):
        forms = []
        for d in range(n // 2 + 1):
            remaining = n - 2 * d
            for a in range(remaining + 1):
                for b in range(remaining - a + 1):
                    c = remaining - a - b
                    exponent = a + 3 * b + 5 * c
                    # The complete list u^a*v^b*w^c*z^d, of weight n.
                    form = (F(0),) * exponent + z_powers[d]
                    row = form + (F(0),) * (6 * n + 1 - len(form))
                    assert all(value == 0 for j, value in enumerate(row)
                               if (j + n) % 2)
                    assert row[0] == row[6 * n]
                    forms.append(form)
        rank = rational_rank(forms, 6 * n + 1)
        ranks.append(rank)
        allowed_exponents = [j for j in range(6 * n + 1) if (j + n) % 2 == 0]
        # For positive even n the two distinct endpoint coefficients
        # obey one independent equality. For n=0 the equality is tautological;
        # for odd n both endpoint coefficients already vanish by parity.
        endpoint_constraints = int(n > 0 and n % 2 == 0)
        section_dimension = len(allowed_exponents) - endpoint_constraints
        assert rank == section_dimension == (1 if n == 0 else 3 * n), (
            n, rank, section_dimension)
    generators = (u, v, w)
    degree_one_products = [mul(generators[i], generators[j])
                           for i in range(3) for j in range(i, 3)]
    assert rational_rank(degree_one_products, 13) == 5
    assert ranks[2] == 6

    # Independently reconstruct the ambient Hilbert sequence of the
    # finite-tail defect model from h_n-h_(n-3)=b_n and h_negative=0.
    def finite_tail_dimension(n):
        return (1, 2, 5)[n] if n < 3 else 3 * n

    ambient = []
    for n in range(31):
        ambient.append(F(finite_tail_dimension(n)) +
                       (ambient[n - 3] if n >= 3 else F(0)))
        assert ambient[n] == p2(n) - int(n % 3 != 0), (n, ambient[n])
    print("PASS: cubic-boundary CI Hilbert identity and exact binary-form relations;")
    print("      rational span ranks equal parity/endpoint section dimensions in degrees 0..12")
    print("      (rank B_1^2=5, dim B_2=6); finite-tail recurrence verified through degree 30")


def check_cubic_section_defects():
    """Finite exact checks of defect telescoping and Laurent identities.

    The distributions below are formal dimension data: nonnegative finite
    defects in residues 1 and 2 with equal mass. They are not claimed to be
    realized by graded domains or categories. The Hilbert/Euler checks
    explicitly impose the additional assumption hat_b_n=3*n for n>0.
    Laurent identities are compared coefficient by coefficient on their
    full finite support, so there is no truncation in those comparisons.
    """
    distributions = (
        {},
        {1: 1, 2: 1},
        {1: 1, 4: 2, 10: 1, 2: 2, 8: 1, 14: 1},
        {4: 2, 7: 1, 16: 2, 5: 1, 11: 3, 20: 1},
        {1: 2, 7: 1, 22: 1, 2: 1, 5: 1, 17: 2},
    )
    check_bound = max(n for defect in distributions for n in defect) + 12

    def clean(poly):
        return {n: F(c) for n, c in poly.items() if c}

    def t3_minus_one(poly):
        result = {}
        for n, coefficient in poly.items():
            result[n + 3] = result.get(n + 3, F(0)) + coefficient
            result[n] = result.get(n, F(0)) - coefficient
        return clean(result)

    masses = []
    for defect in distributions:
        # These are hypotheses of the formal family, not conclusions
        # about an algebra whose existence has been established.
        assert all(isinstance(n, int) and n > 0 and n % 3 in (1, 2)
                   and isinstance(c, int) and c > 0
                   for n, c in defect.items())
        residue_masses = tuple(sum(c for n, c in defect.items() if n % 3 == r)
                               for r in (1, 2))
        assert residue_masses[0] == residue_masses[1]
        epsilon = residue_masses[0]
        masses.append(epsilon)
        assert sum(defect.values()) == 2 * epsilon
        # Nonnegative boundary dimensions are also needed for the
        # conditional Hilbert data used below. No multiplication is assumed.
        assert all(c <= 3 * n for n, c in defect.items())

        cutoff = max(defect, default=0)
        e_positive = clean({
            n: sum(c for degree, c in defect.items()
                   if degree > n and degree % 3 == n % 3)
            for n in range(1, cutoff + 1) if n % 3
        })
        ext = dict(e_positive)
        for n, coefficient in e_positive.items():
            ext[-n - 3] = coefficient
        if epsilon:
            ext[-1] = ext[-2] = F(epsilon)

        def e(n):
            return ext.get(n, F(0))

        bound = check_bound
        for n in range(-bound, bound + 1):
            assert e(n) == e(-n - 3), (defect, n)
            if n % 3 == 0:
                assert e(n) == 0
        for n in range(1, bound + 1):
            assert e(n - 3) - e(n) == defect.get(n, 0), (defect, n)
        for r in (1, 2):
            partial = F(0)
            for n in range(r, bound + 1, 3):
                partial += defect.get(n, 0)
                assert partial == epsilon - e(n), (defect, n)
            assert partial == epsilon

        c = clean(defect)
        rhs = dict(c)
        for n, coefficient in c.items():
            rhs[-n] = -coefficient
        assert t3_minus_one(ext) == clean(rhs)
        positive_rhs = t3_minus_one(e_positive)
        for n in (1, 2):
            positive_rhs[n] = positive_rhs.get(n, F(0)) + epsilon
        assert clean(positive_rhs) == c
        assert sum(ext.values()) == F(2, 3) * sum(
            n * coefficient for n, coefficient in c.items())
        assert (not ext) == (not defect) == (epsilon == 0)

        # Conditional branch: hat_b_n=3*n, hence b_n=3*n-delta_n.
        # Reconstruct h from the cut rather than from the target formula.
        h = []
        for n in range(bound + 1):
            b_n = F(1 if n == 0 else 3 * n - defect.get(n, 0))
            assert b_n >= 0
            h.append(b_n + (h[n - 3] if n >= 3 else F(0)))
            expected = p2(n) - epsilon * int(n % 3 != 0) + e(n)
            assert h[n] == expected, (defect, n, h[n], expected)
            assert 0 <= h[n] <= p2(n)

        def section(n):
            return h[n] if n >= 0 else F(0)

        # Serre's degree-2 term is h_(-n-3); check all negative as
        # well as positive Euler degrees in the stated finite window.
        for n in range(-bound, bound + 1):
            q_n = section(n) - e(n) + section(-n - 3)
            assert q_n == p2(n) - epsilon * int(n % 3 != 0), (defect, n)

    # A one-sided defect is deliberately outside the balanced family.
    # This is the numerical obstruction to the smooth-cubic subring
    # C + V + T_(>=2), not a computational proof of the categorical theorem.
    unbalanced = {1: 1}
    assert sum(c for n, c in unbalanced.items() if n % 3 == 1) != sum(
        c for n, c in unbalanced.items() if n % 3 == 2)
    assert masses == [0, 1, 4, 5, 4]
    print("PASS: five formal defect distributions (residue masses 0,1,4,5,4);")
    print("      full-support Laurent identities, telescoping, and first-moment identity")
    print("      conditional standard-saturation Hilbert/Euler formulas through degree 34")
    print("      (and corresponding negative degrees); unbalanced defect rejected")


def exact_rank(matrix):
    """Rank by Gaussian elimination over Q, with no floating-point steps."""
    if not matrix:
        return 0
    width = len(matrix[0])
    assert all(len(row) == width for row in matrix)
    work = [[F(entry) for entry in row] for row in matrix]
    pivot_row = 0
    for col in range(width):
        pivot = next((r for r in range(pivot_row, len(work))
                      if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        # Echelon form suffices for rank; every operation is exact.
        for row in range(pivot_row + 1, len(work)):
            factor = work[row][col]
            if factor:
                work[row] = [a - factor * b for a, b in
                             zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def verify_degenerate_beilinson_bar():
    """Generate the relative normalized bar complex of one explicit algebra.

    Vertices are 0, 1, 2; arrows v_i: 0 -> 1 and w_a: 1 -> 2 have
    relations w_0*v_i=0, and w_1*v_i, w_2*v_i are the six length-two
    basis paths. Here K is the span of the three vertex idempotents,
    J is the radical, and C^n=Hom_{K-K}(J^{tensor_K n}, Lambda).
    Actual multiplication generates the differential matrices; neither
    the minimal bimodule resolution nor its predicted ranks are used.
    """
    # A basis entry is (name, source, target, path length).
    basis = [(f"e{i}", i, i, 0) for i in range(3)]
    basis += [(f"v{i}", 0, 1, 1) for i in range(3)]
    basis += [(f"w{a}", 1, 2, 1) for a in range(3)]
    basis += [(f"u{a}{i}", 0, 2, 2)
              for a in (1, 2) for i in range(3)]
    index = {entry[0]: pos for pos, entry in enumerate(basis)}
    assert len(index) == len(basis)
    radical = [pos for pos, entry in enumerate(basis) if entry[3] > 0]
    vertices = [pos for pos, entry in enumerate(basis) if entry[3] == 0]

    def multiply(left, right):
        """Basis product: compose right first, then left; None denotes zero."""
        if left is None or right is None:
            return None
        lname, lsource, ltarget, llen = basis[left]
        rname, rsource, rtarget, rlen = basis[right]
        if lsource != rtarget:
            return None
        if llen == 0:
            return right
        if rlen == 0:
            return left
        if lname.startswith("w") and rname.startswith("v"):
            a = int(lname[1:])
            i = int(rname[1:])
            return None if a == 0 else index[f"u{a}{i}"]
        return None

    multiplication = {(left, right): multiply(left, right)
                      for left, right in product(range(len(basis)), repeat=2)}

    def table_product(left, right):
        if left is None or right is None:
            return None
        return multiplication[left, right]

    # A consistency check of the input algebra, independent of cohomology.
    for left, middle, right in product(range(len(basis)), repeat=3):
        assert table_product(table_product(left, middle), right) == \
               table_product(left, table_product(middle, right))

    def chains(length):
        """Basis of J^{tensor_K length}; zero products remain tensor inputs."""
        if length == 1:
            return [(entry,) for entry in radical]
        return [chain + (right,)
                for chain in chains(length - 1) for right in radical
                if basis[chain[-1]][1] == basis[right][2]]

    def cochains(length):
        """Elementary K-bimodule maps: one input chain, one parallel output."""
        result = []
        for chain in chains(length):
            source = basis[chain[-1]][1]
            target = basis[chain[0]][2]
            for out, (_, out_source, out_target, _) in enumerate(basis):
                if out_source == source and out_target == target:
                    result.append((chain, out))
        return result

    c0 = vertices
    c1, c2, c3 = (cochains(degree) for degree in (1, 2, 3))
    c1_position = {key: pos for pos, key in enumerate(c1)}
    c2_position = {key: pos for pos, key in enumerate(c2)}
    d0 = [[0 for _ in c0] for _ in c1]
    d1 = [[0 for _ in c1] for _ in c2]

    # delta(c)(x) = x*c - c*x, with c one vertex idempotent.
    for column, c in enumerate(c0):
        for x in radical:
            for sign, out in ((1, table_product(x, c)),
                              (-1, table_product(c, x))):
                if out is not None:
                    d0[c1_position[((x,), out)]][column] += sign

    # delta(f)(x,y) = x*f(y) - f(x*y) + f(x)*y.
    # This is generated on all elementary cochains and composable J-pairs.
    for column, ((input_element,), output_element) in enumerate(c1):
        for pair in chains(2):
            x, y = pair
            terms = []
            if y == input_element:
                terms.append((1, table_product(x, output_element)))
            xy = table_product(x, y)
            if xy == input_element:
                terms.append((-1, output_element))
            if x == input_element:
                terms.append((1, table_product(output_element, y)))
            for sign, out in terms:
                if out is not None:
                    d1[c2_position[(pair, out)]][column] += sign

    # Verify the complex before computing cohomology.
    for row in range(len(c2)):
        for column in range(len(c0)):
            composite = sum(d1[row][middle] * d0[middle][column]
                            for middle in range(len(c1)))
            assert composite == 0, (row, column, composite)

    rank_d0 = exact_rank(d0)
    rank_d1 = exact_rank(d1)
    dimensions = (len(c0), len(c1), len(c2), len(c3))
    assert len(c3) == 0, "A nonzero third bar term was found."
    hochschild = (len(c0) - rank_d0,
                  len(c1) - rank_d0 - rank_d1,
                  len(c2) - rank_d1)

    # These assertions compare derived output to the mathematical prediction;
    # they are never used to generate matrices or perform rank elimination.
    assert dimensions == (3, 54, 54, 0), dimensions
    assert (rank_d0, rank_d1) == (2, 38), (rank_d0, rank_d1)
    assert hochschild == (1, 14, 16), hochschild
    return {
        "algebra_dimension": len(basis),
        "radical_dimension": len(radical),
        "cochain_dimensions": dimensions,
        "differential_ranks": (rank_d0, rank_d1),
        "HH_dimensions": hochschild,
        "d1_d0_zero": True,
        "multiplication_associative": True,
        "arithmetic": "Fraction Gaussian elimination over Q",
    }



def verify_cubic_euler_discriminant():
    """Check G_e, the full change of basis, and its two orthogonal blocks."""
    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]

    def matrix_product(left, right):
        assert len(left[0]) == len(right)
        result = []
        for row in left:
            output_row = []
            for col in transpose(right):
                value = (F(0),)
                for x, y in zip(row, col):
                    value = add(value, mul(x, y))
                output_row.append(value)
            result.append(output_row)
        return result

    gram = [[qmodel(j - i, 3) for j in range(5)] for i in range(5)]
    integer_change = [
        [1, 0, 0, -1, 0],
        [1, 1, 0, 3, -1],
        [1, 1, 1, -3, 3],
        [0, 1, 1, 1, -3],
        [0, 0, 1, 0, 1],
    ]
    change = [[(F(x),) for x in row] for row in integer_change]
    transformed = matrix_product(matrix_product(transpose(change), gram), change)

    constant_block = [[15, 33, 60], [6, 15, 33], [6, 6, 15]]
    polynomial_block = [[(F(x), F(-6)) for x in row]
                        for row in constant_block]
    periodic_block = [[(F(0), F(18)), (F(0), F(-9))],
                      [(F(0), F(-9)), (F(0), F(18))]]
    expected = [[(F(0),) for _ in range(5)] for _ in range(5)]
    for i in range(3):
        for j in range(3):
            expected[i][j] = polynomial_block[i][j]
    for i in range(2):
        for j in range(2):
            expected[i + 3][j + 3] = periodic_block[i][j]
    assert transformed == expected

    assert det(change) == (F(27),)
    assert det(polynomial_block) == (F(3**6),)
    assert det(periodic_block) == (F(0), F(0), F(3**5))
    assert det(gram) == (F(0), F(0), F(3**5))
    assert det(transformed) == mul(mul(det(change), det(change)), det(gram))
    print("PASS: symbolic cubic Euler Gram and full basis-change identity;")
    print("      det(T)=27, det(H_e)=3^6, periodic block=9e*A_2,")
    print("      det(G_e)=3^5*e^2; off-diagonal blocks vanish identically")
    print("      The nonsquare and lattice-index conclusions are proved in the text.")

def main():
    verify_cubic_euler_discriminant()
    one_minus_t = (F(1), F(-1))
    cubic_denominator = power(one_minus_t, 3)
    check_series(lambda n: p2(n), cubic_denominator, (F(1),))
    check_series(lambda n: p2(3 * n), cubic_denominator,
                 tuple(map(F, (1, 7, 1))))
    # The numerator cancellation for a degree-3 elliptic central quotient.
    assert mul((1, 1, 1), one_minus_t) == (F(1), F(0), F(0), F(-1))
    # The equation determining the three degree-one generators.
    assert mul((-3, 1), (3, 1, 1)) == tuple(map(F, (-9, 0, -2, 1)))
    # Gram computation after b=a^2-a, symbolic in a.
    a, b = (F(0), F(1)), tuple(map(F, (0, -1, 1)))
    gram = [[(F(1),), a, b], [(F(0),), (F(1),), a],
            [(F(0),), (F(0),), (F(1),)]]
    v = [(F(1),), scale(a, -1), a]
    for j in range(3):
        result = (F(0),)
        for i in range(3):
            result = add(result, mul(v[i], gram[i][j]))
        assert result == (F(int(j == 0)),)
    for kind, determinant_coefficient in ((3, 243), (6, 1)):
        matrix = [[qmodel(j - i, kind) for j in range(5)] for i in range(5)]
        assert det(matrix) == tuple(map(F, (0, 0, determinant_coefficient)))
        quadratic = (1, 1, 1) if kind == 3 else (1, -1, 1)
        recurrence = mul(power((-1, 1), 3), quadratic)
        # For each residue mod 6, the left hand side is a degree <=2
        # polynomial in n; three points per residue certify the identity.
        for n in range(-12, 13):
            result = (F(0),)
            for j, c in enumerate(recurrence):
                result = add(result, scale(qmodel(n + j, kind), c))
            assert result == (F(0),), (kind, n, result)
            assert qmodel(n, kind) == qmodel(-n - 3, kind)
            if n % 3 == 0:
                assert qmodel(n, kind) == (p2(n),)
        assert qmodel(-1, kind) == (F(0), F(-1))
        # e=1 gives nonnegative section dimensions in the model.
        for n in range(36):
            assert sum(qmodel(n, kind)) >= 0
        print(f"PASS: rank-5 model {kind}, symbolic determinant "
              f"{determinant_coefficient}*e^2 and exact recurrence")
    for n in range(40):
        weighted_6n = sum(6 * n - 4 * j + 1 for j in range(3 * n // 2 + 1))
        weighted_2n = sum(2 * n - 4 * j + 1 for j in range(n // 2 + 1))
        assert weighted_6n == p2(3 * n)
        assert weighted_2n == p2(n)
    print("PASS: Hilbert series, central quotient, Euler Gram identities,")
    print("      cubic factorization, and weighted monomial counts")
    check_low_degree_constraints()
    check_weighted_fiber()
    check_c_ex_series()
    check_conic_boundary()
    check_cubic_boundary_obstacles()
    check_cubic_section_defects()
    bar_result = verify_degenerate_beilinson_bar()
    print("PASS: degenerate Beilinson algebra, relative normalized bar complex;")
    print(f"      C dimensions={bar_result['cochain_dimensions']}, "
          f"differential ranks={bar_result['differential_ranks']}")
    print(f"      HH dimensions={bar_result['HH_dimensions']}; "
          "associative multiplication and d1*d0=0 verified")
    print("All exact checks passed. Categorical existence, hypotheses,")
    print("and the general recognition theorem are not tested here.")


if __name__ == '__main__':
    main()
