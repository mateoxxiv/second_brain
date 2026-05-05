"""
Line equation in 3D: parametric and symmetric forms.
Demonstrates: tracing a line from a point + direction, the symmetric form,
and finding the intersection of a line with a plane.
See also: plane_equation.py, point_to_plane_distance.py
"""

import numpy as np


def line(r0: np.ndarray, d: np.ndarray, t: float) -> np.ndarray:
    """Point on the line at parameter t."""
    return r0 + t * d


def line_plane_intersection(r0: np.ndarray, d: np.ndarray,
                             n: np.ndarray, D: float) -> tuple[float, np.ndarray] | None:
    """
    Intersect line r(t) = r0 + t*d with plane n·x + D = 0.
    Returns (t*, point) or None if line is parallel to the plane.
    """
    denom = np.dot(n, d)
    if np.isclose(denom, 0):
        return None   # line parallel to plane
    t_star = -(np.dot(n, r0) + D) / denom
    return t_star, line(r0, d, t_star)


# ---------------------------------------------------------------------------
# Basic: trace a line, show parametric points
# ---------------------------------------------------------------------------
r0 = np.array([1., 0., 0.])
d  = np.array([2., 1., -1.])

print("=== Basic: parametric form ===")
for t in [-1, 0, 0.5, 1, 2]:
    print(f"  t={t:4.1f} → {line(r0, d, t)}")

# ---------------------------------------------------------------------------
# Intermediate: line perpendicular to a plane, find intersection
# ---------------------------------------------------------------------------
# Plane: 3x - y + 2z - 6 = 0  →  n=(3,-1,2), D=-6
n = np.array([3., -1., 2.])
D = -6.
Q = np.array([1., 1., 0.])   # external point; line direction = plane normal

result = line_plane_intersection(Q, n, n, D)
print("\n=== Intermediate: line ⊥ plane, intersection ===")
if result:
    t_star, foot = result
    print(f"  t* = {t_star:.4f}")
    print(f"  foot = {foot}")
    print(f"  foot on plane? {np.isclose(np.dot(n, foot) + D, 0)}")   # True

# ---------------------------------------------------------------------------
# Advanced: check if two lines intersect or are skew
# ---------------------------------------------------------------------------
r1 = np.array([1., 0., 0.])
d1 = np.array([1., 1., 0.])
r2 = np.array([0., 1., 0.])
d2 = np.array([1., -1., 0.])

# Solve r1 + t*d1 = r2 + s*d2  →  t*d1 - s*d2 = r2 - r1
# Build 3x2 system and check least-squares residual
A = np.column_stack([d1, -d2])
b = r2 - r1
ts, residuals, rank, _ = np.linalg.lstsq(A, b, rcond=None)
p1 = line(r1, d1, ts[0])
p2 = line(r2, d2, ts[1])
print("\n=== Advanced: line intersection check ===")
print(f"  t={ts[0]:.4f}, s={ts[1]:.4f}")
print(f"  point on L1: {p1}")
print(f"  point on L2: {p2}")
print(f"  intersect? {np.allclose(p1, p2)}")   # True for these lines


def exercises():
    """
    Exercise 1 (Basic):
        Line through P0=(2,-1,3) with d=(1,2,-2).
        What point does t=2 give?
        Verify it satisfies the symmetric form (x-2)/1 = (y+1)/2 = (z-3)/(-2).
        Expected: t=2 → (4, 3, -1)

    Exercise 2 (Intermediate):
        Plane: x + y + z = 3. Point: Q=(4,0,0).
        Write the perpendicular line through Q (d = plane normal = [1,1,1]).
        Find where it hits the plane.
        Expected: t* = -1/3, foot = (11/3, 1/3, 1/3) ≈ (3.667, 0.333, 0.333)

    Exercise 3 (Advanced):
        Lines: r1(t)=(0,0,0)+t(1,0,0) and r2(s)=(0,1,0)+s(0,0,1).
        Are they parallel, intersecting, or skew?
        Hint: solve r1=r2, check if a solution exists.
        Expected: skew (non-parallel, non-intersecting)
    """
    pass
