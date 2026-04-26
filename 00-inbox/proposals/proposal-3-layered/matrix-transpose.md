---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[matrix-multiplication]]"
  - "[[special-matrices]]"
sources:
  - "https://www.youtube.com/watch?v=kYB8IZa5AuE"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Flip a matrix so rows become columns. The key rule: $(AB)^T = B^TA^T$ (order reverses). This is why transpose is everywhere in ML — dot products, backprop, and normal equations all use it.

---

## Intuition

Imagine your matrix as a spreadsheet. Transpose rotates the whole grid 90°: what was row 1 is now column 1.

```
Before:          After transpose:
1  2  3          1  4
4  5  6    →     2  5
                 3  6
```

The shape flips too: a $2 \times 3$ matrix becomes $3 \times 2$.

## Mechanics

$$(A^T)_{ij} = A_{ji}$$

The "socks and shoes" rule for products:

$$(AB)^T = B^T A^T$$

To undo "put on socks, then shoes" you take off shoes first, then socks. Transpose reverses the order.

| Rule | Formula |
|------|---------|
| Double transpose | $(A^T)^T = A$ |
| Sum | $(A+B)^T = A^T + B^T$ |
| Product | $(AB)^T = B^TA^T$ |
| Dot product | $x \cdot y = x^Ty$ |

```python
import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A.T)               # shape: (3,2)
print(A @ A.T)           # always square and symmetric

x, y = np.array([1,2,3]), np.array([4,5,6])
print(x @ y == x.T @ y)  # True — dot product is transpose-multiply
```

## In ML

Transpose is not a notation trick — it's load-bearing in three places:

**Backpropagation** — the forward pass multiplies by $W$; the backward pass multiplies by $W^T$. This is how gradients travel in reverse through the network.

**Normal equations** — $\hat{\beta} = (X^TX)^{-1}X^Ty$. The $X^T$ projects $y$ onto the column space of $X$.

**Covariance matrix** — $\Sigma = \frac{1}{n}X^TX$ captures feature relationships. Always square and symmetric because of transpose.
