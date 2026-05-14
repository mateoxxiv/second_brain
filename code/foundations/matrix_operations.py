"""
Matrix Operations — From Scratch
=================================
Demonstrates core matrix operations and their connection to ML concepts.
Covers: transpose, multiplication, inverse, transformation, special matrices.

Run: python code/foundations/matrix_operations.py
     python code/foundations/matrix_operations.py <demo_name>
     python code/foundations/matrix_operations.py exercises
"""

import sys
import numpy as np


# --- Core Matrix Operations (from scratch) ---

def transpose(A: np.ndarray) -> np.ndarray:
    """Flip rows and columns — no np.transpose or .T.
    Rows become columns, columns become rows.
    """
    rows, cols = A.shape
    result = np.zeros((cols, rows))
    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]
    return result


def mat_vec_mult(A: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Matrix-vector multiplication from scratch.
    Each entry = dot product of row i with v.
    Or equivalently: linear combination of columns weighted by v.
    """
    rows, cols = A.shape
    result = np.zeros(rows)
    for i in range(rows):
        for j in range(cols):
            result[i] += A[i][j] * v[j]
    return result


def mat_mult(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Matrix multiplication from scratch.
    Entry (i,j) = dot product of row i of A with column j of B.
    Inner dimensions must match: (m x p) @ (p x n) = (m x n).
    """
    m, p1 = A.shape
    p2, n = B.shape
    assert p1 == p2, f"Inner dimensions don't match: {p1} vs {p2}"
    result = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            for k in range(p1):
                result[i][j] += A[i][k] * B[k][j]
    return result


def scalar_mult(k: float, A: np.ndarray) -> np.ndarray:
    """Scalar multiplication: multiply every entry of A by scalar k.
    This is the vector space 'scaling' operation for M_mxn.
    """
    rows, cols = A.shape
    result = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            result[i][j] = k * A[i][j]
    return result


def det_2x2(A: np.ndarray) -> float:
    """Determinant of a 2x2 matrix: ad - bc."""
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inverse_2x2(A: np.ndarray) -> np.ndarray:
    """2x2 inverse: swap diagonal, negate off-diagonal, divide by det.
    Returns None if singular (det = 0).
    """
    d = det_2x2(A)
    if abs(d) < 1e-10:
        return None  # singular
    return (1 / d) * np.array([[A[1][1], -A[0][1]],
                                [-A[1][0], A[0][0]]])


def inverse_gauss(A: np.ndarray) -> np.ndarray:
    """Inverse via Gaussian elimination: [A | I] → [I | A_inv].
    Works for any square matrix. Returns None if singular.
    """
    n = A.shape[0]
    # Build augmented matrix [A | I]
    aug = np.hstack([A.astype(float), np.eye(n)])

    for col in range(n):
        # Find pivot (largest absolute value for stability)
        max_row = col
        for row in range(col + 1, n):
            if abs(aug[row][col]) > abs(aug[max_row][col]):
                max_row = row
        aug[[col, max_row]] = aug[[max_row, col]]  # swap rows

        # Check for zero pivot (singular)
        if abs(aug[col][col]) < 1e-10:
            return None

        # Scale pivot row to get 1 on diagonal
        aug[col] = aug[col] / aug[col][col]

        # Eliminate all other rows
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = aug[row] - factor * aug[col]

    # Right half is the inverse
    return aug[:, n:]


def is_symmetric(A: np.ndarray) -> bool:
    """Check if A = A^T."""
    return np.allclose(A, A.T)


def is_orthogonal(A: np.ndarray) -> bool:
    """Check if A^T @ A = I (columns are orthonormal)."""
    return np.allclose(A.T @ A, np.eye(A.shape[0]))


def transform(A: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Apply matrix transformation: linear combination of columns.
    Shows the column view explicitly.
    """
    result = np.zeros(A.shape[0])
    for j in range(A.shape[1]):
        result += v[j] * A[:, j]  # v[j] * column j
    return result


# --- Demos ---

def demo_transformation():
    """A matrix redefines where 'right' and 'up' point."""
    print("=== Matrix as Transformation ===\n")

    A = np.array([[2, 0],
                  [0, 3]])
    v = np.array([3, 2])

    print(f"A = {A.tolist()}")
    print(f"v = {v.tolist()}")
    print(f"\nNew 'right' = {A[:, 0].tolist()}  (column 1)")
    print(f"New 'up'    = {A[:, 1].tolist()}  (column 2)")
    print(f"\nv[0] * col1 + v[1] * col2")
    print(f"= {v[0]}*{A[:, 0].tolist()} + {v[1]}*{A[:, 1].tolist()}")
    result = transform(A, v)
    print(f"= {result.tolist()}")
    print(f"\nVector moved from {v.tolist()} to {result.tolist()}")


def demo_transpose():
    """Transpose flips rows and columns. Dot product = x^T @ y."""
    print("=== Transpose ===\n")

    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    print(f"A shape {A.shape}:\n{A}")
    At = transpose(A)
    print(f"\nA^T shape {At.shape}:\n{At.astype(int)}")

    # Dot product as transpose multiply
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print(f"\nx = {x.tolist()}, y = {y.tolist()}")
    print(f"x · y = {np.dot(x, y)}")
    print(f"x^T @ y = {x.T @ y}  (same thing)")


def demo_multiplication():
    """Matrix multiplication = composition of transformations."""
    print("=== Multiplication ===\n")

    A = np.array([[1, 2],
                  [3, 4]])
    B = np.array([[5, 6],
                  [7, 8]])

    AB = mat_mult(A, B)
    BA = mat_mult(B, A)
    print(f"A = {A.tolist()}")
    print(f"B = {B.tolist()}")
    print(f"\nAB = {AB.astype(int).tolist()}")
    print(f"BA = {BA.astype(int).tolist()}")
    print(f"\nAB == BA? {np.allclose(AB, BA)}")
    print("Order matters! AB means: first B, then A.")

    # Non-square example
    print("\n--- Non-square multiplication ---")
    C = np.array([[1, 2, 3],
                  [4, 5, 6]])  # 2x3
    D = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])   # 3x2
    CD = mat_mult(C, D)
    print(f"C (2x3) @ D (3x2) = result ({CD.shape[0]}x{CD.shape[1]})")
    print(f"CD = {CD.astype(int).tolist()}")


def demo_inverse():
    """Inverse undoes a transformation. A @ A_inv = I."""
    print("=== Inverse ===\n")

    # 2x2 formula
    A = np.array([[4, 7],
                  [2, 6]])
    d = det_2x2(A)
    A_inv = inverse_2x2(A)
    print(f"A = {A.tolist()}")
    print(f"det(A) = {d}")
    print(f"A_inv = {A_inv.tolist()}")
    print(f"A @ A_inv = {(A @ A_inv).tolist()}  (identity)")

    # Singular matrix
    print("\n--- Singular matrix (no inverse) ---")
    S = np.array([[1, 2],
                  [2, 4]])
    print(f"S = {S.tolist()}, det = {det_2x2(S)}")
    print(f"S⁻¹ = {inverse_2x2(S)}  (None = no inverse)")

    # 3x3 via Gaussian elimination
    print("\n--- 3x3 inverse via Gaussian elimination ---")
    B = np.array([[1, 2, 1],
                  [2, 5, 3],
                  [1, 3, 3]])
    B_inv = inverse_gauss(B)
    print(f"B = {B.tolist()}")
    print(f"B_inv = {B_inv.tolist()}")
    identity = B @ B_inv
    print(f"B @ B_inv ≈ I? {np.allclose(identity, np.eye(3))}")


def demo_solve_vs_inverse():
    """Why solve(A, b) is better than inv(A) @ b."""
    print("=== Solve vs Inverse ===\n")

    # System: c1 + 2c2 = 5, c1 - c2 = 3
    A = np.array([[1, 2],
                  [1, -1]])
    b = np.array([5, 3])

    print(f"System: A @ x = b")
    print(f"A = {A.tolist()}")
    print(f"b = {b.tolist()}")

    x_solve = np.linalg.solve(A, b)
    x_inv = np.linalg.inv(A) @ b

    print(f"\nsolve(A, b) = {x_solve.tolist()}")
    print(f"inv(A) @ b  = {x_inv.tolist()}")
    print(f"Same answer? {np.allclose(x_solve, x_inv)}")
    print("\nBoth work, but solve is faster and more stable.")
    print("It uses Gaussian elimination internally — no inverse needed.")


def demo_special_matrices():
    """Symmetric, diagonal, orthogonal — each with special powers."""
    print("=== Special Matrices ===\n")

    # Scalar multiplication (vector space operation)
    A = np.array([[1., 2.], [3., 4.]])
    print(f"Scalar multiplication (axiom 6 — closure):")
    print(f"  3·A =\n{scalar_mult(3, A)}")
    print(f"  1·A = A?  {np.allclose(scalar_mult(1, A), A)}")       # axiom 10
    print(f"  A + (-1)·A = 0?  {np.allclose(A + scalar_mult(-1, A), np.zeros((2,2)))}")  # axiom 5

    # Symmetric
    S = np.array([[2, 1],
                  [1, 3]])
    print(f"Symmetric: {S.tolist()}")
    print(f"  S == S^T? {is_symmetric(S)}")
    print(f"  Eigenvalues are real: {np.linalg.eigvals(S).tolist()}")

    # Diagonal
    D = np.diag([3, 5])
    D_inv = np.diag([1/3, 1/5])
    print(f"\nDiagonal: {D.tolist()}")
    print(f"  Inverse = invert each entry: {D_inv.tolist()}")
    print(f"  D @ D⁻¹ = I? {np.allclose(D @ D_inv, np.eye(2))}")

    # Orthogonal (rotation by 45°)
    theta = np.pi / 4
    Q = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    print(f"\nOrthogonal (45° rotation):")
    print(f"  Q^T @ Q = I? {is_orthogonal(Q)}")
    print(f"  Q⁻¹ = Q^T? {np.allclose(np.linalg.inv(Q), Q.T)}")
    v = np.array([1, 0])
    print(f"  ||v|| = {np.linalg.norm(v)}, ||Qv|| = {np.linalg.norm(Q @ v):.4f}")
    print(f"  Norm preserved — orthogonal matrices don't stretch!")


def demo_common_transforms():
    """Visualize what common matrices do to a vector."""
    print("=== Common Transformations ===\n")

    v = np.array([1.0, 1.0])
    transforms = {
        "Identity":       np.array([[1, 0], [0, 1]]),
        "Scale x2":       np.array([[2, 0], [0, 2]]),
        "Stretch y":      np.array([[1, 0], [0, 2]]),
        "Rotate 90°":     np.array([[0, -1], [1, 0]]),
        "Reflect x-axis": np.array([[1, 0], [0, -1]]),
        "Collapse to x":  np.array([[1, 0], [0, 0]]),
    }

    print(f"v = {v.tolist()}\n")
    for name, M in transforms.items():
        result = M @ v
        det = det_2x2(M.astype(float))
        print(f"  {name:16s}: {v.tolist()} → {result.tolist():20s}  det={det:5.1f}")


# --- Exercises ---

def exercises():
    """Progressive exercises: basic → intermediate → advanced."""
    correct = 0
    total = 0

    def check(name, got, expected, tol=1e-6):
        nonlocal correct, total
        total += 1
        if isinstance(expected, np.ndarray):
            passed = np.allclose(got, expected, atol=tol)
        elif isinstance(expected, bool):
            passed = got == expected
        elif expected is None:
            passed = got is None
        elif isinstance(expected, tuple):
            passed = got == expected
        else:
            passed = abs(got - expected) < tol
        status = "PASS" if passed else "FAIL"
        if not passed:
            print(f"  [{status}] {name}: got {got}, expected {expected}")
        else:
            print(f"  [{status}] {name}")
            correct += 1

    print("=" * 60)
    print("MATRIX OPERATIONS — EXERCISES")
    print("=" * 60)

    # --- BASIC (1-7) ---
    print("\n--- BASIC ---\n")

    # 1. Transpose
    print("Exercise 1: Transpose")
    A = np.array([[1, 2, 3], [4, 5, 6]])
    check("transpose shape", transpose(A).shape, (3, 2))
    check("transpose values", transpose(A), np.array([[1, 4], [2, 5], [3, 6]]))

    # 2. Matrix-vector multiplication
    print("\nExercise 2: Matrix-vector multiplication")
    A = np.array([[2, 0], [0, 3]])
    v = np.array([3, 2])
    check("A @ v", mat_vec_mult(A, v), np.array([6, 6]))

    # 3. Transformation view
    print("\nExercise 3: Column view of transformation")
    A = np.array([[1, 0], [0, 2]])
    v = np.array([3, 4])
    result = v[0] * A[:, 0] + v[1] * A[:, 1]
    check("column combination", result, np.array([3, 8]))

    # 4. Matrix multiplication
    print("\nExercise 4: Matrix multiplication")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    check("A @ B", mat_mult(A, B), np.array([[19, 22], [43, 50]]))
    check("AB != BA", np.allclose(mat_mult(A, B), mat_mult(B, A)), False)

    # 5. Determinant 2x2
    print("\nExercise 5: Determinant")
    A = np.array([[4, 7], [2, 6]])
    check("det(A)", det_2x2(A), 10.0)

    # 6. Inverse 2x2
    print("\nExercise 6: Inverse 2x2")
    A_inv = inverse_2x2(A)
    check("A @ A_inv = I", A @ A_inv, np.eye(2))

    # 7. Identity check
    print("\nExercise 7: Identity matrix")
    I = np.eye(3)
    v = np.array([1, 2, 3])
    check("I @ v = v", I @ v, v)

    # 7b. Scalar multiplication (vector space axiom 6)
    print("\nExercise 7b: Scalar multiplication")
    A = np.array([[1., 2.], [3., 4.]])
    check("3·A",            scalar_mult(3, A),  np.array([[3., 6.], [9., 12.]]))
    check("axiom 10: 1·A=A", scalar_mult(1, A),  A)
    check("axiom 5: (-1)·A", scalar_mult(-1, A), np.array([[-1., -2.], [-3., -4.]]))
    check("k·A same shape",  scalar_mult(5, A).shape, A.shape)   # axiom 6: closure

    # --- INTERMEDIATE (8-13) ---
    print("\n--- INTERMEDIATE ---\n")

    # 8. Solve a system
    print("Exercise 8: Solve Ax = b")
    A = np.array([[1, 2], [1, -1]])
    b = np.array([5, 3])
    x = np.linalg.solve(A, b)
    check("solution", x, np.array([11/3, 2/3]))

    # 9. Non-square multiplication
    print("\nExercise 9: Non-square multiplication")
    A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
    B = np.array([[7], [8], [9]])          # 3x1
    result = mat_mult(A, B)
    check("(2x3) @ (3x1) shape", result.shape, (2, 1))
    check("(2x3) @ (3x1) values", result, np.array([[50], [122]]))

    # 10. Transpose properties
    print("\nExercise 10: (AB)^T = B^T @ A^T")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    AB_T = transpose(mat_mult(A, B))
    BT_AT = mat_mult(transpose(B), transpose(A))
    check("socks and shoes", AB_T, BT_AT)

    # 11. Singular matrix detection
    print("\nExercise 11: Singular matrix")
    S = np.array([[1, 2], [2, 4]])
    check("det = 0", det_2x2(S), 0.0)
    check("no inverse", inverse_2x2(S), None)

    # 12. Symmetric check
    print("\nExercise 12: Symmetric matrix")
    A = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
    check("A is symmetric", is_symmetric(A), True)
    B = np.array([[1, 2], [3, 4]])
    check("B is not symmetric", is_symmetric(B), False)
    # Covariance matrices are always symmetric
    X = np.random.randn(100, 3)
    X = X - X.mean(axis=0)
    cov = X.T @ X / (len(X) - 1)
    check("covariance is symmetric", is_symmetric(cov), True)

    # 13. Orthogonal matrix
    print("\nExercise 13: Orthogonal matrix")
    theta = np.pi / 3  # 60 degrees
    Q = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    check("Q^T @ Q = I", is_orthogonal(Q), True)
    v = np.array([3, 4])
    check("norm preserved", np.linalg.norm(Q @ v), np.linalg.norm(v))

    # --- ADVANCED (14-18) ---
    print("\n--- ADVANCED ---\n")

    # 14. Inverse via Gaussian elimination
    print("Exercise 14: 3x3 inverse via Gauss")
    A = np.array([[1, 2, 1], [2, 5, 3], [1, 3, 3]])
    A_inv = inverse_gauss(A)
    check("A @ A_inv = I", A @ A_inv, np.eye(3))
    check("matches numpy", A_inv, np.linalg.inv(A))

    # 15. Composition of transformations
    print("\nExercise 15: Composition")
    # Rotate 90° then scale by 2 = scale by 2 then rotate 90°?
    R = np.array([[0, -1], [1, 0]])  # rotate 90°
    S = np.array([[2, 0], [0, 2]])   # scale x2
    v = np.array([1, 0])
    # For uniform scaling, order doesn't matter
    check("SR @ v", (S @ R) @ v, np.array([0, 2]))
    check("RS @ v", (R @ S) @ v, np.array([0, 2]))
    check("uniform scale commutes with rotation", S @ R, R @ S)

    # 16. Non-uniform scaling doesn't commute
    print("\nExercise 16: Non-commutative example")
    S2 = np.array([[2, 0], [0, 1]])  # stretch x only
    check("S2 @ R != R @ S2", np.allclose(S2 @ R, R @ S2), False)

    # 17. Projection matrix
    print("\nExercise 17: Projection matrix")
    # Project onto x-axis: P = [[1,0],[0,0]]
    P = np.array([[1, 0], [0, 0]])
    v = np.array([3, 7])
    check("projection", P @ v, np.array([3, 0]))
    # Projection applied twice = same as once (idempotent)
    check("P^2 = P", P @ P, P)

    # 18. Solve vs inverse (numerical comparison)
    print("\nExercise 18: Solve vs inverse accuracy")
    np.random.seed(42)
    A = np.random.randn(5, 5)
    b = np.random.randn(5)
    x_solve = np.linalg.solve(A, b)
    x_inv = np.linalg.inv(A) @ b
    check("same result", x_solve, x_inv)
    # Both should satisfy A @ x = b
    check("solve satisfies Ax=b", A @ x_solve, b)
    check("inv satisfies Ax=b", A @ x_inv, b)

    # --- SUMMARY ---
    print(f"\n{'=' * 60}")
    print(f"Results: {correct}/{total} passed")
    print(f"{'=' * 60}")


# --- CLI Runner ---

DEMOS = {
    "transformation": demo_transformation,
    "transpose": demo_transpose,
    "multiplication": demo_multiplication,
    "inverse": demo_inverse,
    "solve": demo_solve_vs_inverse,
    "special": demo_special_matrices,
    "transforms": demo_common_transforms,
}

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] == "all":
        for name, fn in DEMOS.items():
            fn()
            print()
    elif args[0] == "exercises":
        exercises()
    elif args[0] in DEMOS:
        DEMOS[args[0]]()
    else:
        print(f"Usage: python {sys.argv[0]} [{'|'.join(DEMOS.keys())}|exercises|all]")
