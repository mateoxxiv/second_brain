---
tags:
  - status/seed
  - probability
related:
  - "[[test-statistic]]"
  - "[[normal-approximation-to-binomial]]"
  - "[[hypothesis-test-decision-methods]]"
  - "[[p-value]]"
  - "[[confidence-interval-for-proportion]]"
  - "[[exact-binomial-test]]"
  - "[[binomial-distribution-requirements]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-3 Parte 1 (Ejemplos 1–3; Fundamentos del estadístico de prueba)"
---

> **TL;DR** — To test a claim about a proportion, standardize $\hat p$ with the H0 standard error, $z = (\hat p - p)/\sqrt{pq/n}$, and read it on the normal curve; valid when $np \ge 5$ and $nq \ge 5$.

---

## Intuition

Under H0 the count of successes is binomial. When $n$ is large enough, that binomial looks normal, so "how surprising is $\hat p$?" becomes "how many standard errors is $\hat p$ from the claimed $p$?". This is the general [[test-statistic]] template applied to one proportion.

## Mechanics

**Requirements** — (1) simple random sample; (2) binomial conditions: fixed $n$, independent trials, two outcomes, constant $p$ ([[binomial-distribution-requirements]]); (3) $np \ge 5$ and $nq \ge 5$, using the **claimed** $p$, not $\hat p$.

**Where the statistic comes from** — the [[normal-approximation-to-binomial]] gives $z = (x - np)/\sqrt{npq}$. Divide top and bottom by $n$ and write $\hat p = x/n$:
$$z = \frac{x/n - p}{\sqrt{npq}/n} = \frac{\hat p - p}{\sqrt{pq/n}}$$
No [[continuity-correction]]: with large $n$ its effect is tiny.

**Getting $x$ from a percentage** — 55% of 104 is 57.2, so $x = 57$ (round to a whole count). Then use $\hat p = 57/104 = 0.548$, not 0.55.

**Worked, XSORT** (668 girls in 726 births, α = 0.05, H0: $p = 0.5$, H1: $p > 0.5$):

| Method | Result | Decision |
|---|---|---|
| P-value | $z = 22.64$, $P \approx 0$ (table: 0.0001) | reject H0 |
| Traditional | $22.64 > 1.645$ | reject H0 |
| 90% CI | $0.904 < p < 0.937$, all above 0.5 | support claim |

Triola prints $z = 22.63$ because it rounds $\hat p$ to 0.920 first.

**Worked, pregnancy guesses** (57 of 104 correct, two-tailed, H0: $p = 0.5$): $z = 0.98$, $P = 2(0.1635) = 0.327 > 0.05$, critical values $\pm 1.96$, 95% CI $0.452 < p < 0.644$ contains 0.5. Fail to reject. You cannot conclude the rate *is* 50% ([[concluding-hypothesis-tests-in-plain-language]]).

**The CI is not equivalent here.** The test uses $\sqrt{pq/n}$ (claimed $p$); the interval uses $\sqrt{\hat p\hat q/n}$ (sample). So they can disagree near the boundary. Triola's rule: estimate with a CI, test with the P-value or critical value.

```python
import math
from scipy import stats

def one_prop_z(x: int, n: int, p0: float, tail: str = "two") -> tuple[float, float]:
    z = (x / n - p0) / math.sqrt(p0 * (1 - p0) / n)   # SE under H0 uses p0
    p = {"left": stats.norm.cdf(z), "right": stats.norm.sf(z),
         "two": 2 * stats.norm.sf(abs(z))}[tail]
    return z, p

print(one_prop_z(57, 104, 0.5))   # (0.981, 0.3268)
```

## In ML

**Is a classifier better than chance?** — accuracy on $n$ test items is $\hat p$; test against the chance rate $p_0$ (0.5 for balanced binary). Same formula.

**Conversion-rate checks** — "the new page converts above 3%" is a right-tailed one-proportion test. The two-group A/B version uses a pooled two-proportion $z$ (Triola Ch. 9).

## Exercises

**Basic** — 60 heads in 100 flips, H1: $p \ne 0.5$, α = 0.05. Compute $z$, the P-value, and decide.

**Intermediate** — 20 successes in 30 trials, H0: $p = 0.9$. Check the requirements. Which one fails, and which test should you use instead?

**Advanced** — Find $x$ and $n$ where the 95% Wald CI excludes $p_0$ but the two-tailed $z$ test does not reject (or the reverse). Explain using the two standard errors.
