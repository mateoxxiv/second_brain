---
tags:
  - status/seed
  - probability
related:
  - "[[probability-density-function]]"
  - "[[standard-normal-distribution]]"
  - "[[cdf-and-quantiles]]"
  - "[[monte-carlo-simulation]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-2 (Distribuciones uniformes, Ejemplos 1–2)"
---

> **TL;DR** — The continuous uniform on $[a,b]$ is a flat rectangle of height $1/(b-a)$, so every probability is just **width × height**. It is the simplest case of "area = probability."

---

## Intuition

"Any value in the range is equally likely." That is the continuous version of a fair die. Because the curve is flat, the density is a rectangle, and you never need calculus: every probability is the area of a smaller rectangle.

Triola uses it as a teaching bridge before the normal. The normal's bell is hard to measure, but the *principle* is identical: find the area of the region you care about.

## Mechanics

$X \sim U(a,b)$ has [[probability-density-function|density]]

$$f(x) = \frac{1}{b-a}, \quad a \le x \le b \quad (\text{0 elsewhere})$$

**Where the height comes from.** The rectangle has width $b-a$ and must have area 1, so the height is forced: height $= 1/\text{range}$.

$$P(c \le X \le d) = \underbrace{(d-c)}_{\text{width}} \cdot \underbrace{\frac{1}{b-a}}_{\text{height}} = \frac{d-c}{b-a}$$

**Worked (Newport Power and Light).** Voltage is uniform on [123.0, 125.0] V. Range = 2, so height = 0.5. Then
$P(X > 124.5) = (125.0-124.5)\times 0.5 = 0.25$.

| Property | Formula | Why it matters |
|---|---|---|
| Height | $1/(b-a)$ | forced by total area = 1 |
| Mean | $(a+b)/2$ | the center, by symmetry |
| Variance | $(b-a)^2/12$ | spread grows with the square of the width |
| CDF | $(x-a)/(b-a)$ | a straight line from 0 to 1, see [[cdf-and-quantiles]] |

```python
from scipy import stats
# scipy parameterizes U(a, b) as loc=a, scale=b-a  (a classic gotcha)
V = stats.uniform(loc=123.0, scale=2.0)
print(V.pdf(124))        # 0.5  → the height
print(1 - V.cdf(124.5))  # 0.25 → area to the right of 124.5
```

## In ML

**The seed of all randomness.** `np.random.rand()` gives $U(0,1)$, and every other distribution is sampled by transforming it. [[cdf-and-quantiles|Inverse transform sampling]] returns $F^{-1}(u)$ for $u \sim U(0,1)$. It also powers [[monte-carlo-simulation]].

**Initialization and search.** Xavier/Glorot *uniform* init draws weights from $U(-r, r)$, with $r$ chosen using the variance formula $(b-a)^2/12$ so that activations keep a stable variance. Random hyperparameter search samples from uniforms (often on a log scale for learning rates).

## Exercises

**Basic** — A bus arrives uniformly between 0 and 20 minutes. Find the height of the density, $P(\text{wait} < 5)$, and the mean wait.

**Intermediate** — Derive $E[X]=(a+b)/2$ and $\text{Var}(X)=(b-a)^2/12$ by integration.

**Advanced** — Glorot uniform uses $U(-r, r)$ with target variance $2/(n_{in}+n_{out})$. Use the variance formula to derive $r = \sqrt{6/(n_{in}+n_{out})}$.
