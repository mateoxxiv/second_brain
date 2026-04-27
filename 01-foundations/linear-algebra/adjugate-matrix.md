---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[cofactor]]"
  - "[[determinant]]"
  - "[[matrix-inverse]]"
  - "[[special-matrices]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — The adjugate is the transpose of the cofactor matrix. Multiplying $A$ by its adjugate always gives $\det(A)\cdot I$, so dividing by $\det(A)$ gives the inverse: $A^{-1} = \frac{1}{\det(A)}\,\text{adj}(A)$.

---

## Intuition

If you compute every [[cofactor]] of a matrix and arrange them into a grid, you get the **cofactor matrix** $C$. Transpose it — you get the **adjugate** $\text{adj}(A)$.

The remarkable identity: $A \cdot \text{adj}(A) = \det(A) \cdot I$.

Why? When row $i$ of $A$ is multiplied by cofactors from the *same* row, the sum equals $\det(A)$ (by definition of cofactor expansion). When row $i$ is multiplied by cofactors from a *different* row $k$, the sum equals the determinant of a matrix with two identical rows — which is always zero. So the product is diagonal with $\det(A)$ on every entry.

Divide both sides by $\det(A)$ and the inverse appears. The 2×2 formula you know from [[matrix-inverse]] is exactly this, hidden in plain sight.

## Mechanics

**Cofactor matrix** $C$ — replace every entry $(i,j)$ with its [[cofactor]] $C_{ij}$.

**Adjugate** — transpose of the cofactor matrix:

$$\text{adj}(A) = C^T, \qquad \text{adj}(A)_{ij} = C_{ji}$$

**The core identity:**

$$A\,\text{adj}(A) = \det(A)\cdot I$$

**Inverse formula** (when $\det(A) \neq 0$):

$$\boxed{A^{-1} = \frac{1}{\det(A)}\,\text{adj}(A)}$$

**2×2 verification** — the formula you already know IS this:

$$A=\begin{bmatrix}a&b\\c&d\end{bmatrix},\quad C=\begin{bmatrix}d&-c\\-b&a\end{bmatrix},\quad \text{adj}(A)=C^T=\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

$$A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}\checkmark$$

```python
import numpy as np
from cofactor import cofactor  # or inline the function

def adjugate(A):
    n = A.shape[0]
    C = np.array([[
        ((-1)**(i+j)) * np.linalg.det(
            np.delete(np.delete(A, i, 0), j, 1))
        for j in range(n)] for i in range(n)])
    return C.T

A = np.array([[1,2,3],[0,4,5],[1,0,6]], dtype=float)
adj = adjugate(A)
det = np.linalg.det(A)

print(np.allclose(A @ adj, det * np.eye(3)))  # True
print(np.allclose(adj / det, np.linalg.inv(A)))  # True
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Gradient of the determinant** — differentiating $\det(A)$ with respect to $A$ gives $\frac{\partial\,\det(A)}{\partial A} = \text{adj}(A)^T$. This gradient appears when optimising log-likelihoods of multivariate Gaussians, where the normalization term contains $\det(\Sigma)$.

**[[cramer-rule]]** — solves $A\mathbf{x}=\mathbf{b}$ analytically: $x_j = \det(A_j)/\det(A)$, where $A_j$ replaces column $j$ with $\mathbf{b}$. Equivalent to $\mathbf{x} = \text{adj}(A)\,\mathbf{b}\,/\,\det(A)$. Conceptually clean, computationally impractical ($O(n^4)$).

**Why [[gaussian-elimination]] wins** — the adjugate requires computing $n^2$ cofactors, each an $(n-1)\times(n-1)$ determinant. Total cost: $O(n^4)$. Gaussian elimination solves $Ax=b$ in $O(n^3)$. Use the adjugate to *understand* the inverse; use `np.linalg.solve` to *compute* it.

## Exercises

**Basic** — Build the cofactor matrix and adjugate for $A=\begin{bmatrix}3&1\\2&4\end{bmatrix}$. Compute $A^{-1}$ using the formula. Verify with NumPy.

**Intermediate** — For $A=\begin{bmatrix}1&2\\3&4\\0&1\end{bmatrix}$... wait, this is not square. Can you compute an adjugate for a non-square matrix? Why or why not?

**Advanced** — Prove the identity $A\,\text{adj}(A) = \det(A)\cdot I$. Focus on why the off-diagonal entries $(A\,\text{adj}(A))_{ik}$ equal zero when $i\neq k$. (Hint: which determinant does that sum compute?)
