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

### Methodology — finding the habit and correcting with it

Running example: the real data is 5 student heights, which give s = 4.7 cm. We want σ.

**Step 1 — Name the tool.** Which estimator (s) and which sample size (n = 5, your real n). The habit belongs to this pair, so both must match your real situation.

**Step 2 — Check the shape of your real data.** Look at its histogram. Heights are bell-shaped, so the shape is normal. This is the only real assumption in the method.

**Step 3 — Build the sugar bag.** A random-number machine with that shape and **any** center and spread you like: normal, center 170, σ = 10. No real data goes in. Its true value θ_fake = 10 is known because you chose it.

| Machine setting | Affects h? | How to choose it |
|---|---|---|
| Center, spread σ | No | anything convenient |
| **Shape** | **Yes** | match the real data's histogram (Step 2) |
| **Sample size n** | **Yes** | your real n (Step 1) |

**Step 4 — Throw many darts.** Draw a sample of n = 5 from the machine and compute s. Repeat N = 100,000 times, giving s₁, s₂, …, s_N. Single values jump around (4.28, 15.79, …): that's the shake.

**Step 5 — Average them.** The shake cancels ([[law-of-large-numbers]]) and only the habit remains:

$$\bar{\hat\theta} = \frac{1}{N}\sum_{i=1}^{N}\hat\theta_i \qquad (\text{here } 9.41)$$

**Step 6 — Compute the habit.**

$$h = \frac{E[\hat\theta]}{\theta} \;\approx\; \frac{\bar{\hat\theta}}{\theta_{\text{fake}}} = \frac{9.41}{10} = 0.94$$

So s with n = 5 lands at about 94% of the truth on average: it reads about 6% low.

**Step 7 — Divide or subtract? Repeat Steps 3–6 with a different spread.** σ = 100 gives an average of 94.04, so the **ratio** stays 0.94 while the **gap** grows (0.59 → 5.96). A fixed ratio means a multiplicative habit, so you **divide**. A fixed gap would mean an additive habit, and you'd **subtract** it instead. For s it's always multiplicative, because scaling all data by k scales s by k.

**Step 8 — Throw the sugar bag away.** Keep only h = 0.94. The fake σ never touches your real data.

**Step 9 — Correct the real estimate.**

$$\hat\theta_{\text{corrected}} = \frac{\hat\theta_{\text{real}}}{h} = \frac{4.7}{0.94} \approx 5.0 \text{ cm}$$

**Step 10 — Report the shake.** The correction fixes only the habit. A single estimate still wobbles (for s with n = 5, about ±35% of σ), so report a ± or an interval, not just 5.0.

**Cross-check with theory:** for normal data the habit of s is known exactly, h = c₄(n): 0.798, 0.940, 0.973, 0.991 for n = 2, 5, 10, 30. Step 6 matches c₄(5) = 0.940.

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
