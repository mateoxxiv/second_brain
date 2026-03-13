**Related**: [[eigenvalues-and-eigenvectors]], [[matrix-operations]], [[special-matrices]], [[matrix-inverse]], [[projection]], [[linear-combination]]
**Tags**: #status/growing

## Core Idea

Spectral decomposition breaks a symmetric matrix into its **ingredient list**:
each ingredient is an eigenvalue (the strength) times a direction piece (built
from one eigenvector).

```
A = lambda1 * (q1 @ q1^T) + lambda2 * (q2 @ q2^T) + ...
```

Each piece q_i @ q_i^T is a [[projection]] matrix onto that eigenvector's
direction. The eigenvalue tells you how much weight that direction carries.

Written compactly: $A = Q \Lambda Q^T$, where Q packs the eigenvectors as
columns and Lambda is the diagonal matrix of eigenvalues.

## Details

### Building It From Eigenvalues

Start with A = [[2,1],[1,2]]. We already know from [[eigenvalues-and-eigenvectors]]:

```
lambda = 1  ->  eigenvector [1,-1]  ->  normalized: q1 = [0.707, -0.707]
lambda = 3  ->  eigenvector [1, 1]  ->  normalized: q2 = [0.707,  0.707]
```

Build the "direction piece" for each eigenvector using the outer product
(column times row = matrix):

```
q1 @ q1^T = [0.707]  @ [0.707, -0.707] = [[ 0.5, -0.5],
            [-0.707]                       [-0.5,  0.5]]

q2 @ q2^T = [0.707] @ [0.707, 0.707] = [[0.5, 0.5],
            [0.707]                      [0.5, 0.5]]
```

Each of these is a projection matrix — it takes any vector and returns only
the part pointing along that eigenvector.

Now rebuild A by weighting each piece by its eigenvalue:

```
A = 1 * [[ 0.5, -0.5],   +   3 * [[0.5, 0.5],
         [-0.5,  0.5]]            [0.5, 0.5]]

  = [[ 0.5, -0.5],       +   [[1.5, 1.5],
     [-0.5,  0.5]]             [1.5, 1.5]]

  = [[2, 1],
     [1, 2]]   <- that's A!
```

### The Compact Formula: A = Q Lambda Q^T

**How to build each piece** (no computation — just packing values):

```
Step 1: Find eigenvalues and eigenvectors (you already know how)
   lambda1 = 1,  q1 = [0.707, -0.707]
   lambda2 = 3,  q2 = [0.707,  0.707]

Step 2: Pack eigenvectors as COLUMNS into Q
   Q = [q1 | q2] = [[0.707,  0.707],     <- first column is q1
                     [-0.707, 0.707]]     <- second column is q2

Step 3: Put eigenvalues on the diagonal of Lambda
   Lambda = [[1, 0],     <- lambda1
             [0, 3]]     <- lambda2

Step 4: Q^T is just Q transposed (flip rows and columns)
   Q^T = [[ 0.707, -0.707],
          [ 0.707,  0.707]]
```

Now multiply Q @ Lambda @ Q^T to verify it equals A:

Compute step by step:

**Step 1 — Q @ Lambda** (scales each column by its eigenvalue):

```
[[0.707*1,  0.707*3],    = [[0.707,  2.121],
 [-0.707*1, 0.707*3]]       [-0.707, 2.121]]
```

**Step 2 — result @ Q^T**:

```
[[0.707,  2.121],  @  [[0.707, -0.707],
 [-0.707, 2.121]]      [0.707,  0.707]]

= [[0.5+1.5,  -0.5+1.5],   = [[2, 1],
   [-0.5+1.5,  0.5+1.5]]      [1, 2]]   <- A!
```

### Why This Only Works for Symmetric Matrices

The Spectral Theorem (from [[special-matrices]]) guarantees that symmetric
matrices have:

1. **Real eigenvalues** — so Lambda has real numbers
2. **Orthogonal eigenvectors** — so $Q^T = Q^{-1}$ (free inverse)

Without orthogonal eigenvectors, $Q^{-1} \neq Q^T$ and you'd need the more
general form $A = V \Lambda V^{-1}$ (which requires computing an actual
inverse — more expensive and less stable).

### Killer Application: Matrix Powers

Without spectral decomposition:

```
A^10 = A @ A @ A @ A @ A @ A @ A @ A @ A @ A    (9 matrix multiplications)
```

With spectral decomposition:

```
A^10 = Q Lambda^10 Q^T
```

And Lambda^10 is trivial — just raise each diagonal entry to the 10th power:

```
Lambda^10 = [[1^10,  0   ],    = [[1,     0    ],
              [0,    3^10]]       [0, 59049]]
```

This works because the Q^T and Q in the middle cancel:

```
A^2 = (Q L Q^T)(Q L Q^T) = Q L (Q^T @ Q) L Q^T = Q L I L Q^T = Q L^2 Q^T
```

### Killer Application: Low-Rank Approximation

The ingredient list formula lets you **approximate** a matrix by keeping only
the most important pieces:

```
Full:    A = 3 * (piece from q2) + 1 * (piece from q1)
Approx:  A_approx = 3 * (piece from q2)    <- drop the small eigenvalue
```

```
A_approx = 3 * [[0.5, 0.5],    = [[1.5, 1.5],
                [0.5, 0.5]]       [1.5, 1.5]]
```

Not perfect, but captures 75% of the "energy" (3 out of 3+1 = 4).

This is exactly what **PCA** does:
- Data has a covariance matrix (symmetric)
- Decompose it into eigenvalue-weighted directions
- Keep only the top-k eigenvalues
- You compressed the data while keeping the most important variation

Variance explained by keeping top-k: $\frac{\sum_{i=1}^{k} \lambda_i}{\sum_{i=1}^{n} \lambda_i}$

### Key Properties

| Property | Formula | Why it helps |
|----------|---------|-------------|
| Matrix powers | $A^k = Q\Lambda^k Q^T$ | Raise diagonal entries to power k |
| Inverse | $A^{-1} = Q\Lambda^{-1}Q^T$ | Invert diagonal entries |
| Trace | $\text{tr}(A) = \sum \lambda_i$ | Sum of eigenvalues |
| Determinant | $\det(A) = \prod \lambda_i$ | Product of eigenvalues |
| Rank | rank = number of non-zero eigenvalues | Count the ingredients |
| Positive definite | All $\lambda_i > 0$ | Check the diagonal |

## Code Example

```python
import numpy as np

A = np.array([[2, 1], [1, 2]], dtype=float)

# Decompose
eigenvalues, Q = np.linalg.eigh(A)  # eigh for symmetric
Lambda = np.diag(eigenvalues)

# Rebuild: A = Q @ Lambda @ Q^T
A_rebuilt = Q @ Lambda @ Q.T
print(np.allclose(A, A_rebuilt))     # True

# Matrix power the easy way
k = 10
A_power = Q @ np.diag(eigenvalues**k) @ Q.T

# Low-rank approximation (keep top-1 eigenvalue)
top = np.argmax(eigenvalues)
q_top = Q[:, top:top+1]
A_approx = eigenvalues[top] * (q_top @ q_top.T)

# Ingredient list form
A_sum = sum(lam * np.outer(q, q)
            for lam, q in zip(eigenvalues, Q.T))
print(np.allclose(A, A_sum))         # True
```

> For runnable implementation with exercises, see: [[code/foundations/eigenvalues_and_eigenvectors.py]]

## Connections

- [[eigenvalues-and-eigenvectors]] — the ingredients (eigenvalues + eigenvectors) that this decomposition uses
- [[special-matrices]] — only works for symmetric matrices (Spectral Theorem)
- [[projection]] — each $q_i q_i^T$ is a projection onto the eigenvector direction
- [[linear-combination]] — A is a linear combination of rank-1 projection matrices
- [[matrix-inverse]] — inverse is trivial: just invert the diagonal eigenvalues
- Forward link: PCA — spectral decomposition of the covariance matrix
- Forward link: SVD — generalizes this to non-symmetric and non-square matrices

## Sources

- [3Blue1Brown — Eigenvectors and Eigenvalues](https://www.3blue1brown.com/lessons/eigenvalues) — visual decomposition intuition
- [MIT 18.06 — Strang, Lecture 22: Diagonalization](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Hadrienj — Eigendecomposition](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.7-Eigendecomposition/) — Python examples
- [Mathematics for Machine Learning — Chapter 4.2](https://mml-book.github.io/book/mml-book.pdf) — spectral theorem + PCA connection
