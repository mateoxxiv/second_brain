---
tags:
  - status/seed
  - probability
related:
  - "[[identifying-unusual-results]]"
  - "[[statistical-significance]]"
  - "[[critical-region-and-significance-level]]"
  - "[[hypothesis-test-decision-methods]]"
  - "[[continuity-correction]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Valor P; Ejemplos 7–8; Figura 8-5; Advertencia)"
---

> **TL;DR** — The P-value is the probability, assuming H0 is true, of a test statistic at least as extreme as the one observed. Small P means the data are hard to explain under H0.

---

## Intuition

Instead of asking "did the statistic cross a cutoff?", ask "how surprising is this?" The P-value is the tail area beyond the observed statistic. It is the rare-event rule from [[identifying-unusual-results]] applied to a test statistic, and it is what [[statistical-significance]] was measuring informally.

## Mechanics

Triola's rule (Figura 8-5), with $z$ the observed statistic:

- **Left-tailed** H1: $P$ = area to the left of $z$.
- **Right-tailed** H1: $P$ = area to the right of $z$.
- **Two-tailed** H1: $P$ = twice the area beyond $|z|$ in the tail where the statistic falls.

Decision rule: reject H0 when $P \le \alpha$.

XSORT example ($z = 3.21$):
- Right-tailed: area to the right is 0.0007, so $P = 0.0007$.
- Two-tailed: the book doubles the rounded table value, $2 \times 0.0007 = 0.0014$. More precise computation gives 0.0013.

```python
from scipy.stats import norm

z = 3.21
p_right = norm.sf(z)           # area to the right of z
p_two = 2 * norm.sf(abs(z))    # two-tailed P-value
print(round(p_right, 4), round(p_two, 4))   # 0.0007  0.0013
```

**Watch out**

- **P is not the population proportion.** Triola's warning box: $P$ is a probability about a statistic; $p$ is a parameter.
- **P is not the probability that H0 is true.** It is computed assuming H0 is true.
- **Normal approximation shifts small P-values.** For 13 of 14 births, the exact binomial tail is $P(X \ge 13) \approx 0.0009$, a plain normal $z$ gives 0.0007, and the book quotes 0.0016 with a continuity correction. See [[continuity-correction]].

## In ML

**Significance of a score gap** — comparing two models' cross-validation scores uses the same tail logic: a P-value small enough means the gap is unlikely to be noise.

**Many metrics** — a dashboard with dozens of metrics will show small P-values by chance. See [[multiple-testing-problem]].

## Exercises

**Basic** — A left-tailed test gives $z = -2.10$. Find $P$ using the area to the left.

**Intermediate** — A two-tailed test gives $z = 1.80$. Find $P$. Decide at α = 0.05.

**Advanced** — The book's two-tailed P (0.0014) is twice a rounded table value. Recompute from the exact $z$ and explain why rounding matters more when $P$ is tiny.
