---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[kernel-and-range]]"
  - "[[basis-and-dimension]]"
  - "[[row-and-column-spaces]]"
  - "[[gaussian-elimination]]"
domain: linear-algebra
sources:
  - "Anton, Howard. Introducción al Álgebra Lineal. §5.2, Teoremas 3 y 4"
---

> **TL;DR** — For any linear transformation $T: V \to W$ with $\dim(V) = n$, $\text{rank}(T) + \text{nullity}(T) = n$ — every dimension of the input space either survives into the range or collapses into the kernel, and there's nowhere else for it to go.

---

## Intuition

$T$ takes $n$ dimensions of input and does one of two things to each of them: lets it survive through to the output (contributing to the **rank** — the size of what's reachable) or crushes it to zero (contributing to the **nullity** — the size of the kernel). Since every input dimension must do exactly one of these two things, the two numbers always add up to $n$, no matter what $T$ is.

Check it against the [[kernel-and-range]] examples: the rotation by 45° has kernel $=\{\mathbf{0}\}$ (nullity 0) and range $=\mathbb{R}^2$ (rank 2) — $0+2=2$. The flattening map $T(x,y)=(x,0)$ has kernel = the y-axis (nullity 1) and range = the x-axis (rank 1) — $1+1=2$. Both started with $n=2$ input dimensions; the split is different, but the total is fixed.

## Mechanics

**Theorem 3 — Dimension Theorem (Anton §5.2)** — If $T: V \to W$ is a linear transformation from an $n$-dimensional vector space $V$ to a vector space $W$, then:

$$\text{rank}(T) + \text{nullity}(T) = n$$

where $\text{rank}(T) = \dim(R(T))$ and $\text{nullity}(T) = \dim(\ker(T))$.

**Why $n$ (domain) and never $\dim(W)$ (codomain)** — rank and nullity both answer the same question: *what happened to each of the input's dimensions?* Every one of the $n$ input directions either survives into the output (rank) or collapses to zero (nullity) — there's no third option, so the two must add up to exactly what you started with: $n$. The codomain's size plays no role in this budget; it only owns whatever the survivors land in, not a separate pool of directions being counted. (E.g. $T:\mathbb{R}^5\to\mathbb{R}^7$ with rank 3 has nullity $5-3=2$ — never $7-3$; the codomain's dimension 7 is irrelevant to the sum, only to whether $T$ happens to be onto.)

**Special case — $T$ is multiplication by a matrix.** Let $V = \mathbb{R}^n$, $W = \mathbb{R}^m$, and $T(\mathbf{x}) = A\mathbf{x}$ for an $m \times n$ matrix $A$. **Columns = domain dimension $n$, rows = codomain dimension $m$** — forced by the mechanics of matrix-vector multiplication itself: $A\mathbf{x}$ is a weighted sum of $A$'s columns, so $\mathbf{x}$ must supply exactly one weight per column (hence $n$ columns ⟺ input lives in $\mathbb{R}^n$); each row produces one output coordinate via a dot product (hence $m$ rows ⟺ output lives in $\mathbb{R}^m$). The dimension theorem becomes:

$$\text{nullity}(T) = n - \text{rank}(T) = (\text{number of columns of } A) - \text{rank}(T) \qquad (5.4)$$

Two identifications make (5.4) concrete: $\text{nullity}(T)$ is the dimension of the **solution space of $A\mathbf{x} = \mathbf{0}$** (that's exactly $\ker(T)$), and $\text{rank}(T)$ is the **rank of the matrix $A$** (the dimension of its column space, which is $R(T)$). Substituting gives:

**Theorem 4 (Anton §5.2)** — If $A$ is an $m \times n$ matrix, then the dimension of the solution space of $A\mathbf{x} = \mathbf{0}$ is:

$$n - \text{rank}(A)$$

where $n$ is the number of columns of $A$ (the number of unknowns).

**Corollary — full row rank means onto.** If $A$ is $m \times n$ and $\text{rank}(A) = m$, then $R(T) = \mathbb{R}^m$ — every vector in the codomain is reachable, with no exceptions.

**Why this is true**: $R(T)$ is always a subspace of $\mathbb{R}^m$ (Theorem 2, [[kernel-and-range]]), so $\dim(R(T)) = \text{rank}(A) \leq m$ always. When $\text{rank}(A)$ hits the maximum possible value $m$, $R(T)$ is a subspace of $\mathbb{R}^m$ with the *full* dimension $m$ — and there is no proper subspace of $\mathbb{R}^m$ with dimension $m$ (any basis of size $m$ already spans all of $\mathbb{R}^m$, by [[basis-and-dimension]]'s Theorem 8). So $R(T)$ can't be a strict subset — it must be all of $\mathbb{R}^m$.

**Common mix-up to avoid**: this corollary is about *existence* (can you reach $\mathbf{w}$ at all?), which depends on $\text{rank}(A)$ vs. $m$ — **not** about *how many* solutions exist once you can, which is what nullity governs. A large nullity does not imply everything is reachable. Counterexample: $A = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&0\end{bmatrix}$ has rank 2, nullity $4-2=2$ (plenty of free variables — infinitely many solutions whenever solvable). But $\text{rank}(A)=2 < m=3$, so $R(T)$ is only a 2D subspace of $\mathbb{R}^3$; a target like $(0,0,1)$ has **zero** solutions, despite the large kernel. Existence (rank vs. $m$) and multiplicity (nullity) are independent questions.

| Quantity | Formula | Meaning |
|---|---|---|
| rank$(T)$ | $\dim(R(T))$ | dimensions of $W$ actually reachable |
| nullity$(T)$ | $\dim(\ker(T))$ | input dimensions collapsed to zero |
| rank$(A)$ | number of pivot columns (row-reduce $A$) | dimension of column space of $A$ |
| solution space of $A\mathbf{x}=\mathbf{0}$ | dimension $= n - \text{rank}(A)$ | free variables in the general solution |

```python
import numpy as np

A = np.array([[1, 2, 3], [2, 4, 6]])   # 2x3, rows are dependent -> rank-deficient
n_cols = A.shape[1]                     # n = 3 (number of unknowns)

rank = np.linalg.matrix_rank(A)         # rank(A) = 1
nullity = n_cols - rank                 # nullity = 3 - 1 = 2 (two free variables)

print(f"rank={rank}, nullity={nullity}, rank+nullity={rank+nullity}, n={n_cols}")
# rank=1, nullity=2, rank+nullity=3, n=3  -> theorem holds
```

## In ML

**Rank-deficient design matrices** — in linear regression $\hat{\mathbf{y}} = X\boldsymbol\beta$, if $X$ ($n$ samples $\times$ $p$ features) has rank $< p$ (redundant or collinear features), the dimension theorem says nullity $>0$: there are infinitely many $\boldsymbol\beta$ giving the exact same predictions. This is exactly why collinearity makes the normal equations unsolvable without regularization.

**Layer capacity and bottlenecks** — a linear layer $\mathbf{z}=W\mathbf{x}$ with $W$ of shape $(m,n)$ can have rank at most $\min(m,n)$. A bottleneck layer ($m < n$) forces nullity $\geq n-m > 0$ by the theorem — information is necessarily lost, which is the entire mechanism behind autoencoder compression and low-rank adapters (LoRA).

**Degrees of freedom in optimization** — the nullity of a system's Jacobian or Hessian at a solution tells you how many directions leave the loss unchanged (flat directions). The dimension theorem quantifies the trade-off directly: more directions preserved (rank) means fewer directions are redundant (nullity), and vice versa.

## Exercises

**Basic** — For $T(x,y,z) = (x-z, y-z, 0)$ on $\mathbb{R}^3$ (from the [[kernel-and-range]] advanced exercise), you already found $\ker(T)$ and $R(T)$. Verify rank$(T)$ + nullity$(T) = 3$ using their dimensions.

**Intermediate** — A $4 \times 6$ matrix $A$ has rank 3. Using Theorem 4, how many free variables appear in the general solution of $A\mathbf{x}=\mathbf{0}$? If you're also told $A\mathbf{x}=\mathbf{b}$ has at least one solution, how many solutions does it have in total?

**Advanced** — Prove the dimension theorem for the matrix special case directly from Gaussian elimination: relate the number of pivot columns (rank) and free columns (nullity) in row echelon form of $A$ to $n$, the total column count. See [[gaussian-elimination]] and [[row-and-column-spaces]].
