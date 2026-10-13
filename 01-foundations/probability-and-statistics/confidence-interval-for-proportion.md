---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval]]"
  - "[[margin-of-error]]"
  - "[[point-estimate]]"
  - "[[normal-approximation-to-binomial]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Procedimiento para construir un intervalo de confianza; Requisitos; Ejemplo 3)"
---

> **TL;DR** — To build a confidence interval for p: check the requirements, find z_{α/2}, compute E, then report p̂ ± E rounded to three significant figures.

---

## Intuition

The confidence interval is a recipe. The recipe only works when the sample is random and the normal approximation is safe. Checking the requirements first is the step that protects the rest of the calculation, because the formula doesn't warn you when its assumptions fail.

## Mechanics

**Requirements.**
1. The sample is a simple random sample. A voluntary-response sample breaks the method.
2. The binomial conditions hold: a fixed number of trials, independent trials, two outcomes, and constant p.
3. There are at least 5 successes and 5 failures, so np̂ ≥ 5 and nq̂ ≥ 5. Use p̂ in place of p when checking, because p is unknown.

**Procedure.**
1. Verify the requirements.
2. Find z_{α/2} for the chosen confidence level. Use 1.96 for 95%.
3. Compute E = z_{α/2} · √(p̂q̂ / n).
4. Form the limits p̂ − E and p̂ + E.
5. Round the limits to three significant figures.

**Notation.** The same interval can be written as p̂ ± E, as (p̂ − E, p̂ + E), or as p̂ − E < p < p̂ + E.

**Triola's Ejemplo 3** (n = 1501, p̂ = 0.70, 95%):

- Requirements: 0.70 × 1501 ≈ 1051 successes and 450 failures, both at least 5.
- E = 1.96 · √(0.70 · 0.30 / 1501) ≈ 0.023
- Interval: 0.70 − 0.023 < p < 0.70 + 0.023, so 0.677 < p < 0.723.
- As percentages: 67.7% < p < 72.3%.

Triola's conclusion is that the interval lies entirely above 0.5, so the majority holds the view. Be careful with the exact claim: the interval supports "more than half," given the confidence level.

```python
import math
from scipy.stats import norm
p_hat, n = 0.70, 1501                              # the reported 70%
assert n * p_hat >= 5 and n * (1 - p_hat) >= 5     # requirement check
z = norm.ppf(0.975)                                # 1.96
E = z * math.sqrt(p_hat * (1 - p_hat) / n)         # ≈ 0.0232
print(round(p_hat - E, 3), round(p_hat + E, 3))    # 0.677 0.723
```

## In ML

**A/B conversion rates.** Before reporting a conversion interval, check that the number of conversions and non-conversions are both at least 5. A test with 3 conversions in 500 visitors fails the requirement, so the normal interval isn't valid and an exact method is needed.

**Accuracy on a test set.** Accuracy is a proportion, so the same recipe applies if the test examples were drawn at random. If the test set was curated, the requirement fails even when the numbers look large.

**Reporting.** Always state the confidence level and the sample size, following Triola's list for survey results.

## Exercises

**Basic** — A random sample of n = 400 has p̂ = 0.30. Verify the requirements, then build the 95% interval.

**Intermediate** — A sample of n = 50 has p̂ = 0.08. Check the requirements. If they fail, explain why the normal interval would be unreliable.

**Advanced** — Triola says the requirement uses p̂ rather than p. Why is that acceptable, and under what conditions could it mislead you?
