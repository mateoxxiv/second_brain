---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval-for-mean]]"
  - "[[standard-normal-distribution]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[margin-of-error]]"
  - "[[estimating-sigma-for-sample-size]]"
  - "[[normal-distribution]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística, 11ª ed. §7-4 (Pearson, 2013)"
---

> **TL;DR** — When you replace an unknown population standard deviation with the sample's s, the standardized mean follows a Student t distribution with n − 1 degrees of freedom, which has heavier tails than the normal and so needs wider critical values.

---

## Intuition

Dividing by the true σ gives a clean yardstick. Dividing by s is a noisier yardstick, because s itself wobbles from sample to sample, and small samples wobble the most. A t distribution is the normal curve with extra uncertainty built in: its tails are fatter, so values far from the center are more likely. As the sample grows, s becomes a reliable stand-in for σ and the t curve converges to the normal.

The question it answers is "how far can the sample mean be from μ, measured in standard errors, when I only have s?" It matters because using z there would make intervals too narrow and overstate your confidence.

## Mechanics

Start with the known-σ case. If the population is normal, Z = (x̄ − μ)/(σ/√n) is exactly standard normal. Replace σ with s:

$$T = \frac{\bar{x} - \mu}{s/\sqrt{n}}$$

Two facts make T a t distribution, with ν = n − 1 degrees of freedom. For a normal population, the sample mean and variance are independent, and V = (n−1)s²/σ² follows a chi-square distribution with n − 1 degrees of freedom. Then

$$T = \frac{Z}{\sqrt{V/\nu}} \sim t_{\nu}$$

The density is

$$f(t) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\left(\frac{\nu}{2}\right)}\left(1+\frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}$$

| Property | Statement | Why it matters |
|----------|-----------|----------------|
| Degrees of freedom | ν = n − 1 | Sets how fat the tails are |
| Center | Mean 0 (for ν > 1) | Symmetric, like the normal |
| Spread | Variance ν/(ν − 2) for ν > 2; undefined for ν ≤ 2 | The SD exceeds 1 only when ν > 2 |
| Large n | t → z as ν → ∞ | Normal is the limit, not a different rule |
| Critical values | t₀.₀₂₅ > z₀.₀₂₅ for every finite ν | Intervals widen to keep the same confidence |

Check against the table: for 95% confidence, t₀.₀₂₅ = 2.447 with ν = 6, 2.009 with ν = 50, and z₀.₀₂₅ = 1.960.

```python
from scipy import stats

t_crit = stats.t.ppf(0.975, df=6)   # 2.447: two-tailed 95%, n = 7
z_crit = stats.norm.ppf(0.975)      # 1.960: the known-sigma value
```

## In ML

**Estimating an unknown noise scale** — Any time a model's uncertainty is estimated from finite data, the same effect appears: estimated scale adds spread. The t curve is the exact correction for a normal population with σ estimated from n points.

**Confidence intervals as a sanity check** — The interval x̄ ± t·s/√n is the mean-estimate version used when comparing model metrics across a few runs. With 3 runs (ν = 2), the t critical value is 4.303, so a 95% interval is more than twice as wide as the naive z-based one.

**Robustness limits** — The t interval assumes a roughly normal population. Heavy skew or outliers make the nominal coverage wrong for small n, which is why the vault's [[confidence-interval-for-mean]] note requires either normality or n > 30.

## Exercises

**Basic** — A random sample of n = 7 has a normal population. Find t₀.₀₂₅ and t₀.₀₅ (two-tailed 90%) for ν = 6, using the table or scipy. Confirm both are larger than the z values 1.960 and 1.645.

**Intermediate** — Two samples have the same s = 10. One has n = 15 and the other n = 150. Compare their 95% critical values and the widths of their intervals. How much of the width difference comes from s and how much from the critical value?

**Advanced** — The book states the t SD is "greater than 1." For which n is that true, and what happens to the variance when n = 3? Why does this make the t interval still usable for n = 3 even though the variance is undefined?

## Gaps: notes still to create

- [[t-interval-for-mean]] — the procedure x̄ ± t·s/√n, the z-versus-t decision flowchart (Triola Figure 7-6 and Table 7-1), and worked examples.
