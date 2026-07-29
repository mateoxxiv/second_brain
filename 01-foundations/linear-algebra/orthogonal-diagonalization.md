---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[diagonalization]]"
  - "[[orthogonal-matrix]]"
  - "[[gram-schmidt]]"
  - "[[spectral-decomposition]]"
  - "[[special-matrices]]"
  - "[[eigenspace]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §6.3 — Definición, Teoremas 5-8, Ejemplos 12-14."
---

> **TL;DR** — A matrix can be diagonalized with an *orthogonal* P exactly when it's symmetric — and symmetric matrices are the one case where diagonalization is always guaranteed to work.

---

## Intuition

[[diagonalization]] asks "can I find *some* invertible P that diagonalizes A?" This note asks a stricter question: can P be **orthogonal** — a pure rotation/reflection, with the free inverse $P^{-1}=P^T$? That's strictly more useful (no matrix inversion needed to undo P), but it's not always possible. The remarkable fact: it's possible *exactly* when A is symmetric — and for symmetric matrices, it's **never blocked** by the failure modes that break ordinary diagonalization (deficient eigenspaces, complex eigenvalues).

## Mechanics

**Definition** — $A$ is **orthogonally diagonalizable** if there's an orthogonal $P$ such that $P^{-1}AP\, (=P^TAP)$ is diagonal; $P$ **orthogonally diagonalizes** $A$.

**Theorem 5**: $A$ ($n\times n$) is orthogonally diagonalizable ⟺ $A$ has an orthonormal set of $n$ eigenvectors. This is just [[diagonalization|Theorem 2]] combined with [[orthogonal-matrix|Theorem 28]]'s fact that a matrix is orthogonal exactly when its columns are orthonormal — build $P$ from orthonormal eigenvectors and it's automatically both the diagonalizing matrix *and* orthogonal.

**Why this forces symmetry** — if $P^{-1}AP=D$ with $P$ orthogonal, then $A=PDP^{-1}=PDP^T$. Transpose both sides: $A^T=(PDP^T)^T=PD^TP^T=PDP^T=A$ (since $D$ is diagonal, $D^T=D$). So $A^T=A$: **orthogonally diagonalizable matrices are always symmetric**.

**Theorem 6**: $A$ is orthogonally diagonalizable ⟺ $A$ is symmetric. (The converse — that every symmetric matrix *can* be orthogonally diagonalized — is the harder direction; Anton omits the proof.)

**Theorem 7** — the shortcut that makes building $P$ easy: for a symmetric $A$, eigenvectors from **different** eigenspaces are automatically orthogonal. No work required there — orthogonality *within* a repeated eigenspace is the only thing left to arrange, via [[gram-schmidt]].

**Procedure**: (1) find a basis for each eigenspace of $A$; (2) apply Gram-Schmidt to each basis individually, producing an orthonormal basis *for that eigenspace*; (3) stack all these vectors as columns of $P$. Since Theorem 7 already guarantees orthogonality *across* eigenspaces, and Gram-Schmidt guarantees orthonormality *within* each one, the combined set is fully orthonormal — $P$ is orthogonal and diagonalizes $A$.

**Theorem 8 — the guarantee** (why symmetric matrices never fail to diagonalize): for a symmetric $A$, (a) the characteristic equation has **only real roots** — no complex eigenvalues, ever; (b) if $\lambda$ repeats $k$ times as a root, its eigenspace has **exactly $k$ dimensions** — geometric multiplicity always equals algebraic multiplicity. Both failure modes from [[diagonalization]] (complex spectrum, deficient eigenspace) are structurally impossible for symmetric matrices.

**Worked example (Ejemplo 13)** — for $A=\begin{bmatrix}4&2&2\\2&4&2\\2&2&4\end{bmatrix}$, the characteristic equation is $(\lambda-2)^2(\lambda-8)=0$. The eigenspace for $\lambda=2$ has basis $\mathbf u_1=(-1,1,0)$, $\mathbf u_2=(-1,0,1)$; Gram-Schmidt orthonormalizes these to $\mathbf v_1=(-\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2},0)$, $\mathbf v_2=(-\tfrac{1}{\sqrt6},-\tfrac{1}{\sqrt6},\tfrac{2}{\sqrt6})$. The eigenspace for $\lambda=8$ gives $\mathbf u_3=(1,1,1)$, normalized to $\mathbf v_3=(\tfrac{1}{\sqrt3},\tfrac{1}{\sqrt3},\tfrac{1}{\sqrt3})$. $P=[\mathbf v_1\ \mathbf v_2\ \mathbf v_3]$ orthogonally diagonalizes $A$ to $\text{diag}(2,2,8)$.

| Property | Statement | Why it matters |
|---|---|---|
| Definition | $\exists$ orthogonal $P$: $P^TAP=D$ | free inverse — $P^{-1}=P^T$ |
| Existence (Thm 5) | orthonormal set of $n$ eigenvectors | direct upgrade of [[diagonalization\|Theorem 2]] |
| Characterization (Thm 6) | orthogonally diagonalizable ⟺ symmetric | one easy property to check: $A=A^T$ |
| Cross-eigenspace orthogonality (Thm 7) | eigenvectors of different eigenspaces are orthogonal for free | only Gram-Schmidt *within* each eigenspace is needed |
| Guarantee (Thm 8) | real roots only + geometric = algebraic multiplicity, always | symmetric matrices can never be defective |

```python
import numpy as np

A = np.array([[4, 2, 2], [2, 4, 2], [2, 2, 4]], dtype=float)

# eigh is the symmetric-specific solver: exploits Theorem 8 to
# guarantee real eigenvalues and return orthonormal eigenvectors directly
eigenvalues, P = np.linalg.eigh(A)
print(eigenvalues)                       # [2. 2. 8.]
print(np.allclose(P.T @ P, np.eye(3)))   # True — P is orthogonal
print(np.allclose(P.T @ A @ P, np.diag(eigenvalues)))  # True
```

## In ML

**PCA is only clean because covariance matrices are symmetric** — Theorem 6 guarantees the covariance matrix is *always* orthogonally diagonalizable, and Theorem 8 guarantees that guarantee never breaks, no matter how many variances tie (repeated eigenvalues). This is exactly why PCA never hits the "defective matrix" edge case that plagues general eigendecomposition.

**`eigh` vs `eig`** — numerical libraries expose a dedicated symmetric solver (`np.linalg.eigh`) precisely because Theorem 8's real-root guarantee lets it skip the numerically unstable machinery general `eig` needs — the kind of instability that produces spurious tiny complex components on a repeated real eigenvalue (see [[eigenspace]] for that failure mode on non-symmetric matrices).

**[[spectral-decomposition]]** — $A=Q\Lambda Q^T$ *is* orthogonal diagonalization, just renamed for the symmetric-matrix context; this note supplies the "why it's always possible" that spectral decomposition takes for granted.

## Exercises

**Basic** — Redo the Gram-Schmidt step from Ejemplo 13 by hand: starting from $\mathbf u_1=(-1,1,0)$, $\mathbf u_2=(-1,0,1)$, derive $\mathbf v_1$ and $\mathbf v_2$ and verify $\mathbf v_1 \cdot \mathbf v_2 = 0$.

**Intermediate** — Anton's Ejemplo 14 gives a symmetric $5\times5$ matrix with characteristic equation $(\lambda-4)^2(\lambda-1)^2(\lambda-2)=0$. Without solving any eigenvector equation, use Theorem 8 to state the dimension of each of the three eigenspaces.

**Advanced** — Earlier you found a non-symmetric matrix whose repeated real eigenvalue produced tiny spurious complex components under `np.linalg.eig`, and a deficient eigenspace by hand. Using Theorem 8, explain precisely why a **symmetric** matrix could never produce either symptom — which specific clause of Theorem 8 rules out each failure mode?
