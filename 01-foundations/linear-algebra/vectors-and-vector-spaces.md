**Related**: [[Matrix Operations and Properties]], [[Linear Transformations]]
**Tags**: #status/seed

## Core Idea

A vector is an element of a vector space — an object that can be added to other
vectors and multiplied by scalars. In ML, vectors are the fundamental data
representation: every data point, every embedding, every row of weights is a
vector in $\mathbb{R}^n$.

## Details

### Vector in $\mathbb{R}^n$

An ordered tuple of $n$ real numbers:

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

### Core Operations

| Operation | Formula | ML Use |
|-----------|---------|--------|
| Addition | $\mathbf{u} + \mathbf{v} = [u_i + v_i]$ | Gradient accumulation, residual connections |
| Scalar mult. | $c\mathbf{v} = [cv_i]$ | Learning rate scaling, feature normalization |
| Dot product | $\mathbf{u} \cdot \mathbf{v} = \sum u_i v_i$ | Similarity, attention scores, linear layers |
| Norm (L2) | $\|\mathbf{v}\| = \sqrt{\sum v_i^2}$ | Regularization, distance metrics |

### The Dot Product Identity

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$

This is why cosine similarity works: normalizing by norms isolates the angle
$\theta$, which captures directional similarity regardless of magnitude.

### Vector Space Axioms

A vector space $V$ over $\mathbb{R}$ must satisfy closure under addition and scalar
multiplication, plus: commutativity, associativity, distributivity, and existence
of zero vector and additive inverses.

### Key Concepts

- **Linear independence**: No vector in the set can be expressed as a linear
  combination of others. ML analogy: non-redundant features.
- **Basis**: Minimal spanning set of linearly independent vectors.
- **Dimension**: Number of basis vectors needed. $\dim(\mathbb{R}^n) = n$.
- **Span**: All possible linear combinations of a set of vectors.
- **Subspace**: A subset that is itself a vector space (must contain the origin).

## Code Example

```python
import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# Dot product — the core operation behind attention and similarity
dot = np.dot(u, v)  # 32

# Cosine similarity — used in RAG, embeddings, recommendation systems
cos_sim = dot / (np.linalg.norm(u) * np.linalg.norm(v))  # 0.974

# Check linear independence via rank
vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
rank = np.linalg.matrix_rank(vectors)  # 3 = independent
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- The dot product is the foundation of [[Matrix Operations and Properties]] — matrix
  multiplication is just organized dot products
- [[Linear Transformations]] map vectors between spaces — neural network layers
  are linear transformations
- Vector norms lead to [[Regularization (L1/L2)]] in ML — penalizing weight magnitude
- Basis and dimension connect directly to [[PCA]] — finding the optimal low-dimensional basis for data

## Sources

- [3Blue1Brown — Essence of Linear Algebra (Chapter 1)](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- [MIT 18.06 — Gilbert Strang, Lecture 1](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2](https://mml-book.github.io/book/mml-book.pdf)
