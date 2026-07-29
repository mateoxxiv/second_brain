---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[change-of-basis]]"
  - "[[orthonormal-bases]]"
  - "[[gram-schmidt]]"
  - "[[matrix-inverse]]"
  - "[[angles-and-orthogonality]]"
  - "[[singular-value-decomposition]]"
  - "[[orthogonal-diagonalization]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introduccion al Algebra Lineal. S4.10 -- Theorems 27, 28, Examples 67-68."
---

> **TL;DR** — An orthogonal matrix satisfies A^{-1} = A^T, equivalently its rows and columns are orthonormal sets; such matrices represent rigid rotations and reflections that preserve all lengths and angles.

---

## Intuition

An orthogonal matrix is a "perfectly clean" transformation: no stretching, no shearing — only rotation or reflection. Because it preserves distances and angles, its inverse just undoes the rotation, which geometrically is the same as transposing.

The name comes from its rows and columns forming orthonormal sets. Think of it as a matrix whose columns are an orthonormal basis: applying it re-expresses vectors in that new basis without distorting the space.

## Mechanics

**Definition:** A square matrix $A$ is **orthogonal** if $A^{-1} = A^T$, equivalently $A^T A = I$.

**Theorem 27 (Anton S4.10):** If $P$ is the [[change-of-basis|transition matrix]] between two [[orthonormal-bases|orthonormal bases]] in an inner product space, then $P^{-1} = P^T$ — i.e., $P$ is orthogonal.

*Why?* The columns of $P$ are the old ONB vectors expressed in the new ONB. They remain orthonormal, so by Theorem 28, $P$ is orthogonal.

**Theorem 28 (Anton S4.10):** For an $n \times n$ matrix $A$, these are equivalent:

| | Condition |
|---|---|
| (a) | $A$ is orthogonal ($A^T A = I$) |
| (b) | Row vectors of $A$ form an orthonormal set in $\mathbb{R}^n$ |
| (c) | Column vectors of $A$ form an orthonormal set in $\mathbb{R}^n$ |

**Key consequence:** $\det(A) = \pm 1$ always, since $1 = \det(I) = \det(A^T A) = \det(A)^2$.

**Rotations vs reflections** — for orthogonal coordinate transformation $[x;y] = A[x';y']$:

| $\det(A)$ | Geometric meaning |
|---|---|
| $+1$ | Pure rotation (orientation preserved) |
| $-1$ | Rotation + reflection (orientation flips) |

Same rule applies in $\mathbb{R}^3$: det $= +1$ is rotation around some axis; det $= -1$ involves a reflection in one coordinate plane.

**Example 67:** $A = \begin{bmatrix}1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 0 & 0 & 1 \\ 1/\sqrt{2} & -1/\sqrt{2} & 0\end{bmatrix}$ — rows are orthonormal, so $A$ is orthogonal and $A^{-1} = A^T$.

**Example 68 (45 degrees rotation):** $A = \begin{bmatrix}1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2}\end{bmatrix}$, $\det = 1$ — pure rotation. Column vectors give the new x' and y' axis directions.

```python
import numpy as np

def is_orthogonal(A: np.ndarray, tol: float = 1e-10) -> bool:
    return np.allclose(A.T @ A, np.eye(A.shape[0]), atol=tol)

# Rotation matrix — det = +1
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
print(is_orthogonal(R))                      # True
print(f"det = {np.linalg.det(R):.4f}")       # 1.0

# Reflection across x-axis — det = -1
F = np.array([[1., 0.], [0., -1.]])
print(is_orthogonal(F))                      # True
print(f"det = {np.linalg.det(F):.4f}")       # -1.0

# Inverse = transpose (no solver needed)
v = np.array([3., 1.])
print(np.allclose(R.T @ (R @ v), v))        # True
```

## In ML

**QR decomposition** — any full-rank matrix $A = QR$ where $Q$ is orthogonal (columns from [[gram-schmidt|Gram-Schmidt]]) and $R$ is upper-triangular. Every eigenvalue solver and least-squares algorithm builds on this.

**Orthogonal weight initialization** — initializing weight matrices via QR decomposition of a random Gaussian matrix produces orthogonal weights that preserve gradient norms at initialization: $\|Qx\| = \|x\|$ for all $x$.

**SVD and PCA** — $A = U\Sigma V^T$ expresses any matrix as two orthogonal matrices sandwiching a diagonal. The $V$ columns are the principal directions in PCA and form an orthonormal basis by Theorem 28.

**[[orthogonal-diagonalization]]** — when $A$ is square and symmetric, the same "orthonormal columns" idea lets $Q$ both diagonalize $A$ ($Q^TAQ=D$) and serve as its own inverse ($Q^{-1}=Q^T$) — the mechanism behind [[spectral-decomposition]].

## Exercises

**Basic** — Verify that $A = \begin{bmatrix}0 & -1 \\ 1 & 0\end{bmatrix}$ (90 degree rotation) satisfies $A^T A = I$. Compute $\det(A)$. Is it a rotation or reflection?

**Intermediate** — Prove that the product of two orthogonal matrices is orthogonal. Then prove that the inverse of an orthogonal matrix is also orthogonal.

**Advanced** — Show that any orthogonal matrix preserves inner products: $\langle Au, Av \rangle = \langle u, v \rangle$ for all $u, v \in \mathbb{R}^n$. Conclude that it preserves norms and angles. (Use $\langle u, v \rangle = u^T v$ and $A^T A = I$.)
