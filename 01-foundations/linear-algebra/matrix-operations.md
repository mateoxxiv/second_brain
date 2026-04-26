---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[what-is-a-matrix]]"
  - "[[matrix-inverse]]"
  - "[[special-matrices]]"
  - "[[determinant]]"
  - "[[eigenvalues-and-eigenvectors]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=XkY2DOUCWMU"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Matrix arithmetic: addition is element-wise, transpose flips rows and columns, multiplication composes transformations (right-to-left). Non-commutativity ($AB \neq BA$) is the critical property to internalize.

---

## Intuition

**Addition** — element-wise, same rules as scalar arithmetic. Matrices must have the same shape.

**Transpose** — flip over the main diagonal: rows become columns. The "socks and shoes" rule: $(AB)^T = B^TA^T$. To undo "put on socks then shoes," remove shoes first.

**Multiplication** — applying transformation $B$ then $A$, read right-to-left like function composition $f(g(x))$. Each output entry is a dot product of a row from $A$ with a column from $B$.

Why NOT commutative: rotating then shearing ≠ shearing then rotating. Order of transformations matters.

## Mechanics

**Addition:** $(A+B)_{ij} = A_{ij} + B_{ij}$ (same dimensions required)

**Transpose:** $(A^T)_{ij} = A_{ji}$; shape flips from $m\times n$ to $n\times m$

**Multiplication:** $(AB)_{ij} = \sum_k A_{ik}B_{kj}$ (inner dimensions must match)

| Property | Rule |
|---|---|
| Not commutative | $AB \neq BA$ in general |
| Associative | $(AB)C = A(BC)$ |
| Transpose of product | $(AB)^T = B^TA^T$ |
| Inverse of product | $(AB)^{-1} = B^{-1}A^{-1}$ |
| Dot product | $\mathbf{x}\cdot\mathbf{y} = \mathbf{x}^T\mathbf{y}$ |

```python
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A + B)         # [[6,8],[10,12]] — element-wise
print(A.T)           # [[1,3],[2,4]]   — transposed
print(A @ B)         # [[19,22],[43,50]]
print(B @ A)         # [[23,34],[31,46]] — different!

x, y = np.array([1,2,3]), np.array([4,5,6])
print(x @ y)         # 32 — dot product = xᵀy
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**Transpose in ML** — dot product is secretly $\mathbf{x}^T\mathbf{y}$. Backpropagation uses $W^T$ (errors flow backward through transposed weights). Normal equations: $\hat{\beta} = (X^TX)^{-1}X^T\mathbf{y}$.

**Matrix multiplication as composition** — a neural network's forward pass is a chain of matrix multiplications with nonlinearities: $\hat{y} = \sigma(W_3\sigma(W_2\sigma(W_1\mathbf{x})))$. Without $\sigma$, the whole chain collapses to a single matrix $W_3W_2W_1$.

**Practical note** — never compute $A^{-1}$ explicitly. Use `np.linalg.solve(A, b)` — same result, fewer floating-point errors.

## Exercises

**Basic** — Compute $A^T$ and $AB$ by hand for $A = \begin{bmatrix}1&0\\2&3\end{bmatrix}$, $B = \begin{bmatrix}2&1\\1&2\end{bmatrix}$. Verify $AB \neq BA$.

**Intermediate** — Verify the socks-and-shoes rule: compute $(AB)^T$ and $B^TA^T$ for the same matrices. Show they're equal.

**Advanced** — A 3-layer neural network has weight matrices $W_1, W_2, W_3$. Without activation functions, show the network is equivalent to a single matrix. What does this prove about depth without nonlinearity?
