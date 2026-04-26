---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[matrix-operations]]"
  - "[[matrix-inverse]]"
  - "[[determinant]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[spectral-decomposition]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Symmetric, diagonal, orthogonal, triangular, singular, and positive-definite matrices each carry structural guarantees that simplify computation. Recognizing them is how you read ML equations fluently.

---

## Intuition

Most matrices are general — they stretch, rotate, and shear in arbitrary ways. Special matrices constrain those operations: orthogonal matrices only rotate (no stretching), diagonal matrices only scale each axis independently, symmetric matrices have a clean decomposition guaranteed by the Spectral Theorem.

Covariance matrices are symmetric. Rotation matrices are orthogonal. SVD produces all three special types at once.

## Mechanics

| Type | Definition | Key property | ML use |
|------|---|---|---|
| **Symmetric** | $A = A^T$ | Real eigenvalues; orthogonal eigenvectors | Covariance, Hessians, PCA |
| **Diagonal** | $a_{ij} = 0$ for $i\neq j$ | Trivial inverse; eigenvalues = diagonal | SVD, batch norm scaling |
| **Triangular** | Zeros above/below diagonal | $\det$ = product of diagonal; easy solve | LU decomposition |
| **Orthogonal** | $Q^TQ = I$ | Preserves lengths/angles; $Q^{-1} = Q^T$ | Rotations, PCA, weight init |
| **Singular** | $\det = 0$ | Not invertible; collapses a dimension | Indicates redundant features |
| **Positive definite** | $\mathbf{x}^TA\mathbf{x} > 0$ | All eigenvalues positive; unique minimum | Convex optimization, Cholesky |

**Orthogonal matrices** — $Q^{-1} = Q^T$ means the inverse is free (just transpose). Preserves the norm $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ — no stretching or shrinking.

**Positive definite** — equivalent to: all eigenvalues $> 0$, all pivots $> 0$, $A = B^TB$ for some full-rank $B$.

```python
import numpy as np

A = np.array([[2,1],[1,3]])
print(np.allclose(A, A.T))        # True — symmetric

t = np.pi/4
Q = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
print(np.allclose(Q.T @ Q, np.eye(2)))  # True — orthogonal
print(np.linalg.norm(Q @ [3,4]))        # 5.0 — lengths preserved

print(all(np.linalg.eigvalsh(A) > 0))   # True — positive definite
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Covariance matrix** $\Sigma = \frac{1}{n}X^TX$ — always symmetric and positive semi-definite. The eigenvectors are the principal components; eigenvalues are the variances.

**Orthogonal weight initialization** — initializing neural network weights as orthogonal matrices prevents vanishing/exploding gradients because all eigenvalues have $|\lambda| = 1$.

**Hessian** — the matrix of second derivatives of a loss function is symmetric (by Schwarz's theorem). Positive definite Hessian → convex local landscape → unique minimum.

## Exercises

**Basic** — For $A = \begin{bmatrix}3&1\\1&2\end{bmatrix}$: is it symmetric? Compute its eigenvalues. Is it positive definite?

**Intermediate** — Build a $2\times2$ rotation matrix for $\theta = 30°$. Verify $Q^TQ = I$ and that it preserves the norm of $[1, 0]$.

**Advanced** — Why do symmetric matrices always have real eigenvalues? Sketch a proof using the fact that $\mathbf{x}^TA\mathbf{x}$ is always real for real $A$.
