---
tags:
  - status/seed
  - probability
related:
  - "[[measures-of-center]]"
  - "[[characteristics-of-data]]"
  - "[[normal-distribution]]"
  - "[[parameter-vs-statistic]]"
  - "[[skewness]]"
  - "[[coefficient-of-variation]]"
  - "[[chebyshevs-theorem]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 3, §3-3."
---

> **TL;DR** — Variation measures how *spread out* data is; the **standard deviation** — the (nearly) average distance of values from the [[measures-of-center|mean]], in the data's own units — is the dominant measure, and its whole point is *interpreting* spread, not just computing it.

---

## Intuition

Two IQ samples can share the *same mean of 100* yet look completely different: one tightly clustered, one widely scattered. [[measures-of-center|Center]] alone can't tell them apart — you need a number for **spread**. That number answers "how far, typically, is a value from the mean?" Small spread = values huddle near the mean; large spread = they sprawl. This is the second half of describing a distribution (the "V" in [[characteristics-of-data|CVDOT]]).

## Mechanics

### Range — the crude first measure
$$\text{range} = (\text{max}) - (\text{min})$$
Uses only the two extremes, so it's **very sensitive to outliers** and ignores everything in between. Cheap and intuitive (used in process-control charts), but weak.

### Building the standard deviation from scratch
Start from each value's **deviation from the mean**, $x - \bar{x}$. For 1, 3, 14 ($\bar{x}=6$): deviations are −5, −3, 8.

- **Why not just average the deviations?** They always sum to **zero** (positives cancel negatives) — useless. We must kill the signs first.
- **Option A — absolute values** → the *mean absolute deviation* (MAD): $\text{MAD}=\dfrac{\sum |x-\bar{x}|}{n}$. For 1,3,14: $(5+3+8)/3 = 5.3$.
- **Why NOT the MAD?** Absolute value is **not an algebraic operation** (algebraic = +, ×, powers, roots — not $|\cdot|$). This breaks later inferential math: variances have an **additivity property** (the variance of a sum of independent variables = sum of their variances) that MAD lacks, and the sample MAD is a **biased** estimator. So instead we **square** the deviations (also removes signs, stays algebraic, mimics a distance formula → sum of squares).

### The two sample formulas (algebraically identical)

| | Formula | Use |
|---|---------|-----|
| **3-4** (definitional) | $s=\sqrt{\dfrac{\sum (x-\bar{x})^2}{n-1}}$ | shows *what it means* — RMS distance from the mean |
| **3-5** (shortcut) | $s=\sqrt{\dfrac{n\sum x^2 - (\sum x)^2}{n(n-1)}}$ | faster by hand / used in calculators & software |

Worked (1, 3, 14): squared deviations 25, 9, 64 → sum 98 → ÷(n−1)=2 → 49 → √49 = **7.0**. Formula 3-5 gives the same 7.0. Units stay in the **original units** (7.0 *satellites*).

### Population vs. sample — notation & the n−1 twist
$$s = \sqrt{\frac{\sum(x-\bar{x})^2}{n-1}} \quad\text{(sample)} \qquad \sigma = \sqrt{\frac{\sum(x-\mu)^2}{N}} \quad\text{(population)}$$

| Quantity | Sample [[parameter-vs-statistic\|statistic]] | Population parameter |
|----------|--------|-----------|
| Std. deviation | $s$ | $\sigma$ |
| Variance | $s^2$ | $\sigma^2$ |
| Divisor | $n-1$ | $N$ |

**Why divide by n−1 (not n)?** Only $n-1$ deviations are *free*: once the mean is fixed, the last value is determined (**degrees of freedom**). Dividing by $n-1$ makes $s^2$ an **unbiased estimator** of $\sigma^2$; dividing by $n$ systematically *underestimates* it.

### Variance = (standard deviation)²
$s^2$ and $\sigma^2$. It's the key quantity for inference (ANOVA, the additivity property), but its **units are squared** ("square minutes"?) — meaningless to interpret directly, which is exactly why we report the standard deviation instead.

```python
import numpy as np
x = np.array([1, 3, 14])
x.std(ddof=1)   # 7.0   sample s   (ddof=1 → divide by n-1)
x.std(ddof=0)   # 5.72  population σ (divide by N)
x.var(ddof=1)   # 49.0  sample variance s²
```

## Interpreting s — three tools

**1. Range rule of thumb.** Fast two-way estimate:
- *Estimate s from the range:* $s \approx \dfrac{\text{range}}{4}$ (crude! FICO example: range/4 = 101.5 vs. true s = 92.2).
- *Flag unusual values:* "common" range ≈ $\bar{x} \pm 2s$; anything outside is unusual. (IQ 100±2·15 → 70 to 130, so 135 is unusual.)

**2. Empirical Rule (68–95–99.7)** — *only for approximately [[normal-distribution|normal]] data*:
- ≈ **68%** within $\bar{x} \pm 1s$
- ≈ **95%** within $\bar{x} \pm 2s$
- ≈ **99.7%** within $\bar{x} \pm 3s$

**3. [[chebyshevs-theorem|Chebyshev's theorem]]** — for *any* distribution, at least $1-\frac{1}{K^2}$ of values lie within $K$ std. deviations (≥75% within 2, ≥89% within 3). Weaker but universal. *(Own note.)*

> Comparing two datasets' std. deviations is only fair when they share the same units/scale **and** similar means. Otherwise use the [[coefficient-of-variation]] (s/x̄, unitless).

## In ML

**σ is the scale in standardization.** The z-score $z=\frac{x-\mu}{\sigma}$ — the heart of `StandardScaler` and [[normal-distribution|normalization]] — divides by the standard deviation, putting every feature on a common "how many σ from the mean" ruler so distance- and gradient-based models aren't dominated by large-unit features.

**Variance IS the signal that many models chase.** PCA keeps the directions of *maximum variance*; feature selection often drops near-zero-variance columns; the bias–variance decomposition splits error using this exact quantity. The additivity of variances underlies why independent noise sources add in quadrature.

**s² and the loss are the same object.** Minimizing mean squared error is minimizing the (population-style) variance of the residuals *when their mean is zero* — which OLS with an intercept guarantees — the sum-of-squares that defines $s$ is the sum-of-squares least-squares regression drives down.

## Exercises

**Basic** — For 5, 8, 11 compute the range, then $s$ by Formula 3-4 (find the mean, deviations, square, ÷(n−1), √). Confirm with Formula 3-5.

**Intermediate** — A normal dataset has $\bar{x}=500$, $s=100$. Using the Empirical Rule, what % of values fall in [300, 700]? Then use Chebyshev for the *same* interval — why is the answer smaller, and which one is right here?

**Advanced** — Explain, with the "sum of deviations = 0" fact, why we can't just average raw deviations. Then argue why squaring (→ variance) is preferred over absolute value (→ MAD), citing the additivity property and the n−1 unbiasedness result.
