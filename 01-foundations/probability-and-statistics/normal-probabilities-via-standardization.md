---
tags:
  - status/seed
  - probability
related:
  - "[[z-score]]"
  - "[[standard-normal-distribution]]"
  - "[[normal-distribution]]"
  - "[[probability-density-function]]"
  - "[[finding-values-from-normal-areas]]"
  - "[[cdf-and-quantiles]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-3 (Fórmula 6-2, Figura 6-11, Ejemplos 1–2)"
---

> **TL;DR** — To get a probability from **any** normal $N(\mu,\sigma)$, convert the boundary $x$ to $z=\frac{x-\mu}{\sigma}$ (Formula 6-2). The area left of $x$ **equals** the area left of $z$ under $N(0,1)$, so one table ($\Phi$) answers every normal question.

---

## Intuition

Heights in inches, birth weights in grams: every normal curve has its own center and width. Standardizing is like changing a map's units and origin. The terrain doesn't change, only the labels on the ruler. After you shift by $\mu$ and rescale by $\sigma$, every bell curve becomes the same curve, the [[standard-normal-distribution]], and its areas are already tabulated. The shaded region keeps its **shape and its area**. Only the axis labels change (Figure 6-11).

## Mechanics

**Why the area is preserved (derivation).** Start from the normal density and substitute $u=\frac{t-\mu}{\sigma}$, so $dt=\sigma\,du$:

$$P(X<x)=\int_{-\infty}^{x}\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac12\left(\frac{t-\mu}{\sigma}\right)^2}dt=\int_{-\infty}^{\frac{x-\mu}{\sigma}}\frac{1}{\sqrt{2\pi}}e^{-u^2/2}\,du=\Phi\!\left(\tfrac{x-\mu}{\sigma}\right)$$

The $\sigma$ from $dt$ cancels the $\frac1\sigma$ in the density. That cancellation is the whole reason one table is enough.

**Procedure (x → probability):**
1. Sketch the bell, mark $\mu$ and the $x$ value(s), and shade the region you want.
2. Convert each boundary $x$ to $z=\frac{x-\mu}{\sigma}$, **rounded to 2 decimals** (the precision of Table A-2).
3. Read $\Phi(z)$ from Table A-2 (or use technology), then combine left / right / between areas as in [[standard-normal-distribution]].

| Triola example | Standardize | Area |
|---|---|---|
| Men's heights $N(69.0,\,2.8)$, door of 80 in | $z=\frac{80-69.0}{2.8}=3.93$ | $\Phi(3.93)\approx0.9999$ (tech: 0.999957) |
| Birth weights $N(3420,\,495)$, between 2450 and 4390 g | $z=\frac{2450-3420}{495}=-1.96,\ \ z=\frac{4390-3420}{495}=1.96$ | $0.9750-0.0250=0.9500$ |

So 99.99% of men fit through a standard 80 in door, and 95% of babies need no special treatment. The birth-weight limits sit at exactly $\mu\pm1.96\sigma$, which is why the answer is the familiar 95%.

```python
from scipy.stats import norm
print(norm.cdf(80, loc=69.0, scale=2.8))   # 0.999957  no manual z needed
z = (80 - 69.0) / 2.8                       # 3.93 (rounded)
print(norm.cdf(z))                          # same area on N(0,1)
print(norm.cdf(4390, 3420, 495) - norm.cdf(2450, 3420, 495))  # ≈ 0.9500
```

## In ML

**Feature standardization is this exact move.** `StandardScaler` applies $z=\frac{x-\mu}{\sigma}$ per feature. Under a Gaussian assumption, $\Phi(z)$ then turns a raw reading into a percentile, and that is how a z-score anomaly detector converts "3.93 SDs above the mean" into "rarer than 1 in 20,000".

**The reparameterization trick.** VAEs sample $x=\mu+\sigma\,\varepsilon$ with $\varepsilon\sim N(0,1)$. This is Formula 6-2 run backwards, and the change of variables above is why the samples have the right distribution while gradients flow through $\mu$ and $\sigma$.

## Exercises

**Basic** — Men's heights $N(69.0,\,2.8)$: what fraction are shorter than 64 in? Taller than 72 in?

**Intermediate** — Birth weights $N(3420,\,495)$: find $P(3000<x<4000)$. Then show that for **any** normal, $P(\mu-k\sigma<X<\mu+k\sigma)$ depends only on $k$, and explain what that says about the Empirical Rule.

**Advanced** — Standardizing preserves probabilities only because the map $x\mapsto\frac{x-\mu}{\sigma}$ is linear and increasing. What goes wrong if $\sigma<0$ were allowed? Why can't you standardize a **skewed** distribution and then use Table A-2 (see [[skewness]])?
