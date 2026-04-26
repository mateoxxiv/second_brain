---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[matrix-multiplication]]"
  - "[[special-matrices]]"
---

**What**: Flip a matrix over its main diagonal. Rows ↔ columns. Shape $m \times n$ becomes $n \times m$.

**Formula**: $(A^T)_{ij} = A_{ji}$

**The one rule to remember**: Product transpose reverses order — $(AB)^T = B^TA^T$. Same as "socks before shoes, shoes off first."

**Why ML cares**:
- Dot product is secretly transpose-multiply: $\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^T\mathbf{y}$
- Backprop flows through $W^T$ (reverse of forward pass $W$)
- Normal equations: $\hat{\beta} = (X^TX)^{-1}X^Ty$

**Quick check**:
```python
A = np.array([[1,2,3],[4,5,6]])
A.T.shape   # (3, 2)  ← flipped
(A.T).T     # back to A
```

→ [[vector-operations]] | [[matrix-multiplication]] | [[special-matrices]]
