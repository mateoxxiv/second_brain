---
tags:
  - status/seed
  - probability
related:
  - "[[characteristics-of-data]]"
  - "[[frequency-distribution]]"
  - "[[skewness]]"
  - "[[weighted-mean]]"
  - "[[normal-distribution]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 3, §3-2."
---

> **TL;DR** — A measure of center is a single value that locates the middle of a dataset; the four candidates (mean, median, mode, midrange) answer "where is the center?" differently, and the key axis separating them is **resistance** to extreme values.

---

## Intuition

Given a pile of numbers, "what's a typical value?" has no single answer — it depends on *how* you define the middle. The **mean** is the balance point (fair share if you redistribute the total equally). The **median** is the positional middle (half below, half above). The **mode** is the most common value. The **midrange** is just halfway between the smallest and largest. They agree on symmetric data and diverge on skewed data, which is exactly why comparing them is informative (see [[skewness]]).

> **Never say "average."** Triola bans the word as a name for a measure of center — it's ambiguous. Say *mean* or *median*.

## Mechanics

For a sample of size $n$ with values $x$ (population size $N$):

| Measure | Formula | Resistant? | Key property |
|---------|---------|-----------|--------------|
| **Mean** | $\bar{x}=\dfrac{\sum x}{n}$ (sample), $\mu=\dfrac{\sum x}{N}$ (pop.) | ❌ no | uses *every* value; most reliable across samples (lowest sampling variability) |
| **Median** $\tilde{x}$ | middle of the *sorted* list; if $n$ even, mean of the two middle values | ✅ yes | ignores magnitude of extremes |
| **Mode** | most frequent value(s); can be 0, 1 (unimodal), 2 (bimodal), or more | ✅ yes | **only** measure valid for [[data-types-and-levels-of-measurement\|nominal]] data |
| **Midrange** | $\dfrac{\max+\min}{2}$ | ❌ no (worst) | uses *only* the two extremes; rarely used |

**Resistance is the organizing idea.** A statistic is *resistant* if a few extreme values don't move it much. The mean uses every value, so one outlier drags it (word-count example: mean 20,456.6 vs. median 25,433 for the same five values). The midrange is built *entirely* from the two extremes, so it's the least resistant.

**Round-off rule** — carry one more decimal place than the original data; round only the **final** answer, never intermediate steps. (Mode values aren't rounded — they're actual data points.)

```python
import numpy as np
from scipy import stats
x = np.array([27531, 15684, 5638, 27997, 25433])
x.mean()            # 20456.6  — pulled down by the small 5638
np.median(x)        # 25433.0  — resistant
stats.mode(x)       # no repeat → each value once
(x.max()+x.min())/2 # 16817.5  — midrange, uses only extremes
```

## In ML

**The mean is the L2 optimum, the median is L1.** The mean minimizes squared error $\sum(x-c)^2$ and the median minimizes absolute error $\sum|x-c|$ — the same split that separates MSE from MAE loss. This is *why* least-squares regression is outlier-sensitive and quantile/robust regression is not.

**Resistance drives robust statistics.** Preferring the median (or trimmed mean) when outliers exist is the intuition behind robust estimators, RANSAC, and median-based normalization; imputing missing values with the median rather than the mean is standard when a feature is skewed.

**Mode is the classifier's answer.** Majority vote in k-NN and the leaf prediction of a classification tree are modes; for [[data-types-and-levels-of-measurement|nominal]] targets it's the *only* center that means anything.

## Exercises

**Basic** — For 5,638; 15,684; 25,433; 27,531; 27,997 compute mean, median, and midrange by hand. Which two are close, and which is pulled toward the low value?

**Intermediate** — Add 8,077 to the list above (now $n=6$). Recompute the median. Explain why the median changed only slightly while the mean dropped, and connect this to *resistance*.

**Advanced** — Show that the mean minimizes $\sum_i (x_i-c)^2$ over $c$ by differentiating and setting to zero. Then argue (no calculus needed) why the minimizer of $\sum_i |x_i-c|$ is the median. What does each result imply about outlier sensitivity?
