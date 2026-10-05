---
tags:
  - status/seed
  - probability
related:
  - "[[unbiased-and-biased-estimators]]"
  - "[[bias-correction]]"
  - "[[parameter-vs-statistic]]"
  - "[[population-and-sample]]"
  - "[[measures-of-variation]]"
  - "[[skewness]]"
  - "[[law-of-large-numbers]]"
  - "[[multiplication-rule]]"
  - "[[monte-carlo-simulation]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-4 (Distribuciones muestrales y estimadores, Ejemplos 1–5, Tablas 6-2 a 6-5)"
---

> **TL;DR** — The **sampling distribution** of a statistic is the distribution of *all* the values that statistic takes over every possible sample of size n from the same population. It describes how much your one estimate can wobble, and every inference method is built on it.

---

## Intuition

You only ever hold **one** sample: 106 body temperatures with x̄ = 98.20 °F. But that x̄ is one draw from a bag of all the x̄'s you *could* have gotten. The sampling distribution is that bag. Its **center** tells you whether the statistic aims at the true [[parameter-vs-statistic|parameter]]. Its **spread** tells you how far one sample can land from the target. Its **shape** tells you which table (normal or not) you may use. You never see the bag directly. Theory (or simulation) describes it, so your single sample can be judged against it.

## Mechanics

**Definition.** For a statistic (x̄, s², p̂, range, …): the distribution of its values over all samples of the same size n from the same population. It can be shown as a table, a probability histogram, or a formula. A statistic computed from one sample is a single value. Its sampling distribution is a whole [[discrete-probability-distribution|probability distribution]].

**Triola's die experiment** (Table 6-2: roll a die n = 5 times, repeat 10,000 times; population μ = 3.5, σ² = 35/12 ≈ 2.92, p(odd) = 0.5):

| Statistic | Simulated mean | Exact center | Shape |
|---|---|---|---|
| Sample mean x̄ | 3.49 | 3.5 = μ | ≈ normal |
| Sample variance s² | 2.88 | 2.92 = σ² | **skewed right** (s² ≥ 0, long upper tail) |
| Sample proportion p̂ | 0.50 | 0.5 = p | ≈ normal (really Binomial(5, 0.5)/5) |

The **center** is the bias question ([[unbiased-and-biased-estimators]]). The **shape** is a [[skewness]] question. These are two different meanings of the Spanish *sesgado/a*: biased vs. skewed.

**Spread = standard error.** The SD of the sampling distribution of x̄ is σ/√n, **not** σ: 1.71/√5 ≈ 0.76 for the die. A bigger n gives a narrower bag. The [[central-limit-theorem]] (§6-5) adds that the bag's shape tends to normal.

**Small enough to list (Example 4).** Population {2, 3, 10}, n = 2 *with replacement* → 3² = 9 equally likely samples. The sample ranges 0, 1, 8, 1, 0, 7, 8, 7, 0 give P(0) = 3/9, P(1) = P(7) = P(8) = 2/9. That table *is* the sampling distribution of the range. For the die there are 6⁵ = 7,776 samples, too many to list, which is why Triola simulates.

**Why with replacement?** (1) For a small sample from a large population it barely matters (the 5% guideline in [[multiplication-rule]]). (2) Replacement makes draws independent, which keeps the formulas simple.

```python
import numpy as np
rng = np.random.default_rng(0)
rolls = rng.integers(1, 7, size=(10_000, 5))      # 10,000 samples of n=5 die rolls
means = rolls.mean(axis=1)                        # one x̄ per sample
s2    = rolls.var(axis=1, ddof=1)                 # one s² per sample (divide by n-1)
p_odd = (rolls % 2 == 1).mean(axis=1)             # one p̂ per sample
print(means.mean(), s2.mean(), p_odd.mean())      # 3.495  2.906  0.501
print(means.std())                                # 0.761 ≈ σ/√5 = 0.764, NOT σ = 1.708
```

## In ML

**The bootstrap builds a sampling distribution from one dataset.** Resample your data with replacement many times, recompute the statistic, and the spread of the results estimates the standard error, with no formula needed.

**Every evaluation metric has one.** Test accuracy on n examples is one draw from the sampling distribution of p̂, with SE ≈ √(p(1−p)/n). A 1-point gain on a 200-example test set is inside the noise.

**A mini-batch gradient is a sample statistic.** Its sampling distribution is centered on the full-data gradient (unbiased), with spread shrinking like 1/√batch size. That spread is the "noise" in SGD.

## Exercises

**Basic** — Population {1, 4, 7}, n = 2 with replacement. List all 9 samples, compute each x̄, and build the sampling distribution of x̄ as a table. Is its mean equal to μ = 4?

**Intermediate** — For the die (σ ≈ 1.71), what n makes the SD of x̄ equal to 0.25? Why does halving that SD require quadrupling n?

**Advanced** — Explain why the sampling distribution of s² must be right-skewed for small n even when the population is symmetric. (Hint: s² ≥ 0, its mean is fixed at σ², and occasionally one sample is very spread out.)
