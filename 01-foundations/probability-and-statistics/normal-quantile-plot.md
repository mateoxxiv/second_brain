---
tags:
  - status/seed
  - probability
related:
  - "[[assessing-normality]]"
  - "[[standard-normal-distribution]]"
  - "[[cdf-and-quantiles]]"
  - "[[normal-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-6 (Gráfica cuantilar normal; procedimiento de 5 pasos; Ejemplo 2, duración de películas)"
---

> **TL;DR** — A normal quantile plot pairs each sorted data value with the z-score it would have in a perfect normal sample; a straight line means the data look normal.

---

## Intuition

Sort your data. The smallest value sits at the bottom 1/n of the sample, the next at the 2nd 1/n, and so on. Ask: if this sample were truly normal, what z-score would each of those positions have? Then plot the real values against those expected z-scores. If the data are normal, the real values and the expected z-scores move in step, so the points fall on a line. If the points bend or drift, the shape of the data differs from a normal.

## Mechanics

**Five-step construction** (Triola):

| Step | Action |
|------|--------|
| 1 | Sort the data from smallest to largest. |
| 2 | Find the cumulative areas $\frac{1}{2n}, \frac{3}{2n}, \frac{5}{2n}, \dots$ (one per sorted value). |
| 3 | Convert each area to a z-score with the standard normal table, calculator, or software. |
| 4 | Plot the points $(x, z)$: $x$ is the sorted data value, $z$ its expected z-score. |
| 5 | Judge straightness: a line means normal; a systematic curve or stray points mean not. |

Why $\frac{2i-1}{2n}$ and not $\frac{i}{n}$: each value is the middle of its $1/n$ slice, so the largest area is $\frac{2n-1}{2n} < 1$ and its z-score stays finite.

**Worked example** (film durations, $n = 5$): 110, 96, 170, 125, 119.

1. Sort: 96, 110, 119, 125, 170.
2. Areas: $\frac{1}{10}, \frac{3}{10}, \frac{5}{10}, \frac{7}{10}, \frac{9}{10}$ = 0.1, 0.3, 0.5, 0.7, 0.9.
3. Z-scores: $-1.28,\ -0.52,\ 0,\ 0.52,\ 1.28$.
4. Points: $(96, -1.28),\ (110, -0.52),\ (119, 0),\ (125, 0.52),\ (170, 1.28)$.
5. The points lie close to a line with no systematic pattern, so these five durations are consistent with a normal population. With only five values, this is weak evidence.

```python
import numpy as np
from scipy.stats import norm
x = np.sort([110, 96, 170, 125, 119])
p = (np.arange(1, len(x) + 1) - 0.5) / len(x)   # (2i-1)/2n
z = norm.ppf(p)                                  # [-1.28, -0.52, 0, 0.52, 1.28]
```

## In ML

**Residual diagnostics.** A Q–Q plot of regression residuals is the standard check of the normal-error assumption behind squared-error loss. Curved ends signal heavy tails that MSE may overweight.

**Reading the slope.** If $x = \mu + \sigma z$ holds, the line has intercept $\mu$ and slope $\sigma$. The plot therefore also gives rough estimates of the mean and spread.

## Exercises

**Basic** — For the sample 10, 14, 30 ($n = 3$), find the areas $\frac{2i-1}{2n}$ and the expected z-scores. Check that $z \approx -0.97,\ 0,\ 0.97$.

**Intermediate** — The sample 1, 2, 3, 4, 20 is strongly right-skewed. Compute its five points. Which end of the plot bends away from the line, and why?

**Advanced** — Using $x = \mu + \sigma z$, explain why the fitted line's slope estimates $\sigma$. What happens to the plot if the data are normal but you plot $z$ against $x$ instead of $x$ against $z$?
