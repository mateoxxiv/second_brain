---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[plane-equation]]"
  - "[[gaussian-elimination]]"
  - "[[cramer-rule]]"
  - "[[determinant]]"
  - "[[linear-independence]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. Ch. 3 — Fig. 3.30, Theorem 6."
---

> **TL;DR** — Every equation in a 3×3 linear system defines a plane; solving the system means finding where three planes intersect, and the six possible geometric configurations map exactly to "unique / infinite / no solution."

---

## Intuition

When you write `ax + by + cz = k`, you are not just writing an algebraic expression — you are cutting through 3D space with a flat surface. A 3×3 system is three knives. The question "does this system have a solution?" is really asking "do these three cuts ever meet?"

If three walls of a room meet at a corner, they share exactly one point. If two walls are parallel, they never meet. The algebra knows nothing about knives or walls — but the geometry reveals why.

## Mechanics

Each equation `ax + by + cz = k` is a [[plane-equation]] with normal n = [a, b, c]. A 3×3 system:

```
ax + by + cz = k₁
dx + ey + fz = k₂
gx + hy + iz = k₃
```

is three planes. The solution set is their geometric intersection.

**The six cases (Anton Fig. 3.30):**

| Case | Geometry | Solutions |
|---|---|---|
| (a) | Three parallel planes | None |
| (b) | Two planes parallel, third cuts both | None |
| (c) | Three planes, no common intersection (triangular prism) | None |
| (d) | Three coincident planes (identical) | Infinite — full plane |
| (e) | Three planes meeting in a line | Infinite — a line |
| (f) | Three planes meeting at one point | Exactly one |

**Algebraic detector** — the [[determinant]] of the coefficient matrix tells you which regime:

- det(A) ≠ 0 → case (f): unique solution (planes are independent, meet at one point)
- det(A) = 0, consistent → cases (d) or (e): infinite solutions
- det(A) = 0, inconsistent → cases (a), (b), or (c): no solution

This is exactly [[cramer-rule]]'s three cases, now seen as geometry.

```python
import numpy as np

def classify_system(A: np.ndarray, b: np.ndarray) -> str:
    det = np.linalg.det(A)
    if not np.isclose(det, 0):
        return "unique solution (3 planes meet at one point)"
    aug = np.column_stack([A, b])
    rank_A, rank_aug = np.linalg.matrix_rank(A), np.linalg.matrix_rank(aug)
    if rank_A == rank_aug:
        return f"infinite solutions (planes meet in a {'plane' if rank_A == 1 else 'line'})"
    return "no solution (planes have no common intersection)"

A = np.array([[1.,0,0],[0,1.,0],[0,0,1.]])
b = np.array([1.,2.,3.])
print(classify_system(A, b))   # unique solution
```


## In ML

**Feature space geometry** — in a linear classifier, each weight equation w · x = b defines a hyperplane in feature space. Training a model with n features and n constraints is geometrically the same as intersecting n hyperplanes — the solution is the weight vector at their meeting point.

**[[gaussian-elimination]] as plane manipulation** — row operations in Gaussian elimination are geometric: adding a multiple of one plane equation to another tilts and shifts planes while preserving their intersection. Elimination succeeds when the planes converge to a unique point (case f) and fails (or produces free variables) in cases (d) and (e).

**Rank and solution dimensionality** — the rank of A counts the number of truly independent planes. Rank 3 = case (f). Rank 2 = planes collapse to a line (case e). Rank 1 = all three planes are the same (case d). This connects directly to [[linear-independence]] of the rows.

## Exercises

**Basic** — Draw (by hand or mentally) cases (a) and (f) from Figure 3.30. For case (f), describe what geometric property of the three planes guarantees a unique intersection. What does that correspond to algebraically?

**Intermediate** — Classify each system without solving: (1) A = identity matrix, b = [1,2,3]; (2) A has two identical rows, b arbitrary; (3) A has det = 0 and b = [0,0,0]. Which case (a)–(f) does each correspond to?

**Advanced** — Explain why case (e) (infinite solutions along a line) always implies rank(A) = 2. Use [[linear-independence]] to justify why two independent planes always intersect in a line in R³, and why adding a third dependent plane leaves that line unchanged.
