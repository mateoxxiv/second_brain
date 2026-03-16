**Related**: [[projection]], [[vector-operations]], [[vector-norms]], [[basis-and-dimension]], [[linear-independence]], [[special-matrices]], [[singular-value-decomposition]]
**Tags**: #status/growing

## Core Idea

Gram-Schmidt takes any set of [[linear-independence|independent]] vectors and
turns them into an **orthonormal** set — all perpendicular to each other, all
length 1. It works by repeatedly removing "shadows" ([[projection]]s) to
extract only the perpendicular part.

```
Input:  v1, v2, v3, ...  (independent, any directions)
Output: q1, q2, q3, ...  (orthonormal — perpendicular + unit length)
```

## Details

### Why Orthonormal Bases Matter

| Operation | Regular basis | Orthonormal basis |
|-----------|--------------|-------------------|
| Find coordinates | Solve a system | Just dot products |
| Matrix inverse | Expensive | Free — just transpose (Q^-1 = Q^T) |
| Projection | Full formula | Simple dot product |

This is why [[special-matrices|orthogonal matrices]] are powerful — their
columns are orthonormal.

### The Recipe

The key insight: the [[projection]] formula gives you the "shadow" of one
vector along another. Gram-Schmidt **subtracts** that shadow to get the
perpendicular part (the residual).

When projecting onto a unit vector q, the formula simplifies:

```
General projection:    (u . v / v . v) * v
Projection onto unit:  (u . q) * q            ← denominator = 1
```

**Step 1** — normalize the first vector:

```
q1 = v1 / ||v1||
```

**Step 2** — remove v2's shadow on q1, normalize what's left:

```
shadow = (v2 . q1) * q1          ← projection of v2 onto q1
u2 = v2 - shadow                  ← residual (perpendicular to q1)
q2 = u2 / ||u2||                  ← normalize to unit length
```

**Step 3** — remove v3's shadow on q1 AND q2, normalize:

```
u3 = v3 - (v3 . q1)*q1 - (v3 . q2)*q2
q3 = u3 / ||u3||
```

**General step k**: subtract projections onto ALL previous q's:

```
uk = vk - sum of (vk . qi)*qi for i = 1 to k-1
qk = uk / ||uk||
```

Each step removes everything that points along previous directions. What's
left MUST be perpendicular to all of them.

### Worked Example (2D)

```
v1 = [1, 1]
v2 = [1, 0]
```

**Step 1:**

```
||v1|| = sqrt(2)
q1 = [1/sqrt(2), 1/sqrt(2)] = [0.707, 0.707]
```

**Step 2:**

```
v2 . q1 = 1*0.707 + 0*0.707 = 0.707

shadow = 0.707 * [0.707, 0.707] = [0.5, 0.5]
u2 = [1, 0] - [0.5, 0.5] = [0.5, -0.5]

||u2|| = sqrt(0.25 + 0.25) = 0.707
q2 = [0.5, -0.5] / 0.707 = [0.707, -0.707]
```

**Verify:**

```
q1 . q2 = 0.707*0.707 + 0.707*(-0.707) = 0.5 - 0.5 = 0  ✓ orthogonal
||q1|| = 1  ✓     ||q2|| = 1  ✓ unit length
```

### Worked Example (3D)

```
v1 = [1, 1, 0]     v2 = [1, 0, 1]     v3 = [0, 1, 1]
```

**Step 1:** q1 = [0.707, 0.707, 0]

**Step 2:**
```
v2 . q1 = 0.707
shadow = [0.5, 0.5, 0]
u2 = [0.5, -0.5, 1]
q2 = [0.408, -0.408, 0.816]
```

**Step 3:**
```
v3 . q1 = 0.707       v3 . q2 = 0.408
u3 = [0, 1, 1] - 0.707*q1 - 0.408*q2
   = [-0.667, 0.667, 0.667]
q3 = [-0.577, 0.577, 0.577]
```

All pairs orthogonal, all unit length. Same span as original vectors.

### Connection to QR Decomposition

Gram-Schmidt naturally produces the **QR decomposition**: A = QR, where
Q is orthogonal and R is upper triangular.

- Q = the orthonormal vectors we computed (as columns)
- R = the coefficients we used (the dot products and norms)

QR is used for:
- Solving least squares (linear regression)
- Computing eigenvalues (QR algorithm)
- Numerically stable alternative to normal equations

### When It Fails

Gram-Schmidt fails (produces a zero vector) when the input vectors are
[[linear-independence|linearly dependent]]. If u_k = 0 at some step, it means
v_k was already in the span of v1...v_{k-1} — it had no perpendicular part
to extract.

## Code Example

```python
import numpy as np

def gram_schmidt(V):
    """Orthonormalize columns of V using Gram-Schmidt."""
    Q = np.zeros_like(V, dtype=float)
    for k in range(V.shape[1]):
        q = V[:, k].astype(float)
        # Subtract projections onto all previous q's
        for j in range(k):
            q -= np.dot(q, Q[:, j]) * Q[:, j]
        Q[:, k] = q / np.linalg.norm(q)
    return Q

# Test
V = np.array([[1, 1], [1, 0]], dtype=float).T  # columns = vectors
Q = gram_schmidt(V.T)  # pass as column matrix

# Verify
v1 = np.array([1, 1], dtype=float)
v2 = np.array([1, 0], dtype=float)
V = np.column_stack([v1, v2])
Q = gram_schmidt(V)
print(Q)                              # [[0.707, 0.707], [0.707, -0.707]]
print(np.allclose(Q.T @ Q, np.eye(2)))  # True — orthonormal
```

## Connections

- [[projection]] — Gram-Schmidt IS repeated projection (subtract the shadow, keep the residual)
- [[vector-norms]] — normalization step makes vectors unit length
- [[linear-independence]] — input must be independent; dependent vectors produce zero residuals
- [[basis-and-dimension]] — output is an orthonormal basis for the same subspace
- [[special-matrices]] — Q matrix from Gram-Schmidt is orthogonal ($Q^TQ = I$)
- [[singular-value-decomposition]] — SVD algorithms use Gram-Schmidt internally
- Forward link: QR decomposition — direct product of Gram-Schmidt

## Sources

- [3Blue1Brown — Gram-Schmidt in context of projections](https://www.3blue1brown.com/)
- [MIT 18.06 — Strang, Lecture 17: Orthogonal Matrices and Gram-Schmidt](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 3.4](https://mml-book.github.io/book/mml-book.pdf)
