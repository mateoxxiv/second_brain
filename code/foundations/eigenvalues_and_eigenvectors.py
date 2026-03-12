"""
Eigenvalues and Eigenvectors --from scratch and with NumPy.

Demonstrates:
- What eigenvalues/eigenvectors are geometrically
- Computing them via the characteristic equation (2x2 by hand)
- NumPy's eig() and eigh() for general vs symmetric matrices
- The spectral decomposition A = Q Λ Qᵀ
- Trace and determinant relationships
- Power iteration: finding the dominant eigenvector iteratively
- PCA on a small 2D dataset using the covariance matrix
- Visualising eigenvectors as the "axes" of a data ellipse

Run: python eigenvalues_and_eigenvectors.py
"""

from __future__ import annotations
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math


# ─────────────────────────────────────────────
# 1. CHARACTERISTIC EQUATION --2x2 by hand
# ─────────────────────────────────────────────

def characteristic_polynomial_2x2(A: np.ndarray) -> tuple[float, float, float]:
    """
    For a 2x2 matrix A = [[a, b], [c, d]],
    det(A - λI) = λ² - tr(A)λ + det(A)
    Returns coefficients (1, -tr, det) so poly is λ² + coeff[1]λ + coeff[2].
    """
    a, b = A[0]
    c, d = A[1]
    trace = a + d
    det = a * d - b * c
    # λ² - trace·λ + det = 0
    return 1.0, -trace, det


def eigenvalues_2x2(A: np.ndarray) -> tuple[float, float]:
    """Solve characteristic polynomial for a 2x2 matrix analytically."""
    _, b, c = characteristic_polynomial_2x2(A)
    # λ² + bλ + c = 0  →  λ = (-b ± √(b²-4c)) / 2
    discriminant = b**2 - 4 * c
    if discriminant < 0:
        raise ValueError("Complex eigenvalues --matrix has no real eigenvalues.")
    sqrt_d = math.sqrt(discriminant)
    lam1 = (-b + sqrt_d) / 2
    lam2 = (-b - sqrt_d) / 2
    return lam1, lam2


def eigenvector_2x2(A: np.ndarray, lam: float) -> np.ndarray:
    """
    Solve (A - λI)v = 0 for a 2x2 matrix.
    At least one of the rows gives a non-trivial constraint; use the first non-zero row.
    """
    B = A - lam * np.eye(2)
    # Row 0: B[0,0]*v1 + B[0,1]*v2 = 0
    # If B[0,0] ≈ 0 and B[0,1] ≈ 0, use row 1
    row = B[0] if not np.allclose(B[0], 0) else B[1]
    if abs(row[0]) > abs(row[1]):
        # v1 = -row[1]/row[0] * v2; set v2 = 1
        v = np.array([-row[1] / row[0], 1.0])
    else:
        # v2 = -row[0]/row[1] * v1; set v1 = 1
        v = np.array([1.0, -row[0] / row[1]])
    return v / la.norm(v)  # normalise to unit length


def demo_characteristic_equation() -> None:
    """Walk through the full hand computation for A = [[2,1],[1,2]]."""
    A = np.array([[2.0, 1.0],
                  [1.0, 2.0]])

    print("=" * 55)
    print("CHARACTERISTIC EQUATION --A = [[2,1],[1,2]]")
    print("=" * 55)
    print(f"A =\n{A}\n")

    lam1, lam2 = eigenvalues_2x2(A)
    print(f"Characteristic polynomial: L^2 - {np.trace(A):.0f}L + {la.det(A):.0f} = 0")
    print(f"Eigenvalues: L1 = {lam1:.4f}, L2 = {lam2:.4f}\n")

    v1 = eigenvector_2x2(A, lam1)
    v2 = eigenvector_2x2(A, lam2)

    print(f"Eigenvector for L1={lam1:.0f}:  v1 = {v1}")
    print(f"  Verify A@v1 = L1*v1: {np.allclose(A @ v1, lam1 * v1)}")
    print(f"Eigenvector for L2={lam2:.0f}:  v2 = {v2}")
    print(f"  Verify A@v2 = L2*v2: {np.allclose(A @ v2, lam2 * v2)}")
    print(f"\nOrthogonality check (v1.v2): {np.dot(v1, v2):.6f}  (=0 for symmetric A)")
    print(f"Trace check: tr(A)={np.trace(A):.0f} = L1+L2 = {lam1+lam2:.0f}")
    print(f"Det check:   det(A)={la.det(A):.0f} = L1*L2 = {lam1*lam2:.0f}\n")


# ─────────────────────────────────────────────
# 2. SPECTRAL DECOMPOSITION  A = Q Λ Qᵀ
# ─────────────────────────────────────────────

def spectral_decomposition(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Decompose symmetric A into Q and Λ such that A = Q Λ Qᵀ.
    Uses np.linalg.eigh (numerically stable for symmetric matrices).
    Returns (Q, eigenvalues) --columns of Q are eigenvectors sorted ascending.
    """
    eigenvalues, Q = la.eigh(A)   # already returns sorted eigenvalues
    return Q, eigenvalues


def demo_spectral_decomposition() -> None:
    A = np.array([[2.0, 1.0],
                  [1.0, 2.0]])
    Q, lams = spectral_decomposition(A)

    print("=" * 55)
    print("SPECTRAL DECOMPOSITION  A = Q L Q^T")
    print("=" * 55)
    Lambda = np.diag(lams)
    A_reconstructed = Q @ Lambda @ Q.T
    print(f"Q (eigenvectors as columns):\n{Q}\n")
    print(f"L (diagonal of eigenvalues):\n{Lambda}\n")
    print(f"Q L Q^T =\n{A_reconstructed}")
    print(f"Reconstruction matches A: {np.allclose(A_reconstructed, A)}\n")

    # Rank-1 outer product representation
    print("Spectral sum: A = sum( Li * qi @ qi^T )")
    A_sum = sum(lam * np.outer(q, q) for lam, q in zip(lams, Q.T))
    print(f"Sum matches A: {np.allclose(A_sum, A)}\n")


# ─────────────────────────────────────────────
# 3. POWER ITERATION --dominant eigenvector
# ─────────────────────────────────────────────

def power_iteration(
    A: np.ndarray,
    n_iterations: int = 100,
    tol: float = 1e-10,
) -> tuple[float, np.ndarray]:
    """
    Find the dominant eigenvalue and eigenvector of A via power iteration.

    Algorithm:
        1. Start with a random unit vector b.
        2. Repeatedly compute b = A @ b / ||A @ b||.
        3. The vector converges to the dominant eigenvector.
        4. The Rayleigh quotient bᵀAb / bᵀb converges to the dominant eigenvalue.
    """
    n = A.shape[0]
    rng = np.random.default_rng(42)
    b = rng.normal(size=n)
    b /= la.norm(b)

    for _ in range(n_iterations):
        b_new = A @ b
        b_new /= la.norm(b_new)
        if la.norm(b_new - b) < tol:
            break
        b = b_new

    eigenvalue = float(b @ A @ b)  # Rayleigh quotient
    return eigenvalue, b


def demo_power_iteration() -> None:
    A = np.array([[4.0, 1.0],
                  [2.0, 3.0]])

    print("=" * 55)
    print("POWER ITERATION --dominant eigenvector")
    print("=" * 55)
    lam_dom, v_dom = power_iteration(A)
    lams_true, vecs_true = la.eig(A)
    idx = np.argmax(np.abs(lams_true))

    print(f"A =\n{A}")
    print(f"Power iteration -> L = {lam_dom:.6f},  v = {v_dom}")
    print(f"NumPy (true)    -> L = {lams_true[idx]:.6f}")
    print(f"Verify A@v = L*v: {np.allclose(A @ v_dom, lam_dom * v_dom, atol=1e-6)}\n")


# ─────────────────────────────────────────────
# 4. PCA VIA EIGENDECOMPOSITION
# ─────────────────────────────────────────────

def pca_eigen(X: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    PCA using eigendecomposition of the covariance matrix.

    Args:
        X: data matrix of shape (n_samples, n_features), assumed zero-mean.
        k: number of principal components to keep.

    Returns:
        components:   (k, n_features) --top-k eigenvectors (principal axes)
        eigenvalues:  (k,) --variance explained per component
        X_projected:  (n_samples, k) --data in the new basis
    """
    n = X.shape[0]
    cov = (X.T @ X) / (n - 1)           # covariance matrix (n_features × n_features)
    eigenvalues, eigenvectors = la.eigh(cov)  # ascending order

    # Reverse so largest eigenvalue is first
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    components = eigenvectors[:, :k].T   # (k, n_features)
    X_projected = X @ eigenvectors[:, :k]  # (n_samples, k)

    return components, eigenvalues[:k], X_projected


def demo_pca() -> None:
    """Generate correlated 2D data and run PCA; show variance explained."""
    rng = np.random.default_rng(0)
    # Correlated data: x₂ ≈ 2x₁ + noise
    n = 200
    x1 = rng.normal(0, 1, n)
    x2 = 2 * x1 + rng.normal(0, 0.5, n)
    X = np.column_stack([x1, x2])
    X -= X.mean(axis=0)  # centre

    components, eigenvalues, X_proj = pca_eigen(X, k=2)
    total_var = eigenvalues.sum()

    print("=" * 55)
    print("PCA VIA EIGENDECOMPOSITION")
    print("=" * 55)
    print(f"Covariance matrix:\n{(X.T @ X) / (n - 1)}\n")
    print(f"PC1 direction: {components[0]}  (L = {eigenvalues[0]:.4f})")
    print(f"PC2 direction: {components[1]}  (L = {eigenvalues[1]:.4f})")
    print(f"Variance explained: PC1 = {eigenvalues[0]/total_var:.1%},  "
          f"PC2 = {eigenvalues[1]/total_var:.1%}\n")

    # Optional plot (comment out if running headless)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].scatter(X[:, 0], X[:, 1], alpha=0.4, s=10, label="data")
    origin = np.zeros(2)
    scale = 2
    for i, (comp, lam) in enumerate(zip(components, eigenvalues)):
        axes[0].annotate(
            "", xy=origin + scale * comp * np.sqrt(lam),
            xytext=origin,
            arrowprops=dict(arrowstyle="->", color=f"C{i+1}", lw=2)
        )
    axes[0].set_title("Data with Principal Components")
    axes[0].set_aspect("equal")
    axes[0].legend()

    axes[1].scatter(X_proj[:, 0], X_proj[:, 1], alpha=0.4, s=10)
    axes[1].set_xlabel("PC1")
    axes[1].set_ylabel("PC2")
    axes[1].set_title("Projected Data (PCA basis)")

    plt.tight_layout()
    plt.savefig("pca_eigenvectors_demo.png", dpi=100)
    plt.close()
    print("Plot saved to pca_eigenvectors_demo.png\n")


# ─────────────────────────────────────────────
# 5. EIGENVALUE MAGNITUDE AND STABILITY
# ─────────────────────────────────────────────

def demo_stability() -> None:
    """Show how eigenvalue magnitude controls iterative convergence vs divergence."""
    print("=" * 55)
    print("EIGENVALUE MAGNITUDE AND STABILITY")
    print("=" * 55)

    cases = {
        "Converging (L < 1)":  np.array([[0.5, 0.0], [0.0, 0.3]]),
        "Stable (L = 1)":      np.eye(2),
        "Diverging (L > 1)":   np.array([[2.0, 0.0], [0.0, 1.5]]),
        "Oscillating (L < 0)": np.array([[-0.8, 0.0], [0.0, -0.6]]),
    }

    v0 = np.array([1.0, 1.0])
    steps = 10

    for label, M in cases.items():
        lams = la.eigvals(M)
        v = v0.copy()
        for _ in range(steps):
            v = M @ v
        print(f"{label}: eigenvalues = {np.round(lams, 2)},  "
              f"||v|| after {steps} steps = {la.norm(v):.4f}")
    print()


# ─────────────────────────────────────────────
# EXERCISES
# ─────────────────────────────────────────────

def exercises() -> None:
    """
    Progressive exercises on eigenvalues and eigenvectors.

    Work through each one before checking the expected output.
    """

    print("=" * 55)
    print("EXERCISES")
    print("=" * 55)

    # ── BASIC ──────────────────────────────────────────────

    # Exercise 1
    # Compute eigenvalues of A = [[3, 0], [0, 5]] by hand
    # (diagonal matrix --eigenvalues are the diagonal entries).
    # Expected: λ₁ = 3, λ₂ = 5
    print("Exercise 1 --diagonal matrix [[3,0],[0,5]]")
    A1 = np.array([[3.0, 0.0], [0.0, 5.0]])
    lams1 = la.eigvalsh(A1)
    print(f"  Eigenvalues: {sorted(lams1)}  (expected [3.0, 5.0])\n")

    # Exercise 2
    # Verify that for A = [[0, -1],[1, 0]] (a 90° rotation),
    # no real eigenvectors exist (the characteristic polynomial has no real roots).
    # Expected: discriminant < 0
    print("Exercise 2 --rotation matrix [[0,-1],[1,0]]")
    A2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    _, b, c = characteristic_polynomial_2x2(A2)
    disc = b**2 - 4 * c
    print(f"  Discriminant = {disc}  (expected -4 < 0 -> no real eigenvalues)\n")

    # ── INTERMEDIATE ───────────────────────────────────────

    # Exercise 3
    # For A = [[1, 2],[2, 1]], compute eigenvalues and eigenvectors by hand,
    # then verify with NumPy. Check that eigenvectors are orthogonal.
    # Expected eigenvalues: -1 and 3
    print("Exercise 3 --[[1,2],[2,1]]")
    A3 = np.array([[1.0, 2.0], [2.0, 1.0]])
    lam3a, lam3b = eigenvalues_2x2(A3)
    v3a = eigenvector_2x2(A3, lam3a)
    v3b = eigenvector_2x2(A3, lam3b)
    print(f"  L1 = {lam3a:.4f}, v1 = {v3a}")
    print(f"  L2 = {lam3b:.4f}, v2 = {v3b}")
    print(f"  v1.v2 = {np.dot(v3a, v3b):.6f}  (expected ~0)")
    print(f"  (expected eigenvalues: 3.0 and -1.0)\n")

    # Exercise 4
    # Reconstruct A = [[4,2],[1,3]] from its eigendecomposition.
    # (Not symmetric --use np.linalg.eig, not eigh.)
    # Hint: A = V diag(λ) V⁻¹
    print("Exercise 4 --reconstruct [[4,2],[1,3]] from eigendecomposition")
    A4 = np.array([[4.0, 2.0], [1.0, 3.0]])
    lams4, V4 = la.eig(A4)
    A4_reconstructed = V4 @ np.diag(lams4) @ la.inv(V4)
    print(f"  Original:      {A4[0]}  /  {A4[1]}")
    print(f"  Reconstructed: {np.round(A4_reconstructed[0], 4)}  /  {np.round(A4_reconstructed[1], 4)}")
    print(f"  Match: {np.allclose(A4, A4_reconstructed)}\n")

    # ── ADVANCED ───────────────────────────────────────────

    # Exercise 5
    # Power iteration vs numpy: for A = [[3,1],[1,3]], run 50 iterations
    # of power iteration starting from [1,0]. Check convergence to dominant eigenvector.
    print("Exercise 5 --power iteration convergence for [[3,1],[1,3]]")
    A5 = np.array([[3.0, 1.0], [1.0, 3.0]])
    lam5_power, v5_power = power_iteration(A5, n_iterations=50)
    lams5_true, vecs5_true = la.eigh(A5)
    idx5 = np.argmax(lams5_true)
    v5_true = vecs5_true[:, idx5]
    # Eigenvectors match up to sign
    aligned = np.allclose(np.abs(v5_power), np.abs(v5_true), atol=1e-6)
    print(f"  Power iter L = {lam5_power:.6f}   (true: {lams5_true[idx5]:.6f})")
    print(f"  Directions match (up to sign): {aligned}\n")

    # Exercise 6 (proof / derivation challenge)
    # Show that if λ is an eigenvalue of A, then λ² is an eigenvalue of A².
    # Hint: start from Av = λv and apply A again.
    print("Exercise 6 -- A^2 shares eigenvectors with A (eigenvalue squared)")
    A6 = np.array([[2.0, 1.0], [1.0, 2.0]])
    lams6, V6 = la.eigh(A6)
    lams6_sq = la.eigvalsh(A6 @ A6)
    print(f"  Eigenvalues of A:    {sorted(lams6)}")
    print(f"  Squared:             {sorted(lams6**2)}")
    print(f"  Eigenvalues of A^2:  {sorted(lams6_sq)}")
    print(f"  Match: {np.allclose(sorted(lams6**2), sorted(lams6_sq))}\n")

    # Exercise 7 (open-ended)
    # Generate a random 3×3 positive definite matrix, compute its eigendecomposition,
    # project a random vector onto its top-1 eigenvector (power-iteration style),
    # and verify ||proj|| ≤ ||v||.
    print("Exercise 7 --random 3x3 PSD, project onto top eigenvector")
    rng = np.random.default_rng(7)
    B = rng.normal(size=(3, 3))
    A7 = B.T @ B + np.eye(3)  # positive definite
    lam7, v7 = power_iteration(A7, n_iterations=200)
    v_random = rng.normal(size=3)
    proj = (v_random @ v7) * v7
    print(f"  Dominant eigenvalue: {lam7:.4f}")
    print(f"  ||v_random|| = {la.norm(v_random):.4f},  ||proj|| = {la.norm(proj):.4f}")
    print(f"  Projection shortens vector: {la.norm(proj) <= la.norm(v_random) + 1e-9}\n")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    demo_characteristic_equation()
    demo_spectral_decomposition()
    demo_power_iteration()
    demo_stability()
    demo_pca()
    exercises()
