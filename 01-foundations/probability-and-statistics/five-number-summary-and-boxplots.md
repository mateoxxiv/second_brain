---
tags:
  - status/seed
  - probability
related:
  - "[[quartiles-and-iqr]]"
  - "[[percentiles]]"
  - "[[measures-of-center]]"
  - "[[skewness]]"
  - "[[histogram]]"
  - "[[characteristics-of-data]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §3-4 (Ejemplos 7–11)."
---

> **TL;DR** — The **5-number summary** (min, $Q_1$, median, $Q_3$, max) compresses a dataset to five landmarks; a **boxplot** draws them, and the *modified* boxplot adds a $1.5\times\text{IQR}$ rule to flag outliers.

---

## Intuition

You can describe an entire distribution's *skeleton* with five numbers: where it starts, where its middle half begins and ends, its center, and where it stops. That's the **5-number summary**, and the **boxplot** is its picture — a box spanning the [[quartiles-and-iqr|middle 50%]] with a line at the median, and whiskers reaching to the extremes. One glance tells you center, spread, and symmetry: a median hugging one side of the box, or a lopsided whisker, signals [[skewness|skew]]. Boxplots carry less detail than a [[histogram]] (they hide multimodality), so for a *single* dataset a histogram wins — but line several boxplots up on **one shared scale** and they become the sharpest tool for *comparing* groups.

## Mechanics

**5-number summary** = minimum, $Q_1$, median ($Q_2$), $Q_3$, maximum. *Worked* (35 movie budgets): **4.5, 35, 68, 113, 225** (\$M).

**Skeletal boxplot** — build a scale covering min→max; draw the box from $Q_1$ to $Q_3$ with a line at the median; extend whiskers to the min and max.

**Modified boxplot** — the version software draws. It separates true outliers from the reach of the whiskers using the interquartile range:

$$\text{outlier if } x > Q_3 + 1.5\,(\text{IQR})\quad\text{or}\quad x < Q_1 - 1.5\,(\text{IQR})$$

Then: mark each outlier with its own symbol (\*), and shorten the whiskers to the most extreme values that are **not** outliers.

*Worked* (female pulse rates): $Q_1=68,\ Q_3=80 \Rightarrow \text{IQR}=12,\ 1.5\times\text{IQR}=18$. Upper fence $=80+18=98$, so 104 and 124 are outliers; lower fence $=68-18=50$, and nothing falls below it.

```python
import numpy as np
q1, med, q3 = np.percentile(data, [25, 50, 75])
lo, hi = q1 - 1.5*(q3-q1), q3 + 1.5*(q3-q1)     # the 1.5·IQR fences
outliers = data[(data < lo) | (data > hi)]
# matplotlib: plt.boxplot(data)  → modified boxplot by default
```

## In ML

**The $1.5\times\text{IQR}$ fence is the workhorse outlier filter.** It's the default in most EDA and in `matplotlib`/`seaborn` boxplots, preferred over the $|z|>3$ rule because its thresholds are built from resistant quartiles, not the outlier-sensitive mean and SD.

**Boxplots read distribution shape fast.** Comparing feature distributions across a class label — several boxplots on a shared axis — surfaces separability, scale differences, and skew at a glance, all inputs to the [[characteristics-of-data|CVDOT]] checklist during exploratory analysis.

## Exercises

**Basic** — Give the 5-number summary for 4.5, 35, 68, 113, 225 already computed above — then sketch the skeletal boxplot on a 0–250 scale.

**Intermediate** — A dataset has $Q_1=35$, $Q_3=113$. Compute the $1.5\times\text{IQR}$ fences. Is a value of 240 an outlier? Is 10?

**Advanced** — Two boxplots on the same scale have identical medians and boxes but very different whisker lengths. What does that tell you about their distributions — and why could their *means* still differ even though the medians match? Tie your answer to [[skewness]].
