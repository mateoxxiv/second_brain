---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[special-matrices]]"
  - "[[projection]]"
  - "[[singular-value-decomposition]]"
  - "[[matrix-inverse]]"
  - "[[orthogonal-diagonalization]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=PFDu9oVAE-g"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Break a symmetric matrix into an ingredient list: $A = Q\Lambda Q^T$. Each ingredient is one eigenvalue × one rank-1 projection matrix. Matrix powers and inverses become trivial.

---

## Intuition

Every symmetric matrix can be seen as a **weighted sum of simple projections**:

```
A = λ₁·(q₁qᵀ₁) + λ₂·(q₂qᵀ₂) + ...
```

Each $q_i q_i^T$ projects onto one eigenvector direction. The eigenvalue $\lambda_i$ is the weight of that direction. To compute $A^{10}$, raise each weight to the 10th power — the directions $Q$ stay the same.

This only works for symmetric matrices because the Spectral Theorem guarantees real eigenvalues and orthogonal eigenvectors ($Q^T = Q^{-1}$, the free inverse) — see [[orthogonal-diagonalization]] for why that guarantee holds.

## Mechanics

$$A = Q\Lambda Q^T$$

- $Q$ = orthogonal matrix (eigenvectors as columns)
- $\Lambda$ = diagonal matrix (eigenvalues on diagonal)

**Key operations become trivial:**

| Operation | Formula | Why cheap |
|---|---|---|
| Powers | $A^k = Q\Lambda^k Q^T$ | Raise diagonal entries to $k$ |
| Inverse | $A^{-1} = Q\Lambda^{-1}Q^T$ | Invert diagonal entries |
| Trace | $\text{tr}(A) = \sum \lambda_i$ | Sum of eigenvalues |
| Determinant | $\det(A) = \prod \lambda_i$ | Product of eigenvalues |

**Low-rank approximation:** keep only the top-$k$ largest eigenvalue terms:
$$A \approx \sum_{i=1}^k \lambda_i q_i q_i^T$$

Variance explained: $\frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^n \lambda_i}$

```python
import numpy as np

A = np.array([[2,1],[1,2]], dtype=float)
eigenvalues, Q = np.linalg.eigh(A)   # eigh for symmetric
Lambda = np.diag(eigenvalues)

print(np.allclose(A, Q @ Lambda @ Q.T))  # True — rebuilt A

# Matrix power the easy way
k = 10
A_k = Q @ np.diag(eigenvalues**k) @ Q.T

# Low-rank (keep top-1 component)
top = np.argmax(eigenvalues)
A_approx = eigenvalues[top] * np.outer(Q[:,top], Q[:,top])
```


## In ML

**PCA** is spectral decomposition of the covariance matrix. Each ingredient $\lambda_i q_i q_i^T$ is one principal component. Keeping the top-$k$ components is low-rank approximation of the data.

**Kernel methods (SVMs, Gaussian processes)** — the kernel matrix is symmetric positive semi-definite. Spectral decomposition reveals its structure and enables efficient computation.

**Quadratic forms** — in optimization, $\mathbf{x}^T A \mathbf{x}$ evaluated in the eigenbasis becomes $\sum \lambda_i z_i^2$. Positive eigenvalues → bowl (convex); negative → saddle point.

## Exercises

**Basic** — For $A = \begin{bmatrix}3&1\\1&3\end{bmatrix}$: find eigenvalues and eigenvectors, build $Q$ and $\Lambda$, verify $Q\Lambda Q^T = A$.

**Intermediate** — Compute $A^5$ for the same matrix using $Q\Lambda^5 Q^T$. Verify against direct multiplication.

**Advanced** — The low-rank approximation $A_k = \sum_{i=1}^k \lambda_i q_i q_i^T$ minimizes the Frobenius norm $\|A - A_k\|_F$. Why? (Hint: what is $\|A - A_k\|_F^2$ in terms of eigenvalues?)
