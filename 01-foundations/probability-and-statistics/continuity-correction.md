---
tags:
  - status/seed
  - probability
related:
  - "[[normal-approximation-to-binomial]]"
  - "[[binomial-distribution]]"
  - "[[normal-probabilities-via-standardization]]"
  - "[[identifying-unusual-results]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §6-6 (Correcciones por continuidad, Figura 6-22, Ejemplos 1–2)"
---

> **TL;DR** — A discrete count $x$ becomes the interval $x - 0.5$ to $x + 0.5$ on the continuous normal curve, and the wording ("at least", "more than", "exactly") decides which boundary to use.

---

## Intuition

The binomial puts all its probability on whole numbers: 1149, 1150, 1151. A normal curve is continuous, so the bar for 1150 has to be drawn as a slice of width 1 centered on 1150. The slice runs from 1149.5 to 1150.5. The correction spreads each whole number into that slice, so the area of the slice matches the probability of the integer.

## Mechanics

**Rule:** a discrete value $x$ is represented by $[x - 0.5,\ x + 0.5]$.

**Choosing the boundary.** Start from the wording, then choose which side of the slice to cut:

| Statement | Area to shade | Boundary used |
|-----------|---------------|---------------|
| at least 8 (includes 8) | right of 7.5 | 7.5 |
| more than 8 (excludes 8) | right of 8.5 | 8.5 |
| at most 8 (includes 8) | left of 8.5 | 8.5 |
| fewer than 8 (excludes 8) | left of 7.5 | 7.5 |
| exactly 8 | between 7.5 and 8.5 | both |

The rule of thumb: when $x$ is included, the boundary is the outer edge of its slice (7.5 for "at least 8", 8.5 for "at most 8"). When $x$ is excluded, the boundary is the inner edge (8.5 for "more than 8", 7.5 for "fewer than 8").

**Exact value (the "exactly x" case).** Subtract the two cumulative areas:

$$P(X = x) \approx P(Z \le \tfrac{(x+0.5) - \mu}{\sigma}) - P(Z \le \tfrac{(x-0.5) - \mu}{\sigma})$$

**Worked (Pew survey):** $n = 2822$, $p = 0.75$, so $\mu = 2116.5$ and $\sigma = 23.00$. For exactly 2060:

- $z_{\text{upper}} = (2060.5 - 2116.5)/23.00 = -2.43$, area 0.0075
- $z_{\text{lower}} = (2059.5 - 2116.5)/23.00 = -2.48$, area 0.0066
- Difference: about 0.0009 (rounded z); exact binomial 0.00087

```python
from scipy.stats import norm, binom
mu, sd = 2822 * 0.75, (2822 * 0.75 * 0.25) ** 0.5
approx = norm.cdf(2060.5, mu, sd) - norm.cdf(2059.5, mu, sd)
print(approx, binom.pmf(2060, 2822, 0.75))   # ~0.00085 vs 0.00087
```

## In ML

**Discrete counts approximated by continuous curves.** Any time you replace a count (correct predictions, clicks, errors) with a normal, the same half-unit adjustment applies. Skipping it biases tail probabilities by roughly half a unit on the count scale, which matters most when the counts are small relative to $\sigma$.

## Exercises

**Basic** — Write the continuity-corrected boundary for each: (a) at least 12, (b) more than 12, (c) at most 12.

**Intermediate** — Using the table above, state the area you would shade for "fewer than 20 successes" and for "20 or more". Why do these two sum to 1 once corrected?

**Advanced** — For $P(X \le 3)$ with $n = 20$ and $p = 0.5$, compute the exact value, the uncorrected normal value, and the corrected normal value. Which approximation is closer, and why might the half-unit correction not always help at small $n$?
