---
tags:
  - status/seed
  - probability
related:
  - "[[quartiles-and-iqr]]"
  - "[[measures-of-center]]"
  - "[[cdf-and-quantiles]]"
  - "[[z-score]]"
  - "[[five-number-summary-and-boxplots]]"
  - "[[ogive]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §3-4 (Ejemplos 2–5)."
---

> **TL;DR** — The **$k$-th percentile** $P_k$ is the value below which about $k\%$ of an ordered dataset falls; percentiles are *rank-based* measures of position that split the data into 100 equal-count groups.

---

## Intuition

A z-score locates a value by *distance* (standard deviations from the mean). A **percentile** locates it by *rank* — its standing in the sorted line-up. Telling a parent their child is "at the 90th percentile for height" says nothing about centimeters; it says the child is taller than about 90% of peers. That's often the more useful framing: percentiles ignore units *and* the shape of the distribution, answering only "what fraction sits below?" They divide the sorted data into 100 groups with ~1% of values each ($P_1,\dots,P_{99}$), a special case of **quantiles** (a.k.a. fractiles). By definition $P_{50}$ = the [[measures-of-center|median]].

## Mechanics

There is no universal formula — Triola gives two simple, complementary procedures.

**(1) Value → percentile.** For a specific $x$:
$$\text{percentile of }x=\frac{\text{number of values} < x}{\text{total number of values}}\times 100 \quad(\text{round to nearest integer})$$
*E.g.* in 35 sorted movie budgets, 6 are below \$29M → $\frac{6}{35}\times100\approx 17$. So \$29M is the **17th percentile**: it separates the bottom 17% from the top 83%.

**(2) Percentile → value.** Compute the **locator** $L=\dfrac{k}{100}\cdot n$, then:

| Is $L$ an integer? | $P_k$ is… |
|---|---|
| **No** | round $L$ **up**; $P_k$ = value at that position |
| **Yes** | $P_k$ = mean of the $L$-th and $(L{+}1)$-th values |

*E.g.* ($n=35$): $P_{90}$ → $L=31.5$ → round up to 32 → 32nd value = \$150M. $P_{60}$ → $L=21$ (integer) → average of 21st (\$70M) and 22nd (\$72M) = **\$71M**.

```python
import numpy as np
data = np.sort(budgets)
pct_of = (np.sum(data < 29) / data.size) * 100      # value → percentile
# value at a percentile — numpy's default 'linear' interpolation, which can differ
# slightly from Triola's locator rule (no numpy method matches it exactly):
p90 = np.percentile(data, 90, method="linear")       # software methods vary!
```

> **Warning** — calculators and libraries disagree on the interpolation rule, so a computed percentile may differ slightly from the hand method. State which convention you used.

## In ML

**Percentiles are the empirical [[cdf-and-quantiles|quantile function]].** Procedure (1) *is* the empirical CDF evaluated at $x$; procedure (2) is its inverse. The [[ogive]] graphs the same relationship. Understanding both directions is what makes quantile normalization, calibration curves, and reliability diagrams click.

**Robust summaries & thresholds.** Ranking by percentile underlies decision rules that must ignore scale and outliers — the "85th-percentile rule" traffic engineers use to set speed limits, or picking the 95th-percentile latency (p95) as a service-level objective instead of a mean that a few slow requests would wreck.

## Exercises

**Basic** — In 20 sorted values, 13 are below the score 88. What percentile is 88?

**Intermediate** — For $n=40$ sorted speeds, find $P_{85}$ using the locator method. ($L=34$, an integer — so what do you do?) Then round to the nearest multiple of 5 for a posted speed limit.

**Advanced** — Explain why procedures (1) and (2) are *not* exact inverses of each other (feed the output of one into the other and watch it drift). What causes the mismatch, and how do continuous-distribution quantiles avoid it?
