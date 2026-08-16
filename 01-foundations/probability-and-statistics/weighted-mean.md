---
tags:
  - status/seed
  - probability
related:
  - "[[measures-of-center]]"
  - "[[frequency-distribution]]"
  - "[[characteristics-of-data]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 3, §3-2 Parte 2."
---

> **TL;DR** — A weighted mean lets some values count more than others, $\bar{x}=\dfrac{\sum(w\cdot x)}{\sum w}$; the ordinary [[measures-of-center|mean]] is the special case where all weights equal 1, and the **mean of a [[frequency-distribution]]** is just a weighted mean with the frequencies as weights.

---

## Intuition

The plain mean treats every value as equally important. But often they aren't: a 4-credit course should influence your GPA more than a 1-credit one; a class-interval containing 90 students should count more than one containing 3. A weighted mean fixes this by attaching a **weight** $w$ to each value — "how much this value counts" — and averaging accordingly. If all weights are equal, it collapses back to the ordinary mean, so it's a strict generalization, not a new idea.

## Mechanics

**Weighted mean (Formula 3-3):**
$$\bar{x}=\frac{\sum (w\cdot x)}{\sum w}$$
Multiply each value by its weight, sum the products, divide by the sum of the weights.

**Mean from a frequency distribution (Formula 3-2)** — the same formula, where the weight is the class **frequency** $f$ and the value is the class **mark** $x$ (midpoint), because we *assume every value in a class sits at its midpoint*:
$$\bar{x}=\frac{\sum (f\cdot x)}{\sum f}$$
This is an **approximation** of the true mean — it discards the exact values inside each class. (Triola's 186 men: grouped estimate 15,913.5 vs. true 15,668.5.)

| Case | Weight $w$ | Value $x$ | Note |
|------|-----------|-----------|------|
| Ordinary mean | 1 for all | data value | special case, $\sum w = n$ |
| GPA | credits | grade points | Triola's 3.07 example |
| Grouped data | class frequency $f$ | class mark | approximates the true mean |

```python
import numpy as np
grades  = np.array([4, 4, 3, 2, 0])   # A A B C F → quality points
credits = np.array([3, 4, 3, 3, 1])   # weights
np.average(grades, weights=credits)   # 3.07  (= 43/14)
```

> ⚠️ **The per-capita trap (Triola Ex. 7).** The mean of the 50 U.S. state per-capita incomes ($33,442) is *not* the national per-capita income ($34,586) — states have wildly different populations, so you must **weight each state's mean by its population**. Averaging means without weights silently assumes equal group sizes.

## In ML

**Weighted loss handles class imbalance.** Multiplying each sample's loss by a class weight (rare classes weighted up) is a weighted mean of per-sample losses — the standard fix for skewed labels in `class_weight='balanced'` and weighted cross-entropy.

**Ensembles and attention are weighted means.** A weighted-average ensemble, the convex combination in boosting, and the softmax-weighted sum of value vectors in **attention** ($\sum \alpha_i v_i$ with $\sum \alpha_i = 1$) are all $\frac{\sum w x}{\sum w}$ with learned or normalized weights.

**Expected value is a weighted mean.** $E[X]=\sum x\, p(x)$ is exactly this formula with probabilities as weights (summing to 1) — the bridge from descriptive statistics to probability distributions.

## Exercises

**Basic** — Compute the GPA for A(3 cr), A(4 cr), B(3 cr), C(3 cr), F(1 cr) using A=4, B=3, C=2, F=0. Confirm you get 3.07 and explain why it differs from the unweighted mean of {4,4,3,2,0}.

**Intermediate** — A frequency distribution has classes with marks 5, 15, 25 and frequencies 46, 90, 40. Estimate the mean. Why is this only an approximation of the true mean?

**Advanced** — Prove that when all weights are equal ($w_i = c$), the weighted mean reduces to the ordinary mean. Then explain, using the per-capita example, what assumption you make when you average a set of group means *without* weights.
