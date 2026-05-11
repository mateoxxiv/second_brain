"""
Euclidean n-space: norm, distance, Cauchy-Schwarz, and triangle inequality.
Demonstrates how 2D/3D geometry generalizes to R^n.
See also: vectors_and_spaces.py, dot_product.py
"""

import numpy as np


def euclidean_distance(u: np.ndarray, v: np.ndarray) -> float:
    """Euclidean (L2) distance between two points in R^n."""
    return float(np.linalg.norm(u - v))


def cauchy_schwarz_sides(u: np.ndarray, v: np.ndarray) -> tuple[float, float]:
    """Returns (|u·v|, ||u||·||v||) — left and right sides of Cauchy-Schwarz."""
    return abs(float(np.dot(u, v))), float(np.linalg.norm(u) * np.linalg.norm(v))


# ---------------------------------------------------------------------------
# Basic: norm and distance in R^4
# ---------------------------------------------------------------------------
u4 = np.array([1., 0., 0., 1.])
v4 = np.array([0., 1., 1., 0.])

print("=== Basic: norm and distance in R^4 ===")
print(f"||u|| = {np.linalg.norm(u4):.4f}")            # sqrt(2) ≈ 1.4142
print(f"||v|| = {np.linalg.norm(v4):.4f}")            # sqrt(2) ≈ 1.4142
print(f"d(u,v) = {euclidean_distance(u4, v4):.4f}")   # 2.0

# ---------------------------------------------------------------------------
# Intermediate: Cauchy-Schwarz and scalar projection
# ---------------------------------------------------------------------------
a = np.array([3., 4.])
b = np.array([1., 2.])
lhs, rhs = cauchy_schwarz_sides(a, b)

print("\n=== Intermediate: Cauchy-Schwarz ===")
print(f"|a·b| = {lhs:.4f}")               # 11.0
print(f"||a||·||b|| = {rhs:.4f}")         # 5 * sqrt(5) ≈ 11.1803
print(f"Cauchy-Schwarz holds? {lhs <= rhs + 1e-9}")  # True

a_unit = a / np.linalg.norm(a)
scalar_proj = float(np.dot(a_unit, b))
print(f"Scalar projection of b onto a: {scalar_proj:.4f}")  # 11/5 = 2.2

# ---------------------------------------------------------------------------
# Advanced: triangle inequality
# ---------------------------------------------------------------------------
u3 = np.array([1., 2., 3.])
v3 = np.array([4., 5., 6.])
lhs_tri = float(np.linalg.norm(u3 + v3))
rhs_tri = float(np.linalg.norm(u3) + np.linalg.norm(v3))

print("\n=== Advanced: triangle inequality ===")
print(f"||u+v|| = {lhs_tri:.4f}")
print(f"||u|| + ||v|| = {rhs_tri:.4f}")
print(f"Triangle inequality holds? {lhs_tri <= rhs_tri + 1e-9}")  # True

# Equality holds iff u and v are parallel (same direction)
u_parallel = np.array([1., 0.])
v_parallel = np.array([3., 0.])   # same direction as u
lhs_eq = float(np.linalg.norm(u_parallel + v_parallel))
rhs_eq = float(np.linalg.norm(u_parallel) + np.linalg.norm(v_parallel))
print(f"Equality case (parallel): {np.isclose(lhs_eq, rhs_eq)}")  # True


def exercises():
    """
    Exercise 1 (Basic):
        Compute d(u,v) for u=(1,0,0,1) and v=(0,1,1,0) in R^4.
        Expected: sqrt((1-0)^2 + (0-1)^2 + (0-1)^2 + (1-0)^2) = sqrt(4) = 2.0

    Exercise 2 (Intermediate):
        u=[3,4], v=[1,2].
        (a) Verify Cauchy-Schwarz: |u·v| vs ||u||·||v||.
            Expected: 11 ≤ 5*sqrt(5) ≈ 11.1803
        (b) Compute unit vector û and show û·v = scalar projection of v onto u.
            Expected: û = [0.6, 0.8], û·v = 0.6 + 1.6 = 2.2

    Exercise 3 (Advanced):
        Prove triangle inequality from Cauchy-Schwarz.
        Start: ||u+v||^2 = ||u||^2 + 2(u·v) + ||v||^2
        Apply CS: 2(u·v) ≤ 2||u||·||v||
        Result: ||u+v||^2 ≤ (||u|| + ||v||)^2 → take sqrt both sides.
        When does equality hold? Only when u = k·v for some k ≥ 0 (same direction).
    """
    pass
