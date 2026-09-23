---
tags:
  - status/seed
  - probability
related:
  - "[[discrete-probability-distribution]]"
  - "[[expected-value]]"
  - "[[binomial-mean-and-variance]]"
  - "[[measures-of-center]]"
  - "[[measures-of-variation]]"
  - "[[weighted-mean]]"
  - "[[identifying-unusual-results]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-2 (Fórmulas 5-1 a 5-4)"
---

> **TL;DR** — The mean, variance, and standard deviation of a [[discrete-probability-distribution|probability distribution]] are just the sample formulas with each value re-weighted by its probability $P(x)$ instead of its frequency.

---

## Intuition

For a *sample* you sum values and divide by $n$. But a probability distribution is what you'd see over *infinitely many* trials — there's no finite $n$ to divide by. The fix: weight each value $x$ by how often it occurs, and "how often" over infinite trials *is* its probability $P(x)$. So the mean becomes a [[weighted-mean|weighted average]] with the probabilities as weights. Same for spread: variance is the probability-weighted average squared distance from the mean.

This is the theoretical counterpart to the sample [[measures-of-center|mean]] and [[measures-of-variation|standard deviation]]: those describe the data you *collected*, these describe the process that *generates* it.

## Mechanics

For a discrete random variable with distribution $P(x)$:

| Quantity | Formula | Note |
|----------|---------|------|
| **Mean** (5-1) | $\mu = \sum [\,x\cdot P(x)\,]$ | = the [[expected-value|expected value]] $E$ |
| **Variance** (5-2) | $\sigma^2 = \sum [\,(x-\mu)^2\cdot P(x)\,]$ | definitional — easier to *understand* |
| **Variance** (5-3) | $\sigma^2 = \sum [\,x^2\cdot P(x)\,] - \mu^2$ | shortcut — easier to *compute* |
| **Std. dev.** (5-4) | $\sigma = \sqrt{\sum [\,x^2\cdot P(x)\,] - \mu^2}$ | root of the variance |

**Why 5-1 works (derivation).** Start from a frequency-table mean over a population of size $N$: $\mu = \frac{\sum(f\cdot x)}{N} = \sum\!\big(x\cdot \tfrac{f}{N}\big)$. The ratio $f/N$ — frequency over population size — *is* the probability of $x$. Substitute $P(x)$ for $f/N$ and you've moved from finite relative frequency to infinite-trial probability: $\mu = \sum[x\cdot P(x)]$. The same swap turns the sample-variance formula into 5-2.

**Rounding rule.** Round $\mu, \sigma, \sigma^2$ to one more decimal place than the values of $x$. Integer $x$ → one decimal.

```python
x = [0,1,2,3,4,5]; P = [0.001,0.015,0.088,0.264,0.396,0.237]
mu  = sum(xi*pi for xi,pi in zip(x,P))               # 3.8
var = sum((xi-mu)**2*pi for xi,pi in zip(x,P))       # 0.9
sd  = var**0.5                                        # 1.0
```

## In ML

**Expectation and variance of a loss are distribution parameters.** When you reason about the *expected* loss or the *variance* of a gradient estimate, you're computing exactly $\sum x P(x)$ (or its integral form). Minibatch SGD works because the batch gradient is an unbiased estimate of this population mean.

**Variance is the budget you spend on uncertainty.** $\sigma^2$ of a predictive distribution quantifies confidence; the shortcut formula $E[X^2]-(E[X])^2$ is the identity used everywhere from computing the variance of a [[discrete-probability-distribution|categorical output]] to the bias–variance decomposition.

## Exercises

**Basic** — For $P(1){=}0.5,\ P(2){=}0.3,\ P(3){=}0.2$, compute $\mu$ by hand.

**Intermediate** — Using the same distribution, compute $\sigma^2$ with the definitional formula (5-2), then again with the shortcut (5-3). Confirm they match.

**Advanced** — Prove algebraically that $\sum[(x-\mu)^2 P(x)] = \sum[x^2 P(x)] - \mu^2$. (Expand the square and use $\sum x P(x) = \mu$ and $\sum P(x)=1$.)
