---
tags:
  - status/seed
  - probability
related:
  - "[[population-and-sample]]"
  - "[[sampling-distribution]]"
  - "[[unbiased-and-biased-estimators]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[statistical-significance]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-3."
---

> **TL;DR** — A *parameter* describes a whole population; a *statistic* describes a sample — same kind of number (a mean, a proportion), but one is the fixed truth you want and the other is the estimate you actually have.

---

## Intuition

You care about a population but can only measure a [[population-and-sample|sample]] of it. So every numeric summary comes in two flavors: the true value out in the population (the **parameter**) and the value you computed from your sample (the **statistic**). The parameter is fixed but usually unknown; the statistic is known but wobbles from sample to sample. All of inferential statistics is the art of reasoning *from* the statistic you have *to* the parameter you want.

The tell is simple: **ask what the number was computed from.** Whole population → parameter. Subset → statistic.

## Mechanics

| | **Parameter** | **Statistic** |
|---|---|---|
| Describes | The entire population | A sample |
| Known? | Usually unknown (fixed) | Known (varies by sample) |
| Role | The target of inference | The estimate |
| Mean | $\mu$ | $\bar{x}$ |
| Std. dev. | $\sigma$ | $s$ |
| Proportion | $p$ | $\hat{p}$ |

**Worked examples (Triola §1-3):**

- **Parameter** — The 100 senators in a U.S. Congress; 55% are of one party. That 55% is a *parameter*: it's computed from *every* senator, i.e. the whole population.
- **Statistic** — In 1936 *Literary Digest* surveyed 2.3 million adults; 57% favored Landon. That 57% is a *statistic*: it comes from a sample, not the full voting population (and — see [[population-and-sample]] — a badly-drawn one that got the election wrong).

The notation convention is a memory aid: **plain symbols (μ, σ, p) for the population parameter; Roman letters with marks (x̄, s, p̂) for the sample statistic.** (μ and σ are Greek; p is the exception — plain p for the parameter, hatted p̂ for the statistic.)

```python
import numpy as np
rng = np.random.default_rng(0)
population = rng.normal(170, 10, size=1_000_000)  # "true" population of heights

mu = population.mean()                 # parameter: computed from everyone
sample = rng.choice(population, 50)
x_bar = sample.mean()                  # statistic: computed from a sample
print(mu, x_bar)                       # ~170.0  vs  ~168.4 -- the estimate misses a bit
```

## In ML

**Training metrics are statistics; true performance is a parameter** — your accuracy on a test set is a *statistic* estimating the model's real accuracy on the whole data-generating population (the parameter). That's why a single test score has uncertainty and why cross-validation exists: to see how much the statistic wobbles.

**Estimation is the core game** — fitting a model is estimating population parameters (weights, class probabilities) from a sample. [[statistical-significance]] and later hypothesis testing exist precisely to quantify how far a sample statistic can stray from the parameter by chance alone.

## Exercises

**Basic** — For each, say parameter or statistic: (a) the mean age of *all* employees at a 40-person company; (b) the mean age of 500 users sampled from an app's 2M-user base; (c) σ of a population; (d) x̄ of a survey.

**Intermediate** — You compute a sample proportion p̂ = 0.62. Explain in one sentence what unknown quantity it is estimating and why two different samples would give two different values of p̂.

**Advanced** — A statistic is called *[[unbiased-and-biased-estimators|unbiased]]* if its average over all possible samples equals the parameter. Explain why the sample mean x̄ is an unbiased estimator of μ, but dividing a sample variance by n (instead of n−1) gives a *biased* estimator of σ².
