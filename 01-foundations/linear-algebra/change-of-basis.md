---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[coordinate-vector]]"
  - "[[basis-and-dimension]]"
  - "[[orthogonal-matrix]]"
  - "[[orthonormal-bases]]"
  - "[[matrix-inverse]]"
  - "[[linear-transformations]]"
  - "[[diagonalization]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introduccion al Algebra Lineal. S4.10 -- Theorems 26, Examples 63-66."
---

> **TL;DR** — The transition matrix P converts coordinate vectors between bases via [v]_{B'} = P[v]_B; its columns are the old basis vectors expressed in the new basis, and its inverse reverses the change.

---

## Intuition

The same vector looks different in different coordinate systems — like the same city described by GPS coordinates versus a street address. The transition matrix is the translator: feed it coordinates in the old system, it outputs coordinates in the new system.

Building P is mechanical: express each old basis vector as a linear combination of the new basis vectors, then stack those coordinate vectors as columns. One matrix multiplication converts any vector from old to new coordinates.

## Mechanics

**Setup:** $B = \{u_1, u_2\}$ and $B' = \{u_1', u_2'\}$ are two bases for $V$. Express each old basis vector in the new basis:

$$u_1 = a\,u_1' + b\,u_2', \qquad u_2 = c\,u_1' + d\,u_2'$$

For $v = k_1 u_1 + k_2 u_2$, substituting and collecting terms gives $[v]_{B'} = \begin{bmatrix}a & c \\ b & d\end{bmatrix}\begin{bmatrix}k_1\\k_2\end{bmatrix}$.

**General formula (eq. 4.34):**

$$[\mathbf{v}]_{B'} = P\,[\mathbf{v}]_B, \qquad P = \bigl[[u_1]_{B'} \;\big|\; [u_2]_{B'} \;\big|\; \cdots \;\big|\; [u_n]_{B'}\bigr]$$

$P$ is the **transition matrix from $B$ to $B'$**. The $k$-th column = coordinates of the $k$-th *old* basis vector in the *new* basis.

**Theorem 26 (Anton S4.10):** $P$ is always invertible, and $P^{-1}$ is the transition matrix from $B'$ back to $B$:

$$[\mathbf{v}]_B = P^{-1}[\mathbf{v}]_{B'}$$

*Proof sketch:* let $Q$ be the transition from $B'$ to $B$. Applying both changes in sequence must return the original: $[v]_B = QP[v]_B$ for all $v$, which forces $QP = I$.

**Example 63:** $B$ = standard basis; $B' = \{[1,1]^T,[2,1]^T\}$. Solve to express $u_1, u_2$ in $B'$: $u_1 = -u_1' + u_2'$, $u_2 = 2u_1' - u_2'$. So:

$$P = \begin{bmatrix}-1 & 2 \\ 1 & -1\end{bmatrix}$$

For $v=[7,2]^T$: $[v]_{B'} = P[7,2]^T = [-3,5]^T$. Verify: $-3[1,1]^T + 5[2,1]^T = [7,2]^T$.

**Rotation (Example 64-65):** rotating coordinate axes by $\theta$ counterclockwise is a change of basis; the transition matrix is:

$$P_{2D} = \begin{bmatrix}\cos\theta & \sin\theta \\ -\sin\theta & \cos\theta\end{bmatrix}, \qquad P_{3D\text{(z-axis)}} = \begin{bmatrix}\cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1\end{bmatrix}$$

```python
import numpy as np

def transition_matrix(old_basis: np.ndarray, new_basis: np.ndarray) -> np.ndarray:
    """Columns of P = old basis vectors expressed in new basis coordinates."""
    return np.linalg.solve(new_basis, old_basis)

# Example 63
B_old = np.eye(2)
B_new = np.array([[1., 1.], [2., 1.]]).T   # columns = new basis vectors
P = transition_matrix(B_old, B_new)
print(P)                                    # [[-1, 2], [1, -1]]

v_B  = np.array([7., 2.])
v_Bp = P @ v_B
print(v_Bp)                                 # [-3, 5]
print(np.allclose(np.linalg.inv(P) @ v_Bp, v_B))  # True
```

## In ML

**PCA** — dimensionality reduction is a change of basis: from the standard feature basis to the eigenvectors of the covariance matrix (principal components). The transition matrix $W$ (eigenvector matrix) maps data points to principal component scores: $z = W^T x$.

**[[diagonalization|Diagonalization]]** — $A = PDP^{-1}$ expresses a matrix in the eigenvector basis where it becomes diagonal. Change of basis makes repeated application trivial: $A^k = PD^kP^{-1}$.

**RoPE (Rotary Position Embedding)** — encodes token position by applying 2D rotation matrices to pairs of query/key dimensions. Each position uses a different rotation angle — a structured, invertible change of basis.

## Exercises

**Basic** — $B = \{(1,0),(0,1)\}$ and $B' = \{(1,2),(1,3)\}$ in $\mathbb{R}^2$. Build $P$, find $[v]_{B'}$ for $v=(5,3)$, then recover $v$ using $P^{-1}$.

**Intermediate** — If $P$ is the transition from $B$ to $B'$ and $Q$ from $B'$ to $B''$, what is the transition matrix from $B$ to $B''$? Prove it.

**Advanced** — Prove Theorem 26 in full: show $P$ is invertible by constructing $Q$ (transition from $B'$ to $B$) and proving $QP = I$ by substituting $x = u_1, u_2, \ldots, u_n$ into the identity $[x]_B = QP[x]_B$.
