"""
Point-to-plane distance: distance formula, signed distance, and foot of perpendicular.
Demonstrates the connection between the distance formula and the foot derivation.
See also: plane_equation.py, line_equation_3d.py
"""

import numpy as np


def distance_to_plane(P: np.ndarray, n: np.ndarray, D: float) -> float:
    """Unsigned distance from P to plane n·x + D = 0."""
    return abs(np.dot(n, P) + D) / np.linalg.norm(n)


def signed_distance(P: np.ndarray, n: np.ndarray, D: float) -> float:
    """Signed distance: positive = same side as n, negative = opposite."""
    return (np.dot(n, P) + D) / np.linalg.norm(n)


def foot_of_perpendicular(P: np.ndarray, n: np.ndarray, D: float) -> np.ndarray:
    """Closest point on the plane to P."""
    t_star = -(np.dot(n, P) + D) / np.dot(n, n)
    return P + t_star * n


# ---------------------------------------------------------------------------
# Basic: distance from a point to a plane
# ---------------------------------------------------------------------------
n = np.array([1., 0., 0.])   # plane x = 1 → x - 1 = 0 → D = -1
D = -1.
P = np.array([4., 2., 3.])

print("=== Basic ===")
print(f"Distance: {distance_to_plane(P, n, D)}")   # 3.0
print(f"Signed:   {signed_distance(P, n, D)}")     # 3.0 (P is on the +x side)

# ---------------------------------------------------------------------------
# Intermediate: foot of perpendicular, verify it lies on the plane
# ---------------------------------------------------------------------------
n2 = np.array([1., 1., 1.])
D2 = -3.   # plane x + y + z = 3
Q  = np.array([4., 0., 0.])

foot = foot_of_perpendicular(Q, n2, D2)
print("\n=== Intermediate ===")
print(f"Foot: {foot}")
print(f"Foot on plane? {np.isclose(np.dot(n2, foot) + D2, 0)}")         # True
print(f"Q→foot parallel to n? {np.allclose(np.cross(foot - Q, n2), 0)}")# True
print(f"Distance via formula: {distance_to_plane(Q, n2, D2):.4f}")
print(f"Distance via foot:    {np.linalg.norm(Q - foot):.4f}")           # same

# ---------------------------------------------------------------------------
# Advanced: signed distance — point on each side of the plane
# ---------------------------------------------------------------------------
n3 = np.array([0., 1., 0.])   # plane y = 0 (the xz-plane), D = 0
D3 = 0.
above = np.array([0., 3., 0.])
below = np.array([0., -2., 0.])

print("\n=== Advanced: signed distance ===")
print(f"Above plane: sd = {signed_distance(above, n3, D3)}")   # +3.0
print(f"Below plane: sd = {signed_distance(below, n3, D3)}")   # -2.0


def exercises():
    """
    Exercise 1 (Basic):
        Plane: 2x - y + 2z = 6. Point: P=(3,1,2).
        Compute distance using the general form formula.
        Verify: ||n|| first, then apply |a*x1 + b*y1 + c*z1 + D| / ||n||.
        Expected: ||n|| = 3, distance = |6-6-1+2-6|/3... recalculate carefully.

    Exercise 2 (Intermediate):
        Plane: x + y + z = 3. Point: Q=(4,0,0).
        Find the foot of the perpendicular.
        Confirm: foot on plane, Q→foot parallel to n=[1,1,1].
        Expected: foot = (2, -1, -1)... verify by substituting into plane.

    Exercise 3 (Advanced):
        Derive the distance formula from foot_of_perpendicular.
        Show that ||Q - foot|| = |n·Q + D| / ||n||.
        Hint: substitute t* = -(n·Q + D)/||n||² into ||t*·n||.
    """
    pass
