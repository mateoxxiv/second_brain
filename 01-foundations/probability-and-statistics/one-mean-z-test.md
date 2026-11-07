---
tags:
  - status/seed
  - probability
related:
  - "[[one-mean-t-test]]"
  - "[[test-statistic]]"
  - "[[hypothesis-test-decision-methods]]"
  - "[[p-value]]"
  - "[[confidence-interval-for-mean]]"
  - "[[one-proportion-z-test]]"
  - "[[central-limit-theorem]]"
  - "[[standard-error-of-the-mean]]"
  - "[[student-t-distribution]]"
  - "[[assessing-normality]]"
  - "[[identifying-unusual-results]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-4 (Prueba de una afirmación respecto de una media: σ conocida; Ejemplos 1–3)"
---

> **TL;DR** — To test a claim about μ when σ is known, standardize x̄ with the standard error of the mean, $z = (\bar x - \mu_0)/(\sigma/\sqrt n)$, and read it on the normal curve. Here the P-value, critical-value and CI methods always agree.

---

## Intuition

You ask: "If the true mean really were $\mu_0$, how surprising is the sample mean I got?" The [[central-limit-theorem]] says the means of samples of size $n$ form a normal curve centered at $\mu_0$ with spread $\sigma/\sqrt n$. So you count how many of those spreads separate $\bar x$ from $\mu_0$. This is the rare-event rule from [[identifying-unusual-results]]: if a result this extreme would rarely happen under H0, then H0 is probably wrong.

## Mechanics

**Requirements**: (1) a simple random sample; (2) σ is known; (3) the population is normal **or** $n > 30$. When $n \le 30$, accept normality if there are no outliers and the histogram is roughly bell-shaped ([[assessing-normality]]). The method is *robust* to mild non-normality but **not** to non-random samples.

**Where the statistic comes from**: under H0, $\bar x \sim N(\mu_0,\ \sigma^2/n)$, because $\mathrm{Var}(\bar x) = \sigma^2/n$ ([[standard-error-of-the-mean]]). Subtract the mean and divide by the SD:
$$z = \frac{\bar x - \mu_{\bar x}}{\sigma/\sqrt n},\qquad \mu_{\bar x} = \mu_0 \text{ (the value claimed in H0)}$$

**Why all three methods agree here** (unlike [[one-proportion-z-test]]): the test and the CI from [[confidence-interval-for-mean]] use the *same* SE, $\sigma/\sqrt n$, since σ does not depend on the claim. For a one-tailed test at α, use a $1-2\alpha$ CI.

**Worked, overloaded boats** ($n = 40$, $\bar x = 172.55$ lb, σ = 26 lb, H1: μ > 166.3, α = 0.05):

$$z = \frac{172.55 - 166.3}{26/\sqrt{40}} = \frac{6.25}{4.111} = 1.52$$

| Method | Result | Decision |
|---|---|---|
| P-value | right tail of 1.52 → $P = 0.0643$ (software: 0.0642) $> 0.05$ | fail to reject H0 |
| Traditional | $1.52 < z_{0.05} = 1.645$ | fail to reject H0 |
| 90% CI | $165.8 < \mu < 179.3$ contains 166.3 | can't support the claim |

Conclusion: there is not enough evidence that the mean weight exceeds 166.3 lb. This does **not** show that it equals 166.3 ([[concluding-hypothesis-tests-in-plain-language]]).

**Knowing σ is rare.** In practice σ is unknown, you plug in $s$, and the statistic follows the [[student-t-distribution]]: that is the [[one-mean-t-test]] (§8-5). This section is the clean teaching case.

```python
import math
from scipy import stats

def one_mean_z(x_bar: float, mu0: float, sigma: float, n: int, tail: str = "two"):
    z = (x_bar - mu0) / (sigma / math.sqrt(n))   # SE = sigma/sqrt(n), the same under H0 and the CI
    p = {"left": stats.norm.cdf(z), "right": stats.norm.sf(z),
         "two": 2 * stats.norm.sf(abs(z))}[tail]
    return z, p

print(one_mean_z(172.55, 166.3, 26, 40, "right"))   # (1.520, 0.0642)
```

## In ML

**Monitoring a known metric**: if a model's latency or error has a long, stable history (so σ is effectively known), a z-test on a new batch's mean flags drift. This is the logic behind a control chart's ±3σ/√n limits.

**Large-n shortcut**: with thousands of evaluation examples, $s \approx \sigma$ and t ≈ z. That's why many A/B-testing tools report z for means.

## Exercises

**Basic**: $n = 36$, $\bar x = 103$, σ = 12, H0: μ = 100, two-tailed, α = 0.05. Find $z$ and the P-value, and decide. *(z = 1.50, P = 0.1336)*

**Intermediate**: With the boat data ($\bar x = 172.55$, σ = 26), what is the smallest $n$ that would make the right-tailed test reject at α = 0.05? *(n = 47)*

**Advanced**: Prove algebraically that for a right-tailed test, "$z > z_\alpha$" ⇔ "$\mu_0$ lies below the lower bound of the $1-2\alpha$ CI". Then explain why the same proof fails for a proportion.
