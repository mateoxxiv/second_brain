"""
Planes as linear systems: each equation ax + by + cz = k is a plane.
Demonstrates the 6 geometric cases (Anton Fig. 3.30) and how rank/det
maps to unique, infinite, or no solution.
"""

import numpy as np


def classify_system(A: np.ndarray, b: np.ndarray) -> str:
    det = np.linalg.det(A)
    if not np.isclose(det, 0):
        return "unique solution — 3 planes meet at one point (case f)"
    rank_A = np.linalg.matrix_rank(A)
    rank_aug = np.linalg.matrix_rank(np.column_stack([A, b]))
    if rank_A == rank_aug:
        dim = 3 - rank_A
        label = "plane" if dim == 2 else "line"
        return f"infinite solutions — planes meet in a {label} (case d/e)"
    return "no solution — planes have no common intersection (case a/b/c)"


# ---------------------------------------------------------------------------
# Case (f): unique — three independent planes meeting at one point
# ---------------------------------------------------------------------------
A_f = np.array([[1., 0, 0],
                [0., 1, 0],
                [0., 0, 1]])
b_f = np.array([1., 2., 3.])
print("Case (f):", classify_system(A_f, b_f))
print("  solution:", np.linalg.solve(A_f, b_f))   # [1. 2. 3.]

# ---------------------------------------------------------------------------
# Case (e): infinite — three planes meeting in a line (rank 2)
# ---------------------------------------------------------------------------
A_e = np.array([[1., 0, 0],
                [0., 1, 0],
                [0., 2, 0]])   # row 3 = 2 * row 2 → rank 2
b_e = np.array([1., 1., 2.])  # consistent: b3 = 2*b2
print("\nCase (e):", classify_system(A_e, b_e))

# ---------------------------------------------------------------------------
# Case (a/b/c): no solution — parallel or non-intersecting planes
# ---------------------------------------------------------------------------
A_n = np.array([[1., 0, 0],
                [1., 0, 0],
                [0., 1, 0]])   # rows 1 and 2 identical planes
b_n = np.array([1., 2., 0.])  # inconsistent: same plane, different d
print("\nCase (a/b/c):", classify_system(A_n, b_n))


def exercises():
    """
    Exercise 1 (Basic):
        Classify by inspection — no code needed.
        System: x=1, y=2, z=3 (three axis-aligned planes).
        Which case? What is the solution?
        Expected: case (f), solution = (1, 2, 3)

    Exercise 2 (Intermediate):
        Build a system in case (e): two independent planes + one dependent.
        Verify classify_system returns "infinite solutions".
        Hint: make row 3 = row 1 + row 2, b3 = b1 + b2.

    Exercise 3 (Advanced):
        For a random 3x3 A with det != 0 and random b, verify:
          - classify_system returns "unique solution"
          - np.linalg.solve gives the intersection point
          - substituting the solution back into each plane equation (A @ x == b) holds
        What breaks if you set det(A) = 0 by making two rows identical?
    """
    pass
