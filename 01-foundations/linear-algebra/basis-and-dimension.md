**Related**: [[linear-independence]], [[vectors-and-vector-spaces]], [[PCA]]
**Tags**: #status/seed

## Core Idea

A basis is a minimal set of linearly independent vectors that can generate every vector in the space through linear combinations. The dimension is the number of basis vectors needed. PCA is fundamentally about finding the best basis for your data — the one that captures the most variance with the fewest dimensions.

## Details

### Span

The **span** of a set of vectors is all possible linear combinations:

$$\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_k) = \{c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k \mid c_i \in \mathbb{R}\}$$

Example: $\text{span}\left(\begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix}\right) = \mathbb{R}^2$ — these two vectors can reach any point in the plane.

### Basis

A **basis** for a vector space $V$ is a set of vectors that:
1. **Spans** $V$ — every vector in $V$ can be written as a linear combination
2. Is **linearly independent** — no redundant vectors

A basis is the most efficient spanning set: remove any vector and you lose coverage, add any vector and you introduce redundancy.

### Dimension

$$\dim(V) = \text{number of vectors in any basis of } V$$

Key fact: all bases of the same space have the **same size**. This is a theorem, not obvious.

- $\dim(\mathbb{R}^n) = n$
- $\dim(\text{a plane through origin in } \mathbb{R}^3) = 2$
- $\dim(\{0\}) = 0$

### The Standard Basis

The standard basis for $\mathbb{R}^n$ is:

$$\mathbf{e}_1 = \begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix}0\\1\\\vdots\\0\end{bmatrix}, \quad \ldots \quad \mathbf{e}_n = \begin{bmatrix}0\\0\\\vdots\\1\end{bmatrix}$$

Any vector $\mathbf{v} = \begin{bmatrix}v_1\\v_2\\\vdots\\v_n\end{bmatrix} = v_1\mathbf{e}_1 + v_2\mathbf{e}_2 + \cdots + v_n\mathbf{e}_n$

The components of a vector ARE its coordinates in the standard basis.

### Change of Basis

The same vector has **different coordinates** in different bases. Changing basis means expressing a vector in a new coordinate system.

Given a new basis $B = \{\mathbf{b}_1, \mathbf{b}_2\}$, a vector $\mathbf{v}$ has coordinates $[\mathbf{v}]_B = \begin{bmatrix}\alpha_1\\\alpha_2\end{bmatrix}$ such that:

$$\mathbf{v} = \alpha_1 \mathbf{b}_1 + \alpha_2 \mathbf{b}_2$$

### Worked Example: Change of Basis

Standard basis: $\mathbf{e}_1 = \begin{bmatrix}1\\0\end{bmatrix}$, $\mathbf{e}_2 = \begin{bmatrix}0\\1\end{bmatrix}$

New basis: $\mathbf{b}_1 = \begin{bmatrix}1\\1\end{bmatrix}$, $\mathbf{b}_2 = \begin{bmatrix}1\\-1\end{bmatrix}$

Vector: $\mathbf{v} = \begin{bmatrix}3\\1\end{bmatrix}$ (in standard basis)

Find $[\mathbf{v}]_B$: Solve $\alpha_1\begin{bmatrix}1\\1\end{bmatrix} + \alpha_2\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}$

$$\alpha_1 + \alpha_2 = 3$$
$$\alpha_1 - \alpha_2 = 1$$

Adding: $2\alpha_1 = 4 \implies \alpha_1 = 2$. Subtracting: $2\alpha_2 = 2 \implies \alpha_2 = 1$.

So $[\mathbf{v}]_B = \begin{bmatrix}2\\1\end{bmatrix}$ — the same point in space, different coordinates.

### Why Change of Basis Matters in ML

**PCA is a change of basis.** Your original data has coordinates in the feature basis (age, income, height). PCA finds a new basis (principal components) that:
- Is orthogonal (components are independent)
- Is ordered by variance (first component captures the most information)
- Lets you drop low-variance components → dimensionality reduction

**This is not a trick — it's a rotation.** PCA rotates the coordinate system to align with the directions of maximum data spread.

## Code Example

```python
import numpy as np

# Standard basis coordinates
v = np.array([3.0, 1.0])

# New basis
B = np.array([[1, 1],    # b1
              [1, -1]])   # b2

# Change of basis: solve B^T @ coords = v
coords_in_B = np.linalg.solve(B.T, v)
print(f"Standard coords: {v}")           # [3, 1]
print(f"New basis coords: {coords_in_B}")  # [2, 1]

# Verify: reconstruct v from new basis
v_reconstructed = coords_in_B[0] * B[0] + coords_in_B[1] * B[1]
print(f"Reconstructed: {v_reconstructed}")  # [3, 1] ✓
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Basis requires [[linear-independence]] — basis vectors must be independent
- Basis and span define the structure of [[vectors-and-vector-spaces]]
- Change of basis IS what [[PCA]] does — rotating to the principal component basis
- [[Eigenvalues and Eigenvectors]] define the "natural" basis of a linear transformation
- [[Linear Transformations]] are represented as matrices, and the matrix changes depending on the basis

## Sources

- [3Blue1Brown — Change of basis](https://www.youtube.com/watch?v=P2LTAUO1TdA)
- [MIT 18.06 — Strang, Lecture 9: Independence, Basis, Dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.6-2.7](https://mml-book.github.io/book/mml-book.pdf)
