---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[matrix-operations]]"
  - "[[determinant]]"
  - "[[special-matrices]]"
  - "[[spectral-decomposition]]"
  - "[[singular-value-decomposition]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=PFDu9oVAE-g"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Eigenvectors are special directions a matrix only stretches or shrinks (never rotates). The eigenvalue is the stretch factor. They reveal the "natural axes" of any transformation.

---

## Intuition

Most vectors get rotated AND scaled by a matrix. Eigenvectors are the exceptions — they only get scaled. The matrix can only say "go 3× further in this direction" or "flip and go 2× further," never "turn left."

```
A @ [1, 1] = [3, 3] = 3 * [1,1]  ← only stretched (λ=3)
A @ [1,-1] = [1,-1] = 1 * [1,-1] ← unchanged (λ=1)
```

These are the "natural axes" of $A$. Along these directions, the whole transformation collapses to simple scalar multiplication.

## Mechanics

$$A\mathbf{v} = \lambda\mathbf{v}$$

$\mathbf{v}$ = eigenvector (direction that survives), $\lambda$ = eigenvalue (stretch factor).

**To find eigenvalues:** solve the characteristic equation $\det(A - \lambda I) = 0$.

**To find eigenvectors:** for each $\lambda$, solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$.

**Worked example** for $A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$:

$$\det\begin{bmatrix}2-\lambda & 1\\1 & 2-\lambda\end{bmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3) = 0$$

$\lambda_1 = 1$: $(A-I)\mathbf{v}=\mathbf{0}$ → $\mathbf{v}_1 = [1,-1]$
$\lambda_2 = 3$: $(A-3I)\mathbf{v}=\mathbf{0}$ → $\mathbf{v}_2 = [1,1]$

```python
import numpy as np

A = np.array([[2, 1], [1, 2]], dtype=float)
eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)    # [1. 3.]
print(eigenvectors)   # columns = eigenvectors

# Verify: A @ v = lambda * v
v = eigenvectors[:, 1]   # second eigenvector
print(np.allclose(A @ v, eigenvalues[1] * v))  # True
```

> Runnable: [[code/foundations/eigenvalues_and_eigenvectors.py]]

## In ML

**PCA** — the covariance matrix is symmetric, so its eigenvectors are orthogonal. Each eigenvector is a principal component; each eigenvalue is the variance along that component. PCA sorts components by eigenvalue (largest first).

**Stability of gradient descent** — the eigenvalues of the Hessian $H$ determine how fast training converges. The largest eigenvalue sets the maximum safe learning rate: $\alpha < \frac{2}{\lambda_\text{max}}$.

**[[spectral-decomposition]]** — for symmetric matrices, $A = Q\Lambda Q^T$ where $Q$ packs eigenvectors and $\Lambda$ holds eigenvalues on the diagonal. Matrix powers become trivial: $A^k = Q\Lambda^k Q^T$.

## Exercises

**Basic** — Find the eigenvalues of $\begin{bmatrix}4&1\\2&3\end{bmatrix}$ using the characteristic equation. Then find one eigenvector.

**Intermediate** — For $A = \begin{bmatrix}3&1\\0&2\end{bmatrix}$, find all eigenvalues and eigenvectors by hand. Verify with NumPy.

**Advanced** — A matrix has eigenvalue $\lambda = 0$. What does this mean for (1) invertibility, (2) the null space, and (3) the determinant? Connect all three.
