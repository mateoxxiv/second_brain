---
tags:
  - status/seed
  - probability
related:
  - "[[measures-of-variation]]"
  - "[[measures-of-center]]"
  - "[[parameter-vs-statistic]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 3, §3-3."
---

> **TL;DR** — The coefficient of variation, $CV = \frac{s}{\bar{x}}\times 100\%$, expresses the [[measures-of-variation|standard deviation]] as a *percentage of the mean*, making it **unitless** so you can fairly compare the spread of datasets with different units or very different means.

---

## Intuition

You can't directly compare a standard deviation of 3 *inches* with one of 26 *pounds* — different units, no common ground. Even within the same units, a spread of 5 means something very different around a mean of 10 than around a mean of 1,000. The [[measures-of-variation|standard deviation]] alone is **absolute** variation; the CV is **relative** variation — spread *scaled by* the mean. Dividing by the mean cancels the units, so 4.4% vs. 15.3% is a fair comparison no matter what's being measured.

## Mechanics

| | Formula |
|---|---------|
| **Sample** | $CV = \dfrac{s}{\bar{x}} \times 100\%$ |
| **Population** | $CV = \dfrac{\sigma}{\mu} \times 100\%$ |

The units of $s$ and $\bar{x}$ cancel → a pure percentage. Defined for data **without negative values** (a mean near 0 makes it blow up or lose meaning).

**Worked (Triola, men's heights vs. weights):**
- Heights: $\bar{x}=68.34$ in, $s=3.02$ in → $CV = 3.02/68.34 = \mathbf{4.42\%}$
- Weights: $\bar{x}=172.55$ lb, $s=26.33$ lb → $CV = 26.33/172.55 = \mathbf{15.26\%}$

You *cannot* compare 3.02 in against 26.33 lb — but you *can* compare 4.42% against 15.26%: **weights vary much more than heights**, relative to their means. (Makes sense — an adult rarely weighs twice another, but a man being twice another's height never happens.)

```python
import numpy as np
def cv(data):
    data = np.asarray(data, float)
    return data.std(ddof=1) / data.mean() * 100   # sample CV in %
```

> **When to use which:** compare raw standard deviations *only* when datasets share the same units/scale **and** similar means. Otherwise — different units, or very different means — switch to the CV.

## In ML

**Feature screening.** CV per feature flags near-constant columns (tiny CV → little signal) and lets you rank dispersion across features measured on different scales *before* standardizing — a quick unitless triage in EDA.

**Signal-to-noise & stability.** The CV is the inverse of a signal-to-noise ratio ($\bar{x}/s$); it's used to judge measurement reproducibility, A/B-metric stability, and whether a feature's variation is meaningful or just noise around a large mean.

## Exercises

**Basic** — A sample has $\bar{x}=50$, $s=10$. Compute the CV. If another sample has $\bar{x}=500$, $s=50$, which is *relatively* more variable?

**Intermediate** — Daily temperatures in °C give one CV; convert the same data to °F (mean and SD both scale, but the zero shifts). Does the CV stay the same? Explain why the shifting zero makes CV problematic for interval-scale data.

**Advanced** — Why is the CV undefined/misleading when the mean is near zero or the data contains negative values? Give a concrete dataset where a small mean produces an absurdly large CV despite modest absolute spread.
