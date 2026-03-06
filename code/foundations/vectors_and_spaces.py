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
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


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


# --- Exercises ---

def exercises() -> None:
    """
    Linear Algebra Exercises — All Topics
    ======================================
    Covers all 11 topics: vectors, operations, norms, cosine similarity,
    linear combinations, linear independence, basis/dimension, projection,
    projection onto subspaces, Gaussian elimination, determinant.

    Instructions:
    - Implement each function replacing `pass` with your solution
    - Use ONLY the from-scratch functions above (no np.linalg unless stated)
    - Run the file: python vectors_and_spaces.py exercises
    - Each exercise prints PASS or FAIL

    BASIC (1-8): Direct application of definitions
    INTERMEDIATE (9-16): Combine multiple concepts
    ADVANCED (17-22): Proofs, edge cases, "why does this break?"
    """
    print("=" * 60)
    print("  LINEAR ALGEBRA EXERCISES")
    print("=" * 60)

    passed = 0
    total = 0

    def check(name: str, got, expected, tol: float = 1e-6):
        nonlocal passed, total
        total += 1
        if isinstance(expected, np.ndarray):
            ok = np.allclose(got, expected, atol=tol)
        elif isinstance(expected, float):
            ok = abs(got - expected) < tol
        else:
            ok = got == expected
        status = "PASS" if ok else "FAIL"
        if not ok:
            print(f"  [{status}] {name}: got {got}, expected {expected}")
        else:
            print(f"  [{status}] {name}")
            passed += 1

    # =========================================================
    # BASIC — Direct application of formulas
    # =========================================================
    print("\n--- BASIC ---\n")

    # Ex 1: Vector addition and scalar multiplication
    # Compute: 2*[1,3,-2] + 3*[4,-1,5]
    # Expected: [14, 3, 11]
    def ex1() -> np.ndarray:
        u = np.array([1.0, 3.0, -2.0])
        v = np.array([4.0, -1.0, 5.0])
        # YOUR CODE: return the linear combination 2u + 3v
        pass

    result = ex1()
    if result is not None:
        check("Ex1: 2u + 3v", result, np.array([14.0, 3.0, 11.0]))
    else:
        print("  [SKIP] Ex1: not implemented yet")
        total += 1

    # Ex 2: Dot product by hand
    # u = [2, -3, 1], v = [4, 2, -5]
    # Expected: 2*4 + (-3)*2 + 1*(-5) = 8 - 6 - 5 = -3
    def ex2() -> float:
        u = np.array([2.0, -3.0, 1.0])
        v = np.array([4.0, 2.0, -5.0])
        # YOUR CODE: compute dot product from scratch (no np.dot)
        pass

    result = ex2()
    if result is not None:
        check("Ex2: dot product", result, -3.0)
    else:
        print("  [SKIP] Ex2: not implemented yet")
        total += 1

    # Ex 3: Compute all three norms
    # v = [3, -4, 0, 5]
    # Expected: L1=12, L2=sqrt(50)=7.0711, Linf=5
    def ex3() -> tuple[float, float, float]:
        v = np.array([3.0, -4.0, 0.0, 5.0])
        # YOUR CODE: return (l1, l2, linf)
        pass

    result = ex3()
    if result is not None:
        check("Ex3a: L1 norm", result[0], 12.0)
        check("Ex3b: L2 norm", result[1], np.sqrt(50))
        check("Ex3c: Linf norm", result[2], 5.0)
    else:
        print("  [SKIP] Ex3: not implemented yet")
        total += 3

    # Ex 4: Cosine similarity
    # u = [1, 0, 1], v = [0, 1, 1]
    # dot = 1, ||u|| = sqrt(2), ||v|| = sqrt(2)
    # Expected: 1 / (sqrt(2)*sqrt(2)) = 0.5
    def ex4() -> float:
        u = np.array([1.0, 0.0, 1.0])
        v = np.array([0.0, 1.0, 1.0])
        # YOUR CODE: compute cosine similarity from scratch
        pass

    result = ex4()
    if result is not None:
        check("Ex4: cosine similarity", result, 0.5)
    else:
        print("  [SKIP] Ex4: not implemented yet")
        total += 1

    # Ex 5: Is this a linear combination?
    # Can w = [7, 1] be written as c1*[1, 2] + c2*[3, -1]?
    # Solve: c1 + 3*c2 = 7, 2*c1 - c2 = 1
    # Expected: c1 = 10/7 ≈ 1.4286, c2 = 13/7 ≈ 1.8571
    def ex5() -> tuple[float, float]:
        v1 = np.array([1.0, 2.0])
        v2 = np.array([3.0, -1.0])
        w = np.array([7.0, 1.0])
        # YOUR CODE: find c1, c2 such that c1*v1 + c2*v2 = w
        # Hint: solve the 2x2 system using substitution or Cramer's rule
        pass

    result = ex5()
    if result is not None:
        check("Ex5a: c1", result[0], 10.0 / 7.0)
        check("Ex5b: c2", result[1], 13.0 / 7.0)
    else:
        print("  [SKIP] Ex5: not implemented yet")
        total += 2

    # Ex 6: Project u onto v
    # u = [4, 3], v = [1, 0]
    # Expected: [4, 0] (shadow on x-axis)
    def ex6() -> np.ndarray:
        u = np.array([4.0, 3.0])
        v = np.array([1.0, 0.0])
        # YOUR CODE: compute projection from scratch (no numpy shortcuts)
        pass

    result = ex6()
    if result is not None:
        check("Ex6: projection onto x-axis", result, np.array([4.0, 0.0]))
    else:
        print("  [SKIP] Ex6: not implemented yet")
        total += 1

    # Ex 7: Determinant of 2x2 matrix
    # A = [[3, 8], [4, 6]]
    # Expected: 3*6 - 8*4 = 18 - 32 = -14
    def ex7() -> float:
        a, b = 3.0, 8.0
        c, d = 4.0, 6.0
        # YOUR CODE: compute det(A) = ad - bc
        pass

    result = ex7()
    if result is not None:
        check("Ex7: 2x2 determinant", result, -14.0)
    else:
        print("  [SKIP] Ex7: not implemented yet")
        total += 1

    # Ex 8: Check linear independence (2 vectors in R2)
    # v1 = [2, 4], v2 = [1, 2] — is v2 a scalar multiple of v1?
    # Expected: False (dependent: v1 = 2*v2)
    def ex8() -> bool:
        v1 = np.array([2.0, 4.0])
        v2 = np.array([1.0, 2.0])
        # YOUR CODE: return True if independent, False if dependent
        # Hint: check if one is a scalar multiple of the other, or use determinant
        pass

    result = ex8()
    if result is not None:
        check("Ex8: independence check", result, False)
    else:
        print("  [SKIP] Ex8: not implemented yet")
        total += 1

    # =========================================================
    # INTERMEDIATE — Combine multiple concepts
    # =========================================================
    print("\n--- INTERMEDIATE ---\n")

    # Ex 9: Projection + residual verification
    # u = [5, 3], v = [2, 1]
    # Compute p = proj(u onto v) and r = u - p
    # Verify: dot(p, r) = 0 (orthogonal)
    # Expected: p = [26/5, 13/5] = [5.2, 2.6], r = [-0.2, 0.4]
    def ex9() -> tuple[np.ndarray, np.ndarray, float]:
        u = np.array([5.0, 3.0])
        v = np.array([2.0, 1.0])
        # YOUR CODE: compute p, r, and dot(p, r)
        # Return: (projection, residual, dot_product_of_p_and_r)
        pass

    result = ex9()
    if result is not None:
        check("Ex9a: projection", result[0], np.array([5.2, 2.6]))
        check("Ex9b: residual", result[1], np.array([-0.2, 0.4]))
        check("Ex9c: orthogonality (dot≈0)", abs(result[2]), 0.0, tol=1e-10)
    else:
        print("  [SKIP] Ex9: not implemented yet")
        total += 3

    # Ex 10: Norm ordering proof
    # For ANY vector v, prove: Linf(v) <= L2(v) <= L1(v)
    # Test with 5 random vectors in R4. Return True if all satisfy the ordering.
    def ex10() -> bool:
        np.random.seed(42)
        # YOUR CODE: generate 5 random vectors, check the ordering for each
        # Return True if Linf <= L2 <= L1 for all 5
        pass

    result = ex10()
    if result is not None:
        check("Ex10: norm ordering Linf <= L2 <= L1", result, True)
    else:
        print("  [SKIP] Ex10: not implemented yet")
        total += 1

    # Ex 11: Find the angle between two vectors (in degrees)
    # u = [1, 1, 0], v = [0, 1, 1]
    # cos(theta) = dot(u,v) / (||u|| * ||v||) = 1/2
    # Expected: 60 degrees
    def ex11() -> float:
        u = np.array([1.0, 1.0, 0.0])
        v = np.array([0.0, 1.0, 1.0])
        # YOUR CODE: compute angle in degrees
        # Hint: arccos(cosine_similarity) then convert radians to degrees
        pass

    result = ex11()
    if result is not None:
        check("Ex11: angle between vectors (degrees)", result, 60.0, tol=0.01)
    else:
        print("  [SKIP] Ex11: not implemented yet")
        total += 1

    # Ex 12: 3x3 determinant by cofactor expansion
    # A = [[1, 2, 3],
    #       [4, 5, 6],
    #       [7, 8, 9]]
    # Expected: 0 (singular matrix — rows are in arithmetic progression)
    def ex12() -> float:
        # YOUR CODE: compute det(A) using cofactor expansion along row 1
        # det = a(ei-fh) - b(di-fg) + c(dh-eg)
        pass

    result = ex12()
    if result is not None:
        check("Ex12: 3x3 determinant (singular)", result, 0.0)
    else:
        print("  [SKIP] Ex12: not implemented yet")
        total += 1

    # Ex 13: Gaussian elimination (solve a system)
    # x + 2y = 5
    # 3x + 4y = 11
    # Expected: x = 1, y = 2
    def ex13() -> tuple[float, float]:
        # YOUR CODE: solve by Gaussian elimination (by hand logic, no np.linalg)
        # Step 1: eliminate x from equation 2
        # Step 2: back-substitute to find x
        pass

    result = ex13()
    if result is not None:
        check("Ex13a: x", result[0], 1.0)
        check("Ex13b: y", result[1], 2.0)
    else:
        print("  [SKIP] Ex13: not implemented yet")
        total += 2

    # Ex 14: Find a basis for span({v1, v2, v3})
    # v1 = [1, 0, 1], v2 = [2, 0, 2], v3 = [0, 1, 0]
    # v2 = 2*v1, so it's redundant
    # Expected basis: {v1, v3} → dimension = 2
    def ex14() -> int:
        vectors = np.array([[1, 0, 1], [2, 0, 2], [0, 1, 0]])
        # YOUR CODE: find the dimension of the span (number of independent vectors)
        # Hint: what does matrix rank tell you?
        pass

    result = ex14()
    if result is not None:
        check("Ex14: dimension of span", result, 2)
    else:
        print("  [SKIP] Ex14: not implemented yet")
        total += 1

    # Ex 15: Normalize a vector (make it unit length)
    # v = [3, 4]
    # Expected: [0.6, 0.8] (unit vector in same direction)
    def ex15() -> np.ndarray:
        v = np.array([3.0, 4.0])
        # YOUR CODE: return v / ||v||
        pass

    result = ex15()
    if result is not None:
        check("Ex15a: normalized vector", result, np.array([0.6, 0.8]))
        check("Ex15b: has unit length", l2_norm(result), 1.0)
    else:
        print("  [SKIP] Ex15: not implemented yet")
        total += 2

    # Ex 16: Cosine similarity of orthogonal vs parallel vs opposite vectors
    # Return: (sim_orthogonal, sim_parallel, sim_opposite)
    # Expected: (0.0, 1.0, -1.0)
    def ex16() -> tuple[float, float, float]:
        a = np.array([1.0, 0.0])
        b_orth = np.array([0.0, 1.0])     # orthogonal to a
        b_para = np.array([3.0, 0.0])     # parallel to a (same direction)
        b_oppo = np.array([-2.0, 0.0])    # opposite to a
        # YOUR CODE: compute all three cosine similarities
        pass

    result = ex16()
    if result is not None:
        check("Ex16a: orthogonal → 0", result[0], 0.0)
        check("Ex16b: parallel → 1", result[1], 1.0)
        check("Ex16c: opposite → -1", result[2], -1.0)
    else:
        print("  [SKIP] Ex16: not implemented yet")
        total += 3

    # =========================================================
    # ADVANCED — Edge cases, proofs, deeper understanding
    # =========================================================
    print("\n--- ADVANCED ---\n")

    # Ex 17: Projection onto subspace (2D subspace in R3)
    # Project w = [1, 2, 3] onto the plane spanned by u=[1,0,0] and v=[0,1,0]
    # This is the xy-plane, so the projection should drop the z-component
    # Expected: [1, 2, 0]
    def ex17() -> np.ndarray:
        w = np.array([1.0, 2.0, 3.0])
        u = np.array([1.0, 0.0, 0.0])
        v = np.array([0.0, 1.0, 0.0])
        # YOUR CODE: project w onto subspace spanned by {u, v}
        # For orthogonal basis: proj = proj_u(w) + proj_v(w)
        pass

    result = ex17()
    if result is not None:
        check("Ex17: projection onto subspace", result, np.array([1.0, 2.0, 0.0]))
    else:
        print("  [SKIP] Ex17: not implemented yet")
        total += 1

    # Ex 18: Gaussian elimination with 3 equations
    # x + y + z = 6
    # 2x + 3y + z = 14
    # x + y + 2z = 9
    # Expected: x=1, y=3, z=2 (verify: 1+3+2=6, 2+9+2=13... let me check)
    # Actually: 2(1)+3(3)+1(2) = 2+9+2 = 13 ≠ 14... let me fix:
    # x + y + z = 6
    # 2x + 3y + z = 14
    # x + 2y + 3z = 14
    # Solution: x=1, y=2, z=3 (1+2+3=6, 2+6+3=11≠14)
    # Let me use a clean system:
    # x + y + z = 6
    # 2y + 5z = -4
    # 2x + 5y - z = 27
    # From row reduction... let me just use a known one:
    # 2x + y - z = 1
    # x + 3y + 2z = 13
    # x + y + z = 6
    # Expected: x=1, y=2, z=3
    def ex18() -> tuple[float, float, float]:
        # System:
        # 2x + y - z = 1
        # x + 3y + 2z = 13
        # x + y + z = 6
        #
        # YOUR CODE: solve by Gaussian elimination (build augmented matrix, eliminate)
        # Expected: x=1, y=2, z=3
        pass

    result = ex18()
    if result is not None:
        # Verify solution satisfies all equations
        x, y, z = result
        check("Ex18a: eq1 (2x+y-z=1)", 2*x + y - z, 1.0)
        check("Ex18b: eq2 (x+3y+2z=13)", x + 3*y + 2*z, 13.0)
        check("Ex18c: eq3 (x+y+z=6)", x + y + z, 6.0)
    else:
        print("  [SKIP] Ex18: not implemented yet")
        total += 3

    # Ex 19: The determinant-independence connection
    # Given 3 vectors in R3, compute the determinant of the matrix they form.
    # If det = 0, they are dependent. If det ≠ 0, they are independent.
    # Test both cases and return (det_independent, det_dependent).
    def ex19() -> tuple[float, float]:
        # Case 1: independent
        independent = np.array([
            [1, 0, 2],
            [0, 1, 3],
            [0, 0, 1],
        ])
        # Case 2: dependent (row 3 = row 1 + row 2)
        dependent = np.array([
            [1, 0, 2],
            [0, 1, 3],
            [1, 1, 5],
        ])
        # YOUR CODE: compute determinant of each (cofactor expansion or any method)
        # Expected: (1.0, 0.0)
        pass

    result = ex19()
    if result is not None:
        check("Ex19a: independent det ≠ 0", result[0], 1.0)
        check("Ex19b: dependent det = 0", result[1], 0.0)
    else:
        print("  [SKIP] Ex19: not implemented yet")
        total += 2

    # Ex 20: Implement row_echelon (Gaussian elimination) from scratch
    # Input: augmented matrix as 2D numpy array
    # Output: row echelon form (upper triangular)
    # Test with: [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
    # Expected solution: x=2, y=3, z=-1
    def ex20_row_echelon(matrix: np.ndarray) -> np.ndarray:
        """Transform to row echelon form using forward elimination."""
        m = matrix.astype(float).copy()
        rows, cols = m.shape
        # YOUR CODE: implement Gaussian elimination
        # For each pivot column:
        #   1. Find the pivot (first non-zero in column)
        #   2. Swap rows if needed
        #   3. Eliminate all entries below the pivot
        pass
        return m

    test_matrix = np.array([
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3],
    ], dtype=float)

    ref = ex20_row_echelon(test_matrix)
    if ref is not None:
        # The last row should give us z directly, then back-substitute
        # Check it produces the right answer via np.linalg.solve
        A = test_matrix[:, :3]
        b = test_matrix[:, 3]
        expected = np.linalg.solve(A, b)  # [2, 3, -1]
        check("Ex20: row echelon gives correct system", True,
              np.allclose(expected, np.array([2.0, 3.0, -1.0])))
    else:
        print("  [SKIP] Ex20: not implemented yet")
        total += 1

    # Ex 21: The projection error is MINIMAL
    # Show that proj(u onto v) is the closest point on the line of v to u.
    # Pick u = [3, 4], v = [1, 0].
    # Compute ||u - c*v|| for c in [0, 1, 2, 3, 4, 5].
    # The minimum should be at c = 3 (the projection coefficient).
    # Return the c value that minimizes the distance.
    def ex21() -> float:
        u = np.array([3.0, 4.0])
        v = np.array([1.0, 0.0])
        # YOUR CODE: try c = 0, 1, 2, 3, 4, 5
        # For each c, compute ||u - c*v|| (the distance)
        # Return the c with smallest distance
        pass

    result = ex21()
    if result is not None:
        check("Ex21: optimal projection coefficient", result, 3.0)
    else:
        print("  [SKIP] Ex21: not implemented yet")
        total += 1

    # Ex 22: Build an orthogonal basis from two non-orthogonal vectors
    # (Baby Gram-Schmidt)
    # Given u1 = [3, 1], u2 = [2, 2]
    # Step 1: v1 = u1 = [3, 1]
    # Step 2: v2 = u2 - proj(u2 onto v1)
    # Verify: dot(v1, v2) = 0
    # Expected: v1 = [3, 1], v2 = [2, 2] - (8/10)*[3, 1] = [2-2.4, 2-0.8] = [-0.4, 1.2]
    def ex22() -> tuple[np.ndarray, np.ndarray, float]:
        u1 = np.array([3.0, 1.0])
        u2 = np.array([2.0, 2.0])
        # YOUR CODE:
        # v1 = u1
        # v2 = u2 - proj(u2 onto v1)
        # Return: (v1, v2, dot(v1, v2))
        pass

    result = ex22()
    if result is not None:
        check("Ex22a: v1", result[0], np.array([3.0, 1.0]))
        check("Ex22b: v2", result[1], np.array([-0.4, 1.2]))
        check("Ex22c: orthogonal (dot≈0)", abs(result[2]), 0.0, tol=1e-10)
    else:
        print("  [SKIP] Ex22: not implemented yet")
        total += 3

    # =========================================================
    # SUMMARY
    # =========================================================
    print(f"\n{'=' * 60}")
    print(f"  RESULTS: {passed}/{total} passed")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "exercises":
        exercises()
    else:
        demo_basic_operations()
        demo_cosine_similarity_ml()
        demo_norms_comparison()
        demo_projection()
        demo_linear_independence()
        demo_orthogonality()
        if "--plot" in sys.argv:
            demo_visualization()
        print("\nRun 'python vectors_and_spaces.py exercises' to start exercises.")
