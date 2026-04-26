---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[matrix-multiplication]]"
  - "[[vector-operations]]"
  - "[[matrix-operations]]"
---

## What it is

Flip a matrix over its main diagonal — rows become columns, columns become rows.
If $A \in \mathbb{R}^{m \times n}$, then $A^T \in \mathbb{R}^{n \times m}$.

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \implies A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

## Key properties

| Rule | Formula |
|------|---------|
| Double transpose | $(A^T)^T = A$ |
| Sum | $(A + B)^T = A^T + B^T$ |
| Product (socks & shoes) | $(AB)^T = B^T A^T$ |
| Dot product | $\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^T \mathbf{y}$ |

The product rule reverses order — to undo "put on socks then shoes", take off shoes first.

## Why it appears everywhere in ML

| Where | Why |
|-------|-----|
| Normal equations $\hat{\beta} = (X^TX)^{-1}X^T y$ | $X^T$ projects $y$ onto column space of $X$ |
| Backpropagation | Forward uses $W$, backward uses $W^T$ |
| Covariance matrix $\Sigma = \frac{1}{n}X^TX$ | Captures feature-to-feature relationships |

## Code

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.T)          # shape flips: (2,3) → (3,2)
print(A.T.T)        # back to original

x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
print(x @ y)        # 32  (dot product = x^T y)
```

## See also

- [[vector-operations]] — dot product is transpose-multiply
- [[matrix-multiplication]] — $(AB)^T = B^TA^T$, order reverses
- [[special-matrices]] — symmetric matrix: $A = A^T$
