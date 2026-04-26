---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[projection]]"
  - "[[matrix-inverse]]"
  - "[[linear-independence]]"
  - "[[gaussian-elimination]]"
  - "[[basis-and-dimension]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Project a vector onto a subspace (plane, hyperplane) by finding the point in that subspace closest to the vector. The error is always perpendicular to the subspace — this is the geometric heart of least squares regression.

---

## Intuition

Drop a ball above a table. Where it lands is the projection onto the table. The string from the ball to its shadow is perpendicular to the table — and it's the shortest possible string (any other point on the table is farther away).

Least squares regression does exactly this: your target $\mathbf{b}$ doesn't live in the column space of $X$ (data is noisy), so you find the closest point in that space. The residuals are the perpendicular strings.

## Mechanics

Given column matrix $A$ (independent columns) and target $\mathbf{b}$, the projection is:

$$\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$$
$$\mathbf{p} = A\hat{\mathbf{x}} = A(A^TA)^{-1}A^T\mathbf{b}$$

The **projection matrix** $P = A(A^TA)^{-1}A^T$ has two key properties: $P^2 = P$ (project twice = same result) and $P^T = P$ (symmetric).

**Why this formula?** The residual $\mathbf{e} = \mathbf{b} - A\hat{\mathbf{x}}$ must be perpendicular to every column of $A$. This gives $A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}$, which solves to the formula above.

```python
import numpy as np

# Project b onto column space of A
A = np.array([[1,0],[0,1],[1,1]], dtype=float)  # 3D, 2 columns
b = np.array([1, 2, 3], dtype=float)

# Normal equations
x_hat = np.linalg.solve(A.T @ A, A.T @ b)
p = A @ x_hat                  # projection
e = b - p                      # residual

print(A.T @ e)                 # ≈ [0, 0] — residual ⊥ columns ✓
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Linear regression** — fitting $y = X\mathbf{w}$ in closed form: $\hat{\mathbf{w}} = (X^TX)^{-1}X^T\mathbf{y}$. The prediction $\hat{\mathbf{y}} = X\hat{\mathbf{w}}$ is the projection of $\mathbf{y}$ onto the column space of $X$. The residuals $\mathbf{y} - \hat{\mathbf{y}}$ are perpendicular to that space.

**[[gaussian-elimination|Rank-deficiency]]** — if columns of $A$ are dependent, $A^TA$ is singular and the formula breaks. Fix: add regularization $\lambda I$: $\hat{\mathbf{x}} = (A^TA + \lambda I)^{-1}A^T\mathbf{b}$ (Ridge regression).

**PCA** — projects data onto the subspace spanned by the top-$k$ principal components (eigenvectors of the covariance matrix).

## Exercises

**Basic** — Using the formula, project $\mathbf{b} = [1,1,1]^T$ onto the column space of $A = \begin{bmatrix}1\\0\\0\end{bmatrix}$ (a single vector). Verify using the 1D projection formula from [[projection]].

**Intermediate** — Solve the least squares problem: fit a line $y = mx + c$ to the points $(1,1),(2,3),(3,2)$. Set up $X\mathbf{w} = \mathbf{y}$ and solve with normal equations.

**Advanced** — Prove $P^2 = P$ for $P = A(A^TA)^{-1}A^T$. What does this property mean geometrically?
