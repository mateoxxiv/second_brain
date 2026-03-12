**Related**: [[matrix-operations]], [[determinant]], [[linear-independence]], [[basis-and-dimension]], [[projection-onto-subspaces]]
**Tags**: #status/growing

## Core Idea

Take this matrix and apply it to different vectors:

```
A = [[2, 1],
     [1, 2]]

A @ [1, 0] = [2, 1]    ← changed direction (was horizontal, now diagonal)
A @ [0, 1] = [1, 2]    ← changed direction (was vertical, now diagonal)
A @ [1, 1] = [3, 3]    ← SAME direction! just 3x longer
A @ [1,-1] = [1,-1]    ← SAME direction! didn't change at all
```

Most vectors get pushed to a new direction. But [1,1] and [1,-1] are special —
the matrix can only **stretch** them, never rotate them. These are
**eigenvectors**. The stretch factor (3 and 1) is the **eigenvalue**.

```
A @ v = lambda * v

v = eigenvector   (the direction that survives)
lambda = eigenvalue (how much it stretches)
```

Why care? Eigenvectors are the **natural axes** of a transformation. Along these
directions, a complicated matrix behaves like simple multiplication by a number.

## Details

### Geometric Intuition: Directions That Survive

Imagine a transformation that shears a 2D plane — most arrows get tilted. But
certain arrows lie along "eigendirections" where the transformation only
stretches or squishes them. The arrow might double in length ($\lambda = 2$),
shrink to half ($\lambda = 0.5$), flip and double ($\lambda = -2$), or stay
exactly the same ($\lambda = 1$). The direction never changes.

A clean real-world analogy: find the **axis of a 3D rotation**. That axis
vector doesn't rotate at all — it just sits there with $\lambda = 1$. Every
other vector spins around it. Finding the eigenvector *is* finding the axis.

Note that every point on the same line as an eigenvector is also an eigenvector
— scaling by any constant $c$ gives $A(c\mathbf{v}) = \lambda(c\mathbf{v})$.
So eigenvectors define **eigenspaces** (lines, planes, or higher-dimensional
subspaces), not isolated points.

### Finding Eigenvalues: The Characteristic Equation

The question is simple: **for which lambda does A @ v = lambda * v have a
non-zero solution v?**

Let's turn this into something we can solve. Start from:

```
A @ v = lambda * v
```

Move everything to one side:

```
A @ v - lambda * v = 0
```

We want to factor out v. But lambda is a number and A is a matrix — we can't
subtract them directly. So write lambda * v as lambda * I @ v (multiplying by
the identity matrix changes nothing):

```
(A - lambda * I) @ v = 0
```

Now read this sentence: "the matrix (A - lambda * I) sends vector v to zero."

Why does this require det = 0? Remember from [[determinant]] and
[[gaussian-elimination]]:

- **det != 0** → the system has exactly ONE solution → that's v = [0,0] → useless
- **det = 0** → the system has INFINITE solutions → non-zero v exists → eigenvectors!

We NEED the matrix to be singular (det = 0) because we need it to collapse
some direction — the vectors along that collapsed direction are the eigenvectors.

```
det(A - lambda * I) = 0
```

This is the **characteristic equation**. It's a polynomial in lambda — solve it
to find the eigenvalues. Then for each eigenvalue, plug it back and solve for v
using [[gaussian-elimination]].

**Verification step**: after finding each lambda, compute det(A - lambda * I).
If it's 0, you have a real eigenvalue. If not, you made an algebra mistake.

```
Step 1: Solve det(A - lambda * I) = 0  →  gives you the eigenvalues
Step 2: For each lambda, solve (A - lambda * I) @ v = 0  →  gives you the eigenvectors
```

### Worked Example: 2×2 Symmetric Matrix

Let $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$.

**Step 1: Build the characteristic polynomial.**

$$A - \lambda I = \begin{bmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{bmatrix}$$

$$\det(A - \lambda I) = (2 - \lambda)^2 - 1 \cdot 1$$

$$= \lambda^2 - 4\lambda + 4 - 1 = \lambda^2 - 4\lambda + 3$$

**Step 2: Solve for eigenvalues.**

$$\lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3) = 0$$

$$\lambda_1 = 1, \quad \lambda_2 = 3$$

**Step 3a: Eigenvector for $\lambda_1 = 1$.**

$$(A - 1 \cdot I)\mathbf{v} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}\mathbf{v} = \mathbf{0}$$

Both rows say $v_1 + v_2 = 0$, so $v_2 = -v_1$. Choose $v_1 = 1$:

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1 \end{bmatrix} \quad \text{(normalized: } \tfrac{1}{\sqrt{2}}[1, -1]^T\text{)}$$

**Step 3b: Eigenvector for $\lambda_2 = 3$.**

$$(A - 3 \cdot I)\mathbf{v} = \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}\mathbf{v} = \mathbf{0}$$

Both rows say $-v_1 + v_2 = 0$, so $v_2 = v_1$. Choose $v_1 = 1$:

$$\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} \quad \text{(normalized: } \tfrac{1}{\sqrt{2}}[1, 1]^T\text{)}$$

**Verification:**

$$A\mathbf{v}_1 = \begin{bmatrix}2&1\\1&2\end{bmatrix}\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}1\\-1\end{bmatrix} = 1 \cdot \mathbf{v}_1 \checkmark$$

$$A\mathbf{v}_2 = \begin{bmatrix}2&1\\1&2\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}3\\3\end{bmatrix} = 3 \cdot \mathbf{v}_2 \checkmark$$

Notice: $\mathbf{v}_1 \perp \mathbf{v}_2$ (their dot product is $1 \cdot 1 + (-1) \cdot 1 = 0$). This
is not a coincidence — it is guaranteed for symmetric matrices.

### Geometric Meaning of Eigenvalue Magnitude

| Eigenvalue range | Geometric effect | System behavior |
|---|---|---|
| $\lambda > 1$ | Stretch (vector grows) | Iterative application diverges |
| $\lambda = 1$ | No change (fixed direction) | Stable fixed point |
| $0 < \lambda < 1$ | Shrink (vector approaches 0) | Iterative application converges to 0 |
| $\lambda = 0$ | Collapse to zero | Matrix is singular, direction lost |
| $-1 < \lambda < 0$ | Flip and shrink | Oscillating convergence |
| $\lambda < -1$ | Flip and stretch | Oscillating divergence |
| Complex $\lambda$ | Rotation + scaling | Spiral behavior |

If you repeatedly multiply a vector by $A$, the dominant eigenvector (largest
$|\lambda|$) wins out — everything else shrinks away relative to it.

### Symmetric Matrices and the Spectral Theorem

A matrix $A$ is **symmetric** when $A = A^T$ — every entry above the diagonal
mirrors the entry below it. Symmetric matrices arise constantly in ML:
covariance matrices, Gram matrices ($X^TX$), Hessians of smooth loss functions.

The **Spectral Theorem** guarantees that every real symmetric matrix has:

1. **All real eigenvalues** — no complex numbers, even though the characteristic
   polynomial could in principle have complex roots.
2. **Orthogonal eigenvectors** — eigenvectors for distinct eigenvalues are
   perpendicular ($\mathbf{v}_i \cdot \mathbf{v}_j = 0$ for $i \neq j$).
3. **Orthogonal diagonalization** — you can write $A = Q \Lambda Q^T$, where
   $Q$ is an orthogonal matrix (its columns are the unit eigenvectors, and
   $Q^{-1} = Q^T$) and $\Lambda$ is the diagonal matrix of eigenvalues.

$$A = Q \Lambda Q^T = \sum_{i=1}^{n} \lambda_i \mathbf{q}_i \mathbf{q}_i^T$$

The last form is the **spectral decomposition**: $A$ is a sum of rank-1 outer
products, each scaled by an eigenvalue. You can approximate $A$ by keeping only
the largest $k$ terms — this is the mathematical engine behind PCA.

### Key Properties: Trace and Determinant

Two cheap ways to sanity-check eigenvalues without solving the full polynomial:

$$\text{tr}(A) = \sum_{i} a_{ii} = \sum_{i} \lambda_i$$

$$\det(A) = \prod_{i} \lambda_i$$

The trace (sum of diagonal entries) equals the sum of eigenvalues. The
[[determinant]] equals their product.

For our example $A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$:

- $\text{tr}(A) = 2 + 2 = 4 = 1 + 3 = \lambda_1 + \lambda_2$ ✓
- $\det(A) = 4 - 1 = 3 = 1 \times 3 = \lambda_1 \lambda_2$ ✓

Immediate consequences:

- $\det(A) = 0$ iff at least one eigenvalue is zero — confirming the
  [[determinant]] connection to singularity.
- If $\text{tr}(A) > 0$ and $\det(A) > 0$, both eigenvalues are positive
  (matrix is positive definite — a crucial property for covariance matrices and
  Hessians).

## Code Example

```python
import numpy as np

A = np.array([[2, 1],
              [1, 2]], dtype=float)

eigenvalues, eigenvectors = np.linalg.eigh(A)  # eigh for symmetric matrices
# eigenvalues: [1. 3.]
# eigenvectors columns: [-0.707, 0.707] and [0.707, 0.707]

# Verify: Av = λv for each pair
for lam, v in zip(eigenvalues, eigenvectors.T):
    print(np.allclose(A @ v, lam * v))  # True, True

# Spectral reconstruction: A = Q Λ Qᵀ
Q = eigenvectors
Lambda = np.diag(eigenvalues)
print(np.allclose(Q @ Lambda @ Q.T, A))  # True

# Trace and determinant checks
print(np.trace(A), sum(eigenvalues))      # 4.0  4.0
print(np.linalg.det(A), np.prod(eigenvalues))  # 3.0  3.0
```

> For full runnable implementation with exercises, see: [[code/foundations/eigenvalues_and_eigenvectors.py]]

## ML Applications

### PCA: Eigenvectors of the Covariance Matrix

Principal Component Analysis finds the directions of maximum variance in a
dataset. The procedure:

1. Center the data: subtract the mean from each feature.
2. Compute the covariance matrix $\Sigma = \frac{1}{n-1} X^T X$.
3. Find the eigenvectors of $\Sigma$. These are the **principal components** —
   the directions that capture the most variance.
4. The corresponding **eigenvalues** measure how much variance each component
   explains. Sort eigenvalues descending; the first eigenvector is the direction
   of greatest spread.
5. Project data onto the top $k$ eigenvectors to reduce dimensionality.

The covariance matrix is symmetric by construction ($\Sigma = \Sigma^T$), so
the Spectral Theorem applies: real eigenvalues, orthogonal components. PCA is
eigendecomposition of the covariance matrix.

Variance explained by component $i$: $\frac{\lambda_i}{\sum_j \lambda_j}$

### Gradient Stability: Eigenvalues of the Weight Matrix

In deep networks, the **Jacobian** of each layer's transformation is a weight
matrix (or a product of weight matrices). The eigenvalues of this matrix
determine what happens to gradients as they flow backward:

- **Eigenvalue > 1**: gradients grow. Stacked across many layers → **exploding
  gradients**.
- **Eigenvalue < 1**: gradients shrink. Stacked across many layers → **vanishing
  gradients**.

This is why careful initialization (Xavier/He init) and techniques like gradient
clipping or batch normalization target keeping effective eigenvalues near 1. The
**spectral radius** (largest $|\lambda|$) of the weight matrix is the key number.

### Google PageRank: The Dominant Eigenvector

PageRank models the web as a Markov chain: each page is a state, and each link
is a transition probability. The transition matrix $M$ is column-stochastic
(columns sum to 1). The PageRank scores are the entries of the **dominant
eigenvector** (eigenvalue 1) of $M^T$:

$$M^T \mathbf{r} = \mathbf{r}$$

This is the stationary distribution — the vector that doesn't change when you
apply the transition. Iteratively applying $M^T$ to any starting vector converges
to this eigenvector (power iteration). The page with the highest entry has the
highest rank.

### Markov Chains: Stationary Distribution

Any finite, ergodic Markov chain has a unique stationary distribution
$\boldsymbol{\pi}$ satisfying:

$$P^T \boldsymbol{\pi} = \boldsymbol{\pi}$$

This is the eigenvector of $P^T$ with eigenvalue 1. All other eigenvalues have
$|\lambda| < 1$, so the chain forgets its starting state and converges to
$\boldsymbol{\pi}$ over time. The **spectral gap** ($1 - |\lambda_2|$) controls
how fast.

## Connections

- [[determinant]] — $\det(A - \lambda I) = 0$ is the bridge from geometry to
  algebra; $\det(A) = \prod \lambda_i$ links back.
- [[linear-independence]] — eigenvectors for distinct eigenvalues are always
  linearly independent.
- [[basis-and-dimension]] — eigenvectors form a basis for $\mathbb{R}^n$ when
  $A$ has $n$ distinct eigenvalues (or when $A$ is symmetric).
- [[gaussian-elimination]] — used to solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$
  after finding eigenvalues.
- [[projection-onto-subspaces]] — eigenspaces are the natural subspaces to
  project onto in PCA.
- [[matrix-operations]] — eigendecomposition $A = Q\Lambda Q^T$ is one of the
  most important matrix factorizations.

## Sources

- [3Blue1Brown — Essence of Linear Algebra: Eigenvectors and eigenvalues](https://www.3blue1brown.com/lessons/eigenvalues) — best geometric intuition; watch before computing anything
- [Setosa — Visual eigenvalues/eigenvectors](https://setosa.io/ev/eigenvectors-and-eigenvalues/) — interactive browser demo
- [Hadrienj — Deep Learning Book series: Eigendecomposition](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.7-Eigendecomposition/) — bridges math to ML, Python code
- [MIT 18.06 — Strang, Lecture 21: Eigenvalues and Eigenvectors](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — rigorous derivation, worked examples
- [Mathematics for Machine Learning — Chapter 4.2](https://mml-book.github.io/book/mml-book.pdf) — spectral theorem, PCA connection, ML framing
- [Deep Learning Book — Chapter 2.7: Eigendecomposition](https://www.deeplearningbook.org/contents/linear_algebra.html) — Goodfellow et al., concise and application-focused
