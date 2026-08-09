---
tags:
  - status/seed
  - probability
related:
  - "[[data-types-and-levels-of-measurement]]"
  - "[[measures-of-center]]"
  - "[[measures-of-variation]]"
  - "[[normal-distribution]]"
  - "[[principles-of-statistical-thinking]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2 (Repaso y preámbulo)."
---

> **TL;DR** — Any dataset is described by five characteristics — **Center, Variation, Distribution, Outliers, Time (CVDOT)** — and the goal of descriptive statistics is not to make a table or chart, but to *understand* what those five reveal.

---

## Intuition

Before you model or test anything, you have to *know your data* — and "knowing" it means answering five standard questions, no matter the dataset. Triola's whole point in opening Chapter 2: don't get lost producing pretty tables; a table or graph is only a *tool* to see these five things. If you can state a dataset's center, spread, shape, outliers, and time behavior, you understand it; if you can't, you don't — regardless of how many charts you made.

The five are worth memorizing (rare advice from Triola, who dislikes memorization) via the mnemonic **CVDOT** — *"Computer Viruses Destroy Or Terminate."* The Spanish edition uses **CVDVT**, *"Cuidado con los Virus que Destruyen el Valioso Trabajo."*

## Mechanics

**The five characteristics of data:**

| # | Characteristic | Question it answers | Typical tool |
|---|----------------|---------------------|--------------|
| **C** | **Center** | Where is the "middle" / representative value? | [[measures-of-center]] (mean, median, mode) |
| **V** | **Variation** | How spread out are the values? | [[measures-of-variation]] (range, variance, SD) |
| **D** | **Distribution** | What *shape* does the data take? | histogram; bell / uniform / skewed |
| **O** | **Outliers** | Are there values far from the rest? | boxplot, z-scores |
| **T** | **Time** | Do the characteristics *change over time*? | time-series plot |

**Why these five and not others:** together they capture *location* (C), *scale* (V), *form* (D), *anomalies* (O), and *stability* (T) — the minimal set that fully summarizes a one-variable dataset. Each is a separate axis: two datasets can share a center but differ wildly in variation or shape (a key reason a single number like the mean can mislead).

**The choice of representation depends on the [[data-types-and-levels-of-measurement|data type]]** — categorical data gets bar charts and frequencies; quantitative data gets histograms and the numeric summaries above. The characteristic you *want* to see dictates the chart you *make*.

```python
import numpy as np
from scipy import stats
x = np.array([2, 4, 4, 4, 5, 5, 7, 9, 42])   # note the 42
print("Center   :", np.mean(x), np.median(x))          # C: mean pulled up by 42
print("Variation:", np.std(x, ddof=1))                 # V: sample SD
print("Skew     :", stats.skew(x))                     # D: shape (right-skewed)
print("Outlier? :", x[np.abs(stats.zscore(x)) > 2])    # O: 42 flagged
# T (time) needs an ordered/timestamped series, not shown here
```

## In ML

**CVDOT is the checklist for exploratory data analysis (EDA)** — before training, every feature is profiled exactly this way: `df.describe()` gives center + variation, histograms give distribution, boxplots/z-scores flag outliers, and line plots reveal time drift. Skipping this is how silent data problems reach the model.

**Distribution shape drives preprocessing and model choice** — skew and heavy tails prompt log-transforms or scaling; the [[normal-distribution|bell shape]] is an assumption behind many classical methods. Reading D early prevents mis-applied models.

**Outliers and time-drift are production failure modes** — undetected outliers distort loss and gradients, and *time* changes (distribution shift) silently degrade deployed models. Monitoring the same five characteristics of incoming data is core to ML monitoring.

## Exercises

**Basic** — For the dataset {3, 5, 5, 6, 7, 8, 90}, informally describe each of the five characteristics (which one is most striking here?).

**Intermediate** — Give two datasets with the *same mean* but clearly different *variation* and *distribution shape*. What does this prove about relying on the center alone?

**Advanced** — Explain why "Time" is separated out as its own characteristic rather than folded into Distribution. What can a time plot reveal that a static histogram of the same values cannot?
