---
tags:
  - status/seed
  - probability
related:
  - "[[probability-distributions]]"
  - "[[normal-distribution]]"
  - "[[exponential-distribution]]"
  - "[[probability-fundamentals]]"
domain: probability
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
  - "https://docs.scipy.org/doc/scipy/reference/stats.html"
---

> **TL;DR** — CDF = P(X ≤ x). Inverse CDF (quantile function) = "what x gives P(X≤x)=p?". Foundation of confidence intervals, percentiles, and sampling from any distribution.

---

## Intuition

The CDF answers "what fraction of probability mass lies at or below x?" It accumulates probability from left to right. The inverse CDF flips the question: given a probability level p, what value x does it correspond to?

Practical payoff: confidence intervals, anomaly thresholds, and percentiles are all just evaluations of the inverse CDF. Inverse transform sampling lets you draw from any distribution using only Uniform(0,1).

## Mechanics

**CDF:** F(x) = P(X ≤ x)
- Always starts at 0, ends at 1, non-decreasing
- Continuous distribution: F(x) = ∫_{−∞}^x f(t) dt

**Inverse CDF (quantile function):** F^{−1}(p) = inf{x : F(x) ≥ p}

**95% CI from Normal:** lower = F^{−1}(0.025) = −1.96, upper = F^{−1}(0.975) = 1.96

**Inverse transform sampling algorithm:**
1. Draw u ~ Uniform(0, 1)
2. Return x = F^{−1}(u)

This works because F^{−1} maps uniform probability to the correct density.

| Distribution | CDF F(x) | Inverse CDF F^{−1}(p) |
|---|---|---|
| Uniform(a,b) | (x−a)/(b−a) | a + p(b−a) |
| Exponential(λ) | 1 − e^{−λx} | −ln(1−p)/λ |
| Normal(μ,σ) | Φ((x−μ)/σ) | μ + σΦ^{−1}(p) |

```python
import numpy as np
from scipy import stats

# CDF and inverse CDF
print(stats.norm.cdf(1.96))    # 0.9750
print(stats.norm.ppf(0.975))   # 1.96

# 95% confidence interval
alpha = 0.05
lo, hi = stats.norm.ppf(alpha/2), stats.norm.ppf(1 - alpha/2)
print(f"95% CI: [{lo:.4f}, {hi:.4f}]")  # [-1.96, 1.96]

# Inverse transform sampling for Exponential(2) from Uniform only
lam = 2.0
u = np.random.uniform(0, 1, size=100000)
x = -np.log(1 - u) / lam      # F^{-1}(u) for Exponential
print(f"Mean: {x.mean():.4f}  (expected {1/lam:.4f})")
```

> Runnable: [[code/foundations/cdf_and_quantiles.py]]

## In ML

**Confidence intervals.** The 95% CI for a Normal estimate is [μ − 1.96σ, μ + 1.96σ]. The 1.96 comes directly from Normal inverse CDF at p=0.975. Different distributions → different quantile values.

**Anomaly detection thresholds.** Flag x as anomalous if F(x) > 0.99 — it falls in the top 1% of the distribution. This converts the threshold-setting problem into a quantile problem you can solve analytically.

**P-values are CDF evaluations.** A p-value is P(statistic ≥ observed | H₀ true) = 1 − F(observed). Computing p-values requires knowing the CDF of the test statistic under the null hypothesis.

## Exercises

**Basic** — Use scipy to find the 99th percentile of N(0,1). Then find the 1st percentile. What is the relationship?

**Intermediate** — Implement inverse transform sampling for Exponential(2) from scratch using only np.random.uniform. Verify E and Var match the theoretical values.

**Advanced** — Explain why the Normal distribution has no closed-form inverse CDF. What does this mean computationally for confidence interval calculations?
