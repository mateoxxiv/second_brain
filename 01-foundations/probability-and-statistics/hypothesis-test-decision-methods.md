---
tags:
  - status/seed
  - probability
related:
  - "[[p-value]]"
  - "[[critical-region-and-significance-level]]"
  - "[[confidence-interval]]"
  - "[[confidence-interval-for-proportion]]"
  - "[[adjusted-wald-and-wilson-intervals]]"
  - "[[one-tailed-vs-two-tailed-tests]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Criterio de decisión; Figuras 8-8 y 8-9; Tabla 8-2)"
---

> **TL;DR** — The P-value method, the traditional critical-region method, and the confidence-interval method are three routes to the same decision, provided they use the same α.

---

## Intuition

Each method answers the same question, "is the data too unusual under H0?", with a different summary. The P-value compresses the question to one number. The critical region compares the statistic to a boundary. The confidence interval asks whether the claimed value sits inside the plausible range.

## Mechanics

**Method 1 — P-value** (Figura 8-8): compute $P$. Reject H0 if $P \le \alpha$. Most software reports $P$, so this route is now the most common.

**Method 2 — Traditional** (Figura 8-9): compute the statistic, the critical value(s) and the region. Reject H0 if the statistic is inside the region.

**Method 3 — Confidence interval**: build an interval, then reject the claim if the interval excludes the claimed value.
- Two-tailed test: confidence level $1-\alpha$. For α = 0.05, that is 95%.
- One-tailed test: confidence level $1-2\alpha$. For α = 0.05, that is 90% (Table 8-2).

> The paste garbled this rule so both cases read "1 − 2α". Table 8-2 is the reliable source, so the table values above are used here. Verify against the printed book.

XSORT example (13 of 14 girls, $\hat p = 0.929$, α = 0.05, H1: $p > 0.5$):

| Method | Result | Decision |
|---|---|---|
| P-value | $P = 0.0007 \le 0.05$ | reject H0 |
| Traditional | $z = 3.21 > 1.645$ | reject H0 |
| 90% CI (one-tailed) | lower bound ≈ 0.82 $> 0.5$ | reject H0 |

The CI here uses a plain Wald interval, which is poor at n = 14. Treat the lower bound as a rough check. [[adjusted-wald-and-wilson-intervals]] gives a better one.

```python
import math

p_hat, n, z90 = 13 / 14, 14, 1.645        # z for a one-sided 90% interval
se = math.sqrt(p_hat * (1 - p_hat) / n)
lower = p_hat - z90 * se
print(round(lower, 3))                     # about 0.816, above 0.5 -> reject H0
```

## In ML

**Report the effect size with the test** — the CI method gives a range of plausible effects, which tells you more than "p < 0.05". See [[statistical-significance]].

**Which method to use** — report the P-value for software output and the CI for the effect size. Use the critical region when teaching the logic.

## Exercises

**Basic** — $P = 0.03$ and α = 0.05. What is the decision?

**Intermediate** — Two-tailed $z = 2.10$, α = 0.05. Decide by the critical region and by the P-value. Check that the two agree.

**Advanced** — When can the CI method and the test give different answers? Hint: think about small n and proportions near 0 or 1.
