---
tags:
  - status/seed
  - probability
related:
  - "[[measures-of-variation]]"
  - "[[measures-of-center]]"
  - "[[coefficient-of-variation]]"
  - "[[normal-distribution]]"
  - "[[chebyshevs-theorem]]"
  - "[[percentiles]]"
  - "[[feature-scaling]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §3-4 (Ejemplo 1)."
---

> **TL;DR** — A **z-score** restates a value as *its number of standard deviations from the mean*, $z=\dfrac{x-\bar{x}}{s}$ — a unit-free ruler that lets you compare values drawn from completely different distributions.

---

## Intuition

Is a man's height of 76.2 in more extreme than his weight of 237.1 lb? You can't compare inches to pounds directly — apples to oranges. But you *can* ask, for each, "how many [[measures-of-variation|standard deviations]] above its own [[measures-of-center|mean]] is it?" Heights (x̄=68.34, s=3.02) put 76.2 at z=2.60; weights (x̄=172.55, s=26.33) put 237.1 at z=2.45. The height sits *farther* from its mean, so it's the more extreme value. The z-score strips the units and re-centers everything on the mean, collapsing every distribution onto one common scale where numbers are finally comparable.

## Mechanics

$$z = \frac{x-\bar{x}}{s}\ \text{(sample)}\qquad z=\frac{x-\mu}{\sigma}\ \text{(population)}$$

It's an **affine transform**: subtract the mean (re-center to 0), divide by the SD (rescale to unit spread). So a standardized dataset always has **mean 0 and standard deviation 1** — the units cancel, leaving a pure count of SDs.

| $z$ | Position |
|-----|----------|
| $z>0$ | above the mean |
| $z<0$ | below the mean (any $x<\bar{x}$ gives negative $z$) |
| $-2\le z\le 2$ | *common* value |
| $z<-2$ or $z>2$ | *unusual* value |

The **unusual** cutoff comes straight from §3-3's range rule of thumb (most data lies within 2 SD of the mean). **Round z to two decimals** — that's the precision of the standard-normal table (A-2) it feeds in later chapters.

*Worked:* a height of 61.3 in → $z=\frac{61.3-68.34}{3.02}=-2.33$: below the mean *and* unusual.

```python
import numpy as np
def zscore(x, data):
    d = np.asarray(data, float)
    return (x - d.mean()) / d.std(ddof=1)   # ddof=1 → sample s
```

## In ML

**It *is* `StandardScaler`.** Standardization in [[feature-scaling]] applies exactly this transform column-by-column, so no large-unit feature dominates a distance- or gradient-based model. The z-score is the statistics-side name for the same operation.

**It's the gateway to the normal distribution.** Converting $x\to z$ maps any [[normal-distribution|normal]] variable onto the *standard* normal $N(0,1)$, which is why one z-table serves every normal problem — the backbone of Ch. 6 onward.

**Outlier flags.** A common automated rule marks points with $|z|>3$ as outliers — cheap, but fragile: the mean and s it relies on are themselves distorted by the very outliers you're hunting (why [[quartiles-and-iqr|IQR]]-based rules are often preferred).

## Exercises

**Basic** — A test has mean 500, SD 100. Convert scores 620 and 450 to z-scores. Which, if either, is unusual?

**Intermediate** — Two exams: yours is $x=80$ in a class with $\bar{x}=70,s=5$; a friend scores 85 in a class with $\bar{x}=82,s=2$. Who did relatively better, and why does the raw score mislead here?

**Advanced** — Prove that standardizing a dataset always yields mean 0 and SD 1. (Use linearity of the mean and the fact that $\text{SD}(aX+b)=|a|\,\text{SD}(X)$.) Then explain why $|z|>2$ can *never* flag more than 25% of *any* dataset — connect to [[chebyshevs-theorem]].
