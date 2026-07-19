---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[matrix-operations]]"
  - "[[determinant]]"
  - "[[matrix-inverse]]"
  - "[[special-matrices]]"
  - "[[spectral-decomposition]]"
  - "[[singular-value-decomposition]]"
  - "[[complex-eigenvalues]]"
  - "[[eigenspace]]"
  - "[[synthetic-division]]"
  - "[[block-diagonal-matrices]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §6.1 — Definición, Ejemplos 1-4, Ecuación característica."
  - "https://www.youtube.com/watch?v=PFDu9oVAE-g"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Eigenvectors are special directions a matrix only stretches or shrinks (never rotates). The eigenvalue is the stretch factor. They reveal the "natural axes" of any transformation.

---

## Intuition

Most vectors get rotated AND scaled by a matrix. Eigenvectors are the exceptions — they only get scaled. The matrix can only say "go 3× further in this direction" or "flip and go 2× further," never "turn left."

```
A @ [1, 1] = [3, 3] = 3 * [1,1]  ← only stretched (λ=3)
A @ [1,-1] = [1,-1] = 1 * [1,-1] ← unchanged (λ=1)
```

These are the "natural axes" of $A$. Along these directions, the whole transformation collapses to simple scalar multiplication. Three geometric cases for the eigenvalue λ (Anton Fig. 6.1):

| λ range | Effect on the eigenvector |
|---|---|
| λ > 1 | **Dilation** — stretched further out |
| 0 < λ < 1 | **Contraction** — shrunk toward the origin |
| λ < 0 | **Inversion** — flipped to point the opposite way (and scaled by \|λ\|) |

## Mechanics

**Definition** — for an $n \times n$ matrix $A$, a nonzero vector $\mathbf{x} \in \mathbb{R}^n$ is an **eigenvector** of $A$ if $A\mathbf{x}$ is a scalar multiple of $\mathbf{x}$:

$$A\mathbf{x} = \lambda\mathbf{x}$$

$\lambda$ is the corresponding **eigenvalue**. ("Eigen" is German for "own/characteristic" — hence the older names *valores propios*, *valores característicos*, or *raíces latentes*.)

**Where the characteristic equation comes from** — rewrite $A\mathbf{x} = \lambda\mathbf{x}$ as $A\mathbf{x} = \lambda I\mathbf{x}$, then move everything to one side:

$$(\lambda I - A)\mathbf{x} = \mathbf{0}$$

For $\lambda$ to be an eigenvalue, this equation needs a **nonzero** solution $\mathbf{x}$ (the definition explicitly excludes $\mathbf{x}=\mathbf{0}$). By the invertibility equivalence theorem ([[matrix-inverse|Theorem 13]]), a homogeneous system $(\lambda I - A)\mathbf{x}=\mathbf{0}$ has a nontrivial solution *only when* $(\lambda I - A)$ is **not invertible** — i.e. when its determinant is zero:

$$\det(\lambda I - A) = 0 \qquad \text{(the characteristic equation)}$$

This is the same equation as $\det(A-\lambda I)=0$ up to an overall sign — expanding either one gives the same roots.

**To find eigenvalues:** solve the characteristic equation $\det(\lambda I - A) = 0$.

**To find eigenvectors:** for each $\lambda$, solve $(\lambda I - A)\mathbf{v} = \mathbf{0}$ (equivalently $(A-\lambda I)\mathbf v = \mathbf 0$).

**Worked example** for $A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$:

$$\det\begin{bmatrix}2-\lambda & 1\\1 & 2-\lambda\end{bmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-1)(\lambda-3) = 0$$

$\lambda_1 = 1$: $(A-I)\mathbf{v}=\mathbf{0}$ → $\mathbf{v}_1 = [1,-1]$
$\lambda_2 = 3$: $(A-3I)\mathbf{v}=\mathbf{0}$ → $\mathbf{v}_2 = [1,1]$

**Beyond 2×2 — factoring a higher-degree characteristic polynomial** (Anton Example 4): for $A = \begin{bmatrix}0&1&0\\0&0&1\\4&-17&8\end{bmatrix}$, the characteristic equation is the cubic $\lambda^3 - 8\lambda^2+17\lambda-4=0$. With integer coefficients, the **rational root theorem** says any integer root must divide the constant term (here, divisors of $-4$: $\pm1,\pm2,\pm4$). Testing them finds $\lambda=4$ works, so $(\lambda-4)$ is a factor; dividing it out leaves $\lambda^2-4\lambda+1=0$, solved by the quadratic formula: $\lambda = 2\pm\sqrt3$. Full spectrum: $\lambda = 4,\ 2+\sqrt3,\ 2-\sqrt3$. (In practice, matrices this large are handled with iterative numerical methods, not hand factoring.)

**Faster division once a root is found** — full polynomial long division works but is slow to write out by hand; [[synthetic-division]] does the same computation using only a compact row of coefficients, and its last number doubles as a fast way to *test* rational-root candidates (via the Remainder Theorem) before you even commit to dividing.

**Larger matrices with structure** — if the matrix is [[block-diagonal-matrices|block diagonal or block triangular]], skip the characteristic polynomial of the whole matrix entirely: solve each smaller diagonal block's own characteristic equation instead, and combine the results — the full spectrum is just the union of each block's eigenvalues.

**Not every real matrix has real eigenvalues** — see [[complex-eigenvalues]] for the case where the characteristic equation has no real roots.

**Theorem 1 (Anton §6.1) — equivalent ways to say "λ is an eigenvalue of A":**
- (a) λ is an eigenvalue of A.
- (b) The system $(\lambda I - A)\mathbf{x} = \mathbf{0}$ has nontrivial solutions.
- (c) There exists a nonzero $\mathbf{x} \in \mathbb{R}^n$ such that $A\mathbf{x}=\lambda\mathbf{x}$.
- (d) λ is a real solution of the characteristic equation $\det(\lambda I - A) = 0$.

This is the same logical chain as the derivation above, just packaged as a standalone theorem — and (b) is exactly what makes the solution set of $(\lambda I - A)\mathbf{x}=\mathbf{0}$ worth naming on its own: see [[eigenspace]].

```python
import numpy as np

A = np.array([[2, 1], [1, 2]], dtype=float)
eigenvalues, eigenvectors = np.linalg.eig(A)

print(eigenvalues)    # [1. 3.]
print(eigenvectors)   # columns = eigenvectors

# Verify: A @ v = lambda * v
v = eigenvectors[:, 1]   # second eigenvector
print(np.allclose(A @ v, eigenvalues[1] * v))  # True
```


## In ML

**PCA** — the covariance matrix is symmetric, so its eigenvectors are orthogonal. Each eigenvector is a principal component; each eigenvalue is the variance along that component. PCA sorts components by eigenvalue (largest first).

**Stability of gradient descent** — the eigenvalues of the Hessian $H$ determine how fast training converges. The largest eigenvalue sets the maximum safe learning rate: $\alpha < \frac{2}{\lambda_\text{max}}$.

**[[spectral-decomposition]]** — for symmetric matrices, $A = Q\Lambda Q^T$ where $Q$ packs eigenvectors and $\Lambda$ holds eigenvalues on the diagonal. Matrix powers become trivial: $A^k = Q\Lambda^k Q^T$.

## Exercises

**Basic** — Find the eigenvalues of $\begin{bmatrix}4&1\\2&3\end{bmatrix}$ using the characteristic equation. Then find one eigenvector.

**Intermediate** — For $A = \begin{bmatrix}3&1\\0&2\end{bmatrix}$, find all eigenvalues and eigenvectors by hand. Verify with NumPy.

**Advanced** — A matrix has eigenvalue $\lambda = 0$. What does this mean for (1) invertibility, (2) the null space, and (3) the determinant? Connect all three.
