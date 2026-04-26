---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[linear-independence]]"
  - "[[gaussian-elimination]]"
  - "[[matrix-inverse]]"
  - "[[basis-and-dimension]]"
  - "[[matrix-operations]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=Ip3X9LOh2dk"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The determinant measures the area (2D) or volume (nD) of the shape formed by a matrix's columns. Zero means at least one column is redundant — the transformation collapses a dimension.

---

## Intuition

Two vectors form a parallelogram. Three vectors form a 3D box. The determinant is the **signed area/volume** of that shape.

- $\det \neq 0$: full area/volume. Vectors are independent. Matrix is invertible.
- $\det = 0$: the shape is flat. A parallelogram became a line — something was redundant.
- **Sign**: positive → orientation preserved. Negative → mirrored (right hand becomes left hand).

For $[1, 2]$ and $[2, 4]$: the parallelogram collapses to a line. $\det = 1\cdot4 - 2\cdot2 = 0$.

## Mechanics

**2×2:** $\det\begin{bmatrix}a&b\\c&d\end{bmatrix} = ad - bc$ (main diagonal minus anti-diagonal)

**3×3 (cofactor expansion along row 1):**
$$\det = a(ei-fh) - b(di-fg) + c(dh-eg)$$

**Triangular matrices:** $\det$ = product of diagonal entries (no expansion needed).

| Property | Effect |
|----------|--------|
| Scale a row by $k$ | $\det$ multiplies by $k$ |
| Swap two rows | $\det$ flips sign |
| Two equal rows | $\det = 0$ |
| $\det(AB) = \det(A)\cdot\det(B)$ | Chaining scales volumes |

**Equivalence chain** — all of these mean the same thing:
$\det(A) = 0 \iff$ not invertible $\iff$ columns dependent $\iff$ rank $< n \iff Ax=b$ has no unique solution.

```python
import numpy as np

def det_2x2(m): return m[0,0]*m[1,1] - m[0,1]*m[1,0]

A = np.array([[1,2],[3,4]])
print(det_2x2(A))            # -2
print(np.linalg.det(A))      # -2.0

# Independence test
dep = np.array([[1,2],[2,4]])
print(np.linalg.det(dep))    # 0.0 → dependent
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Linear regression** — fitting $\hat{y} = X\mathbf{w}$ requires inverting $X^TX$. If $\det(X^TX) = 0$, features are linearly dependent → no unique solution. This is multicollinearity.

**Gaussian distributions** — the normalization term includes $\frac{1}{\sqrt{\det(\Sigma)}}$ where $\Sigma$ is the covariance matrix. Zero determinant = degenerate distribution (no volume).

**Change of variables** — when transforming integrals, the Jacobian determinant measures how the transformation scales infinitesimal volumes.

## Exercises

**Basic** — Compute by hand: $\det\begin{bmatrix}3&1\\2&4\end{bmatrix}$ and $\det\begin{bmatrix}1&2\\2&4\end{bmatrix}$. Interpret both results.

**Intermediate** — Compute the determinant of $\begin{bmatrix}2&1&0\\1&3&1\\0&1&2\end{bmatrix}$ using cofactor expansion. Verify with NumPy.

**Advanced** — Prove that $\det(AB) = \det(A)\cdot\det(B)$ using the geometric interpretation (what does multiplying two transformations do to volume?).
