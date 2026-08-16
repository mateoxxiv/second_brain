---
tags:
  - status/seed
  - probability
related:
  - "[[measures-of-center]]"
  - "[[characteristics-of-data]]"
  - "[[histogram]]"
  - "[[normal-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 3, §3-2 (Sesgo)."
---

> **TL;DR** — Skewness measures how *lopsided* a distribution is: comparing the [[measures-of-center|mean, median, and mode]] tells you which way the longer tail points, because the outlier-sensitive mean gets dragged into the tail while the resistant median barely moves.

---

## Intuition

A distribution is **symmetric** if the left half of its [[histogram]] is a mirror image of the right. It's **skewed** if one tail is stretched longer than the other. The trick Triola gives: the [[measures-of-center|mean]] is *not resistant*, so a long tail full of extreme values physically pulls it toward that tail — while the median stays put near the bulk of the data. So the *gap and ordering* between mean, median, and mode is a fingerprint of shape. Think of the mean as a boat dragged by an anchor in the long tail.

## Mechanics

Two directions (the sign convention follows the tail, not the peak):

| Shape | Tail | Typical center order | Also called |
|-------|------|----------------------|-------------|
| **Left-skewed** | longer **left** tail | mean ≤ median ≤ mode (roughly) | negative skew |
| **Symmetric** | balanced | mean = median = mode | zero skew |
| **Right-skewed** | longer **right** tail | mode ≤ median ≤ mean (roughly) | positive skew |

**Right skew is more common** because many variables have a hard floor but no ceiling — income can't drop below 0, but a few people earn millions, stretching the right tail.

> ⚠️ **The ordering is a heuristic, not a law.** Triola's own counterexample: −100, 1.0, 1.5, 1.7, 1.8, 2.0, 3.0, 4.0, 5.0, 50.0, 50.0, 60.0 looks **left-skewed** on a histogram, yet mean = 6.7 **>** median = 2.5 — the opposite of the "left-skew ⇒ mean < median" rule. **Mean vs. median alone cannot reliably identify shape; look at the histogram.**

```python
import numpy as np
from scipy.stats import skew
x = np.array([-100,1,1.5,1.7,1.8,2,3,4,5,50,50,60])
x.mean()      # 6.7  — greater than the median...
np.median(x)  # 2.5  ...even though the data is left-skewed
skew(x)       # < 0  → the (moment-based) skewness confirms LEFT skew
```

## In ML

**Skew flags the need to transform features.** Right-skewed features (income, counts, prices) violate the near-normality many models and tests assume; a **log** or **Box–Cox** transform pulls the tail in and often improves linear models, distance metrics, and gradient behavior.

**Mean-vs-median gap = a cheap skew detector in EDA.** `df.describe()` next to `df.median()` instantly signals skew per column — a large gap says "outliers / long tail here," guiding imputation (median over mean) and outlier handling.

**Target skew biases regression.** A skewed target inflates MSE's sensitivity to the tail; log-transforming the target (predicting `log(y)`) is a standard fix, which is exactly the mean-is-not-resistant story in loss-function form.

## Exercises

**Basic** — A dataset has mode 40, median 55, mean 70. Sketch the likely shape and name the skew direction. Which tail is longer?

**Intermediate** — House prices are almost always right-skewed. Explain *why* using the "floor but no ceiling" argument, and state what happens to the mean relative to the median.

**Advanced** — Construct (or use Triola's) a dataset that is visually left-skewed yet has mean > median. Explain why this doesn't contradict the definition of skewness, and what it says about using [[measures-of-center|center measures]] to infer shape.
