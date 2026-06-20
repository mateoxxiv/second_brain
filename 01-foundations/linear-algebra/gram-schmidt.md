---
tags:
  - status/growing
  - linear-algebra
related:
  - "[[orthonormal-bases]]"
  - "[[inner-product-spaces]]"
  - "[[angles-and-orthogonality]]"
  - "[[projection-onto-subspaces]]"
  - "[[basis-and-dimension]]"
  - "[[linear-independence]]"
  - "[[singular-value-decomposition]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §4.9 — Theorem 21, Gram-Schmidt, Example 58."
  - "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Gram-Schmidt converts any basis into an orthonormal one step-by-step: subtract all projections onto previously built vectors, then normalize — proving (Theorem 21) that every finite-dimensional inner product space has an orthonormal basis.

---

## Intuition

You have a messy basis — vectors pointing in overlapping directions. Gram-Schmidt cleans it up one vector at a time:

1. Take u₁. Normalize → v₁.
2. Take u₂. Remove whatever part of u₂ points toward v₁ (the projection). What's left is perpendicular to v₁. Normalize → v₂.
3. Take u₃. Remove projections onto v₁ and v₂. Normalize → v₃.
4. Repeat.

The "removing" step uses the [[orthonormal-bases|projection formula]] (Theorem 20). The remainder is never zero because if it were, uₖ would be a linear combination of u₁,...,u_{k-1} — contradicting the [[linear-independence|linear independence]] of the original basis.

| Operation | General basis | Orthonormal basis |
|---|---|---|
| Find coordinates | Solve a linear system | Just inner products |
| Matrix inverse | Expensive | Free — just transpose |
| Projection | Full formula $(A^TA)^{-1}A^T$ | $QQ^T$ |

## Mechanics

**Theorem 21 (Anton §4.9):** Every nonzero finite-dimensional [[inner-product-spaces|inner product space]] has an [[orthonormal-bases|orthonormal basis]].

*Proof*: any such space has a [[basis-and-dimension|basis]]. The Gram-Schmidt process below constructs an orthonormal one from it. $\blacksquare$

**The Gram-Schmidt Process** — given basis {u₁,...,uₙ} for V, produce orthonormal basis {v₁,...,vₙ}:

$$\mathbf{v}_1 = \frac{\mathbf{u}_1}{\|\mathbf{u}_1\|}$$

$$\mathbf{v}_k = \frac{\mathbf{u}_k - \displaystyle\sum_{j=1}^{k-1}\langle\mathbf{u}_k,\mathbf{v}_j\rangle\mathbf{v}_j}{\left\|\mathbf{u}_k - \displaystyle\sum_{j=1}^{k-1}\langle\mathbf{u}_k,\mathbf{v}_j\rangle\mathbf{v}_j\right\|}, \quad k = 2, 3, \ldots, n$$

**Key invariant**: after step k, {v₁,...,vₖ} is an orthonormal basis for span{u₁,...,uₖ}. The subspace is preserved at each step — GS does not change what is spanned, only the "shape" of the basis.

**Example 58 (Anton §4.9)** — R³ Euclidean inner product, starting from {u₁=(1,1,1), u₂=(0,1,1), u₃=(0,0,1)}:

**Step 1:**
$$\mathbf{v}_1 = \frac{(1,1,1)}{\sqrt{3}} = \left(\tfrac{1}{\sqrt{3}},\tfrac{1}{\sqrt{3}},\tfrac{1}{\sqrt{3}}\right)$$

**Step 2:** $\langle\mathbf{u}_2,\mathbf{v}_1\rangle = \tfrac{2}{\sqrt{3}}$

$$\mathbf{u}_2 - \tfrac{2}{\sqrt{3}}\mathbf{v}_1 = (0,1,1) - \left(\tfrac{2}{3},\tfrac{2}{3},\tfrac{2}{3}\right) = \left(-\tfrac{2}{3},\tfrac{1}{3},\tfrac{1}{3}\right), \quad \left\|\cdot\right\| = \tfrac{\sqrt{6}}{3}$$

$$\mathbf{v}_2 = \left(-\tfrac{2}{\sqrt{6}},\tfrac{1}{\sqrt{6}},\tfrac{1}{\sqrt{6}}\right)$$

**Step 3:** $\langle\mathbf{u}_3,\mathbf{v}_1\rangle = \tfrac{1}{\sqrt{3}},\quad\langle\mathbf{u}_3,\mathbf{v}_2\rangle = \tfrac{1}{\sqrt{6}}$

$$\mathbf{u}_3 - \tfrac{1}{\sqrt{3}}\mathbf{v}_1 - \tfrac{1}{\sqrt{6}}\mathbf{v}_2 = (0,0,1)-\!\left(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3}\right)-\!\left(-\tfrac{1}{3},\tfrac{1}{6},\tfrac{1}{6}\right) = \left(0,-\tfrac{1}{2},\tfrac{1}{2}\right), \quad \left\|\cdot\right\| = \tfrac{1}{\sqrt{2}}$$

$$\mathbf{v}_3 = \left(0,-\tfrac{1}{\sqrt{2}},\tfrac{1}{\sqrt{2}}\right)$$

```python
import numpy as np

def gram_schmidt(basis: list[np.ndarray]) -> list[np.ndarray]:
    ortho = []
    for u in basis:
        v = u.copy().astype(float)
        for q in ortho:
            v -= np.dot(v, q) * q   # modified GS: subtract from running v (numerically stable)
        ortho.append(v / np.linalg.norm(v))
    return ortho

basis = [np.array([1.,1.,1.]), np.array([0.,1.,1.]), np.array([0.,0.,1.])]
Q = np.column_stack(gram_schmidt(basis))
print(np.allclose(Q.T @ Q, np.eye(3)))   # True — orthonormal ✓
```

> Runnable: [[code/foundations/gram_schmidt.py]]

## In ML

**QR decomposition is Gram-Schmidt** — A = QR factors any matrix into Q (orthonormal columns, GS output) and R (upper-triangular, recording the inner products used at each step). Every least-squares solver and eigenvalue algorithm depends on QR. Libraries use Householder reflections for numerical stability, but the mathematical idea is GS.

**PCA columns are GS-ready** — the spectral theorem guarantees eigenvectors of the covariance matrix are already orthogonal. GS normalizes them into the orthonormal principal components used for projection.

**Orthogonal weight initialization** — random Gaussian matrices put through QR (= GS) produce orthonormal weight columns, preserving gradient norms during backpropagation: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ for all x.

## Exercises

**Basic** — Apply GS to {u₁=(1,0,1), u₂=(1,1,0)} in R³. What is the dimension of the resulting ONB? What subspace does it span?

**Intermediate** — Apply GS to {1, x, x²} in P₂ with inner product $\langle p,q\rangle = \int_{-1}^{1} p(x)q(x)\,dx$. Verify that your first two output polynomials are orthogonal. (Hint: $\int_{-1}^1 x\,dx = 0$.)

**Advanced** — Prove the key invariant by induction: after step k of GS, span{v₁,...,vₖ} = span{u₁,...,uₖ}. (Show each uⱼ ∈ span{v₁,...,vⱼ} and each vⱼ ∈ span{u₁,...,uⱼ}, then use induction.)
