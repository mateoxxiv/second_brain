---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[determinant]]"
  - "[[cofactor]]"
  - "[[matrix-inverse]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Sarrus' rule is a diagonal-sum shortcut for 3×3 determinants: extend the matrix by copying its first two columns, then sum three down-right diagonals and subtract three up-right diagonals. It only works for 3×3 — never larger.

---

## Intuition

The [[determinant]] of a 3×3 matrix has exactly 6 terms — one for each permutation of the 3 rows. Sarrus' rule makes those 6 terms **visually obvious** by arranging them as diagonals.

Extend the matrix rightward by repeating columns 1 and 2. You now see six diagonals: three run top-left to bottom-right (positive), three run top-right to bottom-left (negative). Read off the product of each diagonal, add the positives, subtract the negatives. Done.

It is nothing more than [[cofactor]] expansion in disguise — just presented as a pattern you can trace with a pencil.

## Mechanics

Given $A = \begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}$, extend by repeating the first two columns:

$$\begin{array}{ccccc}
a & b & c & a & b \\
d & e & f & d & e \\
g & h & i & g & h
\end{array}$$

**Positive diagonals** (↘): $aei,\; bfg,\; cdh$

**Negative diagonals** (↗): $ceg,\; afh,\; bdi$

$$\boxed{\det(A) = (aei + bfg + cdh) - (ceg + afh + bdi)}$$

| Diagonal direction | Products | Sign |
|---|---|---|
| ↘ top-left to bottom-right | $aei$, $bfg$, $cdh$ | $+$ |
| ↗ top-right to bottom-left | $ceg$, $afh$, $bdi$ | $−$ |

> **Warning**: this rule does NOT generalize to 4×4 or larger. Applying it there gives wrong answers — use [[cofactor]] expansion or [[gaussian-elimination]] instead.

```python
import numpy as np

def sarrus(A):
    a,b,c = A[0]; d,e,f = A[1]; g,h,i = A[2]
    pos = a*e*i + b*f*g + c*d*h
    neg = c*e*g + a*f*h + b*d*i
    return pos - neg

A = np.array([[1,2,3],[0,4,5],[1,0,6]], dtype=float)
print(sarrus(A))             # 22.0
print(np.linalg.det(A))      # 22.0 ✓
```


## In ML

**Hand calculation of 3×3 Jacobians** — when computing the Jacobian determinant for a 3-variable change of variables (common in probability density transformations), Sarrus' rule is the fastest pen-and-paper method.

**Covariance matrices** — for small datasets with exactly 3 features, the covariance matrix $\Sigma$ is 3×3. Checking $\det(\Sigma) = 0$ (degenerate distribution) by hand is practical with Sarrus.

**Knowing the limits** — the rule's failure above 3×3 is itself instructive: it shows why general determinant algorithms must use [[cofactor]] expansion or [[gaussian-elimination]] rather than diagonal tricks.

## Exercises

**Basic** — Use Sarrus' rule to compute $\det\begin{bmatrix}2&1&0\\1&3&1\\0&1&2\end{bmatrix}$. Verify with NumPy.

**Intermediate** — Apply Sarrus to $\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}$ and to $\begin{bmatrix}1&2&3\\1&2&3\\4&5&6\end{bmatrix}$. Explain both results geometrically using [[determinant]] intuition.

**Advanced** — Show algebraically that the Sarrus formula equals the [[cofactor]] expansion along row 1: $a(ei-fh) - b(di-fg) + c(dh-eg)$. Which of the six Sarrus terms maps to which cofactor term?
