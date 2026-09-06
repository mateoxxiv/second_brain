---
tags:
  - status/seed
  - probability
related:
  - "[[percentiles]]"
  - "[[measures-of-center]]"
  - "[[measures-of-variation]]"
  - "[[five-number-summary-and-boxplots]]"
  - "[[skewness]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §3-4 (Ejemplo 6)."
---

> **TL;DR** — The three **quartiles** $Q_1,Q_2,Q_3$ cut an ordered dataset into four equal-count quarters; their spread $\text{IQR}=Q_3-Q_1$ is an **outlier-resistant** measure of variation.

---

## Intuition

Just as 99 [[percentiles]] split data into 100 groups, three quartiles split it into four ~25% chunks. They're the everyday percentiles: $Q_1$ marks the bottom quarter, $Q_2$ is the middle (the [[measures-of-center|median]]), $Q_3$ marks the top quarter. Their real power is what lives *between* them. The **interquartile range**, $Q_3-Q_1$, measures the spread of the *central half* of the data — and because it throws away the top and bottom 25%, no extreme value can touch it. That makes IQR the **resistant** cousin of the [[measures-of-variation|standard deviation]]: where $s$ is inflated by a single outlier, IQR shrugs it off.

## Mechanics

Quartiles are just three specific percentiles, computed with the §3-4 locator method:

$$Q_1=P_{25}\qquad Q_2=P_{50}=\text{median}\qquad Q_3=P_{75}$$

More precisely, *at least* 25% of values are $\le Q_1$ and *at least* 75% are $\ge Q_1$ (symmetrically for $Q_3$). *Worked* ($n=35$ movie budgets): $Q_1=P_{25}$ → $L=8.75$ → round up to 9 → 9th value = **\$35M**.

Several standard statistics are built from quartiles and percentiles:

| Statistic | Formula | Meaning |
|-----------|---------|---------|
| Interquartile range (IQR) | $Q_3-Q_1$ | spread of the middle 50% |
| Semi-interquartile range | $(Q_3-Q_1)/2$ | half of IQR |
| Midquartile | $(Q_3+Q_1)/2$ | a resistant center estimate |
| 10–90 percentile range | $P_{90}-P_{10}$ | spread ignoring the tails |

```python
import numpy as np
q1, q2, q3 = np.percentile(data, [25, 50, 75])
iqr = q3 - q1        # note: numpy's default interpolation differs from Triola's
```

> **No universal convention** — like percentiles, quartile values vary by software (Excel's `QUARTILE.INC` vs `.EXC`, etc.). Expect small discrepancies from the hand method and report your rule.

## In ML

**IQR is the standard outlier detector.** The $1.5\times\text{IQR}$ fence (see [[five-number-summary-and-boxplots]]) flags outliers using only quartiles — unlike the $|z|>3$ rule, its thresholds aren't themselves corrupted by the outliers, so it stays reliable on skewed, heavy-tailed data.

**Resistant spread for skewed features.** When a feature is [[skewness|skewed]] or heavy-tailed, reporting IQR (or using `RobustScaler`, which divides by IQR) beats the SD, which a long tail exaggerates. Quartiles describe "typical spread" honestly when the mean and $s$ would lie.

## Exercises

**Basic** — For the sorted set 4, 8, 12, 16, 20, 24, 28, 32 ($n=8$), find $Q_1,Q_2,Q_3$ and the IQR by the locator method.

**Intermediate** — A dataset has $Q_1=68$, $Q_3=80$. Compute the IQR, the semi-IQR, and the midquartile. Which value beyond $Q_3$ is the smallest that the $1.5\times\text{IQR}$ rule would call an outlier?

**Advanced** — Add one huge outlier to a 20-point dataset and recompute both $s$ and the IQR. Quantify how much each moves, and use that to argue *why* IQR is called "resistant." What breakdown fraction of contamination can the IQR tolerate before it, too, is distorted?
