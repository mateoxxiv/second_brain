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
  - "[[block-diagonal-matrices]]"
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

**Leibniz formula (tree method)** — the general definition behind all methods:

$$\det(A) = \sum_{\sigma} \text{sgn}(\sigma)\; a_{1\sigma(1)}\cdot a_{2\sigma(2)}\cdots a_{n\sigma(n)}$$

Pick one element from each row, never repeating a column. Multiply them. Repeat for every possible column ordering (permutation). Add with sign +1 (even permutation) or −1 (odd permutation).

For 3×3 the tree has 3! = 6 paths — 3 positive, 3 negative. This is exactly what [[sarrus-rule]] encodes visually. [[cofactor]] expansion reorganizes the same sum into a recursive structure. For n×n there are n! paths — impractical beyond 3×3, which is why [[gaussian-elimination]] (O(n³)) is used in practice. If the matrix happens to be [[block-diagonal-matrices|block diagonal or block triangular]], skip all of that — the determinant is just the product of the smaller diagonal blocks' own determinants.

| Property | Formula | Why it matters |
|----------|---------|----------------|
| Scale one row by k | det multiplies by k | Row operations change det predictably |
| Scale whole matrix by k | det(kA) = k^n · det(A) | Each of n rows gets scaled → k applied n times |
| Swap two rows | det flips sign | Orientation reverses |
| Two equal rows | det = 0 | Columns dependent → volume collapses |
| Add k × row i to row j | det unchanged | Gaussian elimination preserves det |
| Transpose | det(A^T) = det(A) | Rows and columns are symmetric for det |
| Inverse | det(A^{-1}) = 1 / det(A) | From det(A · A^{-1}) = det(I) = 1 |
| Product | det(AB) = det(A) · det(B) | Chaining scales volumes |
| Addition | det(A+B) ≠ det(A) + det(B) | det is non-linear — this is NOT an equality |

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

# New properties
k = 3
print(np.linalg.det(k * A))                          # k^2 * det(A) = 9 * -2 = -18
print(np.isclose(np.linalg.det(k*A), k**2 * det_2x2(A)))  # True
print(np.linalg.det(A.T))                            # same as det(A) = -2
print(np.linalg.det(np.linalg.inv(A)))               # 1/det(A) = -0.5

B = np.array([[5,6],[7,8]])
print(np.linalg.det(A+B))                            # NOT det(A)+det(B) — non-linear
print(np.linalg.det(A) + np.linalg.det(B))           # different value
```


## In ML

**Linear regression** — fitting $\hat{y} = X\mathbf{w}$ requires inverting $X^TX$. If $\det(X^TX) = 0$, features are linearly dependent → no unique solution. This is multicollinearity.

**Gaussian distributions** — the normalization term includes $\frac{1}{\sqrt{\det(\Sigma)}}$ where $\Sigma$ is the covariance matrix. Zero determinant = degenerate distribution (no volume).

**Change of variables** — when transforming integrals, the Jacobian determinant measures how the transformation scales infinitesimal volumes.

## Exercises

**Basic** — Compute by hand: $\det\begin{bmatrix}3&1\\2&4\end{bmatrix}$ and $\det\begin{bmatrix}1&2\\2&4\end{bmatrix}$. Interpret both results.

**Intermediate** — Compute the determinant of $\begin{bmatrix}2&1&0\\1&3&1\\0&1&2\end{bmatrix}$ using cofactor expansion. Verify with NumPy.

**Advanced** — Prove that $\det(AB) = \det(A)\cdot\det(B)$ using the geometric interpretation (what does multiplying two transformations do to volume?).
