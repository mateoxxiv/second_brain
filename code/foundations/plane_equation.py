"""
Plane equation: dot-normal, scalar, and general forms.
Demonstrates: defining a plane from a point + normal, finding the normal
via cross product, and verifying point membership.
See also: line_equation_3d.py, point_to_plane_distance.py
"""

import numpy as np


def plane_from_point_and_normal(r0: np.ndarray, n: np.ndarray) -> tuple[np.ndarray, float]:
    """Returns (n, D) for the general form ax + by + cz + D = 0."""
    return n, float(-np.dot(n, r0))


def plane_from_three_points(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> tuple[np.ndarray, float]:
    """Normal via cross product of two edge vectors."""
    n = np.cross(B - A, C - A)
    return n, float(-np.dot(n, A))


def on_plane(P: np.ndarray, n: np.ndarray, D: float, tol: float = 1e-9) -> bool:
    return bool(np.abs(np.dot(n, P) + D) < tol)


# ---------------------------------------------------------------------------
# Basic: plane from point + normal, verify membership
# ---------------------------------------------------------------------------
r0 = np.array([1., 0., 0.])
n  = np.array([1., 0., 0.])
plane_n, D = plane_from_point_and_normal(r0, n)
print("=== Basic ===")
print(f"General form: {plane_n[0]}x + {plane_n[1]}y + {plane_n[2]}z + {D} = 0")
print(f"(1,5,3) on plane? {on_plane(np.array([1.,5.,3.]), plane_n, D)}")   # True
print(f"(2,0,0) on plane? {on_plane(np.array([2.,0.,0.]), plane_n, D)}")   # False

# ---------------------------------------------------------------------------
# Intermediate: plane through three points
# ---------------------------------------------------------------------------
A = np.array([1., 0., 0.])
B = np.array([0., 2., 0.])
C = np.array([0., 0., 3.])
n3, D3 = plane_from_three_points(A, B, C)
print("\n=== Intermediate ===")
print(f"Normal: {n3}")
print(f"General form: {n3[0]}x + {n3[1]}y + {n3[2]}z + {D3:.1f} = 0")
print(f"A on plane? {on_plane(A, n3, D3)}")   # True
print(f"B on plane? {on_plane(B, n3, D3)}")   # True


def exercises():
    """
    Exercise 1 (Basic):
        Plane through (1,2,3) with normal [2,-1,4].
        Write general form ax + by + cz + D = 0. What is D?
        Expected: 2x - y + 4z - 12 = 0, D = -12

    Exercise 2 (Intermediate):
        Points A=(0,0,1), B=(1,0,0), C=(0,1,0).
        Find the normal and general form.
        Verify all three points satisfy the equation.

    Exercise 3 (Advanced):
        Show that replacing n with k·n (any scalar k≠0) gives the same plane.
        Verify: on_plane(P, n, D) == on_plane(P, k*n, k*D) for several P and k.
    """
    pass
