**Related**: [[vectors-and-vector-spaces]], [[vector-operations]], [[vector-norms]], [[cosine-similarity]], [[determinant]], [[linear-independence]], [[gaussian-elimination]], [[basis-and-dimension]], [[projection]], [[projection-onto-subspaces]], [[linear-combination]], [[matrix-inverse]], [[special-matrices]]
**Tags**: #status/evergreen

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

### Matrix Addition and Subtraction

Add or subtract matrices **element by element**. Both matrices must have the
same dimensions — you can't add a 2x3 to a 3x2.

```
A = [[1, 2],    B = [[5, 6],
     [3, 4]]         [7, 8]]

A + B = [[1+5, 2+6],   = [[6,  8],
         [3+7, 4+8]]      [10, 12]]

A - B = [[1-5, 2-6],   = [[-4, -4],
         [3-7, 4-8]]      [-4, -4]]
```

**Scalar multiplication** works the same way — multiply every element:

```
3 * A = [[3, 6],
         [9, 12]]
```

**Properties**:
- $A + B = B + A$ — commutative (order doesn't matter, unlike multiplication!)
- $(A + B) + C = A + (B + C)$ — associative
- $A + 0 = A$ — the zero matrix is the identity element
- $c(A + B) = cA + cB$ — scalar distributes over addition

**Where it shows up**: In [[eigenvalues-and-eigenvectors]], the characteristic
equation requires A - lambda * I — that's matrix subtraction between A and a
scaled identity matrix.

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

See [[matrix-inverse]] for the full note. Key points:

- $A^{-1}$ undoes the transformation: $AA^{-1} = I$
- Only exists when $\det(A) \neq 0$
- 2x2 formula: swap diagonal, negate off-diagonal, divide by det
- Larger matrices: [[gaussian-elimination]] on $[A | I] \to [I | A^{-1}]$
- **In practice**: use `np.linalg.solve(A, b)` instead of computing the inverse

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

See [[special-matrices]] for the full note. Quick reference:

| Type | Definition | Key property |
|------|-----------|-------------|
| **Symmetric** | $A = A^T$ | Real eigenvalues, orthogonal eigenvectors |
| **Diagonal** | zeros off-diagonal | Eigenvalues = diagonal entries |
| **Triangular** | zeros above or below diagonal | det = product of diagonal |
| **Orthogonal** | $Q^TQ = I$ | Preserves lengths, $Q^{-1} = Q^T$ |
| **Singular** | $\det = 0$ | Not invertible |
| **Positive definite** | $\mathbf{x}^TA\mathbf{x} > 0$ | All eigenvalues positive |

## Code Example

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# --- Addition / Subtraction ---
print(A + B)         # [[6, 8], [10, 12]]
print(A - B)         # [[-4, -4], [-4, -4]]
print(3 * A)         # [[3, 6], [9, 12]]

# --- Transpose ---
print(A.T)           # [[1, 3], [2, 4]]

# --- Dot product = transpose multiply ---
x, y = np.array([1, 2, 3]), np.array([4, 5, 6])
print(x @ y)         # 32 (dot product)

# --- Matrix multiplication (not commutative!) ---
print(A @ B)         # [[19, 22], [43, 50]]
print(B @ A)         # [[23, 34], [31, 46]] — different!
```

> For runnable implementation, see: [[code/foundations/matrix_operations.py]]

## Connections

- Matrix columns are [[vectors-and-vector-spaces|vectors]] — the column space is a subspace
- Matrix multiplication is organized [[vector-operations|dot products]]
- [[determinant]] tells you whether a matrix is invertible and how it scales area/volume
- [[linear-independence]] of columns ↔ matrix is invertible ↔ $\det \neq 0$
- [[gaussian-elimination]] is the practical way to solve $Ax = b$ (LU decomposition)
- [[matrix-inverse]] — undoing transformations, solving systems
- [[special-matrices]] — symmetric, orthogonal, diagonal, singular, positive definite
- [[projection-onto-subspaces]] — normal equations use transpose and inverse
- [[eigenvalues-and-eigenvectors]] — special vectors that only get scaled by $A$
- Forward link: [[SVD]] — every matrix = orthogonal x diagonal x orthogonal

## Sources

- [3Blue1Brown — Linear Transformations and Matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE)
- [3Blue1Brown — Matrix Multiplication as Composition](https://www.youtube.com/watch?v=XkY2DOUCWMU)
- [3Blue1Brown — Inverse Matrices](https://www.youtube.com/watch?v=uQhTuRlWMxw)
- [MIT 18.06 — Gilbert Strang, Lectures 1-6](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.2-2.5](https://mml-book.github.io/book/mml-book.pdf)
- [Gregory Gundersen — "Don't Invert That Matrix"](https://gregorygundersen.com/blog/2020/12/09/matrix-inversion/)
