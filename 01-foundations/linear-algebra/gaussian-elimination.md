---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[linear-independence]]"
  - "[[determinant]]"
  - "[[matrix-inverse]]"
  - "[[basis-and-dimension]]"
  - "[[projection-onto-subspaces]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Simplify a system of equations step by step until the answer is obvious. Eliminates one variable at a time by adding multiples of rows to each other — the three allowed moves never change the solution.

---

## Intuition

You're untangling a knot. Don't pull everything at once — free one strand, use that freedom to loosen the next, and so on. Gaussian elimination works the same way: eliminate one variable at a time until only one remains.

Three moves are allowed (they never change the solution):
1. **Swap** two rows
2. **Scale** a row by a constant
3. **Add** a multiple of one row to another

Everything is built from these three.

## Mechanics

Goal: reduce to **row echelon form** (staircase shape, zeros below each pivot), then back-substitute.

```
System:                Augmented matrix:
x + 2y + 3z = 9       | 1  2   3 |  9 |
2x + 5y + 2z = 14  →  | 2  5   2 | 14 |
x + 3y + z = 7        | 1  3   1 |  7 |

After elimination:     | 1  2   3 |  9 |   Back-sub:
R2 -= 2*R1             | 0  1  -4 | -4 |   z=1, y=0, x=6
R3 -= R1, R3 -= R2     | 0  0   2 |  2 |
```

**Three possible outcomes:**

| Echelon form | Interpretation |
|---|---|
| All rows have pivots | Unique solution — full rank |
| Zero row, RHS = 0 | Infinite solutions — dependent feature |
| Zero row, RHS ≠ 0 | No solution — contradictory data |

**Rank** = number of non-zero rows after reduction. Reveals [[linear-independence]].

```python
import numpy as np

A = np.array([[1,2,3],[2,5,2],[1,3,1]], dtype=float)
b = np.array([9,14,7], dtype=float)

x = np.linalg.solve(A, b)         # [6. 0. 1.]
print(np.linalg.matrix_rank(A))   # 3 — full rank

# Dependent case
A_dep = np.array([[1,2,3],[2,4,6],[0,1,1]], dtype=float)
print(np.linalg.matrix_rank(A_dep)) # 2 — rank-deficient
```


## In ML

**Linear regression** — solving $X\mathbf{w} = \mathbf{y}$ is exactly this. Full rank → unique best weights. Rank-deficient → dependent features → unstable weights. No solution → noisy data → use [[projection-onto-subspaces]] (least squares).

**[[matrix-inverse|Matrix inverse]]** — computed by applying Gaussian elimination to $[A\mid I]$ to get $[I\mid A^{-1}]$.

**[[determinant]]** — after elimination, det = product of the pivot values (times $-1$ per row swap).

## Exercises

**Basic** — Solve by hand using Gaussian elimination: $x + y = 3$, $2x + 3y = 8$. Show each row operation.

**Intermediate** — Apply Gaussian elimination to $\begin{bmatrix}1&2&3\\2&4&6\\0&1&1\end{bmatrix}$. What does the result tell you about the vectors' independence?

**Advanced** — What is the connection between the three outcomes of Gaussian elimination (unique / infinite / no solution) and the column space, null space, and rank of the coefficient matrix?
