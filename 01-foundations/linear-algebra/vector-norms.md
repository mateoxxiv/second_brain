---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[cosine-similarity]]"
  - "[[vectors-and-vector-spaces]]"
  - "[[projection]]"
domain: linear-algebra
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://stats.stackexchange.com/questions/45643/why-l1-norm-for-sparse-models"
---

> **TL;DR** — A norm measures vector "size." L1 counts total activity, L2 measures straight-line distance, L-inf tracks the biggest component. The choice of norm changes what "small" means — and that changes how your model behaves.

---

## Intuition

Given weights $\mathbf{w} = [0.5, 0.001, 3.2, 0.0003]$:
- **L2** penalizes overall magnitude — all weights shrink but none reach exactly zero.
- **L1** charges a flat cost per non-zero weight — pushes tiny weights to *exactly* zero → automatic feature selection.
- **L-inf** only cares about 3.2 (the max) — useful when bounding the worst case.

The unit ball shape explains the difference. L1's ball has **corners on the axes** — optimization is likely to hit a corner where some coordinates are zero. L2's ball is a smooth sphere — no corners, no sparsity pressure.

## Mechanics

All three are special cases of the $p$-norm: $\|\mathbf{v}\|_p = \left(\sum_i |v_i|^p\right)^{1/p}$

| Norm | Formula | Ball shape | Behavior |
|------|---------|-----------|---------|
| L1 | $\sum_i \lvert v_i \rvert$ | Diamond (corners on axes) | Promotes sparsity |
| L2 | $\sqrt{\sum_i v_i^2}$ | Sphere (smooth) | Shrinks all uniformly |
| L-inf | $\max_i \lvert v_i \rvert$ | Hypercube | Bounded worst case |

**Ordering**: $\|\mathbf{v}\|_\infty \leq \|\mathbf{v}\|_2 \leq \|\mathbf{v}\|_1$ always holds. For $\mathbf{v}=[3,-4,0]$: $4 \leq 5 \leq 7$.

L-inf is the *limit* of $L_p$ as $p\to\infty$ because all terms with $|v_i| < \max$ vanish as $p$ grows, leaving only the maximum component.

```python
import numpy as np
v = np.array([3.0, -4.0, 0.0])

l1   = np.sum(np.abs(v))        # 7.0
l2   = np.sqrt(np.dot(v, v))    # 5.0
linf = np.max(np.abs(v))        # 4.0
print(f"{linf} ≤ {l2} ≤ {l1}") # 4.0 ≤ 5.0 ≤ 7.0

v_unit = v / l2  # unit vector for cosine similarity
```


## In ML

**Ridge regularization (L2)** — adds $\lambda\|\mathbf{w}\|_2^2$ to the loss. All weights shrink toward zero but none become exactly zero. Useful when all features are expected to matter.

**Lasso regularization (L1)** — adds $\lambda\|\mathbf{w}\|_1$. Drives weak weights to exactly zero, performing automatic feature selection. Preferred when you expect sparsity.

**Adversarial robustness** — FGSM adversarial attacks perturb inputs within an $L_\infty$ ball: each pixel changes by at most $\epsilon$. L-inf bounds the worst-case per-dimension change.

## Exercises

**Basic** — Compute L1, L2, and L-inf for $\mathbf{v} = [1, -2, 2, 0]$. Verify the ordering holds.

**Intermediate** — Explain geometrically why L1 produces sparse solutions and L2 does not. Draw the unit balls and show where a loss function surface would likely touch each.

**Advanced** — Prove that $\lim_{p\to\infty}\|\mathbf{v}\|_p = \max_i|v_i|$. (Hint: factor out the max element and analyze what remains as $p\to\infty$.)
