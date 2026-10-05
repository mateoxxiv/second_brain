---
tags:
  - status/seed
  - probability
related:
  - "[[unbiased-and-biased-estimators]]"
  - "[[sampling-distribution]]"
  - "[[monte-carlo-simulation]]"
  - "[[law-of-large-numbers]]"
  - "[[measures-of-variation]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-4 (estimadores sesgados)"
  - "Wasserman, All of Statistics, §6.2 and §8 (bias; bootstrap)"
  - "https://en.wikipedia.org/wiki/Unbiased_estimation_of_standard_deviation"
---

> **TL;DR** — A biased estimator has a **habit**: on average it lands at a fixed *fraction* of the truth. You measure that habit once on a fake population whose true value you chose (a "sugar bag"), then **divide** every real estimate by it.

---

## Intuition

You can't see the true σ of your real population, so you can't check your estimate against it. But you *can* test the **tool**. A kitchen scale is checked with a bag of sugar known to weigh 1 kg: if it reads 0.94 kg, the scale reads 6% low, and from then on you correct every reading by that amount. The sugar's weight is irrelevant to the flour you weigh later; you keep only the **6%**.

Here the tool is "compute s from n = 5 values." The sugar bag is a computer-made population with a σ *you* chose. Any σ works, because the habit belongs to the tool, not to the population.

## Mechanics

**One estimate = truth + habit + shake.** The habit (bias) is systematic and correctable. The shake (spread of the [[sampling-distribution]]) is random and gets reported as ±.

**The habit, as a ratio:**

$$h = \frac{E[\hat\theta]}{\theta} \;\approx\; \frac{\text{average of } \hat\theta \text{ over many simulated samples}}{\theta_{\text{fake}}}$$

**The correction:**

$$\hat\theta_{\text{corrected}} = \frac{\hat\theta_{\text{real}}}{h}$$

**The experiment (4 steps):**
1. **Fake population.** A random-number machine with the *shape* of your real data (here: normal), any center (170) and any spread (σ = 10). No real data is used.
2. **Many samples.** Draw n = 5 values (your real n) and compute s. Repeat 100,000 times.
3. **Average.** The shake cancels out ([[law-of-large-numbers]]): the average s settles at 9.41.
4. **Habit.** h = 9.41 ÷ 10 = 0.94. Throw the fake σ away and keep only h.

**Apply it:** real data gives s = 4.7, so the corrected estimate is 4.7 ÷ 0.94 ≈ 5.0.

| Machine setting | Affects h? | How to choose it |
|---|---|---|
| Center, spread σ | No | anything convenient |
| **Shape** | **Yes** | match the real data's histogram |
| **Sample size n** | **Yes** | your real n |

**Divide or subtract? Test two spreads.** If the *ratio* stays fixed (σ = 10 gives 9.41, σ = 100 gives 94.04; both are 0.94), the bias is multiplicative, so **divide**. If the *gap* stayed fixed instead (always 0.6 low), it would be additive, so you'd **subtract**. For s it's multiplicative: scaling all data by k scales s by k. Theory gives h = c₄(n) for normal data: 0.798, 0.940, 0.973, 0.991 for n = 2, 5, 10, 30.

```python
import numpy as np
rng = np.random.default_rng(0)
for sigma in (10, 100):                                  # sugar bags: σ chosen, so known
    samples = rng.normal(170, sigma, size=(100_000, 5))  # 100,000 samples of n = 5
    s = samples.std(axis=1, ddof=1)                      # one s per sample
    print(sigma, s.mean(), s.mean() / sigma)             # 9.41 → 0.941 | 94.04 → 0.940
h = 0.94
print(4.7 / h)                                           # real s = 4.7 → corrected ≈ 5.0
```

**No shape known?** Use the bootstrap: resample your *real* data with replacement instead of a machine. Estimated bias ≈ (average of the resampled statistics) − (original statistic). It needs a reasonable n; with 5 values it's crude.

## In ML

**Adam's bias correction.** Adam's moving averages start at 0, so early on they read low by the known factor 1 − βᵗ. Dividing by it is exactly this note's correction, with h computed analytically instead of by simulation.

**Simulation-based calibration.** Testing an estimator or model on synthetic data where the truth is known, then correcting the real-data output, is a standard check across ML (e.g. verifying uncertainty estimates before trusting them).

## Exercises

**Basic** — A tool's average output on a fake population with θ = 50 is 45. What is h? Correct a real estimate of 18.

**Intermediate** — Write the 4-step experiment to find the habit of the sample *range* for n = 5 normal heights. Expect h further from 1 than 0.94, and explain why.

**Advanced** — Repeat the experiment with a right-skewed machine (e.g. lognormal). Does h change? What does that say about using c₄ on skewed data like incomes?
