"""Reproduce the finite table and both examples in the paper (Python 3.9+)."""

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt


def factor(n):
    """Return the exponents in the prime factorization of a positive integer."""
    exponents = {}
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            exponents[divisor] = exponents.get(divisor, 0) + 1
            n //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if n > 1:
        exponents[n] = 1
    return exponents


def divisor_residues(p, t):
    """Compute every possible residue of a positive divisor of M**2 modulo t."""
    x = (p * p + t) // 4
    exponents = factor(x)
    exponents[p] = exponents.get(p, 0) + 2  # M = p**2 * x
    residues = {1}
    for prime, exponent in exponents.items():
        powers = {pow(prime, k, t) for k in range(2 * exponent + 1)}
        residues = {(r * s) % t for r in residues for s in powers}
    return residues


def feasible(p, t):
    """Apply Lemma 2 in its stated range, with p an odd prime."""
    if t <= 0 or t % 4 != 3 or p * p <= t or gcd(p, t) != 1:
        raise ValueError("Offset outside the hypotheses of Lemma 2")
    x = (p * p + t) // 4
    return (-p * p * x) % t in divisor_residues(p, t)


def verify_table():
    offsets = list(range(3, 32, 4))
    counts = Counter()
    for p in range(41, 10000, 2):
        if any(p % d == 0 for d in range(3, isqrt(p) + 1, 2)):
            continue
        first = next((t for t in offsets if feasible(p, t)), None)
        counts[first] += 1

    columns = offsets + [None]  # None means no successful offset through 31.
    values = [counts[t] for t in columns]
    expected = [611, 309, 154, 76, 31, 24, 0, 9, 3]
    if values != expected:
        raise RuntimeError(f"Table mismatch: expected {expected}, computed {values}")
    print(f"Primes in [41, 10000): {sum(values)}")
    print("First offset:", *(str(t) if t is not None else ">31" for t in columns), sep="\t")
    print("Count:       ", *values, sep="\t")


def verify_examples():
    p, r = 43, 11
    n = p * p
    x = (n + r) // 4
    k = (p + 1) // r
    y, z = p * x * k, n * x * k
    if (x, y, z) != (465, 79980, 3439140):
        raise RuntimeError("Example 1 denominators do not match the paper")
    if sum(Fraction(1, d) for d in (x, y, z)) != Fraction(4, n):
        raise RuntimeError("Example 1 fraction identity failed")
    if [feasible(p, t) for t in (3, 7, 11)] != [False, False, True]:
        raise RuntimeError("Example 1 first offset differs from 11")
    print(f"Example 1: 4/{n} = 1/{x} + 1/{y} + 1/{z}; first offset = {r}")

    p, t = 29, 19
    x = (p * p + t) // 4
    target = (-p * p * x) % t
    residues = divisor_residues(p, t)
    # Euler's criterion at the prime modulus 19 gives -1 as residue 18.
    if pow(p, (t - 1) // 2, t) != t - 1:
        raise RuntimeError("Example 2 Legendre symbol differs from -1")
    if x != 215 or target != pow(10, 15, t) or target in residues:
        raise RuntimeError("Example 2 obstruction failed")
    print(f"Example 2: p = {p}, t = {t}, x = {x}; Legendre symbol = -1")
    print(f"  Required divisor residue {target} is absent from {sorted(residues)}")


if __name__ == "__main__":
    verify_table()
    verify_examples()
