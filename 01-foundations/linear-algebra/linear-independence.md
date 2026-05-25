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
  - "[[subspaces]]"
  - "[[general-vector-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.4"
  - "https://www.youtube.com/watch?v=k7RM-ot2NWY"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Vectors are independent when no one vector can be built from the others — each points somewhere genuinely new. The goal: find the *smallest* spanning set, which requires every vector to add something new.

---

## Intuition

You're hiring a team. Person A builds walls. Person B does plumbing. Person C does both — but nothing A and B can't already cover. Person C is **dependent**: they add no new capability. The team is better (smaller) without them.

Spanning sets work the same way. A vector space V can be described by a spanning set S. But you want S as small as possible — studying fewer vectors is easier. The moment a vector in S is a combination of the others, it's redundant: remove it and S still spans the same V. **Linear independence is the condition that guarantees no vector is wasted.**

**Geometric picture (R³):** Three vectors are linearly dependent if and only if all three lie in the same plane through the origin. If one is outside that plane — genuinely pointing somewhere new — they're independent.

## Mechanics

Vectors v₁, …, vₖ are **independent** iff:

```
k₁v₁ + k₂v₂ + ... + kᵣvᵣ = 0   implies   k₁ = k₂ = ... = kᵣ = 0
```

If any non-trivial solution exists (some kᵢ ≠ 0), the set is **dependent** — at least one vector is a combination of the rest.

**Theorem 6 (Anton §4.4):** In Rⁿ, any set with more than n vectors is dependent.

*Why:* Write each vector as a row. The equation k₁v₁ + ... + kᵣvᵣ = 0 becomes a homogeneous system of n equations in r unknowns. When r > n — more unknowns than equations — the system always has non-trivial solutions (Theorem 1, §1.3). So S must be dependent.

| Method | When to use | Key check |
|--------|-------------|-----------|
| Scaling test | 2 vectors | Is one a scalar multiple of the other? |
| [[determinant]] | Square matrix | det ≠ 0 → independent |
| Rank via [[gaussian-elimination]] | Any shape | rank = number of vectors → independent |

```python
import numpy as np

A = np.array([[1,0],[0,1]])    # independent
B = np.array([[1,3],[2,6]])    # dependent (row 2 = 2 × row 1)

print(np.linalg.det(A))         # 1.0  → independent
print(np.linalg.det(B))         # 0.0  → dependent
print(np.linalg.matrix_rank(B)) # 1    < 2 → redundant
```

> Runnable: [[code/foundations/vectors_and_spaces.py]]

## In ML

**Multicollinearity** — if two features are nearly dependent (e.g., temperature in Celsius and Fahrenheit), XᵀX becomes near-singular and weights swing wildly. Same prediction, infinite weight combinations.

**Feature selection** — removing dependent features makes the weight solution unique and the model stable. det = 0 is the quick diagnostic.

**PCA** creates orthogonal (and therefore independent) components, eliminating all redundancy. Each principal component captures genuinely new variance — the minimum spanning description of the data.

## Exercises

**Basic** — Are [1,2] and [3,6] independent? Test with (1) the scaling test and (2) the determinant.

**Intermediate** — Are [1,0,0], [0,1,0], [1,1,1] independent? Use Gaussian elimination to find the rank and identify which vector is redundant.

**Advanced** — Theorem 6 says r > n → dependent in Rⁿ. Does this mean you can never have more than n vectors in a spanning set? What happens to the span when you add a dependent vector?
