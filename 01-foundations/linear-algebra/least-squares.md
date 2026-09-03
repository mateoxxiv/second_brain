---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[projection-onto-subspaces]]"
  - "[[row-and-column-spaces]]"
  - "[[matrix-inverse]]"
  - "[[gram-schmidt]]"
  - "[[rank-nullity-theorem]]"
  - "[[singular-value-decomposition]]"
  - "[[linear-regression]]"
  - "[[platzi-algebra-lineal]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §7.8 (Least Squares)."
  - "Strang, Gilbert. Linear Algebra and Its Applications, §4.3 — the normal equations."
  - "Platzi — Álgebra Lineal, Clase 22 (intuition companion: mínimos cuadrados)."
---

> **TL;DR** — When $A\mathbf{x}=\mathbf{b}$ has **no exact solution** (more equations than unknowns), least squares finds the $\hat{\mathbf{x}}$ that makes $A\hat{\mathbf{x}}$ as close to $\mathbf{b}$ as possible — by solving the **normal equations** $A^\top A\hat{\mathbf{x}}=A^\top\mathbf{b}$.

---

## Intuition

You have 100 noisy data points but only 2 unknowns (a slope and an intercept). That's an **overdetermined** system: 100 equations, 2 unknowns. No single line passes through all 100 points, so $A\mathbf{x}=\mathbf{b}$ is *inconsistent* — $\mathbf{b}$ simply doesn't live in the [[row-and-column-spaces|column space]] of $A$. Demanding an exact solution is hopeless; the honest question becomes *"which $\hat{\mathbf{x}}$ gets us closest?"* Least squares answers it by minimizing the squared length of the **residual** $\mathbf{e}=\mathbf{b}-A\mathbf{x}$. Geometrically, the closest reachable point $A\hat{\mathbf{x}}$ is the [[projection-onto-subspaces|projection]] of $\mathbf{b}$ onto $\text{col}(A)$, and the leftover residual points straight out of that subspace.

## Mechanics

**The problem.** Minimize the squared error over all $\mathbf{x}$:
$$\hat{\mathbf{x}} = \arg\min_{\mathbf{x}} \;\|A\mathbf{x}-\mathbf{b}\|^2$$

**Two derivations of the same result:**

*Geometric* — the residual must be orthogonal to every column of $A$ (else you could shrink it). So $A^\top(\mathbf{b}-A\hat{\mathbf{x}})=\mathbf{0}$, which rearranges to the **normal equations**:
$$\boxed{A^\top A\,\hat{\mathbf{x}} = A^\top\mathbf{b}} \quad\Longrightarrow\quad \hat{\mathbf{x}} = (A^\top A)^{-1}A^\top\mathbf{b}$$

*Calculus* — expand $f(\mathbf{x})=\|A\mathbf{x}-\mathbf{b}\|^2 = \mathbf{x}^\top A^\top A\mathbf{x} - 2\mathbf{x}^\top A^\top\mathbf{b} + \mathbf{b}^\top\mathbf{b}$. Set the gradient to zero: $\nabla f = 2A^\top A\mathbf{x} - 2A^\top\mathbf{b} = \mathbf{0}$ — the *identical* normal equations. (It's a true minimum because $A^\top A$ is positive semidefinite, so $f$ is convex.)

Why this $\hat{\mathbf{x}}$ is provably the *closest* point — not just a critical point — is the Best Approximation Theorem, proved in [[projection-onto-subspaces]].

| Object | Formula | Meaning |
|--------|---------|---------|
| Normal equations | $A^\top A\hat{\mathbf{x}}=A^\top\mathbf{b}$ | square $n\times n$ system, always consistent |
| Solution | $\hat{\mathbf{x}}=(A^\top A)^{-1}A^\top\mathbf{b}$ | needs $A$ full column rank |
| Fitted values | $\mathbf{p}=A\hat{\mathbf{x}}$ | projection of $\mathbf{b}$ onto $\text{col}(A)$ |
| Residual | $\mathbf{e}=\mathbf{b}-\mathbf{p}$ | $\perp \text{col}(A)$ |

```python
import numpy as np
A = np.array([[1,1],[1,2],[1,3]], dtype=float)   # fit y = c + m·x
b = np.array([1., 2., 2.])
x_hat = np.linalg.solve(A.T @ A, A.T @ b)         # normal equations
# np.linalg.lstsq(A, b) does this more stably (via SVD)
```

**When $A^\top A$ is singular** — if the columns of $A$ are dependent (rank-deficient), $A^\top A$ can't be inverted and $\hat{\mathbf{x}}$ isn't unique. Fixes: the **[[singular-value-decomposition|SVD]]** pseudoinverse $A^+$ (picks the minimum-norm solution), or **ridge** $\hat{\mathbf{x}}=(A^\top A+\lambda I)^{-1}A^\top\mathbf{b}$, which restores invertibility. Forming $A^\top A$ also squares the [[rank-nullity-theorem|conditioning]], so production solvers use QR ([[gram-schmidt]]) or SVD instead of the normal equations directly.

## In ML

**It *is* linear regression.** Ordinary least squares fits $\mathbf{y}=X\mathbf{w}$ with exactly $\hat{\mathbf{w}}=(X^\top X)^{-1}X^\top\mathbf{y}$ — see [[linear-regression]]. Every closed-form OLS result is this note applied to a data matrix.

**Squared error is a choice, not a law.** Minimizing $\ell_2$ residuals is what makes the algebra linear and gives a closed form; it also assumes Gaussian noise (least squares = maximum likelihood under it). Swap to $\ell_1$ (LAD) and you gain outlier robustness but lose the clean normal equations.

**Regularization plugs directly in.** Ridge's $+\lambda I$ is the same term that rescues a singular $A^\top A$ — the numerical fix and the statistical fix (shrinking variance) are the *same* operation.

## Exercises

**Basic** — Fit a horizontal line $y=c$ to points $y=1,2,6$ (so $A=[1,1,1]^\top$). Solve the normal equations and confirm $\hat{c}$ is just the mean. Why does least squares reduce to the average here?

**Intermediate** — Derive the normal equations two ways for $A=\begin{psmallmatrix}1&1\\1&2\\1&3\end{psmallmatrix}$, $\mathbf{b}=(1,2,2)$: once by setting the residual $\perp$ the columns, once by $\nabla\|A\mathbf{x}-\mathbf{b}\|^2=0$. Confirm they match.

**Advanced** — Show $A^\top A$ is invertible **iff** $A$ has independent columns. (Hint: suppose $A^\top A\mathbf{v}=\mathbf{0}$; left-multiply by $\mathbf{v}^\top$ to conclude $A\mathbf{v}=\mathbf{0}$.) What does this say about why duplicate/collinear features break OLS?
