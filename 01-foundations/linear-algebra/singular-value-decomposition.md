**Related**: [[spectral-decomposition]], [[eigenvalues-and-eigenvectors]], [[matrix-operations]], [[special-matrices]], [[matrix-inverse]], [[projection]]
**Tags**: #status/seed

## Core Idea

SVD breaks **any** matrix into an ingredient list — same idea as
[[spectral-decomposition]], but works on every matrix (non-symmetric,
non-square, anything).

```
Spectral: A = Q L Q^T     (only symmetric matrices)
SVD:      A = U S V^T     (ANY matrix)
```

Each ingredient is a singular value (the strength) times a piece built from
two vectors (one for each side):

```
A = sigma1 * (u1 @ v1^T) + sigma2 * (u2 @ v2^T) + ...
```

The sigmas are called **singular values** — always positive, and they tell you
how important each piece is. Bigger sigma = more important direction.

## Details

### Why We Need SVD

[[spectral-decomposition]] requires A = A^T (symmetric) and square. But most
real data isn't:
- Training data: 1000 samples x 50 features (not square)
- Images: pixel matrices (not symmetric)
- Any transformation between different-sized spaces

SVD says: give me any matrix, any shape, I'll decompose it.

### The Formula

$$A = U \Sigma V^T$$

For $A \in \mathbb{R}^{m \times n}$:
- $U \in \mathbb{R}^{m \times m}$ — orthogonal (columns are "left singular vectors")
- $\Sigma \in \mathbb{R}^{m \times n}$ — diagonal (singular values on diagonal, rest zeros)
- $V \in \mathbb{R}^{n \times n}$ — orthogonal (columns are "right singular vectors")

### Where Singular Values Come From

A might not be symmetric, but $A^T A$ is **always** symmetric:

```
(A^T A)^T = A^T (A^T)^T = A^T A    <- always equals itself
```

So we can apply eigendecomposition to $A^T A$:

```
Step 1: Compute A^T @ A              (always symmetric, always works)
Step 2: Find eigenvalues of A^T @ A  (characteristic equation)
Step 3: Singular values = sqrt(eigenvalues)
Step 4: V = eigenvectors of A^T @ A
Step 5: U = A @ V / singular values  (one column at a time)
```

### Worked Example

$$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$

**Step 1 — Compute A^T @ A:**

```
A^T @ A = [[1,0],  @  [[1,1],  = [[1, 1],
            [1,1]]     [0,1]]     [1, 2]]
```

**Step 2 — Eigenvalues of A^T @ A:**

```
det([[1-L, 1], [1, 2-L]]) = 0
(1-L)(2-L) - 1 = 0
L^2 - 3L + 1 = 0

L = (3 +- sqrt(5)) / 2
L1 = 2.618,  L2 = 0.382
```

**Step 3 — Singular values:**

```
sigma1 = sqrt(2.618) = 1.618
sigma2 = sqrt(0.382) = 0.618
```

**Step 4 — V (eigenvectors of A^T @ A):**

For L1 = 2.618: solve (A^T A - 2.618 I) v = 0
For L2 = 0.382: solve (A^T A - 0.382 I) v = 0

(Normalize each to unit length)

**Step 5 — U (computed from A, V, and sigmas):**

```
u1 = A @ v1 / sigma1
u2 = A @ v2 / sigma2
```

### Connection to Spectral Decomposition

For symmetric matrices, SVD and spectral decomposition give the same result:
- U = V = Q (the eigenvectors)
- Singular values = absolute values of eigenvalues

SVD is strictly more general — it works where spectral decomposition can't.

### Killer Application: Low-Rank Approximation

Same idea as spectral decomposition, but now for ANY matrix. Sort singular
values from largest to smallest, keep only the top k:

```
Full:   A = sigma1*(u1@v1^T) + sigma2*(u2@v2^T) + ... + sigmaR*(uR@vR^T)
Rank-k: A_k = sigma1*(u1@v1^T) + ... + sigmak*(uk@vk^T)
```

The **Eckart-Young theorem** guarantees: this is the BEST possible rank-k
approximation. No other rank-k matrix gets closer to A.

**Image compression example:**
- A 1000x1000 image = 1,000,000 numbers
- Keep top 50 singular values: 50*(1000+1000+1) = ~100,050 numbers
- 10x compression with minimal visual loss

**Variance captured** by keeping top k:

$$\frac{\sum_{i=1}^{k} \sigma_i^2}{\sum_{i=1}^{r} \sigma_i^2}$$

### Key Applications in ML

| Application | How SVD is used |
|-------------|----------------|
| PCA | SVD of centered data matrix (numerically stable way to compute PCA) |
| Image compression | Keep top-k singular values, reconstruct |
| Recommender systems | Factor user-item matrix into preferences x features |
| Pseudoinverse | $A^+ = V \Sigma^+ U^T$ (solve Ax=b even when A isn't invertible) |
| Noise reduction | Small singular values = noise, drop them |
| Latent Semantic Analysis | SVD of term-document matrix reveals topics |

### Key Properties

| Property | Formula |
|----------|---------|
| Singular values are non-negative | $\sigma_i \geq 0$ always |
| Number of non-zero sigmas = rank | rank(A) = count of $\sigma_i > 0$ |
| Frobenius norm | $\|A\|_F = \sqrt{\sum \sigma_i^2}$ |
| Condition number | $\kappa(A) = \sigma_{max} / \sigma_{min}$ (how "ill-conditioned") |
| Pseudoinverse | $A^+ = V \Sigma^+ U^T$ where $\Sigma^+$ inverts non-zero sigmas |

## Code Example

```python
import numpy as np

A = np.array([[1, 1],
              [0, 1]], dtype=float)

# NumPy SVD
U, sigmas, Vt = np.linalg.svd(A)
# sigmas = [1.618, 0.618]

# Rebuild A from SVD
S = np.zeros_like(A)
np.fill_diagonal(S, sigmas)
A_rebuilt = U @ S @ Vt
print(np.allclose(A, A_rebuilt))  # True

# Low-rank approximation (keep top 1)
k = 1
A_approx = sigmas[0] * np.outer(U[:, 0], Vt[0, :])

# Verify: singular values come from eigenvalues of A^T @ A
eigvals = np.linalg.eigvalsh(A.T @ A)
print(np.allclose(sorted(sigmas**2), sorted(eigvals)))  # True
```

> For runnable implementation with exercises, see: [[code/foundations/svd.py]]

## Connections

- [[spectral-decomposition]] — SVD generalizes this to non-symmetric/non-square matrices
- [[eigenvalues-and-eigenvectors]] — singular values = sqrt(eigenvalues of A^T A)
- [[special-matrices]] — U and V are orthogonal, S is diagonal
- [[matrix-inverse]] — pseudoinverse via SVD works even for singular/non-square matrices
- [[projection]] — low-rank approximation projects data onto the top singular directions
- Forward link: PCA — computed via SVD of the centered data matrix
- Forward link: recommender systems — matrix factorization

## Sources

- [3Blue1Brown — SVD (if available)](https://www.3blue1brown.com/) — visual intuition
- [MIT 18.06 — Strang, Lecture 29: Singular Value Decomposition](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Steve Brunton — SVD YouTube series](https://www.youtube.com/watch?v=gXbThCXjZFM) — excellent visual + applied
- [Mathematics for Machine Learning — Chapter 4.5](https://mml-book.github.io/book/mml-book.pdf)
- [Gregory Gundersen — SVD as Change of Basis](https://gregorygundersen.com/blog/2018/12/10/svd/)
