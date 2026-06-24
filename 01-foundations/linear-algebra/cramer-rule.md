---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[determinant]]"
  - "[[adjugate-matrix]]"
  - "[[cofactor]]"
  - "[[matrix-inverse]]"
  - "[[gaussian-elimination]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Cramer's rule solves $Ax=b$ by replacing each column of $A$ with $b$ one at a time: $x_j = \det(A_j)/\det(A)$. Exact and elegant, but $O(n^4)$ — use it to understand linear systems, not to compute them.

---

## Intuition

When you solve $Ax = b$, you are asking: what scalar weights $x_1, x_2, \ldots$ on the columns of $A$ add up to $b$?

Cramer's rule answers geometrically. The weight $x_j$ on column $j$ equals the **ratio of two volumes**: the volume of the box you get when you swap column $j$ of $A$ with $b$, divided by the original box volume $\det(A)$.

Swapping in $b$ "measures" how much of $b$ belongs to direction $j$. Dividing by $\det(A)$ normalises by the size of the original transformation.

## Mechanics

For $Ax = b$ with $\det(A) \neq 0$, define $A_j$ as the matrix $A$ with **column $j$ replaced by $b$**:

$$\boxed{x_j = \frac{\det(A_j)}{\det(A)}}$$

**Where this comes from** — start from the [[adjugate-matrix]] inverse formula:

$$x = A^{-1}b = \frac{1}{\det(A)}\,\text{adj}(A)\cdot b$$

The $j$-th component of $\text{adj}(A)\cdot b$ is $\sum_i C_{ij}\, b_i$ — a [[cofactor]] expansion of $\det(A_j)$ along column $j$. So $x_j = \det(A_j)/\det(A)$.

**2×2 worked example** — $A = \begin{bmatrix}2&1\\5&3\end{bmatrix}$, $b = \begin{bmatrix}4\\7\end{bmatrix}$:

$$\det(A) = 1, \quad A_1 = \begin{bmatrix}4&1\\7&3\end{bmatrix},\quad A_2 = \begin{bmatrix}2&4\\5&7\end{bmatrix}$$
$$x_1 = \frac{12-7}{1} = 5, \qquad x_2 = \frac{14-20}{1} = -6$$

```python
import numpy as np

def cramer(A, b):
    det_A = np.linalg.det(A)
    n = A.shape[0]
    x = np.zeros(n)
    for j in range(n):
        Aj = A.copy()
        Aj[:, j] = b
        x[j] = np.linalg.det(Aj) / det_A
    return x

A = np.array([[2,1],[5,3]], dtype=float)
b = np.array([4,7], dtype=float)
print(cramer(A, b))            # [5. -6.]
print(np.linalg.solve(A, b))   # [5. -6.] ✓
```


## In ML

**Why it matters conceptually** — Cramer's rule makes the relationship between [[determinant]] and solvability concrete: if $\det(A) = 0$, the formula breaks down (division by zero), confirming $Ax=b$ has no unique solution. This connects directly to the equivalence chain in [[determinant]].

**Normal equations** — the least-squares solution $\hat{w} = (X^TX)^{-1}X^Ty$ could in principle be written with Cramer's rule. In practice, `np.linalg.solve` uses LU factorisation ([[gaussian-elimination]]) at $O(n^3)$, not $O(n^4)$.

**When Cramer's rule IS used** — symbolic computation (SymPy, CAS tools) solves small parametric systems with Cramer's rule because it produces closed-form expressions directly. For example, deriving the 2×2 inverse formula or Kalman filter updates in closed form.

## Exercises

**Basic** — Solve $\begin{bmatrix}1&2\\3&4\end{bmatrix}x = \begin{bmatrix}5\\11\end{bmatrix}$ using Cramer's rule by hand. Verify with `np.linalg.solve`.

**Intermediate** — Apply Cramer's rule to a 3×3 system. Count the number of determinant computations required. Compare to the operation count for [[gaussian-elimination]] on the same system.

**Advanced** — Prove that Cramer's formula $x_j = \det(A_j)/\det(A)$ follows from $x = \text{adj}(A)\,b\,/\,\det(A)$. Show that $[\text{adj}(A)\cdot b]_j = \det(A_j)$ by interpreting it as a cofactor expansion along column $j$.
