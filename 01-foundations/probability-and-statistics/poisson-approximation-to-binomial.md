---
tags:
  - status/seed
  - probability
related:
  - "[[poisson-distribution]]"
  - "[[binomial-distribution]]"
  - "[[binomial-mean-and-variance]]"
  - "[[law-of-large-numbers]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-5 (Poisson como aproximación de la binomial)"
---

> **TL;DR** — When $n$ is large and $p$ is small, a [[binomial-distribution|binomial]] is a pain to compute but is almost exactly [[poisson-distribution|Poisson]]$(\mu = np)$ — use it as a shortcut when $n \ge 100$ and $np \le 10$.

---

## Intuition

The binomial formula chokes when $n$ is huge: factorials like $365!$ overflow, and $p^x q^{n-x}$ underflows. But there's a lucky escape: when trials are *many* ($n$ large) and success is *rare* ($p$ small), the binomial's shape becomes indistinguishable from a Poisson driven by a single number — its mean $\mu = np$.

Intuitively, "many trials, each rarely succeeding" *is* the Poisson setting: rare events scattered across a long interval. So instead of tracking $n$ and $p$ separately, you collapse them into their product $\mu = np$ and use the far simpler one-parameter Poisson formula. You trade two parameters for one, and lose almost no accuracy.

## Mechanics

**When to use it** (both conditions):

| # | Condition | Meaning |
|---|-----------|---------|
| 1 | $n \ge 100$ | many trials |
| 2 | $np \le 10$ | successes stay rare (small $\mu$) |

Then approximate Binomial$(n,p)$ by Poisson with

$$\mu = np, \qquad P(x) = \frac{\mu^x e^{-\mu}}{x!}.$$

Only $\mu$ is needed — the individual $n$ and $p$ drop out once multiplied ([[binomial-mean-and-variance|Formula 5-6]]).

**Why it works.** It's the same limit that *defines* the [[poisson-distribution|Poisson]]: hold $\mu=np$ fixed and let $n\to\infty$, $p\to 0$. The binomial PMF converges term-by-term to $\mu^x e^{-\mu}/x!$. The $n\ge100$, $np\le10$ rule is just "close enough to that limit."

**Worked (Illinois Pick 3).** Play a 3-digit game daily for a year: $n=365$, $p=1/1000$. Both conditions hold ($365\ge100$, $np=0.365\le10$), so $\mu = np = 0.365$ and

$$P(1) = \frac{0.365^1 e^{-0.365}}{1!} = 0.253.$$

The exact binomial gives **0.254** — the Poisson approximation is essentially spot-on.

```python
from scipy.stats import binom, poisson
n, p = 365, 1/1000
mu = n * p                          # 0.365
poisson.pmf(1, mu)                  # 0.2534  (approximation)
binom.pmf(1, n, p)                  # 0.2536  (exact) → nearly identical
```

## In ML

**Rare-event modeling at scale.** Click-through, fraud, ad conversions, packet loss — all are "huge $n$, tiny $p$." Rather than a binomial over millions of impressions, you model the *count* as Poisson($\mu=np$), which is cheaper and the basis of Poisson regression for count targets.

**Numerical stability.** Beyond convenience, the approximation sidesteps computing enormous factorials and vanishing powers that overflow/underflow in the exact binomial — the same reason libraries compute log-probabilities. One parameter $\mu$ is both simpler and better-conditioned.

## Exercises

**Basic** — A factory makes 5000 chips with defect rate $p=0.001$. Check the two conditions, then find $\mu$ and $P(\text{exactly 3 defective})$ using Poisson.

**Intermediate** — For $n=200$, $p=0.02$, compute $P(2)$ both exactly (binomial) and via Poisson. How close are they? Now try $n=20$, $p=0.2$ (same $np=4$) — why is the approximation worse?

**Advanced** — Sketch why the approximation *fails* when $p$ is near 0.5 even for large $n$. Which distribution approximates the binomial in that regime instead, and what condition ([[binomial-distribution|np≥5, nq≥5]]) signals it?
