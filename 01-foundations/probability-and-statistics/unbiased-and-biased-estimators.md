---
tags:
  - status/seed
  - probability
related:
  - "[[sampling-distribution]]"
  - "[[parameter-vs-statistic]]"
  - "[[measures-of-variation]]"
  - "[[measures-of-center]]"
  - "[[expected-value]]"
  - "[[skewness]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-4 (Estimadores insesgados; Ejemplo 4, Tablas 6-4 y 6-5)"
  - "Wasserman, All of Statistics, §6.2 (bias, standard error, MSE)"
---

> **TL;DR** — An estimator is **unbiased** when the mean of its [[sampling-distribution]] equals the parameter it targets: E[θ̂] = θ. Sample mean, variance (÷ n−1) and proportion are unbiased. Range, standard deviation s, and (in general) the median are biased.

---

## Intuition

Think of an archer. **Bias** is where the arrows land *on average*: centered on the bullseye or systematically off to one side. It says nothing about how tightly they cluster. That's the **standard error**, a separate property. An unbiased estimator can still be wildly imprecise for small n. A biased one can be very useful if its bias is small (s for large n). "Unbiased" means "right on average over all possible samples," never "right for *your* sample."

## Mechanics

**Definition.** For a statistic θ̂ estimating parameter θ: bias(θ̂) = E[θ̂] − θ. Unbiased ⟺ bias = 0, i.e. the [[expected-value]] of its sampling distribution equals θ.

| Statistic | Targets | Verdict (Triola) | Why |
|---|---|---|---|
| x̄ | μ | unbiased | E[x̄] = μ by linearity of expectation |
| s² (÷ n−1) | σ² | unbiased | the n−1 divisor is chosen exactly for this ([[measures-of-variation]]) |
| p̂ | p | unbiased | p̂ is a mean of 0/1 values |
| s | σ | **biased low** | E[s] = E[√s²] ≤ √E[s²] = σ, because √ is concave (Jensen) |
| range | population range | **biased low** | a sample can't exceed the population's extremes, and usually misses them |
| median | population median | biased in general | unbiased for symmetric populations; biased for skewed ones |

**Worked (Example 4).** Population {2, 3, 10}, n = 2 with replacement, 9 equally likely samples:

| Statistic | Mean over the 9 samples | Parameter | Verdict |
|---|---|---|---|
| range | 32/9 ≈ 3.56 | 8 | biased |
| s² (÷ n−1) | 12.67 | σ² = 38/3 ≈ 12.67 | unbiased, exactly |
| s² (÷ n) | 6.33 | 12.67 | biased by the factor (n−1)/n = 1/2 |
| s | 2.51 | σ ≈ 3.56 | biased |
| median | 5.0 | population median 3 | biased: for n = 2 the median *is* the mean, so it aims at μ = 5, not at the median |

```python
import numpy as np
from itertools import product
pop = [2, 3, 10]
samples = list(product(pop, repeat=2))                  # 9 samples, each prob 1/9
mean_of = lambda f: np.mean([f(s) for s in samples])    # center of the sampling distribution
print(mean_of(np.ptp), np.ptp(pop))                     # 3.56 vs 8     -> biased
print(mean_of(lambda s: np.var(s, ddof=1)), np.var(pop)) # 12.67 vs 12.67 -> unbiased
print(mean_of(lambda s: np.std(s, ddof=1)), np.std(pop)) # 2.51 vs 3.56  -> biased
```

**Why s is still used.** Its bias shrinks as n grows (for normal data E[s] ≈ σ(1 − 1/(4n))), so for moderate n it's negligible, and s has the right units.

## In ML

**Bias–variance for estimators.** MSE(θ̂) = bias² + variance. A slightly biased estimator with much lower variance can win on MSE. That's exactly what ridge regression and shrinkage exploit, and the same decomposition later describes model error.

**Unbiased gradients make SGD work.** A uniformly sampled mini-batch gradient is an unbiased estimator of the full gradient. Biased sampling (e.g. sorted data) breaks convergence guarantees.

**Biased-by-design estimators are everywhere.** Adam's bias correction (dividing by 1 − βᵗ) exists because its running averages start biased toward 0. Recognizing bias and correcting it is a recurring engineering move.

## Exercises

**Basic** — For population {1, 4, 7} with n = 2 with replacement, compute the mean of the 9 sample variances using ÷ (n−1) and using ÷ n. Which equals σ² = 6?

**Intermediate** — Prove E[x̄] = μ using only linearity of expectation. Then explain why the same trick does *not* prove E[s] = σ.

**Advanced** — Show E[s²_n] = ((n−1)/n)·σ² for the ÷ n version (expand Σ(xᵢ − x̄)² = Σ(xᵢ − μ)² − n(x̄ − μ)²). Then explain why an unbiased estimator can still have a larger MSE than a biased one.
