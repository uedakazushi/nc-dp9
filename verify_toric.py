#!/usr/bin/env python3
"""Exact finite checks for research_notes.tex, using only Python stdlib.

The all-parameter proofs are in the current manuscript and research notes. This program
reproduces lattice-point counts and minimal generators for explicit members
of the family. It does not certify the categorical axioms or prove that a
general noncommutative algebra has a normal toric degeneration.
"""
from fractions import Fraction


def p2(n):
    return Fraction((n + 1) * (n + 2), 2)


def points(q, n):
    """Enumerate the degree-n lattice slice by the three facet inequalities."""
    if n < 0:
        return set()
    return {(x, y, n)
            for y in range(n // 3 + 1)
            for x in range(3 * n + 1)
            if q * x - y >= 0
            and 3 * q * n - q * x - (9 * q - 1) * y >= 0}


def belongs(q, value):
    x, y, n = value
    return (n >= 0 and y >= 0 and q * x >= y
            and 3 * q * n - q * x - (9 * q - 1) * y >= 0)


def formula(q, n):
    return p2(n) + int(n % 3 != 0) + n // (3 * q)


def expected_generators(q):
    return ({(a, 0, 1) for a in range(4)}
            | {(a, j, 3 * j + 1)
               for j in range(1, q) for a in (1, 2, 3)}
            | {(1, q, 3 * q)})


def expected_free_basis(q):
    return ({(0, 0, 0), (1, 0, 1), (2, 0, 1)}
            | {(a, j, 3 * j + 1)
               for j in range(1, q) for a in (1, 2, 3)})


def ray_coordinates(q, value):
    x, y, n = value
    lambda2 = Fraction(y, q)
    lambda1 = (Fraction(x) - lambda2) / 3
    lambda0 = Fraction(n) - lambda1 - 3 * q * lambda2
    return lambda0, lambda1, lambda2


def point_add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def point_sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def minimal_generators_through(q, bound, slices):
    """Independent exhaustive indecomposability check through a finite degree."""
    result = set()
    for n in range(1, bound + 1):
        for value in slices[n]:
            decomposable = any(
                belongs(q, point_sub(value, first))
                for d in range(1, n)
                for first in slices[d])
            if not decomposable:
                result.add(value)
    return result


def hilbert_numerator(q):
    # Numerator obtained from the half-open parallelepiped basis.
    result = {0: 1, 1: 2}
    for j in range(1, q):
        result[3 * j + 1] = 3
    return result


def check_hilbert_identity(q, slices):
    # (1-t)^2(1-t^(3q))H(t) = 1+2t+3 sum t^(3j+1).
    denominator = {0: 1, 1: -2, 2: 1,
                   3 * q: -1, 3 * q + 1: 2, 3 * q + 2: -1}
    numerator = hilbert_numerator(q)
    for n in range(len(slices)):
        coefficient = sum(c * len(slices[n - degree])
                          for degree, c in denominator.items()
                          if degree <= n)
        assert coefficient == numerator.get(n, 0), (q, n, coefficient)
    assert sum(numerator.values()) == 3 * q


def polynomial_add(p, q):
    return tuple((p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q))))


def polynomial_mul(p, q):
    result = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return tuple(result)


STAR_GENERATORS = ((0, 0, 1), (1, 0, 1), (2, 0, 1), (3, 0, 1),
                   (2, 1, 4), (3, 1, 4), (2, 2, 6))
STAR_BASIS = ((0, 0, 0), (1, 0, 1), (2, 0, 1),
              (2, 1, 4), (3, 1, 4), (4, 1, 5))


def star_points(n):
    """Facet description: remove odd-height points on either sloping facet."""
    return {value for value in points(1, n)
            if value[1] % 2 == 0
            or (value[0] != value[1]
                and 3 * value[2] - value[0] - 8 * value[1] != 0)}


def star_decompose(value):
    """Express a monomial as u^i v^j z^k times a B-basis element."""
    answers = []
    for basis_index, basis_value in enumerate(STAR_BASIS):
        dx, dy, dn = point_sub(value, basis_value)
        if dy < 0 or dy % 2:
            continue
        z_power = dy // 2
        if dx - 2 * z_power < 0 or (dx - 2 * z_power) % 3:
            continue
        v_power = (dx - 2 * z_power) // 3
        u_power = dn - v_power - 6 * z_power
        if u_power >= 0:
            answers.append((basis_index, (u_power, v_power, z_power)))
    assert len(answers) == 1, (value, answers)
    return answers[0]


def check_star_ring():
    # Enumerate from the actual seven generators, independently of the facets.
    slices = [{(0, 0, 0)}]
    for n in range(1, 61):
        slices.append({point_add(generator, previous)
                       for generator in STAR_GENERATORS if generator[2] <= n
                       for previous in slices[n - generator[2]]})
    for n, values in enumerate(slices):
        assert values == star_points(n), (n, values ^ star_points(n))
        assert len(values) == p2(n) + int(n % 6 in (1, 2)), n
        if n % 3 == 0:
            assert len(values) == p2(n)
    assert tuple(len(slices[n]) for n in range(1, 7)) == (4, 7, 10, 15, 21, 28)
    assert {point_add(a, b) for a in slices[1] for b in slices[1]} == slices[2]
    assert {point_add(a, b) for a in slices[2] for b in slices[1]} == slices[3]

    # Polynomial identity for the complete rational Hilbert series.
    numerator = tuple(map(Fraction, (1, 2, 0, 0, 2, 1)))
    one_minus_t = tuple(map(Fraction, (1, -1)))
    one_minus_t6 = tuple(map(Fraction, (1, 0, 0, 0, 0, 0, -1)))
    correction = polynomial_mul((0, 1, 1),
                                polynomial_mul(polynomial_mul(one_minus_t, one_minus_t),
                                               one_minus_t))
    assert polynomial_mul(numerator, one_minus_t) == polynomial_add(one_minus_t6, correction)
    denominator = polynomial_mul(polynomial_mul(one_minus_t, one_minus_t), one_minus_t6)
    for n in range(len(slices)):
        coefficient = sum(c * len(slices[n - d]) for d, c in enumerate(denominator) if d <= n)
        assert coefficient == (numerator[n] if n < len(numerator) else 0)

    # All 36 basis-product identities are universal monomial identities.
    # The top-basis coefficient pairs 1 with f, a with d, and b with c.
    for i, a in enumerate(STAR_BASIS):
        for j, b in enumerate(STAR_BASIS):
            basis_index, powers = star_decompose(point_add(a, b))
            if i + j == 5:
                assert basis_index == 5 and powers == (0, 0, 0)
            else:
                assert basis_index != 5
    assert sum((1, 1, 6)) - STAR_BASIS[-1][2] == 3

    # Non-normality witness w=c/a, w^2=z.
    w = (1, 1, 3)
    assert w not in slices[3]
    assert point_add(w, w) == STAR_GENERATORS[-1]
    assert point_sub(STAR_GENERATORS[4], STAR_GENERATORS[1]) == w

    # Only z lies on the common zero face of the two nonnegative forms.
    for generator in STAR_GENERATORS:
        x, y, n = generator
        left, right = x - y, 3 * n - x - 8 * y
        assert left >= 0 and right >= 0
        assert (left == right == 0) == (generator == STAR_GENERATORS[-1])
    # The residue calculation covers every m, because m has two classes mod 2.
    assert {(3 * r + 1) % 6 for r in (0, 1)} == {1, 4}

    # Independently check minimality of the seven generators in finite degrees.
    minimal = set()
    for n in range(1, 13):
        for value in slices[n]:
            if not any(point_sub(value, first) in slices[n - d]
                       for d in range(1, n) for first in slices[d]):
                minimal.add(value)
    assert minimal == set(STAR_GENERATORS)
    print("PASS: A_* actual generators and facet counts in degrees 0..60;")
    print("      exact full Hilbert-series identity, six-element free basis,")
    print("      perfect coefficient pairing, non-normality witness, and face quotient residues")


def main():
    # The row-count simplification is polynomial in m. Check its rational
    # coefficients directly for each of the only three possible residues r.
    for r in range(3):
        row_polynomial = (Fraction(3 * r + 1),
                          Fraction(3 * r) + Fraction(9, 2), Fraction(9, 2))
        p_polynomial = (Fraction((r + 1) * (r + 2), 2),
                        Fraction(3 * r) + Fraction(9, 2), Fraction(9, 2))
        difference = tuple(a - b for a, b in zip(row_polynomial, p_polynomial))
        assert difference == (Fraction(r * (3 - r), 2), 0, 0)
        assert difference[0] == int(r != 0)
    assert p2(-3) == 1
    print("PASS: exact residue-polynomial row-count identity and P(-3)=1")
    check_star_ring()

    for q in range(2, 9):
        slices = [points(q, n) for n in range(6 * q + 1)]
        for n, values in enumerate(slices):
            assert len(values) == formula(q, n), (q, n, len(values), formula(q, n))
        assert tuple(len(slices[n]) for n in (1, 2, 3)) == (4, 7, 10)
        if q >= 3:
            assert len(slices[6]) == 28
        for m in range(q):
            assert len(slices[3 * m]) == p2(3 * m)
        assert len(slices[3 * q]) == p2(3 * q) + 1

        degree2_products = {point_add(u, v) for u in slices[1] for v in slices[1]}
        degree3_products = {point_add(u, v) for u in degree2_products for v in slices[1]}
        assert degree2_products == slices[2]
        assert degree3_products == slices[3]
        check_hilbert_identity(q, slices)

        free_basis = expected_free_basis(q)
        assert len(free_basis) == 3 * q
        assert all(belongs(q, value) and all(0 <= c < 1 for c in ray_coordinates(q, value))
                   for value in free_basis)
        # Directly enumerate the entire bounded half-open parallelepiped.
        enumerated_basis = {
            (x, y, n)
            for x in range(4)
            for y in range(q)
            for n in range(3 * q + 2)
            if all(0 <= c < 1 for c in ray_coordinates(q, (x, y, n)))}
        assert free_basis == enumerated_basis

        # Compare the predicted minimal generators with all decompositions,
        # independently enumerated through one degree past the last generator.
        generated = minimal_generators_through(q, 3 * q + 1, slices)
        assert generated == expected_generators(q), (q, generated)
        assert len(generated) == 3 * q + 2
        assert max(n for x, y, n in generated) == 3 * q
        print(f"PASS: q={q}, slices 0..{6*q}, exact free basis of size {3*q}, "
              f"minimal generators through degree {3*q+1}")

    print("All exact finite checks passed. The infinite-parameter proofs,")
    print("normality, depth, reciprocity argument, and categorical limitations")
    print("are stated and proved or cited in the manuscript and research_notes.tex.")


if __name__ == '__main__':
    main()
