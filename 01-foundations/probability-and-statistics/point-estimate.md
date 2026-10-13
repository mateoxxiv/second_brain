---
tags:
  - status/seed
  - probability
related:
  - "[[unbiased-and-biased-estimators]]"
  - "[[sampling-distribution]]"
  - "[[parameter-vs-statistic]]"
  - "[[binomial-mean-and-variance]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Estimación puntual; Ejemplo 1)"
---

> **TL;DR** — The best single-number estimate of a population proportion p is the sample proportion p̂, but one number says nothing about how far off it might be.

---

## Intuition

A poll of 1501 adults finds 70% who believe in global warming. If someone asks, "what is the share in the whole country?", the honest one-number answer is 0.70. It is the best guess we have. But it's a single arrow. It doesn't say whether the bullseye is close or far, and another poll would land somewhere else. A point estimate answers "what is my best guess?" and leaves "how sure am I?" open.

## Mechanics

Let p̂ = x / n, where x is the number of successes in a sample of size n. Each person is coded 1 (yes) or 0 (no), so p̂ is the average of those 0/1 values.

| Property | Statement | Why it matters |
|----------|-----------|---------------|
| Unbiased | E[p̂] = p | Samples don't systematically over- or under-shoot p |
| Consistent | SD(p̂) → 0 as n grows | More data gives a tighter cluster of estimates |
| Smallest spread | SD(p̂) is smaller than that of any other unbiased estimator | Triola's sense of "most consistent" |

**Why it's unbiased.** Write p̂ = (X₁ + … + Xₙ)/n with each Xᵢ ∈ {0, 1} and P(Xᵢ = 1) = p. Then E[Xᵢ] = p, and linearity gives E[p̂] = p. Each Xᵢ has variance pq, so Var(p̂) = pq/n and SD(p̂) = √(pq/n).

```python
import numpy as np
rng = np.random.default_rng(0)
p, n = 0.70, 1501
p_hats = rng.binomial(1, p, size=(10_000, n)).mean(axis=1)   # 10,000 surveys
print(p_hats.mean())   # ≈ 0.70, unbiased
print(p_hats.std())    # ≈ √(0.7·0.3/1501) ≈ 0.0118
```

## In ML

**Accuracy is a sample proportion.** Test-set accuracy is p̂, the fraction of correct predictions. Reporting 92% alone hides its error, which is about √(p̂q̂/n) for the test size. A confidence interval shows how much a difference of 1% can be trusted.

**A/B tests.** A conversion rate is a sample proportion. Saying "variant B converts 4.4% vs. 4.1%" without an interval hides whether the gap is noise.

**Estimating p from a finite sample.** Any metric computed from a held-out set is a point estimate of its true value over the population. The same unbiased-estimator reasoning applies, and the spread still needs reporting.

## Exercises

**Basic** — A sample of n = 400 finds 120 successes. Compute p̂, then estimate SD(p̂) using p̂ in place of p.

**Intermediate** — Show that E[p̂] = p using only linearity of expectation. Then explain why quadrupling n halves SD(p̂).

**Advanced** — Consider the estimator p̃ = X₁, which uses only the first person's answer. Show it's unbiased, compute its variance, and explain why using all n observations is better.
