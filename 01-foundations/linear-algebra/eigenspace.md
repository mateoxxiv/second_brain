---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[kernel-and-range]]"
  - "[[subspaces]]"
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[spectral-decomposition]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §6.1 — Teorema 1, Ejemplo 5 (eigenespacios)."
---

> **TL;DR** — The eigenspace of A for eigenvalue λ is the entire subspace of vectors that solve (λI−A)x=0 — not just one eigenvector, but every combination of them, and it can have more than one dimension when an eigenvalue repeats.

---

## Intuition

Once you've found an eigenvalue λ, there's rarely just *one* eigenvector for it — there's a whole family: any scalar multiple of an eigenvector is still an eigenvector for the same λ, and sometimes several independent directions share the same λ. That entire family, plus the zero vector, is called the **eigenspace**.

Think of it as "all the directions A treats identically for this particular stretch factor." Usually that's a line (1D). But if an eigenvalue is repeated, it can be a whole plane or more.

## Mechanics

**Definition** — the eigenspace of $A$ corresponding to eigenvalue $\lambda$ is the solution space of $(\lambda I - A)\mathbf{x} = \mathbf{0}$:

$$E_\lambda = \{\mathbf{x} \in \mathbb{R}^n : (\lambda I - A)\mathbf{x} = \mathbf{0}\} = \ker(\lambda I - A)$$

Since it's the [[kernel-and-range|kernel]] of the matrix $(\lambda I - A)$, it's automatically a [[subspaces|subspace]] — closed under addition and scaling, same as any null space.

**Worked example** (Anton Example 5) for $A = \begin{bmatrix}3&-2&0\\-2&3&0\\0&0&5\end{bmatrix}$: characteristic equation $(\lambda-1)(\lambda-5)^2=0$ → eigenvalues $\lambda=1$ and $\lambda=5$ (repeated root).

*For λ = 5*: solving $(5I-A)\mathbf{x}=\mathbf{0}$ reduces to the single equation $x_1+x_2=0$, leaving **two** free variables:
$$\mathbf{x} = s\begin{bmatrix}-1\\1\\0\end{bmatrix} + t\begin{bmatrix}0\\0\\1\end{bmatrix}$$
These two vectors are [[linear-independence|linearly independent]], so they form a **basis for a 2-dimensional eigenspace** $E_5$.

*For λ = 1*: solving $(1\cdot I-A)\mathbf{x}=\mathbf{0}$ leaves only **one** free variable: $\mathbf{x}=t[1,1,0]^T$. $E_1$ is 1-dimensional.

| Eigenvalue | Multiplicity as a root of the characteristic polynomial | dim(eigenspace) |
|---|---|---|
| λ = 1 | 1 | 1 |
| λ = 5 | 2 (repeated root) | 2 |

Here the eigenspace's dimension happens to match the root's multiplicity — that's not guaranteed in general (an eigenspace can be *smaller* than the multiplicity, but never larger), which is exactly the condition that determines whether a matrix can be diagonalized.

```python
import numpy as np
from scipy.linalg import null_space

A = np.array([[3,-2,0],[-2,3,0],[0,0,5]], dtype=float)

E5 = null_space(5*np.eye(3) - A)   # basis vectors as columns, dim = 2
E1 = null_space(1*np.eye(3) - A)   # basis vectors as columns, dim = 1

print(E5.shape[1])   # 2 — matches the hand-derived basis {[-1,1,0], [0,0,1]}
print(E1.shape[1])   # 1 — matches {[1,1,0]}
```

## In ML

**PCA with repeated variance** — if two principal directions share the exact same eigenvalue (equal variance), the covariance matrix's eigenspace for that λ is 2-dimensional — there is no single "correct" choice of the two principal axes within that plane, only a choice of *some* orthonormal basis for it. This is why PCA output can rotate arbitrarily within a subspace of tied eigenvalues.

**Diagonalizability** — a matrix can be written as $A=PDP^{-1}$ only if you can collect enough independent eigenvectors to fill $\mathbb{R}^n$; that requires every eigenspace's dimension to equal its root's multiplicity. [[spectral-decomposition]] guarantees this always works for symmetric matrices.

## Exercises

**Basic** — Find a basis for the eigenspace of $A=\begin{bmatrix}2&0\\0&2\end{bmatrix}$ corresponding to $\lambda=2$. (Notice: this eigenvalue's multiplicity is 2 — what's the dimension of the eigenspace here?)

**Intermediate** — For $A = \begin{bmatrix}4&0&0\\0&4&0\\1&0&4\end{bmatrix}$, the characteristic equation has $\lambda=4$ with multiplicity 3. Find $E_4$ by solving $(4I-A)\mathbf{x}=\mathbf{0}$ — is its dimension 3, or less? What does that tell you about diagonalizing this matrix?

**Advanced** — Prove that $E_\lambda$ is always a subspace directly from the two-condition test in [[subspaces]] (closure under addition and scalar multiplication), without invoking the kernel shortcut.
