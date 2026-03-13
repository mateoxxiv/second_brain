**Related**: [[matrix-operations]], [[determinant]], [[gaussian-elimination]], [[linear-independence]], [[eigenvalues-and-eigenvectors]], [[projection-onto-subspaces]]
**Tags**: #status/growing

## Core Idea

If matrix $A$ transforms space, then $A^{-1}$ **undoes** that transformation.
It only exists when $A$ doesn't collapse any dimension ($\det(A) \neq 0$).

$$AA^{-1} = A^{-1}A = I$$

**Geometric intuition**: When $\det(A) = 0$, the transformation **collapses a
dimension** — it squishes 2D space onto a line, or 3D space onto a plane.
Information is destroyed (multiple inputs map to the same output), so you can't
reverse it. It's like trying to "un-blend" a smoothie back into separate fruits.

## Details

### 2x2 Formula

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

The $ad - bc$ is the [[determinant]]. If it's zero, no inverse exists.

**Recipe**: swap the diagonal, negate the off-diagonal, divide by det.

### Worked Example

$$A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}, \quad \det(A) = 24 - 14 = 10$$

$$A^{-1} = \frac{1}{10}\begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}$$

Verify: $AA^{-1} = I$ ✓

### Inverse of Larger Matrices (via Gaussian Elimination)

For matrices bigger than 2x2, use [[gaussian-elimination]]: place A and the
identity matrix side by side, then row-reduce A to I. Whatever operations you
apply to I produce $A^{-1}$.

```
Start:     [A | I]
Reduce:    [I | A^{-1}]
```

Same row operations you already know — just applied to a wider augmented matrix.
If at any point a row of A becomes all zeros, det = 0 and no inverse exists.

**3x3 Worked Example**:

$$A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 2 & 1 \\ 1 & 1 & 1 \end{bmatrix}$$

```
[1 0 1 | 1 0 0]
[0 2 1 | 0 1 0]
[1 1 1 | 0 0 1]

R3 = R3 - R1:
[1 0 1 | 1  0  0]
[0 2 1 | 0  1  0]
[0 1 0 | -1 0  1]

Swap R2, R3:
[1 0 1 | 1  0  0]
[0 1 0 | -1 0  1]
[0 2 1 | 0  1  0]

R3 = R3 - 2*R2:
[1 0 1 | 1  0  0]
[0 1 0 | -1 0  1]
[0 0 1 | 2  1  -2]

R1 = R1 - R3:
[1 0 0 | -1 -1  2]
[0 1 0 | -1  0  1]
[0 0 1 | 2   1  -2]
```

$$A^{-1} = \begin{bmatrix} -1 & -1 & 2 \\ -1 & 0 & 1 \\ 2 & 1 & -2 \end{bmatrix}$$

### Solving Ax = b

The whole point of the inverse in practice: solving systems of equations.

$$A\mathbf{x} = \mathbf{b} \implies \mathbf{x} = A^{-1}\mathbf{b}$$

Where $A$ = coefficient matrix, $\mathbf{x}$ = unknowns, $\mathbf{b}$ = right-hand side.

### "Don't Invert That Matrix"

In practice, **almost never compute the inverse directly**:

1. **Numerical instability** — floating-point errors amplify through inversion
2. **Computational cost** — solving $Ax = b$ via LU decomposition is faster
   and more stable
3. **Memory** — a sparse matrix's inverse is typically dense

**Use instead**: `np.linalg.solve(A, b)` — think of it as "division for
matrices." It uses [[gaussian-elimination]] (LU decomposition) internally.
For least squares: `np.linalg.lstsq()`.

### Key Properties

| Property | Rule | Intuition |
|----------|------|-----------|
| Self-inverse | $(A^{-1})^{-1} = A$ | Undo the undo = original |
| Inverse of product | $(AB)^{-1} = B^{-1}A^{-1}$ | Undo last step first ("socks and shoes") |
| Transpose of inverse | $(A^T)^{-1} = (A^{-1})^T$ | Transpose and inverse commute |
| Inverse of scalar multiple | $(cA)^{-1} = \frac{1}{c}A^{-1}$ | Undo the scaling too |
| Determinant of inverse | $\det(A^{-1}) = \frac{1}{\det(A)}$ | Inverse reverses the volume scaling |

### When Does the Inverse Exist?

All of these are equivalent — they all say the same thing:

- $\det(A) \neq 0$
- $A$ has no zero [[eigenvalues-and-eigenvectors|eigenvalues]]
- Columns of $A$ are [[linear-independence|linearly independent]]
- $A$ has full rank (rank = number of rows/columns)
- $A\mathbf{x} = \mathbf{0}$ has only the trivial solution
- $A\mathbf{x} = \mathbf{b}$ has exactly one solution for every $\mathbf{b}$

When $A$ is NOT invertible, it's called **singular**.

## Code Example

```python
import numpy as np

A = np.array([[4, 7], [2, 6]])
b = np.array([1, 2])

# Preferred: solve directly (faster, more stable)
x = np.linalg.solve(A, b)        # [0.8, -0.2]

# Avoid: computing inverse explicitly
x_bad = np.linalg.inv(A) @ b     # same answer, worse numerics

# Check if matrix is invertible
det = np.linalg.det(A)            # 10.0 (non-zero = invertible)

# Verify inverse
A_inv = np.linalg.inv(A)
print(A @ A_inv)                  # identity matrix
```

> For runnable implementation with exercises, see: [[code/foundations/matrix_operations.py]]

## Connections

- [[determinant]] — det = 0 means no inverse exists; det tells you how much A scales area/volume
- [[gaussian-elimination]] — the practical algorithm for computing inverses and solving Ax = b
- [[linear-independence]] — columns independent ↔ matrix invertible
- [[eigenvalues-and-eigenvectors]] — eigenvalue = 0 ↔ matrix singular (not invertible)
- [[projection-onto-subspaces]] — projection formula uses $(A^TA)^{-1}$
- [[special-matrices]] — orthogonal matrices have $Q^{-1} = Q^T$ (free inverse!)
- Forward link: regularization adds $\lambda I$ to ensure invertibility

## Sources

- [3Blue1Brown — Inverse Matrices](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- [Gregory Gundersen — "Don't Invert That Matrix"](https://gregorygundersen.com/blog/2020/12/09/matrix-inversion/)
- [MIT 18.06 — Gilbert Strang, Lecture 3: Multiplication and Inverse Matrices](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.2](https://mml-book.github.io/book/mml-book.pdf)
