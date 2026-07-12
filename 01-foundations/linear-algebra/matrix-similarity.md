---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[change-of-basis]]"
  - "[[matrix-of-linear-transformation-general-spaces]]"
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[spectral-decomposition]]"
  - "[[linear-transformations]]"
  - "[[determinant]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.5 — Teorema 7, Ejemplo 35"
---

> **TL;DR** — Two square matrices A and B are **similar** if B = P⁻¹AP for some invertible P; concretely, this happens exactly when A and B represent the *same* linear operator T:V→V, just measured in two different bases.

---

## Intuition

A linear operator T doesn't care what basis you use — but its matrix *representation* does. Similarity formalizes "these two different-looking matrices are secretly the same machine, described with different labels on the dials." Changing basis never changes what T does to a vector; it only changes the numbers you write down to describe that action.

## Mechanics

**Definition (Anton §5.5)** — square matrices A, B are **similar** if there exists an invertible P such that:

$$B = P^{-1}AP$$

**It's a symmetric relation** — rewrite $B=P^{-1}AP$ as $A = PBP^{-1} = (P^{-1})^{-1}BP^{-1}$. Setting $Q=P^{-1}$ gives $A = Q^{-1}BQ$ — so "A is similar to B" and "B is similar to A" are the same fact. By convention, just say **A and B are similar**.

**Theorem 7 — where similarity comes from** — if A is T's matrix with respect to basis B, and A' is T's matrix with respect to basis B', then $A' = P^{-1}AP$, where P is the transition matrix *from B' to B*. (Derived via the commutative square $[x]_{B'} \xrightarrow{P} [x]_B \xrightarrow{A} [T(x)]_B \xrightarrow{P^{-1}} [T(x)]_{B'}$ — see [[matrix-of-linear-transformation-general-spaces]] for the coordinate-bridge machinery this builds on.) Mnemonic for the direction, since it's easy to flip: **new matrix = P⁻¹ (initial matrix) P**.

**Worked example (Example 35)** — $T(x_1,x_2) = (x_1+x_2,\ -2x_1+4x_2)$. Standard matrix (basis $B=\{e_1,e_2\}$): $A=\begin{bmatrix}1&1\\-2&4\end{bmatrix}$. Switch to $B'=\{u_1,u_2\}=\{(1,1),(1,2)\}$: since $u_1=e_1+e_2$, $u_2=e_1+2e_2$, the transition matrix from B' to B is $P=\begin{bmatrix}1&1\\1&2\end{bmatrix}$, with $P^{-1}=\begin{bmatrix}2&-1\\-1&1\end{bmatrix}$. Then:

$$P^{-1}AP = \begin{bmatrix}2&-1\\-1&1\end{bmatrix}\begin{bmatrix}1&1\\-2&4\end{bmatrix}\begin{bmatrix}1&1\\1&2\end{bmatrix} = \begin{bmatrix}2&0\\0&3\end{bmatrix}$$

The standard basis gave a "messy" matrix; $B'$ gives a **diagonal** one — same operator, dramatically simpler description. This is exactly why the standard basis is never assumed to be the best one.

| Property | Statement |
|---|---|
| Symmetric | A~B ⟺ B~A |
| Same operator | A, B similar ⟺ represent the same T in two bases |
| Basis-invariant | similar matrices share determinant, trace, eigenvalues, rank |
| Diagonalizable | A is diagonalizable exactly when it's similar to some diagonal D |

```python
import numpy as np

A = np.array([[1, 1], [-2, 4]])
P = np.array([[1, 1], [1, 2]])   # columns = new basis vectors in old coordinates

A_prime = np.linalg.inv(P) @ A @ P
print(A_prime)   # [[2, 0], [0, 3]] -- diagonal, matches Example 35

print(np.isclose(np.linalg.det(A), np.linalg.det(A_prime)))       # True
print(np.allclose(sorted(np.linalg.eigvals(A)), sorted(np.linalg.eigvals(A_prime))))  # True
```

## In ML

**Diagonalization's entire payoff** — once a matrix is similar to a diagonal D (i.e. $A=PDP^{-1}$), powers become trivial: $A^k = PD^kP^{-1}$, and $D^k$ is just each diagonal entry raised to the $k$-th power. This is the mechanism behind analyzing long-run behavior of Markov chains and the stability of repeatedly-applied weight matrices in RNNs — see [[eigenvalues-and-eigenvectors]] and [[spectral-decomposition]] for the full machinery.

**Basis-invariant quantities matter precisely because of similarity** — determinant, trace, rank, and eigenvalues are all the same for any two similar matrices. That's *why* it's meaningful to talk about "the eigenvalues of a covariance matrix" as a property of the data rather than an artifact of how features happened to be ordered — the underlying operator doesn't change even if you relabel or rotate the coordinate system.

**Reparameterization in neural nets** — permuting hidden units in a layer, or applying any invertible linear change to a layer's internal representation, produces a *different-looking* weight matrix that implements the *identical* function. Similarity is the precise statement of when two seemingly different sets of weights are secretly computing the same thing.

## Exercises

**Basic** — Verify the Example 35 computation by hand: multiply $P^{-1}AP$ step by step and confirm you get $\begin{bmatrix}2&0\\0&3\end{bmatrix}$.

**Intermediate** — For $A=\begin{bmatrix}1&1\\-2&4\end{bmatrix}$ and the same P, pick a concrete vector $x=(3,1)$. Compute $T(x)=Ax$ directly, then separately compute $[x]_{B'}$, apply $A'$, and reconstruct — confirm both routes agree, matching the [[matrix-of-linear-transformation-general-spaces]] indirect procedure.

**Advanced** — Prove that similar matrices always have the same determinant: use $\det(P^{-1}AP) = \det(P^{-1})\det(A)\det(P)$ and the fact that $\det(P^{-1})=1/\det(P)$ (see [[determinant]]). Then explain why this guarantees similar matrices also share the same characteristic polynomial (hint: $\det(A'-\lambda I) = \det(P^{-1}(A-\lambda I)P)$).
