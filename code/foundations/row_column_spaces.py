"""
Row and Column Spaces — Anton §4.6
Demonstrates: row space basis, column space basis, rank, Theorem 14 (consistency check).
"""

import numpy as np


def row_space_basis(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """Return a basis for the row space of A using QR decomposition."""
    _, R = np.linalg.qr(A.T)
    nonzero = R[[i for i, r in enumerate(R) if np.linalg.norm(r) > tol]]
    return nonzero


def col_space_basis(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """Column space of A = row space of A^T."""
    return row_space_basis(A.T, tol)


def in_column_space(A: np.ndarray, b: np.ndarray) -> bool:
    """Theorem 14: Ax=b is consistent iff b is in the column space of A.
    Equivalently: rank([A|b]) == rank(A).
    """
    return np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.column_stack([A, b]))


# ── Example 37 (Anton §4.6) ──────────────────────────────────────────────────
print("=== Example 37 ===")
A37 = np.array([[2, 1, 0],
                [3, -1, 4]], float)
print(f"Row vectors: {A37[0]}, {A37[1]}")
print(f"Column vectors: {A37[:, 0]}, {A37[:, 1]}, {A37[:, 2]}")

# ── Example 38 (Anton §4.6) ──────────────────────────────────────────────────
print("\n=== Example 38: basis for span of 4 vectors in R^5 ===")
A38 = np.array([
    [1, -2,  0,  0, 3],
    [2, -5, -3, -2, 6],
    [0,  5, 15, 10, 0],
    [2,  6, 18,  8, 6],
], float)

rank38 = np.linalg.matrix_rank(A38)
print(f"rank(A) = {rank38}")   # expected: 3

basis_rows = row_space_basis(A38)
print(f"Row space basis ({len(basis_rows)} vectors):")
for v in basis_rows:
    print(f"  {np.round(v, 6)}")

# ── Theorem 14 demo ──────────────────────────────────────────────────────────
print("\n=== Theorem 14: consistency check ===")
B = np.array([[1, 2],
              [2, 4]], float)

b_in  = np.array([3.0, 6.0])   # 3*(col1) — should be consistent
b_out = np.array([3.0, 5.0])   # not a multiple — inconsistent

print(f"b=[3,6] in col(B)? {in_column_space(B, b_in)}")    # True
print(f"b=[3,5] in col(B)? {in_column_space(B, b_out)}")   # False

# ── Theorem 12 demo: rank(A) == rank(A^T) ────────────────────────────────────
print("\n=== Theorem 12: row rank == column rank ===")
A_rect = np.array([[1, 0, 1, 1],
                   [3, 2, 5, 1],
                   [0, 4, 4, -4]], float)
print(f"rank(A)   = {np.linalg.matrix_rank(A_rect)}")
print(f"rank(A^T) = {np.linalg.matrix_rank(A_rect.T)}")   # same


# ── Exercises ─────────────────────────────────────────────────────────────────
def exercises():
    """Progressive exercises on row/column spaces."""

    print("\n=== Exercise 1 (Basic) ===")
    # A = [[2,1,0],[3,-1,4]]. Reason: 2 rows in R^3, 3 cols in R^2.
    # Row vectors are (2,1,0) and (3,-1,4) — neither is a scalar multiple,
    # so they're independent → row space has dim 2.
    # Column vectors: 3 vectors in R^2 → at most dim 2.
    # Theorem 12: both dimensions equal rank(A).
    A = np.array([[2, 1, 0], [3, -1, 4]], float)
    print(f"rank = {np.linalg.matrix_rank(A)}")   # expected: 2

    print("\n=== Exercise 2 (Intermediate) ===")
    A = np.array([[1, 0, 1, 1],
                  [3, 2, 5, 1],
                  [0, 4, 4, -4]], float)
    print(f"rank = {np.linalg.matrix_rank(A)}")
    b_yes = np.array([1.0, 3.0, 0.0])
    b_no  = np.array([1.0, 0.0, 0.0])
    print(f"b=(1,3,0) in col(A)? {in_column_space(A, b_yes)}")
    print(f"b=(1,0,0) in col(A)? {in_column_space(A, b_no)}")

    print("\n=== Exercise 3 (Advanced) ===")
    # Verify: number of pivots in A == number of pivots in A^T
    # (both equal rank — that's why row rank = col rank)
    for shape in [(3, 5), (5, 3), (4, 4)]:
        M = np.random.randn(*shape)
        assert np.linalg.matrix_rank(M) == np.linalg.matrix_rank(M.T), "Theorem 12 violated!"
    print("Theorem 12 holds for 3 random matrices of varying shapes ✓")


if __name__ == "__main__":
    exercises()
