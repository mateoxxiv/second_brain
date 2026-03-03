**Related**: [[linear-independence]], [[vector-operations]], [[vectors-and-vector-spaces]], [[projection]]
**Tags**: #status/seed

## Core Idea

A basis is the "coordinate system" of a vector space — the minimal set of
directions you need to describe any point in that space. The dimension is how
many directions you need. Choosing a different basis is like switching from
GPS coordinates to street addresses: the locations don't change, but the
numbers you use to describe them do. PCA is literally choosing a better
coordinate system for your data.

## Details

### Span: "What can I reach?"

Before understanding basis, you need span. The **span** of a set of vectors
is everything you can reach by combining them:

$$\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_k) = \{c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_k\mathbf{v}_k \mid c_i \in \mathbb{R}\}$$

**Analogy**: Think of mixing paint colors.
- If you have red and blue, you can mix any ratio to get red, blue, purple,
  and everything in between. That full range of colors is the **span**.
- Add yellow, and now you can reach greens, oranges, browns — the span expands.
- Add another shade of red? The span doesn't grow — you already had red.

```
1 vector → span is a LINE (all multiples of that vector)

     *
    /
   /
  /
 *-------> v1
  \
   \
    \
     *

2 independent vectors → span is a PLANE

         * * * * *
        * * * * *
  v2 ↑ * * * * *
       * * * * *
        * * * * *
         --------> v1

3 independent vectors in R^3 → span is ALL of 3D space
```

**Key question**: Given a set of vectors, can you reach every point in the
space, or are you stuck on a line or plane?

### Basis: "The most efficient coordinate system"

A **basis** for a vector space $V$ is a set of vectors that:
1. **Spans** $V$ — you can reach everything (no blind spots)
2. Is **linearly independent** — no redundancy (no wasted vectors)

Why do you need BOTH?
- Span but not independent → you have extra vectors. Like having 4 compass
  directions (N, S, E, W) when 2 would suffice (N and E — you can get S and W
  by going negative). It works, but it's wasteful.
- Independent but doesn't span → you're missing coverage. Like having only
  North — you can't go East.

A basis is the sweet spot: **maximum coverage, zero waste.**

### Worked Example: Is this a basis for $\mathbb{R}^2$?

**Attempt 1**: $\{\begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}2\\0\end{bmatrix}\}$

Independent? No — $\begin{bmatrix}2\\0\end{bmatrix} = 2 \times \begin{bmatrix}1\\0\end{bmatrix}$. Redundant.
Spans $\mathbb{R}^2$? No — both point along the x-axis. Can't reach $(0, 1)$.
**Not a basis.** Fails both tests.

**Attempt 2**: $\{\begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix}\}$

Independent? Yes — neither is a multiple of the other.
Spans $\mathbb{R}^2$? Yes — any $\begin{bmatrix}a\\b\end{bmatrix} = a\begin{bmatrix}1\\0\end{bmatrix} + b\begin{bmatrix}0\\1\end{bmatrix}$.
**This is a basis.** (The standard basis, specifically.)

**Attempt 3**: $\{\begin{bmatrix}1\\1\end{bmatrix}, \begin{bmatrix}1\\-1\end{bmatrix}\}$

Independent? Yes — one isn't a scalar multiple of the other.
Spans $\mathbb{R}^2$? Yes — any 2D point can be expressed as a combination.
**Also a basis!** A different one. The same space can have many bases.

### Dimension: "How many directions does this space have?"

$$\dim(V) = \text{number of vectors in any basis of } V$$

A remarkable theorem: **every basis of the same space has the same number of
vectors.** This isn't obvious. You might think some bases could have 2 vectors
and others 3. They can't. The number is an intrinsic property of the space.

This is why dimension is well-defined:

| Space | Dimension | Meaning |
|-------|-----------|---------|
| A line through origin | 1 | One direction to move |
| A plane through origin | 2 | Two independent directions |
| $\mathbb{R}^3$ | 3 | Three independent directions |
| $\mathbb{R}^{784}$ (flattened 28×28 image) | 784 | 784 independent pixel values |
| $\{\mathbf{0}\}$ (just the zero vector) | 0 | Nowhere to go |

**ML implication**: If your 784-dimensional image data actually lives on a
50-dimensional surface (because most pixels are correlated), the **intrinsic
dimension** is 50. PCA finds this. Autoencoders learn it. The 784 features
are redundant — you only need 50 basis vectors to describe the data.

### The Standard Basis: "Your default coordinate system"

The standard basis for $\mathbb{R}^n$ is the simplest possible:

$$\mathbf{e}_1 = \begin{bmatrix}1\\0\\0\end{bmatrix}, \quad \mathbf{e}_2 = \begin{bmatrix}0\\1\\0\end{bmatrix}, \quad \mathbf{e}_3 = \begin{bmatrix}0\\0\\1\end{bmatrix}$$

Each vector points along one axis. When you write $\mathbf{v} = \begin{bmatrix}3\\-1\\4\end{bmatrix}$,
you're saying: "go 3 units along $\mathbf{e}_1$, then -1 along $\mathbf{e}_2$,
then 4 along $\mathbf{e}_3$."

**The components of a vector ARE its coordinates in the standard basis.**

This is so natural that you forget it's a choice. But it IS a choice — and
sometimes a different basis describes your data better.

### Change of Basis: "Same point, different address"

**Analogy**: Your house has one location on Earth, but multiple valid addresses:
- GPS: (4.7110, -74.0721)
- Street: Calle 85 #15-30, Bogotá
- What3Words: "table.lamp.river"

All describe the same place. A change of basis does the same for vectors:
the point in space doesn't move, but the numbers (coordinates) change.

**Why would you want different coordinates?**
- Your data might be simpler in a different basis (PCA finds one where features
  are uncorrelated)
- Your computation might be faster (diagonal matrices are trivial to work with)
- Your interpretation might be clearer (principal components have meaning)

### How Change of Basis Works

Given a new basis $B = \{\mathbf{b}_1, \mathbf{b}_2\}$, the coordinates
$[\mathbf{v}]_B = \begin{bmatrix}\alpha_1\\\alpha_2\end{bmatrix}$ are the
scalars such that:

$$\mathbf{v} = \alpha_1 \mathbf{b}_1 + \alpha_2 \mathbf{b}_2$$

To find them, you solve this system of equations.

### Worked Example: Change of Basis

Standard basis: $\mathbf{e}_1 = \begin{bmatrix}1\\0\end{bmatrix}$, $\mathbf{e}_2 = \begin{bmatrix}0\\1\end{bmatrix}$

New basis: $\mathbf{b}_1 = \begin{bmatrix}1\\1\end{bmatrix}$, $\mathbf{b}_2 = \begin{bmatrix}1\\-1\end{bmatrix}$

Vector: $\mathbf{v} = \begin{bmatrix}3\\1\end{bmatrix}$ in standard coordinates.

**Question**: What are the coordinates in basis $B$?

Solve $\alpha_1\begin{bmatrix}1\\1\end{bmatrix} + \alpha_2\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}$:

$$\alpha_1 + \alpha_2 = 3$$
$$\alpha_1 - \alpha_2 = 1$$

Add both equations: $2\alpha_1 = 4 \implies \alpha_1 = 2$
Subtract: $2\alpha_2 = 2 \implies \alpha_2 = 1$

$$[\mathbf{v}]_B = \begin{bmatrix}2\\1\end{bmatrix}$$

Verify: $2\begin{bmatrix}1\\1\end{bmatrix} + 1\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}2\\2\end{bmatrix} + \begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}$ ✓

Same point. Different numbers. Different perspective.

### Why This Matters in ML

**PCA is a change of basis.** Your data starts in the feature basis (age,
income, height). PCA finds a new basis where:

```
Feature basis:                    PCA basis:
age ----→                         PC1 (most variance) ----→
income --→                        PC2 (second most) ----→
height --→                        PC3 (least — drop it!) --→

Coordinates: [35, 75000, 180]     Coordinates: [142.5, 3.2, 0.1]
                                  Drop PC3 → [142.5, 3.2]
                                  = dimensionality reduction
```

- Original basis: features are correlated (income and age move together)
- PCA basis: components are uncorrelated (orthogonal), ordered by importance
- Dropping low-variance components = removing the coordinates that don't matter

**This is not a trick — it's a rotation of the coordinate system** to align
with the directions of maximum data spread.

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
print(f"Standard coords: {v}")            # [3, 1]
print(f"New basis coords: {coords_in_B}") # [2, 1]

# Verify: reconstruct v from new basis
v_reconstructed = coords_in_B[0] * B[0] + coords_in_B[1] * B[1]
print(f"Reconstructed: {v_reconstructed}") # [3, 1] ✓

# Show that span of 2 independent vectors in R^2 = all of R^2
# Any random point can be expressed in this basis
random_point = np.array([7.0, -3.0])
coords = np.linalg.solve(B.T, random_point)
print(f"[7, -3] in basis B: {coords}")    # [2, 5]
check = coords[0] * B[0] + coords[1] * B[1]
print(f"Reconstructed: {check}")           # [7, -3] ✓
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Basis requires [[linear-independence]] — basis vectors must be independent
- Span is built from [[vector-operations|linear combinations]]
- Basis and span define the structure of [[vectors-and-vector-spaces]]
- Change of basis IS what [[PCA]] does — rotating to the principal component basis
- [[Eigenvalues and Eigenvectors]] define the "natural" basis of a linear transformation
- [[projection]] and [[projection-onto-subspaces]] find the closest point in a subspace spanned by a basis

## Sources

- [3Blue1Brown — Linear combinations, span, and basis](https://www.youtube.com/watch?v=k7RM-ot2NWY)
- [3Blue1Brown — Change of basis](https://www.youtube.com/watch?v=P2LTAUO1TdA)
- [MIT 18.06 — Strang, Lecture 9: Independence, Basis, Dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.6-2.7](https://mml-book.github.io/book/mml-book.pdf)
