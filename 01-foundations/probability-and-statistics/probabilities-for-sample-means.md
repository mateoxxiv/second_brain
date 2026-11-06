---
tags:
  - status/seed
  - probability
related:
  - "[[central-limit-theorem]]"
  - "[[standard-error-of-the-mean]]"
  - "[[normal-probabilities-via-standardization]]"
  - "[[z-score]]"
  - "[[identifying-unusual-results]]"
  - "[[p-value]]"
  - "[[one-mean-z-test]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-5 (Aplicación del teorema del límite central; regla del evento inusual)"
---

> **TL;DR** — Before you compute a normal probability, ask "**one individual or a mean of n?**". For one value use z = (x − μ)/σ. For a sample mean use z = (x̄ − μ)/(σ/√n). Mixing them up is the classic Ch. 6 mistake.

---

## Intuition

A single tall person is common. A whole elevator full of tall people is rare. Means are pulled toward μ, so the same cutoff is far less extreme for one person than for an average of 25. Same cutoff, different curve: the curve for x̄ is √n times narrower.

## Mechanics

| Question about | Standardize with | Needs |
|---|---|---|
| One value x | $z = \dfrac{x-\mu}{\sigma}$ | a normal population (the CLT says nothing about one value) |
| A mean x̄ of n values | $z = \dfrac{\bar x-\mu}{\sigma/\sqrt n}$ | a normal population **or** n > 30 ([[central-limit-theorem]]) |

The second row is just the [[z-score]] of x̄ on its own [[sampling-distribution]]. That distribution has mean μ and SD σ/√n ([[standard-error-of-the-mean]]).

**Worked (illustrative numbers, not from the book).** Adult weights are normal with μ = 170 lb and σ = 30 lb. An elevator for 25 people is rated at 4,500 lb, so it is overloaded when the mean weight is over 180 lb.

| | Calculation | Probability |
|---|---|---|
| One rider > 180 lb | z = (180 − 170)/30 = 0.33 | 0.3694 (common) |
| Mean of 25 > 180 lb | SE = 30/√25 = 6, z = 10/6 = 1.67 | 0.0478 (rare) |

The safety rating depends on the **mean** of the group, so the second row is the one that matters. Using the first row would overstate the risk by about 8×.

**Rare-event rule** ([[identifying-unusual-results]]): if a result is unlikely under an assumption (P ≤ 0.05), the assumption is probably wrong. Suppose 25 random riders average 182 lb. Then z = 2.0 and P(x̄ ≥ 182) = 0.023, which casts doubt on μ = 170. That is a one-tailed [[p-value]] before the name appears. Ch. 8 formalizes it in the [[one-mean-z-test]].

```python
from math import sqrt
from scipy import stats
mu, sigma, n, cut = 170, 30, 25, 180
p_one  = stats.norm.sf((cut - mu) / sigma)             # one person: SD = sigma
p_mean = stats.norm.sf((cut - mu) / (sigma / sqrt(n))) # mean of n: SD = sigma/sqrt(n)
print(round(p_one, 4), round(p_mean, 4))               # 0.3694 0.0478
```

## In ML

**Alert thresholds on averaged metrics.** If a dashboard averages latency over n requests, set alert limits with σ/√n, not σ. Otherwise the alerts almost never fire, and real regressions hide inside the "normal" band.

**"Is this batch unusual?"** Data-drift checks compare a batch mean of a feature with its training μ, using exactly z = (x̄ − μ)/(σ/√n).

## Exercises

**Basic** — With μ = 100 and σ = 15: find P(x > 105) for one person and P(x̄ > 105) for n = 36. *(0.3694 and 0.0228)*

**Intermediate** — For the elevator, what is the largest number of riders n for which P(mean > 180) is still above 0.10? Interpret this for a safety engineer.

**Advanced** — A population is strongly right-skewed (μ = 10, σ = 10) and n = 4. Why can't you use either formula here? Simulate P(x̄ > 15) and compare it with the normal answer.
