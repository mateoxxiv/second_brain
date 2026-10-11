---
tags:
  - status/seed
  - probability
related:
  - "[[binomial-distribution]]"
  - "[[binomial-mean-and-variance]]"
  - "[[binomial-distribution-requirements]]"
  - "[[poisson-approximation-to-binomial]]"
  - "[[continuity-correction]]"
  - "[[normal-probabilities-via-standardization]]"
  - "[[identifying-unusual-results]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-6 (La distribución normal como aproximación de la distribución binomial)"
---

> **TL;DR** — When $np \ge 5$ and $nq \ge 5$, a binomial with large $n$ is close to a normal with $\mu = np$ and $\sigma = \sqrt{npq}$, so you can replace a sum of many binomial terms with one z-score.

---

## Intuition

A binomial count is a sum of $n$ independent 0/1 trials. Once $n$ is large and neither outcome is too rare, the bar chart of the binomial starts to look like a bell curve. That is the Central Limit Theorem at work: the count is a sum of many small, independent pieces, so its shape approaches the normal.

The practical question is when "close enough" is good enough. Triola's answer is a simple check: both expected counts, $np$ (successes) and $nq$ (failures), must be at least 5.

## Mechanics

**Conditions** (both required):

| Condition | Why it matters |
|-----------|----------------|
| $np \ge 5$ | enough expected successes for the bell to form |
| $nq \ge 5$ | enough expected failures, so the curve is not cut off on one side |

Some textbooks use 10 instead of 5. Triola notes the 5 is a common rule, not an absolute one.

**Parameters** (from the binomial mean and variance):

$$\mu = np, \qquad \sigma = \sqrt{npq}$$

**Procedure:**
1. Check $np \ge 5$ and $nq \ge 5$. If either fails, use technology, Table A-1, or the exact formula instead.
2. Compute $\mu$ and $\sigma$.
3. Identify the discrete value $x$ the problem asks about.
4. Apply the [[continuity-correction]] to $x$, then standardize: $z = (x' - \mu)/\sigma$.
5. Read the area from Table A-2 (or software), and shade the correct side.

**Worked (Viking River survey):** $n = 40{,}000$, $p = 0.03$. Then $np = 1200$ and $nq = 38{,}800$, so the normal applies. $\mu = 1200$ and $\sigma = \sqrt{1164} \approx 34.12$. For "at least 1150", use the boundary $1149.5$:

$$z = \frac{1149.5 - 1200}{34.12} \approx -1.48, \qquad P(X \ge 1150) \approx 1 - 0.0694 = 0.9306$$

The exact binomial value is 0.9313, so the approximation is close.

```python
from scipy.stats import norm, binom
n, p = 40_000, 0.03
mu, sd = n * p, (n * p * (1 - p)) ** 0.5
print(norm.sf(1149.5, mu, sd))     # 0.9306  (approximation)
print(binom.sf(1149, n, p))        # 0.9313  (exact)
```

## In ML

**Confidence intervals for proportions.** The sampling distribution of $\hat p = X/n$ is approximately normal for large $n$, which is why accuracy or conversion-rate intervals use $\pm 1.96\sqrt{p(1-p)/n}$.

**Choosing a method.** The same condition decides whether a binomial-based metric can use the normal shortcut or needs an exact or Poisson approach. Large $n$ with $p$ near 0.5 favors the normal; large $n$ with tiny $p$ favors Poisson ([[poisson-approximation-to-binomial]]).

## Exercises

**Basic** — A coin is flipped 100 times. Check the two conditions for $p = 0.5$, then find $\mu$ and $\sigma$.

**Intermediate** — For $n = 40$ and $p = 0.1$, check the conditions. If they fail, which two alternatives from the procedure would you use, and why?

**Advanced** — Explain why the approximation is worse for small $p$ at a fixed $np$. Compare $np = 5$ with $p = 0.5$ and $np = 5$ with $p = 0.05$ in terms of skewness: which binomial is more symmetric, and how does that affect the normal approximation?
