---
tags:
  - status/seed
  - probability
related:
  - "[[type-i-and-type-ii-errors]]"
  - "[[sample-size-for-proportion]]"
  - "[[critical-region-and-significance-level]]"
  - "[[binomial-distribution]]"
  - "[[normal-approximation-to-binomial]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 Parte 2 (Potencia de una prueba; Ejemplos 11–12)"
---

> **TL;DR** — Power is $1-\beta$: the probability of rejecting H0 when a specific alternative value is true. It rises with α, with n, and with the gap between the true value and the H0 value.

---

## Intuition

Power is a test's sensitivity. A test with low power is like a metal detector set too low: it misses real targets. A non-significant result from a low-power test says little, because the test could not have detected the effect anyway.

## Mechanics

**Power depends on a specific alternative.** Power is $P(\text{reject } H_0 \mid p = p_1)$. Change $p_1$ and the power changes, so one test has many power values.

**What raises power**: a larger gap $|p_1 - p_0|$, a larger α, a larger n, and less variability.

**Triola does not give a power formula.** He defines power, says power calculations are "quite complicated", and recommends technology. The values in his table come from Minitab.

**Formula (normal approximation, one-sided test H1: $p > p_0$).** Reject H0 when $\hat p > p_0 + z_\alpha\sqrt{p_0q_0/n}$. Then

$$1-\beta = \Phi\!\left(\frac{(p_1-p_0)\sqrt{n} - z_\alpha\sqrt{p_0 q_0}}{\sqrt{p_1 q_1}}\right)$$

where $\Phi$ is the standard normal CDF, $q_i = 1-p_i$, and $z_\alpha = 1.645$ for α = 0.05.

**Sample size for a target power** (solve the same equation for n):

$$n = \left(\frac{z_\alpha\sqrt{p_0 q_0} + z_\beta\sqrt{p_1 q_1}}{p_1 - p_0}\right)^2, \qquad z_\beta = z_{1-\beta}$$

**Triola's table** (XSORT, n = 14, α = 0.05, H1: $p > 0.5$). The formula reproduces the book's values:

| True $p$ | 0.6 | 0.7 | 0.8 | 0.9 |
|---|---|---|---|---|
| Power $1-\beta$ (formula) | 0.180 | 0.436 | 0.773 | 0.988 |
| $\beta$ | 0.820 | 0.564 | 0.227 | 0.012 |

The book's text says the power at $p = 0.7$ is 0.564. That conflicts with the table and the formula, which give 0.436 for power and 0.564 for β. Treat 0.564 as β. The book also says the values were computed exactly, but they match the normal approximation, not exact binomial calculations.

```python
import math
from scipy.stats import norm, binom

def power_normal(p0: float, p1: float, n: int, alpha: float = 0.05) -> float:
    """Power of the one-sided z-test of H0: p = p0 against H1: p > p0."""
    z = norm.ppf(1 - alpha)
    numerator = (p1 - p0) * math.sqrt(n) - z * math.sqrt(p0 * (1 - p0))
    return norm.cdf(numerator / math.sqrt(p1 * (1 - p1)))

def power_exact(p0: float, p1: float, n: int, alpha: float = 0.05) -> float:
    """Exact binomial power: smallest cutoff c with P(X >= c | p0) <= alpha."""
    c = min(k for k in range(n + 1) if binom.sf(k - 1, n, p0) <= alpha)
    return binom.sf(c - 1, n, p1)

def sample_size(p0: float, p1: float, alpha: float = 0.05, power: float = 0.80) -> int:
    """Smallest n for the normal-approximation test to reach the target power."""
    z_a, z_b = norm.ppf(1 - alpha), norm.ppf(power)
    n = ((z_a * math.sqrt(p0 * (1 - p0)) + z_b * math.sqrt(p1 * (1 - p1))) / (p1 - p0)) ** 2
    return math.ceil(n)

print([round(power_normal(0.5, p1, 14), 3) for p1 in (0.6, 0.7, 0.8, 0.9)])  # [0.18, 0.436, 0.773, 0.988]
print([round(power_exact(0.5, p1, 14), 3) for p1 in (0.6, 0.7, 0.8, 0.9)])   # [0.124, 0.355, 0.698, 0.956]
print(sample_size(0.5, 0.4))   # 153, Triola's Example 12
```

The exact binomial version is lower because the discrete cutoff at n = 14 forces α down to 0.029. Triola's numbers match the normal approximation.

**Design direction.** Fix α, choose a difference that matters, fix power (0.80), and solve for n. Example 12 checks out: $p_0 = 0.5 \to p_1 = 0.4$, α = 0.05, power 0.80 gives $n \approx 152.5$, rounded up to 153. See [[normal-approximation-to-binomial]] for the approximation's conditions.

## In ML

**Experiment sizing** — deciding how many users an A/B test needs is this calculation. An underpowered test ends with "no significant difference", which tells you little.

**Absence of evidence** — a non-significant result from a low-power test does not show that the effect is absent.

## Exercises

**Basic** — Use `power_normal(0.5, 0.5, 14)`. Why does the answer equal α? Explain using the definition of power.

**Intermediate** — Compare `power_normal` and `power_exact` at $p_1 = 0.6$ for n = 14 and n = 50. Compute the gap at each n (the normal values are 0.18 and 0.407). Why does the approximation become more reliable as n grows?

**Advanced** — Derive the sample-size formula from the power formula by setting $\Phi^{-1}(1-\beta) = (p_1-p_0)\sqrt{n} - z_\alpha\sqrt{p_0q_0}$ over $\sqrt{p_1 q_1}$. Then explain why the required n grows as $1/(p_1-p_0)^2$.
