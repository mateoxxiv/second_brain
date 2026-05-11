"""
General vector spaces: polynomials, matrices, and functions as vector spaces.
Demonstrates that the 10 axioms hold for objects beyond R^n tuples.
See also: vectors_and_spaces.py, euclidean_n_space.py
"""

import numpy as np


# ---------------------------------------------------------------------------
# Basic: polynomials as a vector space (coefficient arrays)
# [a0, a1, a2] ↔ a0 + a1·x + a2·x²
# ---------------------------------------------------------------------------
p = np.array([1., 0., 1.])   # 1 + x²
q = np.array([-3., 2., 0.])  # -3 + 2x
zero = np.zeros(3)            # zero polynomial

print("=== Basic: polynomial vector space ===")
print(f"p + q         = {p + q}")       # [-2.  2.  1.]  →  -2 + 2x + x²
print(f"3·p           = {3 * p}")       # [ 3.  0.  3.]  →  3 + 3x²
print(f"p + (-p) = 0? {np.allclose(p + (-p), zero)}")   # True  (axiom 5)
print(f"1·p = p?      {np.allclose(1 * p, p)}")          # True  (axiom 10)
print(f"p+q = q+p?    {np.allclose(p + q, q + p)}")      # True  (axiom 2)

# ---------------------------------------------------------------------------
# Intermediate: matrices as a vector space
# ---------------------------------------------------------------------------
A = np.array([[1., 2.], [3., 4.]])
B = np.array([[5., 6.], [7., 8.]])
zero_mat = np.zeros((2, 2))

print("\n=== Intermediate: matrix vector space (M_2x2) ===")
print(f"A + B =\n{A + B}")
print(f"2·A   =\n{2 * A}")
print(f"A + zero = A?  {np.allclose(A + zero_mat, A)}")   # True  (axiom 4)
print(f"A + (-A) = 0?  {np.allclose(A + (-A), zero_mat)}") # True  (axiom 5)

# ---------------------------------------------------------------------------
# Advanced: verify ALL 10 axioms on a general vector space (polynomial)
#
# Axiom meanings in plain English:
#   1  Closure (add)      — adding two vectors always stays inside the space
#   2  Commutativity      — order of addition doesn't matter: u+v = v+u
#   3  Associativity      — grouping of addition doesn't matter: (u+v)+w = u+(v+w)
#   4  Zero vector        — there is a neutral element: adding it changes nothing
#   5  Negatives          — every vector has an opposite that cancels it to zero
#   6  Closure (scalar)   — scaling a vector always stays inside the space
#   7  Distributivity I   — scaling distributes over vector addition: k(u+v) = ku+kv
#   8  Distributivity II  — adding scalars distributes over the vector: (k+l)u = ku+lu
#   9  Scalar assoc.      — chaining two scalings equals one combined scaling: k(lu)=(kl)u
#  10  Scalar identity    — scaling by 1 leaves the vector unchanged: 1u = u
# ---------------------------------------------------------------------------
r = np.array([0., 1., -1.])  # x - x²
k, l = 3.0, -2.0

axioms = {
    "1  closure add":     True,                                          # by np array construction
    "2  commutativity":   np.allclose(p + q, q + p),
    "3  associativity":   np.allclose(p + (q + r), (p + q) + r),
    "4  zero vector":     np.allclose(p + zero, p),
    "5  negatives":       np.allclose(p + (-p), zero),
    "6  closure scalar":  True,                                          # by np array construction
    "7  distrib I":       np.allclose(k * (p + q), k*p + k*q),
    "8  distrib II":      np.allclose((k + l) * p, k*p + l*p),
    "9  scalar assoc":    np.allclose(k * (l * p), (k * l) * p),
    "10 scalar identity": np.allclose(1 * p, p),
}

print("\n=== Advanced: all 10 axioms verified on P_2 ===")
for name, result in axioms.items():
    print(f"  Axiom {name}: {'✓' if result else '✗'}")


def exercises():
    """
    Exercise 1 (Basic):
        Polynomials p = 2 + x, q = 1 - x². Compute p+q and 4·p as coefficient arrays.
        Verify p + (-p) = zero polynomial.
        Expected: p+q = [3, 1, -1], 4p = [8, 4, 0]

    Exercise 2 (Intermediate):
        Is the set {(x,y) in R^2 : x >= 0} a vector space?
        Try scaling u=(1,0) by k=-1. Does the result stay in the set?
        Expected: -1·(1,0) = (-1,0) — x < 0, so axiom 6 fails → NOT a vector space.

    Exercise 3 (Advanced):
        Prove the zero vector is unique using only the 10 axioms.
        Assume 0 and 0' both satisfy axiom 4.
        Then: 0 = 0 + 0' = 0' + 0 = 0' (using axioms 4 and 2).
        Implement: show np.zeros(3) is the unique zero for polynomial space
        by testing that any other candidate fails axiom 4 for some p.
    """
    pass
