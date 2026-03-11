**Related**: [[vectors-and-vector-spaces]], [[vector-operations]], [[vector-norms]], [[cosine-similarity]], [[determinant]], [[linear-independence]], [[gaussian-elimination]], [[basis-and-dimension]], [[projection]], [[projection-onto-subspaces]], [[linear-combination]]
**Tags**: #status/growing

## Core Idea

A matrix is a rectangular grid of numbers that serves three roles at once: (1) a
**collection of column vectors** stacked side by side, (2) a **linear
transformation** that reshapes space, and (3) a **data table** where rows are
samples and columns are features. Every operation in ML — from the forward pass
of a neural network to solving for regression coefficients — is matrix
arithmetic.

## Details

### Three Ways to See a Matrix

**As column vectors**: A matrix $A \in \mathbb{R}^{m \times n}$ packages $n$
column vectors, each in $\mathbb{R}^m$. The columns of a weight matrix are
the "directions" the model can combine.

**As a transformation**: A matrix **redefines where the basic directions
point**. Normally "right" = [1,0] and "up" = [0,1]. A matrix changes those
rules. Every vector that says "3 steps right + 2 steps up" follows along
with the new directions.

```
Example: A = [[2, 0],
              [0, 3]]

Before (standard):   "right" = [1,0]     "up" = [0,1]
After (transformed): "right" = [2,0]     "up" = [0,3]

v = [3, 2] = 3·"right" + 2·"up"

Standard: 3·[1,0] + 2·[0,1] = [3, 2]
After A:  3·[2,0] + 2·[0,3] = [6, 6]
```

Column 1 = the new "right". Column 2 = the new "up". That's it. Matrix-vector
multiplication is a [[linear-combination]] of the columns using the vector's
components as coefficients:

$$A\mathbf{v} = v_1 \cdot \text{(column 1)} + v_2 \cdot \text{(column 2)} + \cdots$$

### How a Matrix Transforms a Vector (Step by Step)

Take $\mathbf{v} = [3, 2]$ and $A = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$:

**Step 1** — Break v into its basic directions:

$$\mathbf{v} = 3 \cdot [1,0] + 2 \cdot [0,1] \quad \text{(3 right + 2 up)}$$

**Step 2** — Read the new rules from A's columns:

$$\text{new "right"} = [1, 0] \quad \text{(unchanged)} \qquad \text{new "up"} = [0, 2] \quad \text{(twice as tall)}$$

**Step 3** — Apply the same recipe with new directions:

$$A\mathbf{v} = 3 \cdot [1,0] + 2 \cdot [0,2] = [3,0] + [0,4] = [3, 4]$$

The vector moved from (3, 2) to (3, 4). The x stayed, the y doubled. The
matrix **stretched space vertically**.

```
Before:          After:
    y                y
    |                |    * (3,4)
    |  * (3,2)       |
    |                |
    *----x           *----x
```

**Common transformations**:

| Matrix | What it does |
|--------|-------------|
| $\begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}$ | Uniform scaling (expand everything ×2) |
| $\begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$ | Vertical stretch only |
| $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | 90° rotation counterclockwise |
| $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ | Reflection over x-axis |
| $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$ | Collapse onto x-axis ($\det = 0$, not invertible) |

**As data**: In ML, an $m \times n$ matrix stores $m$ samples with $n$
features. Your entire training set is a matrix.

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \in \mathbb{R}^{m \times n}$$

### Matrix Transpose

Flip the matrix over its main diagonal — rows become columns, columns become
rows.

$$(A^T)_{ij} = A_{ji}$$

If $A \in \mathbb{R}^{m \times n}$, then $A^T \in \mathbb{R}^{n \times m}$.

**Worked example**:

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix} \implies A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

**Properties**:
- $(A^T)^T = A$ — transpose twice = back to original
- $(A + B)^T = A^T + B^T$ — transpose distributes over addition
- $(cA)^T = cA^T$ — scalars pass through
- $(AB)^T = B^TA^T$ — "socks and shoes" reversal (see Key Properties below)

**Key insight**: The [[vector-operations|dot product]] is transpose-then-multiply:

$$\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^T \mathbf{y}$$

This is why transpose appears everywhere in ML:
- **Normal equations**: $\hat{\beta} = (X^TX)^{-1}X^T\mathbf{y}$ — the $X^T$
  projects $\mathbf{y}$ onto the column space of $X$
- **Backpropagation**: Forward pass uses $W$, backward pass uses $W^T$ — the
  gradient flows through the transposed weights
- **Covariance matrix**: $\Sigma = \frac{1}{n-1}X^TX$ — transpose naturally
  captures feature-to-feature relationships

### Matrix Multiplication

Matrix multiplication = **composition of transformations**. If $A$ rotates
space and $B$ shears it, then $AB$ means "first apply $B$, then apply $A$."
Read right to left, like function composition $f(g(x))$.

$$(AB)_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj}$$

For $A \in \mathbb{R}^{m \times p}$ and $B \in \mathbb{R}^{p \times n}$, the
result is $\mathbb{R}^{m \times n}$. The **inner dimensions must match**.

**Worked example**:

$$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} = \begin{bmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

Each entry is a dot product: row $i$ of $A$ dotted with column $j$ of $B$.

#### Why NOT Commutative

$AB \neq BA$ in general. Geometric reason: rotating then shearing ≠ shearing
then rotating. Order of transformations matters.

```
AB = [[19, 22],     BA = [[23, 34],
      [43, 50]]           [31, 46]]     ← different!
```

#### ML Connection

A neural network forward pass is a chain of matrix multiplications with
nonlinearities:

$$\hat{y} = \sigma(W_3 \cdot \sigma(W_2 \cdot \sigma(W_1\mathbf{x} + b_1) + b_2) + b_3)$$

Without the nonlinearities $\sigma$, the entire network collapses to a single
matrix $W_3 W_2 W_1$ — this is why activation functions are essential.

### Identity Matrix

The "do nothing" transformation — like multiplying a number by 1.

$$I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix} \qquad AI = IA = A$$

**ML connection**: Skip connections in ResNets add the identity: $\mathbf{y} =
F(\mathbf{x}) + \mathbf{x}$. If $F$ learns to be zero, the layer acts as
identity. This is why deep ResNets train — at worst, a layer does nothing.
Ridge regularization adds $\lambda I$ to $X^TX$ to ensure invertibility.

### Matrix Inverse

If matrix $A$ transforms space, then $A^{-1}$ **undoes** that transformation.
It only exists when $A$ doesn't collapse any dimension ($\det(A) \neq 0$).

$$AA^{-1} = A^{-1}A = I$$

**Geometric intuition**: When $\det(A) = 0$, the transformation **collapses a
dimension** — it squishes 2D space onto a line, or 3D space onto a plane.
Information is destroyed (multiple inputs map to the same output), so you can't
reverse it. It's like trying to "un-blend" a smoothie back into separate fruits.

#### 2×2 Formula

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

The $ad - bc$ is the [[determinant]]. If it's zero, no inverse exists.

#### Worked Example

$$A = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}, \quad \det(A) = 24 - 14 = 10$$

$$A^{-1} = \frac{1}{10}\begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\ -0.2 & 0.4 \end{bmatrix}$$

Verify: $AA^{-1} = I$ ✓

#### Solving Ax = b

If $A$ is invertible: $A\mathbf{x} = \mathbf{b} \implies \mathbf{x} = A^{-1}\mathbf{b}$

#### "Don't Invert That Matrix"

In practice, **almost never compute the inverse directly**:

1. **Numerical instability** — floating-point errors amplify through inversion
2. **Computational cost** — solving $Ax = b$ via LU decomposition is faster
   and more stable
3. **Memory** — a sparse matrix's inverse is typically dense

**Use instead**: `np.linalg.solve(A, b)` which uses [[gaussian-elimination]]
(LU decomposition) internally. For least squares: `np.linalg.lstsq()`.

### Key Properties

| Property | Rule | Intuition |
|----------|------|-----------|
| Associativity | $(AB)C = A(BC)$ | Grouping transformations doesn't matter |
| Distributivity | $A(B+C) = AB + AC$ | Transform a sum = sum of transforms |
| NOT commutative | $AB \neq BA$ | Order matters |
| Transpose of product | $(AB)^T = B^TA^T$ | "Socks and shoes" rule |
| Inverse of product | $(AB)^{-1} = B^{-1}A^{-1}$ | Undo last step first |
| Transpose of inverse | $(A^T)^{-1} = (A^{-1})^T$ | Transpose and inverse commute |

**"Socks and shoes"**: To undo putting on socks then shoes, you take off
shoes first, then socks. Both transpose and inverse of products reverse the
order.

### Special Matrices

| Type | Definition | Key property | ML use |
|------|-----------|-------------|--------|
| **Symmetric** | $A = A^T$ | Eigenvalues always real, eigenvectors orthogonal | Covariance matrix $\Sigma = \frac{1}{n-1}X^TX$, PCA |
| **Diagonal** | $a_{ij} = 0$ for $i \neq j$ | Inverse = invert each diagonal entry | SVD ($\Sigma$), batch norm scaling |
| **Triangular** | Zeros above (lower) or below (upper) diagonal | det = product of diagonal | LU decomposition, `np.linalg.solve` |
| **Orthogonal** | $Q^TQ = I$, so $Q^{-1} = Q^T$ | Preserves lengths and angles | Orthogonal weight init, QR decomposition, PCA eigenvectors |

**Orthogonal matrices** deserve special attention: their inverse is just the
transpose (free computation), and they preserve norms
($\|Q\mathbf{x}\| = \|\mathbf{x}\|$). In deep learning, orthogonal weight
initialization prevents vanishing/exploding gradients because all eigenvalues
have absolute value 1.

## Code Example

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# --- Transpose ---
print(A.T)           # [[1, 3], [2, 4]]

# --- Dot product = transpose multiply ---
x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
print(x @ y)         # 32 (dot product)
print(x.T @ y)       # 32 (same thing)

# --- Matrix multiplication ---
print(A @ B)         # [[19, 22], [43, 50]]
print(B @ A)         # [[23, 34], [31, 46]] — different!

# --- Inverse (but prefer solve!) ---
A = np.array([[4, 7], [2, 6]])
b = np.array([1, 2])
x_solve = np.linalg.solve(A, b)     # ✓ use this
x_inv = np.linalg.inv(A) @ b        # ✗ avoid this

# --- Orthogonal matrix (rotation by 45°) ---
theta = np.pi / 4
Q = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
print(Q.T @ Q)                       # ≈ identity
print(np.linalg.norm(Q @ [1, 0]))    # 1.0 (norm preserved)
```

> For runnable implementation, see: [[code/foundations/matrix_operations.py]]

## Connections

- Matrix columns are [[vectors-and-vector-spaces|vectors]] — the column space is a subspace
- Matrix multiplication is organized [[vector-operations|dot products]]
- [[determinant]] tells you whether a matrix is invertible and how it scales area/volume
- [[linear-independence]] of columns ↔ matrix is invertible ↔ $\det \neq 0$
- [[gaussian-elimination]] is the practical way to solve $Ax = b$ (LU decomposition)
- [[projection]] formula $A(A^TA)^{-1}A^T\mathbf{b}$ uses transpose and inverse
- The normal equations for linear regression come directly from [[projection-onto-subspaces]]
- Forward link: [[Eigenvalues and Eigenvectors]] — special vectors that only get scaled by $A$
- Forward link: [[SVD]] — every matrix = orthogonal × diagonal × orthogonal

## Sources

- [3Blue1Brown — Linear Transformations and Matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- [3Blue1Brown — Matrix Multiplication as Composition](https://www.youtube.com/watch?v=XkY2DOUCWMU)
- [3Blue1Brown — Inverse Matrices](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- [MIT 18.06 — Gilbert Strang, Lectures 1-6](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.2-2.5](https://mml-book.github.io/book/mml-book.pdf)
- [Gregory Gundersen — "Don't Invert That Matrix"](https://gregorygundersen.com/blog/2020/12/09/matrix-inversion/)
