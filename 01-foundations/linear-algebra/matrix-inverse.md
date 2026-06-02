---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[determinant]]"
  - "[[gaussian-elimination]]"
  - "[[linear-independence]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[special-matrices]]"
  - "[[row-and-column-spaces]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=uQhTuRlWMxw"
  - "https://gregorygundersen.com/blog/2020/12/09/matrix-inversion/"
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.6 — Theorem 13"
---


> **TL;DR** — $A^{-1}$ undoes what $A$ does. It exists only when $A$ doesn't collapse any dimension ($\det A \neq 0$). In practice: never compute the inverse explicitly — use `np.linalg.solve` instead.

---
## Intuition

If $A$ stretches space, $A^{-1}$ un-stretches it. The key insight: when $\det(A) = 0$, the transformation destroys information — multiple inputs map to the same output. You can't reverse it. It's like trying to un-blend a smoothie back into separate fruits.

The six equivalent conditions for invertibility all say the same thing: no information is lost.

## Mechanics

**2×2 formula:** swap diagonal, negate off-diagonal, divide by det:

$$A = \begin{bmatrix}a&b\\c&d\end{bmatrix} \implies A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

**Larger matrices:** apply [[gaussian-elimination]] on the augmented matrix $[A\mid I] \to [I\mid A^{-1}]$.

| Equivalent statements (Theorem 13, Anton §1.7 + §4.6) | All mean: $A$ is invertible |
|-----------------------|----------------------------|
| $\det(A) \neq 0$ | No dimension collapses |
| $A\mathbf{x} = \mathbf{0}$ has only the trivial solution | No vectors are erased |
| $A\mathbf{x} = \mathbf{b}$ is consistent for every $\mathbf{b} \in \mathbb{R}^n$ | [[row-and-column-spaces\|Column space]] = all of $\mathbb{R}^n$ |
| Column vectors are linearly independent | No redundant output directions |
| Row vectors are linearly independent | No redundant input directions |
| $\text{rank}(A) = n$ | No information lost |
| No zero [[eigenvalues-and-eigenvectors\|eigenvalues]] | No "null" directions |

**Key properties:** $(AB)^{-1} = B^{-1}A^{-1}$ (socks-and-shoes), $(A^T)^{-1} = (A^{-1})^T$, $(A^{-1})^{-1} = A$.

```python
import numpy as np

A = np.array([[4, 7], [2, 6]])
b = np.array([1, 2])

# Always prefer solve over inv — faster and more numerically stable
x = np.linalg.solve(A, b)      # [0.8, -0.2]

# Never do this in production:
# x = np.linalg.inv(A) @ b

print(A @ np.linalg.inv(A))    # identity (verify)
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Normal equations** — closed-form linear regression solution: $\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$. Requires $X^TX$ to be invertible — breaks when features are dependent or the system is underdetermined.

**"Don't invert that matrix"** — `np.linalg.inv` accumulates floating-point errors and is slower than solving the system directly. `np.linalg.solve(A, b)` uses LU decomposition internally. For least squares: `np.linalg.lstsq`.

**[[special-matrices|Orthogonal matrices]]** have a free inverse: $Q^{-1} = Q^T$. No computation needed — just transpose.

## Exercises

**Basic** — Compute $A^{-1}$ by hand for $A = \begin{bmatrix}2&1\\5&3\end{bmatrix}$. Verify $AA^{-1} = I$.

**Intermediate** — Use the augmented matrix method $[A\mid I]$ to find the inverse of $\begin{bmatrix}1&2\\3&7\end{bmatrix}$. Show every row operation step.

**Advanced** — Why is computing $(X^TX)^{-1}X^T\mathbf{y}$ numerically dangerous for large $X$? What does `np.linalg.lstsq` do differently? (Hint: look up SVD-based least squares.)
