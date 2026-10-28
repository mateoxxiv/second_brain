---
tags:
  - status/seed
  - probability
related:
  - "[[type-i-and-type-ii-errors]]"
  - "[[sample-size-for-proportion]]"
  - "[[critical-region-and-significance-level]]"
  - "[[binomial-distribution]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 Parte 2 (Potencia de una prueba; Ejemplos 11–12)"
---

> **TL;DR** — Power is 1 − β: the probability of rejecting H0 when a specific alternative value is true. It rises with α, with n, and with the gap between the true value and the H0 value.

---

## Intuition

Power is a test's sensitivity. A test with low power is like a metal detector set too low: it misses real targets. A non-significant result from a low-power test says little, because the test could not have detected the effect anyway.

## Mechanics

- **Power depends on a specific alternative.** Power is $P(\text{reject } H_0 \mid p = p_1)$. Change $p_1$ and the power changes, so one test has many power values.
- **What raises power**: a larger gap between $p_1$ and $p_0$; a larger α; a larger n; less variability in the data.
- **Triola's table** (XSORT, n = 14, α = 0.05, H1: $p > 0.5$). The book reports these power values:

| True $p$ | 0.6 | 0.7 | 0.8 | 0.9 |
|---|---|---|---|---|
| Power $1-\beta$ | 0.180 | 0.564 | 0.773 | 0.988 |

  The table is garbled in the source paste, so these values were reconstructed from the text. My own recomputation with exact binomial cutoffs for n = 14 did **not** reproduce them (at cutoff 13, power at p = 0.6 is 0.008; at cutoff 11, α ≈ 0.029 and power is 0.124). The upward trend matches. Verify the exact values against the book or Minitab before relying on them.

- **Convention**: power of at least 0.80 is common. Some statisticians want 0.85 or 0.90.

```python
import numpy as np

rng = np.random.default_rng(0)

def power(p1: float, n: int = 14, cutoff: int = 13, sims: int = 200_000) -> float:
    """Share of simulated samples that reject H0 when the true proportion is p1."""
    x = rng.binomial(n, p1, size=sims)
    return float(np.mean(x >= cutoff))

print(round(power(0.6), 3), round(power(0.8), 3))   # roughly 0.008 and 0.20
```

**Design direction.** Fix α, pick a difference that matters, fix power (0.80), then solve for n. Triola's Example 12: detecting a drop from 0.5 to 0.4 in coronary disease at α = 0.05 and power 0.80 needs n = 153, computed with Minitab. See [[sample-size-for-proportion]] for the closed-form version.

## In ML

**Experiment sizing** — deciding how many users an A/B test needs is a power calculation. An underpowered test ends with "no significant difference" that is nearly uninformative.

**Absence of evidence** — a non-significant result from a low-power test does not show that the effect is absent.

## Exercises

**Basic** — In the n = 14 setup, what is the power when the true $p$ is 0.5? (Think about what the test's error rate is when H0 is true.)

**Intermediate** — Use the simulation above. Compare power at n = 14 and n = 50 for $p_1 = 0.6$, with a cutoff chosen to keep α near 0.05.

**Advanced** — Why does a power of 0.18 at $p = 0.6$ not make the test "wrong"? What does Triola recommend you settle before running the experiment?
