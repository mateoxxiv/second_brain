---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[eigenvalues-and-eigenvectors]]"
  - "[[eigenspace]]"
  - "[[matrix-similarity]]"
  - "[[change-of-basis]]"
  - "[[spectral-decomposition]]"
  - "[[matrix-of-linear-transformation-general-spaces]]"
  - "[[linear-independence]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §6.2 — Definición, Teoremas 2-4, Ejemplos 7-11."
---

> **TL;DR** — A matrix is diagonalizable exactly when it has n linearly independent eigenvectors; stack them as the columns of P and $P^{-1}AP$ collapses to the diagonal matrix of eigenvalues.

---

## Intuition

A diagonal matrix is the easiest matrix to work with — each axis gets scaled independently, with no mixing between coordinates. Diagonalization asks: is there a basis (necessarily made of eigenvectors) in which *this* matrix looks diagonal? If so, in that basis the transformation really is just "stretch axis 1 by λ₁, axis 2 by λ₂, ..." — all the apparent rotation/shearing you see in the standard basis was just an artifact of describing the same simple action in the wrong coordinates.

## Mechanics

**Definition (Anton §6.2)** — a square matrix $A$ is **diagonalizable** if there exists an invertible $P$ such that $P^{-1}AP$ is diagonal; $P$ is said to **diagonalize** $A$.

**Theorem 2 — the existence criterion**: $A$ ($n\times n$) is diagonalizable ⟺ $A$ has $n$ linearly independent eigenvectors.

*(⇒)* If $A$ is diagonalizable, $P^{-1}AP=D$, so $AP = PD$. Comparing columns: the $i$-th column of $AP$ is $A\mathbf p_i$, and the $i$-th column of $PD$ is $\lambda_i \mathbf p_i$ (each column of $P$ scaled by the matching diagonal entry). So $A\mathbf p_i = \lambda_i \mathbf p_i$ for every $i$ — the columns of $P$ *are* eigenvectors. Since $P$ is invertible, its columns are nonzero and linearly independent.

*(⇐)* Given $n$ linearly independent eigenvectors $\mathbf p_1,\dots,\mathbf p_n$ with eigenvalues $\lambda_1,\dots,\lambda_n$, build $P=[\mathbf p_1 \;\cdots\; \mathbf p_n]$. Column-by-column, $AP = [\lambda_1\mathbf p_1\;\cdots\;\lambda_n\mathbf p_n] = PD$. $P$ is invertible (independent columns), so $P^{-1}AP=D$.

**Procedure**: 
1. find $n$ linearly independent eigenvectors of $A$.
2. stack them as columns of $P$.
3. $P^{-1}AP=D$, with $\lambda_i$ — the eigenvalue for column $\mathbf p_i$ — landing in the $i$-th diagonal slot. Reordering $P$'s columns just permutes $D$'s diagonal to match — there's no canonical order.

**Worked example (Ejemplo 7)** — for $$A=\begin{bmatrix}3&-2&0\\-2&3&0\\0&0&5\end{bmatrix}$$, the eigenvalues are $\lambda=1,5$ (with $\lambda=5$ repeated). The eigenspace for $\lambda=5$ turns out 2-dimensional, spanned by $\mathbf p_1=(-1,1,0)$, $\mathbf p_2=(0,0,1)$; the eigenspace for $\lambda=1$ is spanned by $\mathbf p_3=(1,1,0)$. These three are linearly independent, so $$P=\begin{bmatrix}-1&0&1\\1&0&1\\0&1&0\end{bmatrix}$$ diagonalizes $A$, giving $D=\text{diag}(5,5,1)$.

**Theorem 3 + 4 — a shortcut** — eigenvectors corresponding to *distinct* eigenvalues are automatically linearly independent (Theorem 3). So if an $n\times n$ matrix has $n$ **distinct** eigenvalues, Theorem 2 is satisfied for free: it's diagonalizable, with no need to check eigenspace dimensions at all (Theorem 4). *Proof of Thm 4*: distinct eigenvalues $\Rightarrow$ (Thm 3) their eigenvectors $\mathbf v_1,\dots,\mathbf v_n$ are linearly independent $\Rightarrow$ (Thm 2) $A$ is diagonalizable. **Ejemplo 10** — $$A=\begin{bmatrix}2&1&0\\3&2&0\\0&0&4\end{bmatrix}$$ has eigenvalues $4,\ 2+\sqrt3,\ 2-\sqrt3$ — three distinct values, so $A$ is diagonalizable immediately, without ever computing an eigenvector.

**When it fails** — for $$A=\begin{bmatrix}-3&2\\-2&1\end{bmatrix}$$, the characteristic equation is $(\lambda+1)^2=0$: a single eigenvalue $\lambda=-1$ with multiplicity 2. Solving $(-I-A)\mathbf x=\mathbf 0$ gives $x_1=x_2=t$ — the eigenspace is only **1-dimensional**. With multiplicity 2 but only 1 independent eigenvector, $A$ cannot reach $n=2$ independent eigenvectors, so it is **not diagonalizable**. This is exactly the geometric-vs-algebraic-multiplicity gap from [[eigenspace]].

**The converse of Theorem 4 is false (Ejemplo 11)** — repeated eigenvalues don't automatically doom diagonalizability either. $$A=\begin{bmatrix}3&0\\0&3\end{bmatrix}$$ has the repeated-root characteristic equation $(\lambda-3)^2=0$, yet $A$ is trivially diagonal already ($P=I$ works). Distinct eigenvalues are a convenient **sufficient** test, never a necessary one — Theorem 2's eigenspace-dimension check is the only condition that's both.

**Geometric meaning (Ejemplo 9)** — diagonalizing $A$ is the same problem as finding a basis for $\mathbb R^n$ with respect to which a linear operator $T$'s matrix is diagonal: if $A$ is $T$'s standard matrix, the diagonalizing $P$ *is* the transition matrix from the eigenvector basis to the standard basis. This is [[matrix-similarity]]'s Theorem 7 specialized to the case where the "new" matrix is diagonal — see also [[change-of-basis]].

| Property | Formula | Why it matters |
|---|---|---|
| Diagonalizable | $P^{-1}AP=D$ | basis change turning $A$ into pure independent scaling |
| Existence test | $n$ linearly independent eigenvectors | Theorem 2 — equivalent condition |
| Matrix powers | $A^k = PD^kP^{-1}$ | $D^k$ is trivial: each diagonal entry raised to $k$ |
| Column order | reordering $P$'s columns permutes $D$ to match | no canonical order for $P$ or $D$ |
| Failure mode | eigenspace dim < eigenvalue's multiplicity | not enough independent eigenvectors to fill $P$ |
| Distinct-eigenvalue shortcut | $n$ distinct eigenvalues $\Rightarrow$ diagonalizable | sufficient (Thm 4), not necessary — converse is false |

```python
import numpy as np

A = np.array([[3, -2, 0], [-2, 3, 0], [0, 0, 5]], dtype=float)
P = np.array([[-1, 0, 1], [1, 0, 1], [0, 1, 0]], dtype=float)

D = np.linalg.inv(P) @ A @ P
print(np.round(D, 6))            # diag(5, 5, 1)

# powers become trivial once diagonalized
A_cubed = P @ np.diag(np.diag(D) ** 3) @ np.linalg.inv(P)
print(np.allclose(A_cubed, np.linalg.matrix_power(A, 3)))  # True
```

## In ML

**Cheap matrix powers** — $A^k = PD^kP^{-1}$ turns an expensive repeated matrix multiplication into one cheap elementwise power on the diagonal. This is exactly how long-run behavior of Markov transition matrices and the stability of repeatedly-applied recurrent weight matrices (RNNs) gets analyzed — instead of multiplying $A$ by itself $k$ times, diagonalize once and raise scalars to powers.

**Not every matrix cooperates** — real, non-symmetric matrices can fail to diagonalize (the counterexample above), which is why general-purpose numerical libraries fall back to the Jordan normal form or Schur decomposition when eigenvectors run short. [[spectral-decomposition]] sidesteps this entirely: every **symmetric** matrix (e.g. a covariance matrix) is guaranteed diagonalizable with an *orthogonal* $P$ — no defective cases to worry about.

**PCA is diagonalization in disguise** — computing principal components diagonalizes the covariance matrix, $C = Q\Lambda Q^T$; the eigenvectors in $Q$ are exactly the diagonalizing basis, and $\Lambda$'s diagonal entries (the eigenvalues) are the variances along each new axis.

## Exercises

**Basic** — Diagonalize $A=\begin{bmatrix}4&1\\2&3\end{bmatrix}$: find its eigenvalues/eigenvectors, build $P$, and verify $P^{-1}AP$ is diagonal.

**Intermediate** — For the Ejemplo 7 matrix above, reorder $P$'s columns as $(\mathbf p_3, \mathbf p_1, \mathbf p_2)$ and predict the resulting $D$ before computing it — confirm the permutation rule.

**Advanced** — The Observación following Theorem 3 (Anton §6.2) states that combining a linearly independent set from *each* distinct eigenspace still yields one overall linearly independent set. Use this to explain why checking "eigenspace dimension = multiplicity" **separately for every distinct eigenvalue** is exactly equivalent to Theorem 2's global "$n$ independent eigenvectors" test — i.e., why you never need to check independence *across* eigenspaces, only *within* each one.
