---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[projection]]"
  - "[[vector-norms]]"
  - "[[linear-independence]]"
  - "[[special-matrices]]"
  - "[[singular-value-decomposition]]"
domain: linear-algebra
sources:
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Gram-Schmidt turns any set of independent vectors into an orthonormal set (perpendicular + unit length) by repeatedly removing projections. The result is a [[special-matrices|orthogonal matrix]] $Q$ with $Q^TQ = I$.

---

## Intuition

You have three fence posts leaning in random directions. Gram-Schmidt straightens them into three perfectly perpendicular posts, each exactly 1 unit tall. The procedure: take the first post as-is, then adjust each subsequent post to be perpendicular to all previous ones by removing their "shadow" components.

Why orthonormal bases are worth the effort:

| Operation | General basis | Orthonormal basis |
|---|---|---|
| Find coordinates | Solve a linear system | Just dot products |
| Matrix inverse | Expensive computation | Free — just transpose |
| Projection | Full formula $(A^TA)^{-1}A^T$ | Simple $Q^T$ |

## Mechanics

Given independent vectors $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$:

```
Step 1: Take v1 as-is, normalize
  u1 = v1
  q1 = u1 / ‖u1‖

Step 2: Remove v2's projection onto q1, normalize
  u2 = v2 - (v2·q1)q1
  q2 = u2 / ‖u2‖

Step 3: Remove v3's projections onto q1 and q2, normalize
  u3 = v3 - (v3·q1)q1 - (v3·q2)q2
  q3 = u3 / ‖u3‖
```

Each subtraction removes the "shadow" of the new vector onto all previous orthonormal vectors, leaving only the truly perpendicular component.

```python
import numpy as np

def gram_schmidt(V):
    Q = []
    for v in V:
        u = v.copy().astype(float)
        for q in Q:
            u -= np.dot(v, q) * q   # remove projection
        Q.append(u / np.linalg.norm(u))
    return np.array(Q).T

V = [np.array([1,1,0]), np.array([1,0,1]), np.array([0,1,1])]
Q = gram_schmidt(V)
print(np.allclose(Q.T @ Q, np.eye(3)))  # True — orthonormal ✓
```

> Runnable: [[code/foundations/matrix_operations.py]]

## In ML

**QR decomposition** — Gram-Schmidt is the conceptual basis for $A = QR$ (orthogonal × upper-triangular). Used in eigenvalue algorithms and least squares.

**[[singular-value-decomposition|SVD]]** — the $U$ and $V$ matrices in SVD are orthogonal matrices whose columns are orthonormal vectors. Gram-Schmidt is one way to understand how those orthonormal sets are constructed.

**Orthogonal weight initialization** — initializing neural network weight matrices as orthogonal matrices (via Gram-Schmidt or QR) prevents gradient vanishing/explosion because eigenvalues stay near 1.

## Exercises

**Basic** — Apply Gram-Schmidt to $\mathbf{v}_1 = [1, 0]$, $\mathbf{v}_2 = [1, 1]$. Show each step. Verify $\mathbf{q}_1\cdot\mathbf{q}_2 = 0$.

**Intermediate** — Apply Gram-Schmidt to $[1,1,0]$, $[1,0,1]$, $[0,1,1]$. Verify the result is orthonormal using $Q^TQ = I$.

**Advanced** — Gram-Schmidt can fail if at some step $\mathbf{u}_k = \mathbf{0}$. When does this happen? What does it reveal about the original set of vectors?
