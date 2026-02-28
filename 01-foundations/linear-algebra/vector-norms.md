**Related**: [[vector-operations]], [[cosine-similarity]], [[Regularization (L1/L2)]]
**Tags**: #status/seed

## Core Idea

A norm measures the "size" or "magnitude" of a vector. Different norms measure size differently, and each one appears in a specific ML context: L2 in Ridge regularization, L1 in Lasso (sparsity), and Linf in adversarial robustness. Choosing the right norm changes how your model behaves.

## Details

### Intuition: Three Questions About the Same Vector

Each norm answers a different question about a vector's "size":

| Norm | Question it answers | Analogy |
|------|-------------------|---------|
| L2 | How far is this from zero? | Fly in a straight line to the point |
| L1 | How much total activity is in this vector? | Walk along city streets — every component costs something |
| Linf | What's the single biggest component? | Only the worst offender matters |

**Why not just use L2?** Consider a model weight vector $\mathbf{w} = [0.5, 0.001, 3.2, 0.0003]$:
- **L2** penalizes overall magnitude. All weights shrink, but none reach exactly zero. The tiny $0.001$ survives.
- **L1** charges a cost for every non-zero weight, no matter how small. Pressure pushes $0.001$ and $0.0003$ to exactly zero → **automatic feature selection**.
- **Linf** only cares about $3.2$ (the max). Useful when you need to bound the worst case, not the average.

The choice of norm defines what "small" means to your model, and that changes everything.

### General Definition

A function $\|\cdot\|: \mathbb{R}^n \to \mathbb{R}$ is a norm if it satisfies:

1. **Non-negativity**: $\|\mathbf{v}\| \geq 0$, and $\|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}$
2. **Homogeneity**: $\|c\mathbf{v}\| = |c| \cdot \|\mathbf{v}\|$
3. **Triangle inequality**: $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$

### The $p$-Norm Family

All common norms are special cases of the general $L_p$ norm:

$$\|\mathbf{v}\|_p = \left(\sum_{i=1}^{n} |v_i|^p \right)^{1/p}$$

### L2 Norm (Euclidean)

$$\|\mathbf{v}\|_2 = \sqrt{\sum_{i=1}^{n} v_i^2} = \sqrt{\mathbf{v} \cdot \mathbf{v}}$$

- **Geometric meaning**: Straight-line distance from origin
- **ML use**: Ridge regularization adds $\lambda\|\mathbf{w}\|_2^2$ to the loss — penalizes large weights, keeps all features but shrinks them
- **Why squared?**: We often use $\|\mathbf{v}\|_2^2$ instead of $\|\mathbf{v}\|_2$ because it's differentiable everywhere (no square root), and the gradient is simply $2\mathbf{v}$

### Worked example (L2)

$$\mathbf{v} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$

$$\|\mathbf{v}\|_2 = \sqrt{3^2 + (-4)^2 + 0^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5$$

### L1 Norm (Manhattan)

$$\|\mathbf{v}\|_1 = \sum_{i=1}^{n} |v_i|$$

- **Geometric meaning**: Distance walking along grid lines (like Manhattan streets)
- **ML use**: Lasso regularization adds $\lambda\|\mathbf{w}\|_1$ — promotes **sparsity** by driving some weights exactly to zero. This is feature selection built into the loss function.
- **Why sparsity?**: The L1 ball (set of vectors with $\|\mathbf{v}\|_1 \leq 1$) has corners along the axes. The loss function is most likely to touch the ball at a corner, where some components are exactly zero.

### Worked example (L1)

$$\mathbf{v} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$

$$\|\mathbf{v}\|_1 = |3| + |-4| + |0| = 3 + 4 + 0 = 7$$

### L-infinity Norm (Chebyshev)

$$\|\mathbf{v}\|_\infty = \max_{i} |v_i|$$

- **Geometric meaning**: The largest absolute component — how far the vector extends in any single dimension
- **ML use**: Adversarial robustness. The FGSM attack perturbs inputs within an $L_\infty$ ball: each pixel changes by at most $\epsilon$. The $L_\infty$ ball is a hypercube.

### Derivation: Linf as limit of $L_p$

Why is $\max|v_i|$ called $L_\infty$? Because:

$$\lim_{p \to \infty} \|\mathbf{v}\|_p = \lim_{p \to \infty} \left(\sum_i |v_i|^p\right)^{1/p} = \max_i |v_i|$$

Let $m = \max_i |v_i|$. Factor it out:

$$\|\mathbf{v}\|_p = m \left(\sum_i \left(\frac{|v_i|}{m}\right)^p\right)^{1/p}$$

Each term $\left(\frac{|v_i|}{m}\right)^p \leq 1$, and equals 1 only for the max component. As $p \to \infty$, all non-max terms vanish, leaving $m \cdot 1 = m$. $\blacksquare$

### Norm Comparison Table

| Norm | Formula | Ball shape | ML context |
|------|---------|-----------|------------|
| L1 | $\sum|v_i|$ | Diamond (has corners) | Lasso, sparsity, feature selection |
| L2 | $\sqrt{\sum v_i^2}$ | Circle/sphere (smooth) | Ridge, weight decay, distance metrics |
| Linf | $\max|v_i|$ | Square/hypercube | Adversarial perturbation bounds |

### Unit Balls Visualization

The "unit ball" is the set of all vectors with norm $\leq 1$. Its shape reveals the norm's behavior:

```
L1 ball        L2 ball        Linf ball
(diamond)      (circle)       (square)

    *           ***            ****
   * *         *   *           *  *
  *   *       *     *          *  *
   * *         *   *           *  *
    *           ***            ****
```

The corners of the L1 ball are why Lasso produces sparse solutions — the optimization is likely to hit a corner where some coordinates are zero.

## Code Example

```python
import numpy as np

v = np.array([3.0, -4.0, 0.0])

l1 = np.sum(np.abs(v))         # 7.0 — Manhattan distance
l2 = np.sqrt(np.dot(v, v))     # 5.0 — Euclidean distance
linf = np.max(np.abs(v))       # 4.0 — max component

# Always true: linf <= l2 <= l1 <= sqrt(n) * linf
n = len(v)
print(f"linf={linf} <= l2={l2} <= l1={l1} <= sqrt(n)*linf={np.sqrt(n)*linf:.2f}")
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- L2 norm is derived from the [[vector-operations|dot product]]: $\|\mathbf{v}\|_2 = \sqrt{\mathbf{v} \cdot \mathbf{v}}$
- Norms enable [[cosine-similarity]] by normalizing vectors to unit length
- L1 and L2 norms are the penalty terms in [[Regularization (L1/L2)]]
- Unit norm vectors form the unit sphere — the space where [[cosine-similarity]] lives
- Norm choice affects the geometry of optimization → [[Gradient Descent]]

## Sources

- [3Blue1Brown — Essence of Linear Algebra (Bonus: Norms)](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- [Mathematics for Machine Learning — Chapter 3.1](https://mml-book.github.io/book/mml-book.pdf)
- [Why L1 norm creates sparsity (intuitive explanation)](https://stats.stackexchange.com/questions/45643/why-l1-norm-for-sparse-models)
