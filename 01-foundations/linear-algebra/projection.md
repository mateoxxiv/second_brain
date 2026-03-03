**Related**: [[vector-operations]], [[cosine-similarity]], [[basis-and-dimension]]
**Tags**: #status/seed

## Core Idea

Projection is the operation of finding the "shadow" of one vector onto another — the closest point on a line or subspace. It's the geometric foundation behind least squares regression (project data onto the column space), PCA (project onto principal components), and Gram-Schmidt orthogonalization.

## Details

### Scalar Projection

The **scalar projection** of $\mathbf{u}$ onto $\mathbf{v}$ gives the signed length of the shadow:

$$\text{comp}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|}$$

### Vector Projection

The **vector projection** gives the actual shadow vector:

$$\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \mathbf{v} = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \mathbf{v}$$

### Derivation

We want to find the vector $\mathbf{p}$ on the line spanned by $\mathbf{v}$ that is closest to $\mathbf{u}$.

Since $\mathbf{p}$ is on the line: $\mathbf{p} = c\mathbf{v}$ for some scalar $c$.

The error (residual) is $\mathbf{e} = \mathbf{u} - \mathbf{p} = \mathbf{u} - c\mathbf{v}$.

For $\mathbf{p}$ to be the **closest** point, the error must be **orthogonal** to $\mathbf{v}$:

$$\mathbf{e} \cdot \mathbf{v} = 0$$

$$(\mathbf{u} - c\mathbf{v}) \cdot \mathbf{v} = 0$$

$$\mathbf{u} \cdot \mathbf{v} - c(\mathbf{v} \cdot \mathbf{v}) = 0$$

$$c = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}}$$

$$\boxed{\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \mathbf{v}} \quad \blacksquare$$

### Orthogonal Decomposition

Any vector can be split into two perpendicular pieces — like splitting a force into horizontal and vertical components.

$$\mathbf{u} = \underbrace{\text{proj}_{\mathbf{v}} \mathbf{u}}_{\text{parallel to } \mathbf{v}} + \underbrace{(\mathbf{u} - \text{proj}_{\mathbf{v}} \mathbf{u})}_{\text{perpendicular to } \mathbf{v}}$$

Visually, with $\mathbf{u} = [3, 4]$ and $\mathbf{v} = [5, 0]$:

```
         u = [3, 4]
           *
          /|
         / |
        /  |  ← residual: [0, 4] (perpendicular piece)
       /   |
      /    |
     *-----*
  origin  [3, 0] ← projection (parallel piece)
```

The split: $[3, 4] = [3, 0] + [0, 4]$, and these two pieces are orthogonal: $[3,0] \cdot [0,4] = 0$.

### Why is the residual always perpendicular?

This is not a coincidence — it's guaranteed by the projection formula. The scaling factor $c = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}}$ was chosen specifically to make the residual orthogonal to $\mathbf{v}$:

$$\text{residual} \cdot \mathbf{v} = (\mathbf{u} - c\mathbf{v}) \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{v} - c(\mathbf{v} \cdot \mathbf{v}) = \mathbf{u} \cdot \mathbf{v} - \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}}(\mathbf{v} \cdot \mathbf{v}) = \mathbf{u} \cdot \mathbf{v} - \mathbf{u} \cdot \mathbf{v} = 0$$

We **built** the formula to guarantee orthogonality. $\blacksquare$

### Why perpendicular = best approximation

Perpendicular error is the **smallest possible error**. Any other split would produce a longer residual (by the Pythagorean theorem). This is why "best fit" in linear algebra always means "the one where the error is perpendicular":

- **Linear regression**: $\mathbf{y} = \text{prediction} + \text{residual}$. The prediction is the projection of $\mathbf{y}$ onto the column space of $X$. The residual is perpendicular to that space. Minimizing error = making the residual orthogonal.
- **PCA**: Data = kept components + discarded components. You project onto the top-$k$ directions. What you discard is orthogonal to what you keep.

### Worked Example

$$\mathbf{u} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} 5 \\ 1 \end{bmatrix}$$

Step by step:
1. $\mathbf{u} \cdot \mathbf{v} = (3)(5) + (4)(1) = 19$
2. $\mathbf{v} \cdot \mathbf{v} = 25 + 1 = 26$
3. $c = \frac{19}{26} \approx 0.731$
4. $\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{19}{26}\begin{bmatrix}5\\1\end{bmatrix} = \begin{bmatrix}3.654\\0.731\end{bmatrix}$
5. Residual: $\mathbf{u} - \text{proj} = \begin{bmatrix}3 - 3.654\\4 - 0.731\end{bmatrix} = \begin{bmatrix}-0.654\\3.269\end{bmatrix}$

Verify orthogonality:
$(3.654)(-0.654) + (0.731)(3.269) = -2.390 + 2.390 = 0$ ✓

### Projection onto a Subspace

When projecting onto a subspace spanned by multiple vectors (columns of matrix $A$):

$$\mathbf{p} = A(A^TA)^{-1}A^T\mathbf{u}$$

The matrix $P = A(A^TA)^{-1}A^T$ is the **projection matrix**. It satisfies:
- $P^2 = P$ (projecting twice = projecting once, idempotent)
- $P^T = P$ (symmetric)

### Why Projection Matters in ML

| Application | How projection appears |
|-------------|----------------------|
| **Least squares regression** | Find $\hat{\mathbf{y}} = X\hat{\boldsymbol{\beta}}$ by projecting $\mathbf{y}$ onto the column space of $X$ |
| **PCA** | Project data onto the top-$k$ principal components (eigenvectors of covariance matrix) |
| **Gram-Schmidt** | Build an orthogonal basis by subtracting projections: $\mathbf{u}_2 = \mathbf{v}_2 - \text{proj}_{\mathbf{u}_1}\mathbf{v}_2$ |
| **Residuals** | In regression, the residual $\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}}$ is the component orthogonal to the model |

### Least Squares as Projection (Preview)

In linear regression, you want to solve $X\boldsymbol{\beta} = \mathbf{y}$, but $\mathbf{y}$ doesn't live in the column space of $X$ (no exact solution). The best you can do is project $\mathbf{y}$ onto the column space:

$$X^TX\hat{\boldsymbol{\beta}} = X^T\mathbf{y} \implies \hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$$

This is the **normal equation** — derived directly from projection. The key insight: $X^T(\mathbf{y} - X\hat{\boldsymbol{\beta}}) = \mathbf{0}$ says the residual is orthogonal to the column space.

## Code Example

```python
import numpy as np

u = np.array([3.0, 4.0])
v = np.array([5.0, 1.0])

# Projection of u onto v
scalar = np.dot(u, v) / np.dot(v, v)  # 19/26
proj = scalar * v                      # [3.654, 0.731]
residual = u - proj                    # [-0.654, 3.269]

# Verify orthogonality
print(np.dot(proj, residual))  # ≈ 0 (floating point)
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Projection uses the [[vector-operations|dot product]] and [[vector-norms|norm]]
- [[cosine-similarity]] is the normalized scalar projection
- [[basis-and-dimension|Change of basis]] and projection are complementary: basis change rotates the space, projection reduces dimensions
- Subspace projection leads directly to [[Linear Regression]] (normal equation)
- Gram-Schmidt orthogonalization builds orthogonal bases from projection → connects to [[Eigenvalues and Eigenvectors]]

## Sources

- [3Blue1Brown — Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0)
- [MIT 18.06 — Strang, Lecture 15: Projections onto Subspaces](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 3.8](https://mml-book.github.io/book/mml-book.pdf)
