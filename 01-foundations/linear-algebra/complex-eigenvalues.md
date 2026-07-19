---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[determinant]]"
  - "[[general-vector-spaces]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §6.1 — Ejemplo 3, nota al pie sobre escalares complejos."
---

> **TL;DR** — Some real matrices have a characteristic equation with no real roots — those matrices have no real eigenvalues at all, only complex ones.

---

## Intuition

The [[eigenvalues-and-eigenvectors|characteristic equation]] $\det(\lambda I - A) = 0$ is just a polynomial in $\lambda$. Polynomials don't always have real roots — think of $\lambda^2+1=0$, which has no real solution because no real number squares to $-1$.

Geometrically, this happens when a matrix's only effect on the plane is a **pure rotation** with no stretching axis at all — there's no direction that comes back out as a scalar multiple of itself, because every vector gets turned. Since eigenvectors are defined as directions that *don't* turn, a pure-rotation-like matrix simply has none among real vectors.

## Mechanics

**Worked example** (Anton Example 3) for $A = \begin{bmatrix}-2&-1\\5&2\end{bmatrix}$:

$$\det(\lambda I - A) = \det\begin{bmatrix}\lambda+2 & 1\\-5 & \lambda-2\end{bmatrix} = \lambda^2+1$$

Setting $\lambda^2+1=0$ gives $\lambda^2=-1$, whose only solutions are the imaginary numbers $\lambda = i$ and $\lambda=-i$. **No real eigenvalues exist for this matrix.**

| Case | What happens |
|---|---|
| Characteristic polynomial has $n$ real roots | $A$ has $n$ real eigenvalues (with multiplicity) |
| Some roots are complex | Those eigenvalues (and their eigenvectors) only exist over $\mathbb{C}^n$, not $\mathbb{R}^n$ |
| Working in a real-scalars-only text/library | Complex roots are simply reported as "no eigenvalue" — the matrix is treated as having none in that context |

Complex roots of a real polynomial always come in **conjugate pairs** ($a+bi$ and $a-bi$) — that's why $\lambda=i$ came paired with $\lambda=-i$ above, and never alone.

```python
import numpy as np

A = np.array([[-2, -1],
              [ 5,  2]], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)   # [0.+1.j 0.-1.j] — a conjugate pair, no real part surviving
```

## In ML

**Recurrent neural networks** — the weight matrix's eigenvalues determine long-term dynamics. Complex eigenvalues with modulus close to 1 produce oscillatory (rotating) hidden states rather than pure growth/decay — this is part of why vanishing/exploding gradients analysis in RNNs looks at $|\lambda|$ (modulus), not just sign.

**Discrete dynamical systems** — iterating $x_{t+1} = Ax_t$ with complex eigenvalues produces spiraling trajectories (rotation combined with growth or decay set by $|\lambda|$), unlike the straight-line convergence you get from real eigenvalues.

**Symmetric matrices are safe** — [[spectral-decomposition]] guarantees real eigenvalues for symmetric $A$ (covariance matrices, Hessians). Complex eigenvalues only arise for non-symmetric matrices, which is one more reason PCA and Gaussian covariance math never has to worry about this case.

## Exercises

**Basic** — Verify by hand that $A = \begin{bmatrix}0&-1\\1&0\end{bmatrix}$ (a 90° rotation matrix) has characteristic equation $\lambda^2+1=0$. What does the geometric meaning of "rotation" tell you about why no real eigenvector could possibly exist?

**Intermediate** — For $A=\begin{bmatrix}1&-1\\1&1\end{bmatrix}$, find the characteristic equation and its complex roots. Compute $|\lambda|$ (the modulus) — what does it predict about whether $A^k \mathbf{x}$ grows, shrinks, or stays bounded as $k\to\infty$?

**Advanced** — Prove that complex roots of a real-coefficient polynomial always come in conjugate pairs. (Hint: if $p(\lambda)$ has only real coefficients and $p(a+bi)=0$, apply complex conjugation to the whole equation.)
