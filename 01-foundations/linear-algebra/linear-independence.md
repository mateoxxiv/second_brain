---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[linear-combination]]"
  - "[[basis-and-dimension]]"
  - "[[determinant]]"
  - "[[gaussian-elimination]]"
  - "[[cosine-similarity]]"
  - "[[projection-onto-subspaces]]"
domain: linear-algebra
sources:
  - "https://www.youtube.com/watch?v=k7RM-ot2NWY"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Vectors are independent when no one vector can be built from the others — each points somewhere genuinely new. Redundant features cause unstable models: infinite weight configurations produce the same prediction.

---

## Intuition

You're hiring a team. Person A builds walls. Person B does plumbing. Person C does both — but nothing A and B can't already cover. Person C is **dependent**: they add no new capability.

Vectors work the same. Each vector is a direction. If a direction is reachable by combining others, it's redundant. The span doesn't grow when you add a dependent vector.

Key rule: you can never have more independent vectors than dimensions. In $\mathbb{R}^3$, a 4th vector is always dependent — there are only 3 directions to go.

## Mechanics

Vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$ are **independent** iff:

$$c_1\mathbf{v}_1 + \cdots + c_k\mathbf{v}_k = \mathbf{0} \implies c_1 = \cdots = c_k = 0$$

Three practical methods:

| Method | When to use | Key check |
|--------|-------------|-----------|
| Scaling test | 2 vectors (by eye) | Is one a scalar multiple of the other? |
| [[determinant]] | Square matrix | $\det \neq 0$ → independent |
| Rank via [[gaussian-elimination]] | Any shape | rank = count of vectors → independent |

**Orthogonal ≠ Independent (but orthogonal implies independent).** $[1,0]$ and $[1,1]$ are independent but not orthogonal. All orthogonal non-zero vectors are independent.

```python
import numpy as np

A = np.array([[1,0],[0,1]])    # independent
B = np.array([[1,3],[2,6]])    # dependent (row2 = 2×row1)

print(np.linalg.det(A))        # 1.0  → independent
print(np.linalg.det(B))        # 0.0  → dependent
print(np.linalg.matrix_rank(B))# 1    < 2 → redundant
```

> Runnable: [[code/foundations/vectors_and_spaces.py]]

## In ML

**Multicollinearity** — if two features are nearly dependent (e.g., temperature in Celsius and Fahrenheit), $X^TX$ becomes near-singular and weights swing wildly between runs. Same prediction, infinite weight combinations.

**Feature selection** — removing dependent features makes the weight solution unique and the model stable. [[determinant]] = 0 is the quick diagnostic.

**PCA** creates orthogonal (and therefore independent) components, eliminating all redundancy in one step. Each principal component captures genuinely new variance.

## Exercises

**Basic** — Are $[1,2]$ and $[3,6]$ independent? Test with (1) the scaling test and (2) the determinant.

**Intermediate** — Are $[1,0,0]$, $[0,1,0]$, $[1,1,1]$ independent? Use Gaussian elimination to find the rank and identify which vector is redundant.

**Advanced** — A dataset has features $x_1$, $x_2 = 2x_1 + 1$. Why does $x_2 = 2x_1 + 1$ NOT create the same linear dependence problem as $x_2 = 2x_1$? (Hint: think about the difference between linear dependence and affine dependence.)
