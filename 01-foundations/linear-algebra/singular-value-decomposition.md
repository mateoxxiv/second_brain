---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[spectral-decomposition]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[special-matrices]]"
  - "[[projection]]"
  - "[[gram-schmidt]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=nbBvuuNVfco"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — SVD decomposes ANY matrix (non-symmetric, non-square, anything) into $A = U\Sigma V^T$: a rotation, a stretch, another rotation. Every matrix does exactly these three things.

---

## Intuition

[[spectral-decomposition]] requires symmetric square matrices. Most real data matrices are neither. SVD generalizes it:

```
Spectral: A = Q  Λ  Qᵀ   (symmetric only — same basis on both sides)
SVD:      A = U  Σ  Vᵀ   (any matrix — different bases on each side)
```

**Geometric interpretation:** $A$ transforms a ball into an ellipse. $V^T$ rotates the input, $\Sigma$ stretches each axis, $U$ rotates the result. Any linear transformation = rotate → stretch → rotate.

The singular values $\sigma_i$ (diagonal of $\Sigma$) are always positive and sorted large to small. They measure how much each "direction pair" contributes.

## Mechanics

$$A = U\Sigma V^T$$

- $U \in \mathbb{R}^{m\times m}$: orthogonal, left singular vectors (output directions)
- $\Sigma \in \mathbb{R}^{m\times n}$: diagonal, singular values $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$
- $V \in \mathbb{R}^{n\times n}$: orthogonal, right singular vectors (input directions)

**Ingredient form:** $A = \sum_i \sigma_i \mathbf{u}_i \mathbf{v}_i^T$

**Connection to eigenvalues:**
$$A^TA = V\Sigma^T U^T \cdot U\Sigma V^T = V\Sigma^2 V^T$$

So singular values of $A$ = $\sqrt{\text{eigenvalues of } A^TA}$. The SVD of $A$ is the spectral decomposition of $A^TA$.

```python
import numpy as np

A = np.array([[1,2],[3,4],[5,6]], dtype=float)  # 3×2, not square
U, s, Vt = np.linalg.svd(A, full_matrices=False)

print(s)                              # singular values
print(np.allclose(U @ np.diag(s) @ Vt, A))  # True

# Rank-k approximation
k = 1
A_approx = s[0] * np.outer(U[:,0], Vt[0,:])
```


## In ML

**Dimensionality reduction (PCA via SVD)** — for data matrix $X$, the SVD gives principal components directly: $X = U\Sigma V^T$. The columns of $V$ are the principal directions; $\sigma_i^2 / n$ are the variances. More numerically stable than computing the covariance matrix eigendecomposition.

**Low-rank approximation** — keep only top-$k$ singular values: $A \approx U_k\Sigma_k V_k^T$. Used in recommendation systems (matrix factorization), image compression, and NLP (LSA).

**Pseudoinverse** — for non-square or rank-deficient matrices, $A^+ = V\Sigma^+U^T$ where $\Sigma^+$ inverts only non-zero singular values. Gives the least-squares solution to $A\mathbf{x} = \mathbf{b}$.

## Exercises

**Basic** — Compute the SVD of $A = \begin{bmatrix}1&1\\0&1\\1&0\end{bmatrix}$ using NumPy. List the singular values. What is the rank?

**Intermediate** — Build a rank-1 approximation of a $3\times3$ matrix and compute the fraction of variance explained.

**Advanced** — Show algebraically that the singular values of $A$ are the square roots of the eigenvalues of $A^TA$. Why are all eigenvalues of $A^TA$ non-negative?
