---
tags:
  - status/seed
  - probability
related:
  - "[[null-and-alternative-hypotheses]]"
  - "[[z-score]]"
  - "[[student-t-distribution]]"
  - "[[chi-squared-distribution]]"
  - "[[p-value]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Transformación de datos muestrales en un estadístico de prueba; Ejemplo 4)"
---

> **TL;DR** — The test statistic turns the sample result into a standardized score, measured as if H0 were true, so every test reads on the same scale.

---

## Intuition

"13 girls in 14 births" does not tell you how surprising that is. What matters is the distance from the value H0 claims, measured in standard-error units. That is the [[z-score]] idea applied to a sampling distribution: the test statistic says how many standard errors the sample sits from the H0 value.

## Mechanics

The formulas Triola uses in this chapter:

| Parameter | Statistic | Formula | Distribution |
|---|---|---|---|
| proportion $p$ | $z$ | $z = \dfrac{\hat p - p}{\sqrt{pq/n}}$ | normal |
| mean $\mu$ | $z$ or $t$ | $z = \dfrac{\bar x - \mu}{\sigma/\sqrt{n}}$, or $t$ with $n-1$ df | normal or Student $t$ |
| std. dev. $\sigma$ | $\chi^2$ | $\chi^2 = \dfrac{(n-1)s^2}{\sigma^2}$ | chi-squared, $n-1$ df |

The denominator is the standard error **under H0**. Use the hypothesized $p$ (or $\sigma$), not the sample's own $\hat p$ (or $s$), because H0 is assumed true when the test is built.

Worked (XSORT, 13 girls in 14 births, H0: $p = 0.5$):
$$z = \frac{0.929 - 0.5}{\sqrt{(0.5)(0.5)/14}} = 3.21$$

```python
import math

n, x, p0 = 14, 13, 0.5
p_hat = x / n
se0 = math.sqrt(p0 * (1 - p0) / n)   # standard error under H0: use p0, not p_hat
z = (p_hat - p0) / se0
print(round(p_hat, 3), round(z, 2))  # 0.929 3.21
```

Which distribution to use: $z$ for a proportion when $np \ge 5$ and $nq \ge 5$ (see [[normal-approximation-to-binomial]]); $t$ for a mean when $\sigma$ is unknown (see [[student-t-distribution]]); $\chi^2$ for a standard deviation (see [[chi-squared-distribution]]).

## In ML

**Comparing two models on one test set** — the difference in accuracy divided by its standard error is a test statistic. It follows the same "standardize under H0" template.

**Permutation and bootstrap tests** — these build the null distribution by simulation instead of a formula, then compute a statistic the same way. See [[sampling-distribution]].

## Exercises

**Basic** — 60 heads in 100 flips of a coin, H0: $p = 0.5$. Compute $z$.

**Intermediate** — Same H0, but 240 successes in 400 trials. Compute $z$. What changed compared with the basic case, and why?

**Advanced** — Why does the statistic use $p_0$ in the denominator instead of $\hat p$? Derive the variance of $\hat p$ under H0, then say what goes wrong if you use $\hat p$ instead.
