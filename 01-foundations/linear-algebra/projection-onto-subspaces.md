**Related**: [[projection]], [[basis-and-dimension]], [[linear-independence]], [[matrix-operations]]
**Tags**: #status/growing

## Core Idea

Projection onto a subspace generalizes vector projection from "shadow onto a line"
to "shadow onto a plane (or higher-dimensional flat surface)." Instead of projecting
onto one vector, you project onto the space spanned by multiple vectors. This is
exactly what linear regression does: find the closest point in the model's space to
the actual data.

## Details

### Intuition: From Line to Plane

In [[projection]], we projected onto a single vector — a 1D line. But what if
the "target" is a plane defined by two vectors? Or a 3D space defined by three?

Think of it physically: you hold a ball above a table (a 2D plane in 3D space).
Drop it straight down. Where it lands is the projection onto the plane. The
string from the ball to its shadow is the residual — and it's perpendicular
to the table.

The same rule applies: **the best approximation is the one where the error
is perpendicular to the subspace.**

### Setup

You have:
- A vector $\mathbf{b}$ you want to project (the ball)
- A subspace $S$ spanned by columns of matrix $A = [\mathbf{a}_1 | \mathbf{a}_2 | \cdots | \mathbf{a}_k]$ (the table)

The projection $\mathbf{p}$ must be a linear combination of the columns of $A$:

$$\mathbf{p} = A\hat{\mathbf{x}} = \hat{x}_1 \mathbf{a}_1 + \hat{x}_2 \mathbf{a}_2 + \cdots + \hat{x}_k \mathbf{a}_k$$

We need to find the coefficients $\hat{\mathbf{x}}$ that make the residual perpendicular to the subspace.

### Derivation

The residual is $\mathbf{e} = \mathbf{b} - A\hat{\mathbf{x}}$.

For the residual to be perpendicular to the subspace, it must be orthogonal to
**every column** of $A$. This means:

$$A^T \mathbf{e} = \mathbf{0}$$

Expand:

$$A^T(\mathbf{b} - A\hat{\mathbf{x}}) = \mathbf{0}$$

$$A^T\mathbf{b} - A^TA\hat{\mathbf{x}} = \mathbf{0}$$

$$A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$$

$$\boxed{\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}}$$

The projection itself is:

$$\boxed{\mathbf{p} = A(A^TA)^{-1}A^T\mathbf{b}}$$

Note: this is the exact same logic as single-vector projection. With one vector,
$A^TA$ is just $\mathbf{v} \cdot \mathbf{v}$ (a scalar), and $A^T\mathbf{b}$
is $\mathbf{v} \cdot \mathbf{u}$. The general formula reduces to the familiar
$\frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}}\mathbf{v}$. $\blacksquare$

### The Projection Matrix

The matrix $P = A(A^TA)^{-1}A^T$ is the **projection matrix**. It has two
remarkable properties:

**Idempotent**: $P^2 = P$ — projecting twice gives the same result as projecting
once. If the ball is already on the table, dropping it again doesn't move it.

**Symmetric**: $P^T = P$ — the projection "looks the same from both sides."

### Worked Example

Project $\mathbf{b} = \begin{bmatrix}1\\2\\3\end{bmatrix}$ onto the plane
spanned by $\mathbf{a}_1 = \begin{bmatrix}1\\0\\0\end{bmatrix}$ and
$\mathbf{a}_2 = \begin{bmatrix}0\\1\\0\end{bmatrix}$ (the xy-plane).

Step 1 — Build $A$:

$$A = \begin{bmatrix}1 & 0\\0 & 1\\0 & 0\end{bmatrix}$$

Step 2 — Compute $A^TA$:

$$A^TA = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix} = \begin{bmatrix}1&0\\0&1\end{bmatrix}$$

Step 3 — Compute $A^T\mathbf{b}$:

$$A^T\mathbf{b} = \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\begin{bmatrix}1\\2\\3\end{bmatrix} = \begin{bmatrix}1\\2\end{bmatrix}$$

Step 4 — Solve $\hat{\mathbf{x}} = (A^TA)^{-1}A^T\mathbf{b}$:

$$\hat{\mathbf{x}} = \begin{bmatrix}1&0\\0&1\end{bmatrix}^{-1}\begin{bmatrix}1\\2\end{bmatrix} = \begin{bmatrix}1\\2\end{bmatrix}$$

Step 5 — Projection:

$$\mathbf{p} = A\hat{\mathbf{x}} = \begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}\begin{bmatrix}1\\2\end{bmatrix} = \begin{bmatrix}1\\2\\0\end{bmatrix}$$

Step 6 — Residual:

$$\mathbf{e} = \mathbf{b} - \mathbf{p} = \begin{bmatrix}0\\0\\3\end{bmatrix}$$

The result makes geometric sense: projecting $[1, 2, 3]$ onto the xy-plane gives
$[1, 2, 0]$ — the z-component is stripped. The residual $[0, 0, 3]$ points
straight up, perpendicular to the plane. ✓

### Why This Matters in ML

| Application | The matrix $A$ is... | You're projecting... |
|-------------|---------------------|---------------------|
| **Linear regression** | Feature matrix $X$ (data points × features) | Target $\mathbf{y}$ onto column space of $X$ |
| **PCA** | Top-$k$ eigenvectors of covariance matrix | Data onto principal component subspace |
| **Gram-Schmidt** | Previously orthogonalized vectors | Next vector onto their span (then subtract) |

Linear regression IS subspace projection: $\hat{\boldsymbol{\beta}} = (X^TX)^{-1}X^T\mathbf{y}$
is exactly the formula above with $A = X$ and $\mathbf{b} = \mathbf{y}$.
We'll derive this fully in [[Linear Regression]].

## Code Example

```python
import numpy as np

# Project b onto the plane spanned by columns of A
b = np.array([1.0, 2.0, 3.0])
A = np.array([[1, 0],
              [0, 1],
              [0, 0]])

# Projection formula: p = A @ inv(A^T A) @ A^T @ b
ATA = A.T @ A
ATb = A.T @ b
x_hat = np.linalg.solve(ATA, ATb)  # safer than inv()
p = A @ x_hat        # [1, 2, 0]
e = b - p            # [0, 0, 3]

# Verify: residual is orthogonal to both columns of A
print(A.T @ e)       # [0, 0] — perpendicular to the subspace
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Generalizes [[projection]] from a single vector to multiple vectors
- Requires [[linear-independence]] — columns of $A$ must be independent for $(A^TA)^{-1}$ to exist
- The columns of $A$ form a [[basis-and-dimension|basis]] for the subspace
- Directly leads to [[Linear Regression]] — the normal equation is subspace projection
- [[PCA]] projects data onto the eigenvector subspace of the covariance matrix

## Sources

- [3Blue1Brown — Change of basis](https://www.youtube.com/watch?v=P2LTAUO1TdA)
- [MIT 18.06 — Strang, Lecture 15: Projections onto Subspaces](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 3.8](https://mml-book.github.io/book/mml-book.pdf)
