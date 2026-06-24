---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[projection]]"
  - "[[orthonormal-bases]]"
  - "[[inner-product-spaces]]"
  - "[[angles-and-orthogonality]]"
  - "[[gram-schmidt]]"
  - "[[matrix-inverse]]"
  - "[[linear-independence]]"
  - "[[basis-and-dimension]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.9 — Theorems 22, 23."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Project a vector onto a subspace by finding the closest point in that space. The error (residual) is always perpendicular to the subspace — and the projection is provably the unique closest point (Best Approximation Theorem).

---

## Intuition

Drop a ball above a table. Where it lands is the projection onto the table. The string from the ball to its shadow is perpendicular to the table — and it's the shortest possible string. Any other point on the table is farther from the ball.

This is not just geometric intuition: it is a theorem. Least squares regression does exactly this — your target **b** doesn't live in the column space of X (data is noisy), so you find the closest point in that space. The residuals are the perpendicular strings.

## Mechanics

**Matrix formula** — given matrix A (independent columns) and target **b**, the projection onto col(A) is:

$$\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}, \qquad \mathbf{p} = A\hat{\mathbf{x}} = A(A^TA)^{-1}A^T\mathbf{b}$$

The **projection matrix** $P = A(A^TA)^{-1}A^T$ satisfies $P^2 = P$ (project twice = same result) and $P^T = P$ (symmetric).

*Why?* The residual $\mathbf{e} = \mathbf{b} - A\hat{\mathbf{x}}$ must be perpendicular to every column of A: $A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}$, which gives the formula above.

**Orthonormal shortcut** — if A = Q (orthonormal columns), then $Q^TQ = I$ and the formula collapses to $P = QQ^T$ (no system to solve).

```python
import numpy as np

A = np.array([[1,0],[0,1],[1,1]], dtype=float)  # 3D, 2 columns
b = np.array([1., 2., 3.])

x_hat = np.linalg.solve(A.T @ A, A.T @ b)
p = A @ x_hat          # projection onto col(A)
e = b - p              # residual

print(A.T @ e)         # ≈ [0, 0] — residual ⊥ columns ✓
```


---

**Theorem 22 (Anton §4.9) — Projection Theorem (uniqueness).** If W is a finite-dimensional subspace of an [[inner-product-spaces|inner product space]] V, then every **u** ∈ V can be expressed *uniquely* as:

$$\mathbf{u} = \mathbf{w}_1 + \mathbf{w}_2, \quad \mathbf{w}_1 \in W,\quad \mathbf{w}_2 \perp W$$

*Existence*: by [[gram-schmidt|Gram-Schmidt]] (Theorem 21), W has an [[orthonormal-bases|orthonormal basis]] {v₁,...,vᵣ}. Set $\mathbf{w}_1 = \text{proj}_W\mathbf{u}$ and $\mathbf{w}_2 = \mathbf{u} - \mathbf{w}_1$ (Theorem 20).

*Uniqueness*: suppose $\mathbf{u} = \mathbf{w}_1' + \mathbf{w}_2'$ is another such decomposition. Subtracting:

$$\mathbf{0} = (\mathbf{w}_1' - \mathbf{w}_1) + (\mathbf{w}_2' - \mathbf{w}_2) \implies \mathbf{w}_1' - \mathbf{w}_1 = \mathbf{w}_2' - \mathbf{w}_2$$

Call this vector $\boldsymbol{\Delta}$. The left side shows $\boldsymbol{\Delta} \in W$ (W is a subspace). The right side shows $\boldsymbol{\Delta} \perp W$: for any $\mathbf{x} \in W$, $\langle \mathbf{x}, \boldsymbol{\Delta}\rangle = \langle\mathbf{x},\mathbf{w}_2'\rangle - \langle\mathbf{x},\mathbf{w}_2\rangle = 0 - 0 = 0$.

So $\boldsymbol{\Delta}$ is orthogonal to itself: $\langle\boldsymbol{\Delta},\boldsymbol{\Delta}\rangle = 0$. By axiom 4 (positivity), $\boldsymbol{\Delta} = \mathbf{0}$. Therefore $\mathbf{w}_1' = \mathbf{w}_1$ and $\mathbf{w}_2' = \mathbf{w}_2$. $\blacksquare$

**Distance from a vector to a subspace** — the distance from **u** to W is:

$$d(\mathbf{u}, W) = \|\mathbf{u} - \text{proj}_W\mathbf{u}\| = \|\mathbf{w}_2\|$$

This is the length of the perpendicular dropped from **u** onto W. Among all points in W, $\text{proj}_W\mathbf{u}$ is the foot of that perpendicular — and Theorem 23 proves it is the *closest* point.

**Theorem 23 (Anton §4.9) — Best Approximation Theorem.** If W is a finite-dimensional subspace of V, then for every **u** ∈ V:

$$\|\mathbf{u} - \text{proj}_W\mathbf{u}\| < \|\mathbf{u} - \mathbf{w}\| \quad \text{for all } \mathbf{w} \in W,\; \mathbf{w} \neq \text{proj}_W\mathbf{u}$$

*Proof*: For any $\mathbf{w} \in W$, decompose the error:

$$\mathbf{u} - \mathbf{w} = \underbrace{(\mathbf{u} - \text{proj}_W\mathbf{u})}_{\perp\, W} + \underbrace{(\text{proj}_W\mathbf{u} - \mathbf{w})}_{\in\, W}$$

The two pieces are [[angles-and-orthogonality|orthogonal]] (first is ⊥ W by Theorem 22; second is in W). Apply the Pythagorean theorem (Theorem 17):

$$\|\mathbf{u} - \mathbf{w}\|^2 = \|\mathbf{u} - \text{proj}_W\mathbf{u}\|^2 + \|\text{proj}_W\mathbf{u} - \mathbf{w}\|^2$$

If $\mathbf{w} \neq \text{proj}_W\mathbf{u}$, the second term is positive, so $\|\mathbf{u} - \mathbf{w}\| > \|\mathbf{u} - \text{proj}_W\mathbf{u}\|$. $\blacksquare$

```python
import numpy as np

# Best approximation: proj_W u is closer to u than any other w in W
Q = np.linalg.qr(np.random.randn(5, 3))[0]   # random ONB for a 3D subspace of R^5
u = np.random.randn(5)

proj = Q @ (Q.T @ u)                           # proj_W u = QQ^T u
dist_proj = np.linalg.norm(u - proj)

# Any other w in W
w = Q @ np.random.randn(3)                     # w = Q * arbitrary_coords
dist_w = np.linalg.norm(u - w)

print(f"||u - proj_W u|| = {dist_proj:.4f}")
print(f"||u - w||        = {dist_w:.4f}")
print(f"proj is closer:  {dist_proj < dist_w}")  # True
```

## In ML

**Linear regression** — fitting $\mathbf{y} = X\mathbf{w}$ in closed form: $\hat{\mathbf{w}} = (X^TX)^{-1}X^T\mathbf{y}$. The prediction $\hat{\mathbf{y}} = X\hat{\mathbf{w}}$ is proj onto col(X). Theorem 23 is why OLS minimizes the sum of squared residuals — the projection is provably the closest point in the column space to **y**.

**SVM margin** — the distance from the support vectors to the decision hyperplane is exactly $d(\mathbf{u}, W)$ from above. Maximizing the margin = maximizing this distance.

**PCA reconstruction error** — projecting onto the top-k principal components minimizes the squared reconstruction error ||X − X̂||². Theorem 23 is the formal guarantee: no other k-dimensional subspace produces a smaller error.

**Rank-deficiency** — if columns of A are dependent, $A^TA$ is singular and the formula breaks. Fix: Ridge regression adds $\lambda I$: $\hat{\mathbf{x}} = (A^TA + \lambda I)^{-1}A^T\mathbf{b}$.

## Exercises

**Basic** — Project $\mathbf{b} = [1,1,1]^T$ onto the column space of $A = [1,0,0]^T$ (a single vector). Compute $d(\mathbf{b}, \text{col}(A))$ — the distance from **b** to the line.

**Intermediate** — Prove $P^2 = P$ for $P = A(A^TA)^{-1}A^T$. Then interpret geometrically using Theorem 22: what does projecting twice mean for w₁ and w₂?

**Advanced** — Using Theorem 23, prove that the OLS estimator $\hat{\mathbf{w}} = (X^TX)^{-1}X^T\mathbf{y}$ minimizes $\|\mathbf{y} - X\mathbf{w}\|^2$ over all **w**. (Connect the squared norm to the distance formula and apply the theorem.)
