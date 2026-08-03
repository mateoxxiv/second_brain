---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[matrix-operations]]"
  - "[[special-matrices]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[euclidean-n-space]]"
  - "[[row-and-column-spaces]]"
domain: linear-algebra
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — A matrix is a rectangular array of numbers, $m$ rows by $n$ columns — its shape and entries are all that define it, and everything else in linear algebra is built on top of this one object.

---

## Intuition

A scalar is one number. A vector is a list of numbers. A matrix is the natural next step: a *table* of numbers, indexed by both a row and a column. Nothing more mysterious than that — the power of matrices comes entirely from what you're allowed to *do* with them (see [[matrix-operations]]), not from the object itself.

There are two equally useful ways to look at the same matrix: as a grid of individual scalars, or as several column vectors placed side by side. The second view is what makes matrices the natural container for [[linear-transformations]] and datasets alike.

## Mechanics

**Definition** — an $m \times n$ matrix $A$ is a rectangular array with $m$ rows and $n$ columns:

$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$$

Entry $a_{ij}$ lives in row $i$, column $j$ — row index always comes first.

**Equality** — two matrices are equal only if they have identical dimensions *and* every corresponding entry matches. Shape mismatch means "not equal," not an error to paper over.

| Special case | Shape | Name |
|---|---|---|
| $1 \times n$ | one row | Row vector |
| $m \times 1$ | one column | Column vector |
| $n \times n$ | equal rows/columns | Square matrix |
| $1 \times 1$ | single entry | Scalar |

**The column-vector view** — $A$ can be read as $n$ column vectors placed side by side: $A = [\mathbf{a}_1 \ \mathbf{a}_2 \ \cdots \ \mathbf{a}_n]$. This is the view [[row-and-column-spaces]] and [[matrix-of-linear-transformation]] depend on directly.

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])   # shape (2, 3): 2 rows, 3 columns

print(A.shape)      # (2, 3)
print(A[0, 1])      # a_12 = 2 (0-indexed: row 0, col 1)
print(A[:, 0])       # first column as a vector: [1, 4]
```

## In ML

**Data as a matrix** — a dataset of $n$ samples and $d$ features is stored as an $n \times d$ matrix: each row is one data point, each column is one feature. This is the starting object for nearly every ML algorithm before any model is even chosen.

**Weight matrices** — every linear layer in a neural network is literally a matrix; its shape (`in_features × out_features`) is a design decision that fixes how many numbers define that layer.

**The column-vector view enables everything downstream** — treating $A$ as a list of column vectors is exactly what [[row-and-column-spaces]], [[rank-nullity-theorem]], and [[matrix-of-linear-transformation]] build on to define rank, span, and the transformation a matrix represents.

## Exercises

**Basic** — Write down a $2 \times 3$ matrix of your choice and identify $a_{12}$ and $a_{23}$.

**Intermediate** — A dataset has 100 samples and 5 features. What are the dimensions of its data matrix, and what does each row and column represent?

**Advanced** — Explain why a row vector and a column vector both count as "matrices" under this definition, and precisely what shape distinguishes each from a general $m \times n$ matrix.
