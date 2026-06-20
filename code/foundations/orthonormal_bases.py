"""
Orthonormal bases: definition, verification, coordinate formula, and key properties.
Shows that coordinates in an orthonormal basis reduce to dot products,
and that orthonormal matrices satisfy Q^T Q = I (inverse = transpose).
See: gram_schmidt in matrix_operations.py, angles_and_orthogonality.py
"""

import numpy as np


def is_orthonormal(vectors: list[np.ndarray], ip=None, tol: float = 1e-10) -> bool:
    """Check if a list of vectors forms an orthonormal set under ip."""
    if ip is None:
        ip = lambda u, v: float(np.dot(u, v))
    for i, u in enumerate(vectors):
        if abs(ip(u, u) - 1.0) > tol:
            return False
        for j, v in enumerate(vectors):
            if i != j and abs(ip(u, v)) > tol:
                return False
    return True


def coords_in_onb(v: np.ndarray, Q: np.ndarray) -> np.ndarray:
    """Coordinates of v in the orthonormal basis whose columns are Q."""
    return Q.T @ v   # c_k = <v, q_k> — just dot products


# ---------------------------------------------------------------------------
# Basic: verify orthonormal set in R^3 (Anton Ex. 53) + coordinate formula
# ---------------------------------------------------------------------------
print("=== Basic: orthonormal set in R^3 ===")

v1 = np.array([0., 1., 0.])
v2 = np.array([1/np.sqrt(2), 0.,  1/np.sqrt(2)])
v3 = np.array([1/np.sqrt(2), 0., -1/np.sqrt(2)])

print(f"<v1,v2> = {np.dot(v1,v2):.6f}")   # 0.0
print(f"<v2,v3> = {np.dot(v2,v3):.6f}")   # 0.0
print(f"<v1,v3> = {np.dot(v1,v3):.6f}")   # 0.0
print(f"||v1|| = {np.linalg.norm(v1):.4f}")  # 1.0
print(f"||v2|| = {np.linalg.norm(v2):.4f}")  # 1.0
print(f"||v3|| = {np.linalg.norm(v3):.4f}")  # 1.0
print(f"Is orthonormal: {is_orthonormal([v1, v2, v3])}")  # True

# Coordinate formula: c_k = <v, q_k>
Q = np.column_stack([v1, v2, v3])
v = np.array([3., 1., 2.])
c = coords_in_onb(v, Q)
print(f"\nCoords of v={v} in ONB: {c}")           # dot products directly
print(f"Reconstructed: {Q @ c}")                   # must equal v
print(f"Match: {np.allclose(v, Q @ c)}")           # True

# ---------------------------------------------------------------------------
# Intermediate: Q^T Q = I — inverse = transpose
# ---------------------------------------------------------------------------
print("\n=== Intermediate: Q^T @ Q = I ===")
print(np.allclose(Q.T @ Q, np.eye(3)))             # True
print(np.allclose(Q @ Q.T, np.eye(3)))             # True (Q is square orthonormal)

# General: Q preserves norms
x = np.array([1., 2., 3.])
print(f"||x||     = {np.linalg.norm(x):.4f}")
print(f"||Qx||    = {np.linalg.norm(Q @ x):.4f}") # same — norm preserved
print(f"||Qx||=||x||: {np.isclose(np.linalg.norm(Q@x), np.linalg.norm(x))}")  # True

# ---------------------------------------------------------------------------
# Advanced: orthonormal set in R^2 + verify coordinate formula by hand
# ---------------------------------------------------------------------------
print("\n=== Advanced: R^2 rotated ONB ===")
theta = np.pi / 4   # 45 degrees
q1 = np.array([np.cos(theta), np.sin(theta)])   # (1/√2, 1/√2)
q2 = np.array([-np.sin(theta), np.cos(theta)])  # (-1/√2, 1/√2)

Q2 = np.column_stack([q1, q2])
v2d = np.array([3., 1.])
c2 = coords_in_onb(v2d, Q2)

print(f"q1 = {q1}")
print(f"q2 = {q2}")
print(f"Coords of {v2d}: c1={c2[0]:.4f}, c2={c2[1]:.4f}")
# c1 = <v,q1> = 3*(1/√2) + 1*(1/√2) = 4/√2 = 2√2 ≈ 2.828
# c2 = <v,q2> = 3*(-1/√2) + 1*(1/√2) = -2/√2 = -√2 ≈ -1.414
print(f"Reconstructed: {Q2 @ c2}")                # must equal [3,1]
print(f"Match: {np.allclose(v2d, Q2 @ c2)}")      # True


def exercises():
    """
    Exercise 1 (Basic):
        S = {(1/√2, 1/√2), (-1/√2, 1/√2)}. Verify orthonormal:
        <q1,q2> = -1/2 + 1/2 = 0 ✓
        ||q1||  = sqrt(1/2+1/2) = 1 ✓
        Coords of v=(3,1): c1=<v,q1>=4/√2=2√2, c2=<v,q2>=-2/√2=-√2

    Exercise 2 (Intermediate):
        Proof of coordinate formula:
        <v, q_k> = <sum_j c_j q_j, q_k>
                 = sum_j c_j <q_j, q_k>   (linearity)
                 = sum_j c_j delta_jk      (orthonormality)
                 = c_k   ✓

    Exercise 3 (Advanced):
        ||Qx||^2 = <Qx, Qx> = (Qx)^T(Qx) = x^T Q^T Q x = x^T I x = ||x||^2
        <Qx, Qy> = (Qx)^T(Qy) = x^T Q^T Q y = x^T y = <x, y>
        Geometrically: Q is a rotation/reflection — preserves shape, lengths, angles.
    """
    pass
