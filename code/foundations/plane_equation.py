"""
Dot-normal plane equation: n · (r - r0) = 0
Demonstrates: defining planes from a point + normal, finding normals via cross product,
computing point-to-plane distance, and the connection to SVM hyperplanes.
"""

import numpy as np


def plane_from_point_and_normal(r0: np.ndarray, n: np.ndarray) -> tuple[np.ndarray, float]:
    """Returns (n, d) for the plane ax + by + cz = d."""
    return n, float(np.dot(n, r0))


def plane_from_three_points(A: np.ndarray, B: np.ndarray, C: np.ndarray) -> tuple[np.ndarray, float]:
    """Returns (n, d) by computing normal via cross product of two edge vectors."""
    u = B - A
    v = C - A
    n = np.cross(u, v)
    d = float(np.dot(n, A))
    return n, d


def point_on_plane(P: np.ndarray, n: np.ndarray, d: float, tol: float = 1e-9) -> bool:
    """Check if point P satisfies n · P = d."""
    return bool(np.abs(np.dot(n, P) - d) < tol)


def distance_to_plane(P: np.ndarray, n: np.ndarray, r0: np.ndarray) -> float:
    """Signed distance from P to the plane defined by (n, r0). Positive = same side as n."""
    return float(np.dot(n, P - r0) / np.linalg.norm(n))


# ---------------------------------------------------------------------------
# Basic: define a plane and verify membership
# ---------------------------------------------------------------------------
r0 = np.array([1.0, 0.0, 0.0])
n  = np.array([1.0, 0.0, 0.0])   # plane x = 1 (yz-plane shifted by 1)
plane_n, d = plane_from_point_and_normal(r0, n)
print("=== Basic ===")
print(f"Plane: {plane_n[0]}x + {plane_n[1]}y + {plane_n[2]}z = {d}")
print(f"(1,5,3) on plane? {point_on_plane(np.array([1.,5.,3.]), plane_n, d)}")   # True
print(f"(2,0,0) on plane? {point_on_plane(np.array([2.,0.,0.]), plane_n, d)}")   # False

# ---------------------------------------------------------------------------
# Intermediate: plane through three points, distance from external point
# ---------------------------------------------------------------------------
A = np.array([1.0, 0.0, 0.0])
B = np.array([0.0, 2.0, 0.0])
C = np.array([0.0, 0.0, 3.0])
n3, d3 = plane_from_three_points(A, B, C)
P = np.array([1.0, 1.0, 1.0])
dist = distance_to_plane(P, n3, A)
print("\n=== Intermediate ===")
print(f"Normal: {n3}")
print(f"Plane: {n3[0]}x + {n3[1]}y + {n3[2]}z = {d3}")
print(f"A on plane? {point_on_plane(A, n3, d3)}")    # True
print(f"Distance from P=(1,1,1): {abs(dist):.4f}")   # ~0.9449

# ---------------------------------------------------------------------------
# Advanced: SVM hyperplane — signed distance is the margin
# ---------------------------------------------------------------------------
w = np.array([2.0, 1.0])   # normal vector (weight vector in 2D)
b = -3.0                    # bias: w · x = -b → hyperplane w · x + b = 0

x_pos = np.array([2.0, 1.0])   # positive class sample
x_neg = np.array([0.0, 0.0])   # negative class sample

# signed distance: positive on one side, negative on other
def svm_signed_distance(x, w, b):
    return (np.dot(w, x) + b) / np.linalg.norm(w)

print("\n=== Advanced: SVM signed distance ===")
print(f"x_pos score: {svm_signed_distance(x_pos, w, b):.4f}")   # positive
print(f"x_neg score: {svm_signed_distance(x_neg, w, b):.4f}")   # negative


def exercises():
    """
    Exercise 1 (Basic):
        Plane through (1,2,3) with normal [2,-1,4].
        Write the scalar equation ax + by + cz = d.
        Expected: 2x - y + 4z = 12

    Exercise 2 (Intermediate):
        Three points A=(1,0,0), B=(0,2,0), C=(0,0,3).
        Find the normal and the distance from P=(1,1,1) to the plane.
        Expected: n = [6, 3, 2], d = 6, dist = 11/7 ≈ 1.5714

    Exercise 3 (Advanced):
        Verify that the distance formula equals the scalar projection of (P - r0) onto n_hat.
        Hint: dist = (P - r0) · n_hat, where n_hat = n / ||n||.
        Show they produce the same value for any P, n, r0.
    """
    pass
