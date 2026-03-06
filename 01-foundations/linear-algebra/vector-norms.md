**Related**: [[vector-operations]], [[vectors-and-vector-spaces]], [[cosine-similarity]], [[projection]], [[Regularization (L1/L2)]]
**Tags**: #status/growing

## Core Idea

Given a vector, what does "big" even mean? A vector has multiple components —
there's no single obvious way to summarize its size as one number. Different
norms give different answers, and **the choice of norm changes how your model
behaves.**

| Norm | Question it answers | Analogy |
|------|-------------------|---------|
| **L2** (Euclidean) | How far is this from zero? | Fly in a straight line to the point |
| **L1** (Manhattan) | How much total activity is in this vector? | Walk along city streets — every component costs something |
| **L-infinity** (Chebyshev) | What's the single biggest component? | Only the worst offender matters |

Consider a weight vector $\mathbf{w} = [0.5, 0.001, 3.2, 0.0003]$:
- **L2** penalizes overall magnitude. All weights shrink, but none reach exactly zero. The tiny 0.001 survives.
- **L1** charges a cost for every non-zero weight. Pressure pushes 0.001 and 0.0003 to exactly zero → **automatic feature selection**.
- **Linf** only cares about 3.2 (the max). Useful when you need to bound the worst case.

The choice of norm defines what "small" means to your model. That changes everything.

## Details

### L2 Norm (Euclidean): "Straight-line distance"

The most familiar norm — the distance you'd measure with a ruler:

$$\|\mathbf{v}\|_2 = \sqrt{\sum_{i=1}^{n} v_i^2} = \sqrt{\mathbf{v} \cdot \mathbf{v}}$$

Note that L2 norm is defined via the [[vector-operations|dot product]] with
itself: $\|\mathbf{v}\|_2 = \sqrt{\mathbf{v} \cdot \mathbf{v}}$.

**Geometric meaning**: Straight-line ("as the crow flies") distance from origin
to the point.

**ML use**: Ridge regularization adds $\lambda\|\mathbf{w}\|_2^2$ to the loss —
penalizes large weights, shrinks all features but keeps them all non-zero.

**Why squared?** We often use $\|\mathbf{v}\|_2^2$ instead of $\|\mathbf{v}\|_2$
because:
- No square root → differentiable everywhere (no issues at zero)
- The gradient is simply $2\mathbf{v}$ — clean and cheap to compute
- Minimizing the square minimizes the norm (same optimal point)

#### Worked Example (L2)

$$\mathbf{v} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$

$$\|\mathbf{v}\|_2 = \sqrt{3^2 + (-4)^2 + 0^2} = \sqrt{9 + 16 + 0} = \sqrt{25} = 5$$

This is the 3-4-5 Pythagorean triple — the point $(3, -4, 0)$ is 5 units from
the origin.

### L1 Norm (Manhattan): "City block distance"

$$\|\mathbf{v}\|_1 = \sum_{i=1}^{n} |v_i|$$

**Analogy**: You're in Manhattan. You can't walk diagonally through buildings —
you walk along streets (one axis at a time). The L1 norm measures this
taxi-cab distance: how far you go along each axis, summed up.

**Geometric meaning**: Total "cost" of reaching the point when you can only
move along axes.

**ML use**: Lasso regularization adds $\lambda\|\mathbf{w}\|_1$ — promotes
**sparsity** by driving some weights exactly to zero. This is feature selection
built into the loss function.

**Why does L1 produce sparsity?** The L1 unit ball (all vectors with
$\|\mathbf{v}\|_1 \leq 1$) has **corners** along the axes. The loss function
surface is most likely to touch the ball at a corner, where some components are
exactly zero. L2's ball is a smooth sphere with no corners — the tangent point
is almost never on an axis.

#### Worked Example (L1)

$$\mathbf{v} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$

$$\|\mathbf{v}\|_1 = |3| + |-4| + |0| = 3 + 4 + 0 = 7$$

Compare with L2 = 5. The L1 norm is always larger (or equal) because it
measures a longer path — you're walking around the building instead of through it.

### L-infinity Norm (Chebyshev): "The biggest component wins"

$$\|\mathbf{v}\|_\infty = \max_{i} |v_i|$$

**Analogy**: A chain is only as strong as its weakest link. L-infinity is the
opposite — the vector's "size" is determined entirely by its strongest dimension.
It ignores everything else.

**Geometric meaning**: How far the vector extends in its most extreme dimension.

**ML use**: Adversarial robustness. The FGSM attack perturbs inputs within an
$L_\infty$ ball: each pixel changes by at most $\epsilon$. The $L_\infty$ ball
is a hypercube — it bounds the worst-case change per dimension.

#### Worked Example (Linf)

$$\mathbf{v} = \begin{bmatrix} 3 \\ -4 \\ 0 \end{bmatrix}$$

$$\|\mathbf{v}\|_\infty = \max(|3|, |-4|, |0|) = \max(3, 4, 0) = 4$$

Only the -4 component matters. The 3 and the 0 are irrelevant.

### The $p$-Norm Family: They're All Related

All three norms above are special cases of a single formula:

$$\|\mathbf{v}\|_p = \left(\sum_{i=1}^{n} |v_i|^p \right)^{1/p}$$

- $p = 1$: L1 norm (Manhattan)
- $p = 2$: L2 norm (Euclidean)
- $p \to \infty$: L-infinity norm (max component)

### Derivation: Why is $\max|v_i|$ called $L_\infty$?

Because it's the **limit** of $L_p$ as $p$ grows without bound:

$$\lim_{p \to \infty} \|\mathbf{v}\|_p = \lim_{p \to \infty} \left(\sum_i |v_i|^p\right)^{1/p} = \max_i |v_i|$$

**Proof**: Let $m = \max_i |v_i|$. Factor it out:

$$\|\mathbf{v}\|_p = m \left(\sum_i \left(\frac{|v_i|}{m}\right)^p\right)^{1/p}$$

Each term $\left(\frac{|v_i|}{m}\right)^p \leq 1$, and equals 1 only when
$|v_i| = m$ (the max component). As $p \to \infty$, every term where
$|v_i| < m$ vanishes (a number less than 1 raised to infinity → 0). What
survives is the count of max-valued components, raised to $1/p$, which → 1.

Result: $m \cdot 1 = m = \max_i |v_i|$. $\blacksquare$

### What Makes Something a Norm? (The Axioms)

All norms — L1, L2, Linf, and any $L_p$ — share three properties. These aren't
arbitrary rules; each prevents a specific kind of breakdown:

| Axiom | Formula | What it prevents |
|-------|---------|-----------------|
| **Non-negativity** | $\|\mathbf{v}\| \geq 0$, and $= 0$ iff $\mathbf{v} = \mathbf{0}$ | "Size" should never be negative. And only the zero vector has zero size — if something non-zero measured as zero, your metric would be blind to it |
| **Homogeneity** | $\|c\mathbf{v}\| = |c| \cdot \|\mathbf{v}\|$ | Doubling the vector should double its size. Without this, scaling would break all distance-based algorithms |
| **Triangle inequality** | $\|\mathbf{u} + \mathbf{v}\| \leq \|\mathbf{u}\| + \|\mathbf{v}\|$ | "The shortcut is never longer than the detour." Going directly from A to C can't be farther than going A→B→C. Without this, "nearest neighbor" would be meaningless |

If a function satisfies all three, it's a valid norm. The $L_p$ family for
$p \geq 1$ satisfies all three. For $p < 1$, the triangle inequality breaks —
which is why $L_{0.5}$ is not a true norm.

### Norm Comparison

| Norm | Formula | Ball shape | ML context |
|------|---------|-----------|------------|
| L1 | $\sum|v_i|$ | Diamond (has corners) | Lasso, sparsity, feature selection |
| L2 | $\sqrt{\sum v_i^2}$ | Circle/sphere (smooth) | Ridge, weight decay, distance metrics |
| Linf | $\max|v_i|$ | Square/hypercube | Adversarial perturbation bounds |

### Unit Balls Visualization

The "unit ball" is the set of all vectors with norm $\leq 1$. Its shape
reveals the norm's behavior:

```
L1 ball        L2 ball        Linf ball
(diamond)      (circle)       (square)

    *           ***            ****
   * *         *   *           *  *
  *   *       *     *          *  *
   * *         *   *           *  *
    *           ***            ****

 corners on     smooth          corners at
 axes → WHERE   everywhere →    (±1,±1) →
 sparsity       no sparsity     bounds each
 comes from     preference      dimension
```

The corners of the L1 ball are why Lasso produces sparse solutions — the
optimization is likely to hit a corner where some coordinates are exactly zero.

### Norm Ordering: How They Relate

For any vector $\mathbf{v} \in \mathbb{R}^n$:

$$\|\mathbf{v}\|_\infty \leq \|\mathbf{v}\|_2 \leq \|\mathbf{v}\|_1 \leq \sqrt{n} \cdot \|\mathbf{v}\|_\infty$$

This always holds. The max component is always ≤ straight-line distance,
which is always ≤ taxi-cab distance. Verify with $\mathbf{v} = [3, -4, 0]$:

$$4 \leq 5 \leq 7 \leq \sqrt{3} \cdot 4 \approx 6.93$$

Wait — $7 \leq 6.93$ is false! The bound $\|\mathbf{v}\|_1 \leq \sqrt{n} \cdot \|\mathbf{v}\|_\infty$
is tight (reached when all components equal the max). For our vector, the
correct tighter bound uses $n$ directly: $\|\mathbf{v}\|_1 \leq n \cdot \|\mathbf{v}\|_\infty = 3 \cdot 4 = 12$. ✓

The key takeaway: $\|\mathbf{v}\|_\infty \leq \|\mathbf{v}\|_2 \leq \|\mathbf{v}\|_1$ always holds.

## Code Example

```python
import numpy as np

v = np.array([3.0, -4.0, 0.0])

# Three norms, three different answers
l1 = np.sum(np.abs(v))         # 7.0 — taxi-cab distance
l2 = np.sqrt(np.dot(v, v))     # 5.0 — straight-line distance
linf = np.max(np.abs(v))       # 4.0 — biggest component

# Always true: linf <= l2 <= l1
print(f"linf={linf} <= l2={l2} <= l1={l1}")  # 4.0 <= 5.0 <= 7.0

# Normalizing to unit length (used in cosine similarity)
v_unit = v / l2
print(np.linalg.norm(v_unit))  # 1.0 — unit vector
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- L2 norm is derived from the [[vector-operations|dot product]]: $\|\mathbf{v}\|_2 = \sqrt{\mathbf{v} \cdot \mathbf{v}}$
- Norms enable [[cosine-similarity]] by normalizing vectors to unit length
- Norms give meaning to "distance" inside [[vectors-and-vector-spaces]]
- L1 and L2 norms are the penalty terms in [[Regularization (L1/L2)]]
- Unit norm vectors form the unit sphere — the space where [[cosine-similarity]] lives
- [[projection]] uses the norm to compute the scalar projection
- Norm choice affects the geometry of optimization → [[Gradient Descent]]

## Sources

- [3Blue1Brown — Essence of Linear Algebra (Bonus: Norms)](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- [Mathematics for Machine Learning — Chapter 3.1](https://mml-book.github.io/book/mml-book.pdf)
- [Why L1 norm creates sparsity (intuitive explanation)](https://stats.stackexchange.com/questions/45643/why-l1-norm-for-sparse-models)
