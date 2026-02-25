"""
Vectors and Vector Spaces — From Scratch
=========================================
Demonstrates core vector operations and their connection to ML concepts.
Covers: addition, scalar multiplication, dot product, norms, cosine similarity,
linear independence, projection, and basis.

Run: python code/foundations/vectors_and_spaces.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# --- Core Vector Operations ---

def vector_add(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Component-wise addition — no NumPy operator, see the loop.
    Used in: gradient accumulation, residual connections.
    """
    return np.array([u_i + v_i for u_i, v_i in zip(u, v)])


def scalar_mult(c: float, v: np.ndarray) -> np.ndarray:
    """Scale every component by c — no NumPy operator.
    Used in: learning rate scaling, feature normalization.
    """
    return np.array([c * v_i for v_i in v])


def dot_product(u: np.ndarray, v: np.ndarray) -> float:
    """Compute dot product without np.dot — understand what's happening."""
    return sum(u_i * v_i for u_i, v_i in zip(u, v))


def l1_norm(v: np.ndarray) -> float:
    """L1 (Manhattan) norm — sum of absolute values.
    Used in: Lasso regularization, sparse feature selection.
    """
    return sum(abs(v_i) for v_i in v)


def l2_norm(v: np.ndarray) -> float:
    """L2 (Euclidean) norm — the 'length' of a vector.
    Used in: Ridge regularization, distance metrics, normalization.
    """
    return np.sqrt(dot_product(v, v))


def linf_norm(v: np.ndarray) -> float:
    """L-infinity (Chebyshev) norm — maximum absolute component.
    Used in: adversarial robustness (FGSM attack bounds).
    """
    return max(abs(v_i) for v_i in v)


def cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """Cosine similarity — how 'aligned' two vectors are.
    Used in: embeddings search, attention scores, recommendation systems.
    Returns: -1 (opposite) to 1 (identical direction). 0.0 if either vector is zero.
    """
    norm_u, norm_v = l2_norm(u), l2_norm(v)
    if norm_u == 0 or norm_v == 0:
        return 0.0
    return dot_product(u, v) / (norm_u * norm_v)


def project(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Project u onto v — the 'shadow' of u in the direction of v.
    Foundation for: PCA, least squares regression, Gram-Schmidt.
    Returns zero vector if v is the zero vector.
    """
    v_dot_v = dot_product(v, v)
    if v_dot_v == 0:
        return np.zeros_like(u)
    scalar = dot_product(u, v) / v_dot_v
    return scalar * v


def is_linearly_independent(vectors: np.ndarray) -> bool:
    """Check if a set of vectors is linearly independent via matrix rank.
    Independent vectors = non-redundant features in ML.
    """
    return np.linalg.matrix_rank(vectors) == len(vectors)


# --- Demonstrations ---

def demo_basic_operations():
    """Basic vector operations."""
    print("=" * 50)
    print("BASIC VECTOR OPERATIONS")
    print("=" * 50)

    u = np.array([3.0, 4.0])
    v = np.array([1.0, 2.0])

    print(f"u = {u}")
    print(f"v = {v}")
    print(f"u + v = {vector_add(u, v)}")
    print(f"2 * u = {scalar_mult(2, u)}")
    print(f"dot(u, v) = {dot_product(u, v)}")
    print(f"||u|| = {l2_norm(u)}")  # 5.0 — the classic 3-4-5 triangle
    print(f"cosine_similarity(u, v) = {cosine_similarity(u, v):.4f}")
    print()


def demo_cosine_similarity_ml():
    """Show why cosine similarity matters for embeddings."""
    print("=" * 50)
    print("COSINE SIMILARITY IN ML CONTEXT")
    print("=" * 50)

    # Simulated word embeddings (imagine 3D for simplicity)
    king = np.array([0.8, 0.6, 0.1])
    queen = np.array([0.75, 0.65, 0.1])
    apple = np.array([0.1, 0.05, 0.9])

    print(f"sim(king, queen) = {cosine_similarity(king, queen):.4f}")  # High
    print(f"sim(king, apple) = {cosine_similarity(king, apple):.4f}")  # Low
    print("→ Cosine similarity captures semantic closeness\n")


def demo_projection():
    """Projection — the geometric idea behind PCA and regression."""
    print("=" * 50)
    print("VECTOR PROJECTION")
    print("=" * 50)

    u = np.array([3.0, 4.0])
    v = np.array([1.0, 0.0])  # x-axis

    proj = project(u, v)
    residual = u - proj

    print(f"u = {u}")
    print(f"v = {v} (x-axis)")
    print(f"proj(u onto v) = {proj}")
    print(f"residual = {residual}")
    print(f"proj · residual = {dot_product(proj, residual):.10f}")
    print("→ Projection and residual are orthogonal (dot product ≈ 0)\n")


def demo_norms_comparison():
    """Compare L1, L2, and Linf norms — each matters in different ML contexts."""
    print("=" * 50)
    print("NORM COMPARISON")
    print("=" * 50)

    v = np.array([3.0, -4.0, 1.0])

    print(f"v = {v}")
    print(f"L1 norm  = {l1_norm(v):.2f}  (sum of |components| — Lasso)")
    print(f"L2 norm  = {l2_norm(v):.2f}  (Euclidean length — Ridge)")
    print(f"Linf norm = {linf_norm(v):.2f}  (max |component| — adversarial)")
    print("→ L1 promotes sparsity, L2 penalizes large weights, Linf bounds worst case\n")


def demo_linear_independence():
    """Linear independence — redundancy detection."""
    print("=" * 50)
    print("LINEAR INDEPENDENCE")
    print("=" * 50)

    independent = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    dependent = np.array([[1, 0, 0], [0, 1, 0], [1, 1, 0]])  # v3 = v1 + v2

    print(f"Standard basis independent? {is_linearly_independent(independent)}")
    print(f"With redundant vector independent? {is_linearly_independent(dependent)}")
    print("→ In ML, dependent features waste parameters and cause instability\n")


def demo_orthogonality():
    """Orthogonal and orthonormal vectors — foundation for QR and Gram-Schmidt."""
    print("=" * 50)
    print("ORTHOGONALITY")
    print("=" * 50)

    e1 = np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])

    print("Standard basis vectors:")
    print(f"  e1 · e2 = {dot_product(e1, e2):.1f} (orthogonal)")
    print(f"  e1 · e3 = {dot_product(e1, e3):.1f} (orthogonal)")
    print(f"  ||e1|| = {l2_norm(e1):.1f} (unit length → orthonormal)")

    # Non-trivial orthogonal pair
    a = np.array([1.0, 1.0])
    b = np.array([1.0, -1.0])
    print(f"\na = {a}, b = {b}")
    print(f"  a · b = {dot_product(a, b):.1f} (orthogonal)")
    print(f"  cosine_sim = {cosine_similarity(a, b):.4f}")
    print("→ Orthogonal bases simplify computation — no cross-talk between components\n")


def demo_visualization():
    """Visualize vectors, projection, and the subspace they span."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot 1: Vector operations
    ax1 = axes[0]
    u = np.array([3, 4])
    v = np.array([1, 2])

    ax1.quiver(0, 0, u[0], u[1], angles="xy", scale_units="xy", scale=1,
               color="steelblue", label="u = [3, 4]")
    ax1.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
               color="coral", label="v = [1, 2]")
    ax1.quiver(0, 0, u[0]+v[0], u[1]+v[1], angles="xy", scale_units="xy",
               scale=1, color="green", alpha=0.7, label="u + v")

    ax1.set_xlim(-1, 7)
    ax1.set_ylim(-1, 7)
    ax1.set_aspect("equal")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_title("Vector Addition")

    # Plot 2: Projection
    ax2 = axes[1]
    u = np.array([3.0, 4.0])
    v = np.array([5.0, 1.0])
    proj = project(u, v)
    residual = u - proj

    ax2.quiver(0, 0, u[0], u[1], angles="xy", scale_units="xy", scale=1,
               color="steelblue", label="u")
    ax2.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
               color="coral", label="v")
    ax2.quiver(0, 0, proj[0], proj[1], angles="xy", scale_units="xy", scale=1,
               color="green", label="proj(u→v)")
    ax2.quiver(proj[0], proj[1], residual[0], residual[1], angles="xy",
               scale_units="xy", scale=1, color="purple", alpha=0.7,
               label="residual (⊥)")

    ax2.set_xlim(-1, 6)
    ax2.set_ylim(-1, 5)
    ax2.set_aspect("equal")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_title("Projection (foundation of PCA)")

    plt.tight_layout()
    output_path = Path(__file__).parent / "vectors_visualization.png"
    plt.savefig(output_path, dpi=150)
    plt.show()
    print(f"→ Plot saved to {output_path}")


if __name__ == "__main__":
    demo_basic_operations()
    demo_cosine_similarity_ml()
    demo_norms_comparison()
    demo_projection()
    demo_linear_independence()
    demo_orthogonality()
    demo_visualization()
