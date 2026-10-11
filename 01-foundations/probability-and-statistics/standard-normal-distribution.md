---
tags:
  - status/seed
  - probability
related:
  - "[[normal-distribution]]"
  - "[[z-score]]"
  - "[[probability-density-function]]"
  - "[[complementary-events]]"
  - "[[cdf-and-quantiles]]"
  - "[[critical-values-and-z-alpha]]"
  - "[[normal-probabilities-via-standardization]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-1 (Fórmula 6-1) and §6-2 (Distribución normal estándar, Ejemplos 3–5, Tabla A-2)"
---

> **TL;DR** — The standard normal is the [[normal-distribution|normal]] with $\mu=0,\ \sigma=1$. Its left-cumulative area $\Phi(z)$ is tabulated once (Table A-2), and **left, right, and between** areas all come from that one function.

---

## Intuition

Every normal curve is fixed by just two numbers, the mean $\mu$ and the standard deviation $\sigma$ (Triola, Formula 6-1). That means there are infinitely many bell curves. Instead of tabulating all of them, statisticians tabulate *one*: $N(0,1)$. Any other normal is converted to it with a [[z-score]].

The horizontal axis is **z-scores** (distances, measured in SDs). The body of the table holds **areas** (probabilities). Triola's main warning: **don't mix up z-scores and areas.**

## Mechanics

$$\phi(z)=\frac{1}{\sqrt{2\pi}}e^{-z^2/2}, \qquad \Phi(z)=P(Z<z)=\int_{-\infty}^{z}\phi(t)\,dt$$

$\Phi$ has no closed form, which is why tables and software exist. Table A-2 gives **cumulative area from the left** only, so every question is reduced to left areas:

| Wanted | Formula | Triola example (thermometers, °C) |
|---|---|---|
| Left of $a$ | $\Phi(a)$ | $P(z<1.27)=0.8980$ |
| Right of $a$ | $1-\Phi(a)$ ([[complementary-events\|complement]]) | $P(z>-1.23)=1-0.1093=0.8907$ |
| Between $a,b$ | $\Phi(b)-\Phi(a)$ | $P(-2<z<1.5)=0.9332-0.0228=0.9104$ |

**Symmetry shortcut:** $\Phi(-z) = 1-\Phi(z)$, since the curve is symmetric about 0.

**Table reading:** the row gives the units and tenths (1.2), and the column gives the hundredths (.07), so $z=1.27$. Above $z=3.49$ use 0.9999, and below $-3.49$ use 0.0001. Because it is continuous, $P(z=a)=0$ and ≤ vs. < do not matter ([[probability-density-function]]).

```python
from scipy.stats import norm
print(norm.cdf(1.27))                  # 0.8980  left
print(1 - norm.cdf(-1.23))             # 0.8907  right  (= norm.sf(-1.23))
print(norm.cdf(1.5) - norm.cdf(-2.0))  # 0.9104  between
```

**Tip (Triola):** don't memorize rules. Sketch the bell, shade the region, then write it as a combination of left areas.

## In ML

**Standardization everywhere.** `StandardScaler`, BatchNorm, and LayerNorm push features and activations toward mean 0 and variance 1, the same scale as the standard normal. That makes $|z|$ directly interpretable, and $\Phi(z)$ gives a percentile for anomaly scores.

**$\Phi$ inside networks.** The GELU activation (used in BERT and GPT) is literally $\text{GELU}(x)=x\,\Phi(x)$. Each input is weighted by the probability that a standard normal falls below it.

## Exercises

**Basic** — Using only Table A-2 logic, find $P(z>2.00)$ and $P(-1<z<1)$. Compare the second one with the 68% of the Empirical Rule.

**Intermediate** — Prove $\Phi(-z)=1-\Phi(z)$ from the symmetry $\phi(-t)=\phi(t)$ with a substitution in the integral. Then use it to get $P(z<-1.27)$ from Example 3.

**Advanced** — Why can't $\Phi$ be written with elementary functions? How does `scipy` compute it anyway (hint: the error function, $\Phi(z)=\tfrac12[1+\text{erf}(z/\sqrt2)]$)?
