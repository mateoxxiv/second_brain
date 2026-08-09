---
tags:
  - status/seed
  - probability
related:
  - "[[frequency-distribution]]"
  - "[[relative-frequency-distribution]]"
  - "[[cdf-and-quantiles]]"
  - "[[characteristics-of-data]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-2."
---

> **TL;DR** — A cumulative frequency distribution replaces each class count with a *running total* of that class and all prior ones, answering "how many values fall below this point?" — the discrete, sample version of the [[cdf-and-quantiles|cumulative distribution function]].

---

## Intuition

An ordinary [[frequency-distribution|frequency table]] tells you how many values sit *inside* each class. A cumulative table answers a different, often more useful question: **"how many values are below this threshold?"** Instead of "12 women have pulses in 60–69," you get "12 women have pulses *under 70*, 26 *under 80*, …". This "less than" running total is exactly how percentiles and growth charts work — a pediatrician asking "is this child below the 95th percentile?" is reading a cumulative distribution. It's the sample analogue of the [[cdf-and-quantiles|CDF]].

## Mechanics

**Definition** — the cumulative frequency of a class is the sum of its frequency and *all preceding* classes' frequencies. Two visible changes from the base table: the counts accumulate, and the **class limits become "less than" upper boundaries**.

**Worked example — women's pulses, from Triola Table 2-4** (base frequencies 12, 14, 11, 1, 1, 0, 1):

| Cumulative class | Cumulative frequency | How |
|---|---|---|
| Less than 70 | 12 | 12 |
| Less than 80 | 26 | 12 + 14 |
| Less than 90 | 37 | 12 + 14 + 11 |
| Less than 100 | 38 | + 1 |
| Less than 110 | 39 | + 1 |
| Less than 120 | 39 | + 0 |
| Less than 130 | 40 | + 1 (= total *n*) |

**Two guaranteed properties:**
- It is **monotonically non-decreasing** — a running sum never drops.
- The **final value equals the total *n*** (here 40) — everything is "less than" the top boundary.

Divide by *n* and you get the **cumulative relative frequency** (0→1), the empirical CDF: e.g. "less than 80" = 26/40 = 0.65, so ~65% of pulses are below 80. That value is directly a [[cdf-and-quantiles|percentile]] reading.

```python
from itertools import accumulate
freqs = [12, 14, 11, 1, 1, 0, 1]
cum = list(accumulate(freqs))            # [12, 26, 37, 38, 39, 39, 40]
cum_rel = [c / cum[-1] for c in cum]     # empirical CDF, ends at 1.0
print(cum, [round(r, 3) for r in cum_rel])
```

## In ML

**Cumulative frequency = the empirical CDF** — normalized cumulative frequency is $\hat{F}(x)$, the sample estimate of the true [[cdf-and-quantiles|CDF]]; it underlies quantile computation, the KS test for comparing distributions, and quantile-based feature binning.

**Percentiles and thresholds are cumulative lookups** — asking "what value is the 95th percentile?" inverts the cumulative curve; this drives outlier cutoffs, SLA latency targets (p95/p99), and calibration curves.

**Monotonic cumulative curves power ranking metrics** — ROC and precision-recall curves, and gain/lift charts, are all cumulative sweeps over a score threshold — the same "accumulate as the threshold moves" structure as this table.

## Exercises

**Basic** — From base frequencies {5, 8, 4, 3}, build the cumulative frequencies and confirm the last equals the total.

**Intermediate** — Given the women's cumulative table, estimate the percentage of pulses below 90 and below 100. Which percentile is a pulse of 80 closest to?

**Advanced** — Explain why a cumulative frequency distribution can never decrease, and what it would mean if you computed one and saw a drop (i.e., what error occurred). How does the empirical CDF relate to the true CDF as *n* grows?
