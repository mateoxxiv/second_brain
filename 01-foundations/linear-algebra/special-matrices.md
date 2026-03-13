**Related**: [[matrix-operations]], [[matrix-inverse]], [[determinant]], [[eigenvalues-and-eigenvectors]], [[linear-independence]], [[basis-and-dimension]]
**Tags**: #status/growing

## Core Idea

Not all matrices are created equal. Certain structures — symmetry, orthogonality,
diagonality — give matrices powerful properties that simplify computation and
guarantee nice behavior. Recognizing these structures is essential because they
appear everywhere in ML: covariance matrices are symmetric, rotation matrices are
orthogonal, and SVD produces all three types at once.

## Details

### Symmetric Matrices ($A = A^T$)

A matrix that mirrors across its main diagonal. Entry $(i,j)$ equals entry $(j,i)$.

$$A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} = A^T$$

**Why they matter**: The Spectral Theorem guarantees:
1. All [[eigenvalues-and-eigenvectors|eigenvalues]] are **real** (no complex numbers)
2. Eigenvectors for distinct eigenvalues are **orthogonal**
3. Can be decomposed as $A = Q\Lambda Q^T$ (spectral decomposition)

**Where they show up**:
- **Covariance matrix**: $\Sigma = \frac{1}{n-1}X^TX$ — always symmetric by construction
- **Gram matrix**: $X^TX$ — measures similarity between features
- **Hessian**: second-derivative matrix of a smooth function — symmetric by Schwarz's theorem
- **Kernel matrices**: in SVMs and Gaussian processes

**Quick check**: if you can build a matrix as $B^TB$ or $B + B^T$, it's symmetric.

### Diagonal Matrices

Only non-zero entries are on the main diagonal. Everything else is zero.

$$D = \begin{bmatrix} 3 & 0 \\ 0 & 5 \end{bmatrix}$$

**Properties** (all operations are trivial):
- **Multiply**: $D\mathbf{v}$ scales each component independently: $[3x, 5y]$
- **Inverse**: flip each diagonal entry: $D^{-1} = \text{diag}(1/3, 1/5)$
- **Determinant**: product of diagonal entries: $\det(D) = 15$
- **Eigenvalues**: the diagonal entries ARE the eigenvalues
- **Powers**: $D^k = \text{diag}(d_1^k, d_2^k, \ldots)$

**Where they show up**:
- The $\Lambda$ in spectral decomposition $A = Q\Lambda Q^T$
- The $\Sigma$ in SVD: $A = U\Sigma V^T$
- Batch normalization scaling parameters

### Triangular Matrices

**Upper triangular**: zeros below the diagonal. **Lower triangular**: zeros above.

$$U = \begin{bmatrix} 2 & 3 & 1 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix} \qquad L = \begin{bmatrix} 2 & 0 & 0 \\ 3 & 4 & 0 \\ 1 & 5 & 6 \end{bmatrix}$$

**Properties**:
- **Determinant** = product of diagonal entries (no expansion needed)
- **Solving** $Ux = b$ is trivial: back-substitution (start from bottom row)
- **Solving** $Lx = b$ is trivial: forward-substitution (start from top row)

**Where they show up**:
- LU decomposition: $A = LU$ — this is what `np.linalg.solve` does internally
- [[gaussian-elimination]] produces upper triangular form
- Cholesky decomposition: $A = LL^T$ for positive definite matrices

### Orthogonal Matrices ($Q^TQ = I$)

A matrix whose columns are orthonormal (unit length + mutually perpendicular).
The inverse is just the transpose: $Q^{-1} = Q^T$.

$$Q = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \quad \text{(rotation by } \theta\text{)}$$

**Properties**:
- **Preserves lengths**: $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ — no stretching or shrinking
- **Preserves angles**: dot products unchanged: $(Q\mathbf{x}) \cdot (Q\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$
- **Free inverse**: $Q^{-1} = Q^T$ — no computation needed
- **$\det(Q) = \pm 1$**: +1 for rotations, -1 for reflections
- **Eigenvalues** have $|\lambda| = 1$ — no growing, no shrinking

**Where they show up**:
- PCA: eigenvectors of symmetric matrices form an orthogonal matrix $Q$
- QR decomposition: $A = QR$ (used in eigenvalue algorithms)
- Orthogonal weight initialization — prevents vanishing/exploding gradients because all eigenvalues have $|\lambda| = 1$

### Singular Matrices ($\det = 0$)

A matrix that **collapses a dimension** — it's not invertible.

$$S = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \quad \det = 4 - 4 = 0$$

Row 2 is 2x row 1 — the columns are [[linear-independence|linearly dependent]].
This matrix maps all of 2D space onto a single line.

**Equivalent statements** (all mean the same thing):
- $\det(A) = 0$
- $A$ has a zero [[eigenvalues-and-eigenvectors|eigenvalue]]
- Columns are linearly dependent
- $A\mathbf{x} = \mathbf{0}$ has non-trivial solutions
- $A$ has no [[matrix-inverse|inverse]]
- Rank < number of columns

### Positive Definite Matrices

A symmetric matrix where $\mathbf{x}^T A \mathbf{x} > 0$ for every non-zero
vector $\mathbf{x}$. Think of it as a matrix that always "curves upward" — like
a bowl shape.

**Equivalent statements**:
- All eigenvalues are **positive**
- All pivots (from [[gaussian-elimination]]) are positive
- $A = B^TB$ for some matrix $B$ with independent columns

**Where they show up**:
- Covariance matrices are positive **semi**-definite (eigenvalues $\geq 0$)
- Hessians of convex loss functions are positive definite at the minimum
- Guarantees a unique minimum in optimization

### Quick Reference Table

| Type | Definition | Key property | ML use |
|------|-----------|-------------|--------|
| Symmetric | $A = A^T$ | Real eigenvalues, orthogonal eigenvectors | Covariance, PCA, Hessians |
| Diagonal | $a_{ij} = 0$ for $i \neq j$ | Trivial inverse, eigenvalues = diagonal | SVD, batch norm |
| Triangular | Zeros above or below diagonal | det = product of diagonal, easy to solve | LU decomposition |
| Orthogonal | $Q^TQ = I$ | Preserves lengths, $Q^{-1} = Q^T$ | Rotations, PCA, weight init |
| Singular | $\det = 0$ | Not invertible, collapses a dimension | Feature redundancy |
| Positive definite | $\mathbf{x}^TA\mathbf{x} > 0$ | All eigenvalues positive | Convex optimization |

## Code Example

```python
import numpy as np

# --- Symmetric ---
A = np.array([[2, 1], [1, 3]])
print(np.allclose(A, A.T))          # True

# --- Diagonal ---
D = np.diag([3, 5])
print(np.linalg.inv(D))             # diag(1/3, 1/5)

# --- Orthogonal (rotation 45 degrees) ---
t = np.pi / 4
Q = np.array([[np.cos(t), -np.sin(t)],
              [np.sin(t),  np.cos(t)]])
print(np.allclose(Q.T @ Q, np.eye(2)))  # True (Q^T = Q^-1)
print(np.linalg.norm(Q @ [3, 4]))       # 5.0 (same as [3,4])

# --- Positive definite check ---
eigenvalues = np.linalg.eigvalsh(A)
print(all(eigenvalues > 0))          # True — positive definite

# --- Singular ---
S = np.array([[1, 2], [2, 4]])
print(np.linalg.det(S))             # 0.0 — singular!
```

> For runnable implementation with exercises, see: [[code/foundations/matrix_operations.py]]

## Connections

- [[matrix-operations]] — these are all special cases of general matrices
- [[matrix-inverse]] — orthogonal matrices have free inverses; singular matrices have none
- [[determinant]] — det distinguishes invertible from singular, and equals eigenvalue product
- [[eigenvalues-and-eigenvectors]] — symmetric → real eigenvalues; orthogonal → $|\lambda|=1$; singular → $\lambda=0$
- [[linear-independence]] — singular matrices have dependent columns
- [[spectral-decomposition]] — uses symmetric + diagonal + orthogonal together ($A = Q\Lambda Q^T$)
- Forward link: SVD decomposes ANY matrix into orthogonal x diagonal x orthogonal

## Sources

- [3Blue1Brown — Inverse Matrices (covers singular)](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- [MIT 18.06 — Strang, Lecture 5: Transposes, Permutations, Spaces](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.6: Special Matrices](https://mml-book.github.io/book/mml-book.pdf)
- [Hadrienj — Positive Definite Matrices](https://hadrienj.github.io/posts/Deep-Learning-Book-Series-2.7-Eigendecomposition/)
