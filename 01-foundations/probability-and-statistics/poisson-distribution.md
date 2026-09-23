---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
  - "[[binomial-distribution]]"
  - "[[poisson-approximation-to-binomial]]"
  - "[[exponential-distribution]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-5 (Distribución de Poisson)"
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.packtpub.com/"
  - "https://www.khanacademy.org/math/statistics-probability"
---

> **TL;DR** — Counts rare independent events in a fixed interval. PMF = λ^k · e^{−λ} / k!. Defining property: E[X] = Var(X) = λ. Use this equality as a diagnostic.

---

## Intuition

Poisson answers: "I know events arrive at an average rate of λ per hour. How likely am I to see exactly k arrivals in the next hour?" It's the limiting case of Binomial when you chop the interval into infinitely many tiny sub-intervals — which is also why it can serve as a [[poisson-approximation-to-binomial|shortcut for a large-n, small-p binomial]].

The key diagnostic: in Poisson data, the mean should equal the variance. If your count data has variance much greater than mean (overdispersion), Poisson is the wrong model.

## Mechanics

**PMF** (derived from Binomial limit: n→∞, p→0, np=λ):
$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

$$E[X] = \lambda \qquad \text{Var}(X) = \lambda \qquad \sigma = \sqrt{\lambda}$$

(Triola §5-5 writes the rate as $\mu$; $\mu = \lambda$. The distribution has just **one** parameter — the mean — hence $\sigma=\sqrt{\mu}$.)

**Four requirements.** (1) $x$ = number of occurrences in an interval (time, distance, area, volume…); (2) occurrences are random; (3) independent of each other; (4) uniformly distributed over the interval.

**Contrast with the [[binomial-distribution|binomial]].** Binomial depends on *two* parameters ($n, p$) and $x$ is capped at $n$; Poisson depends on *one* ($\mu$) and $x$ has **no upper bound** ($0,1,2,\dots$).

**Overdispersion diagnostic:** if Var(X) >> E[X], data is not Poisson (use Negative Binomial).

**Goodness of fit.** To test whether counts are Poisson, compare *observed* frequencies to *expected* ones, $N\cdot P(x)$. Triola's earthquake data (93 quakes in 100 years → $\mu=0.93$) matches its Poisson expected frequencies closely, so Poisson is a good model there.

```python
import numpy as np
from math import factorial, exp

def poisson_pmf(k, lam):
    return (lam**k * exp(-lam)) / factorial(k)

lam = 3.0
# Verify probabilities sum to ~1
print(sum(poisson_pmf(k, lam) for k in range(20)))  # ~1.0

# E=Var diagnostic
samples = np.random.poisson(lam=lam, size=100000)
print(f"E[X]   = {samples.mean():.4f}  (expected {lam})")
print(f"Var(X) = {samples.var():.4f}  (expected {lam})")

# Overdispersion check: Var/Mean ratio should be ~1 for Poisson
ratio = samples.var() / samples.mean()
print(f"Var/Mean = {ratio:.3f}  (Poisson ≈ 1.0)")
```

> Runnable: [[code/foundations/poisson_distribution.py]]

## In ML

**NLP word counts.** Word frequency per document roughly follows Poisson for rare words. The simplest language models assume Poisson word generation — more sophisticated models (unigram, n-gram) refine this.

**Anomaly detection.** If you know the expected rate λ of some event (normal server requests, API calls), you can flag time windows where the observed count is in the tail of Poisson(λ). P(X=0) for Poisson(3) = e^{-3} ≈ 0.05 — no events in a window where 3 are expected is already unusual.

**Poisson regression.** When the target is a count (number of accidents, purchases, page views), use Poisson regression instead of linear regression — it avoids negative predictions and has the right distributional assumption.

## Exercises

**Basic** — Compute P(X=0) for Poisson(3). Interpret what it means in a server request monitoring context.

**Intermediate** — Explain why Var = E is a diagnostic for Poisson. What does overdispersion (Var >> E) imply about the data generation process?

**Advanced** — Give two examples from ML where Poisson is the appropriate model and two where it is not. For the non-examples, what alternative distribution would you use?
