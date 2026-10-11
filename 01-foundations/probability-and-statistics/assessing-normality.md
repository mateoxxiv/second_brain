---
tags:
  - status/seed
  - probability
related:
  - "[[normal-distribution]]"
  - "[[standard-normal-distribution]]"
  - "[[histogram]]"
  - "[[five-number-summary-and-boxplots]]"
  - "[[skewness]]"
  - "[[cdf-and-quantiles]]"
  - "[[sampling-distribution]]"
  - "[[normal-quantile-plot]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-7 (Evaluación de la normalidad; gráfica cuantilar normal; Ejemplos 1–4)"
---

> **TL;DR** — Before using a method that assumes normal data, check three things: the histogram looks like a bell, there is at most one outlier, and the normal quantile plot is close to a straight line.

---

## Intuition

Many methods (confidence intervals, z-tests, z-scores) assume the data came from a normal population. Checking that assumption is a judgment call, not a calculation with a single cutoff. You look for evidence against normality, and you reject it only when the evidence is clear. Three views of the same data help: the shape (histogram), the extremes (outliers), and a direct test of straightness (quantile plot).

## Mechanics

**Decision procedure** (Triola):

| Step | Check | Reject normality if… |
|------|-------|----------------------|
| 1 | Histogram | it differs a lot from a bell shape |
| 2 | Outliers | there is more than one outlier (one can be an error or chance, but check it) |
| 3 | Normal quantile plot | the points are not close to a straight line, or show a systematic pattern |

Step 3 is only used when the histogram is roughly symmetric and has at most one outlier. For small samples, be flexible; for large samples, be stricter.

**Normal quantile plot:** points $(x, z)$, where $x$ is the $i$-th smallest sample value and $z$ is the z-score expected for that position in a normal sample. For sample size $n$, the cumulative area to the left of the $i$-th value is taken as $\frac{2i-1}{2n}$, and $z = \Phi^{-1}\!\left(\frac{2i-1}{2n}\right)$.

For $n = 5$, the areas are 0.1, 0.3, 0.5, 0.7, 0.9, giving $z = -1.28, -0.52, 0, 0.52, 1.28$.

```python
import numpy as np
from scipy.stats import norm
x = np.sort([110, 96, 170, 125, 119])
p = (np.arange(1, len(x) + 1) - 0.5) / len(x)   # same as (2i-1)/2n
z = norm.ppf(p)                                  # [-1.28, -0.52, 0, 0.52, 1.28]
print(list(zip(x, z.round(2))))
```

**Reading the plot:** a straight line means the sample is compatible with a normal population. A systematic curve, or points far from the line, means it is not. One stretched point at an end (an outlier) bends the whole pattern, which is why step 2 comes first.

## In ML

**Gaussian assumptions in models.** Linear regression with a squared-error loss assumes normal residuals. A Q–Q plot of the residuals is the standard diagnostic; a curve at the ends signals heavy tails or outliers that the MSE loss may overweight.

**Preprocessing decisions.** Z-scores and Gaussian-based intervals are reliable only if the feature is roughly normal. A skewed histogram or a curved quantile plot is the signal to transform the feature (log, square root, Box–Cox) before standardizing.

## Exercises

**Basic** — For the sample 4, 7, 9, 12 ($n = 4$), find the areas $\frac{2i-1}{2n}$ and the expected z-scores for a normal quantile plot.

**Intermediate** — Replace 170 with 1700 in the film-duration example and explain, using the plot logic, why the pattern breaks even though only one value changed.

**Advanced** — Why does the procedure use $\frac{2i-1}{2n}$ instead of $\frac{i}{n}$? What goes wrong at the extremes if you use $\frac{i}{n}$, where the largest area would be 1 and its z-score infinite?
