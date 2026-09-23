---
tags:
  - status/seed
  - probability
related:
  - "[[binomial-distribution]]"
  - "[[bernoulli-distribution]]"
  - "[[mean-and-variance-of-a-probability-distribution]]"
  - "[[identifying-unusual-results]]"
  - "[[statistical-significance]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-4 (Formulas 5-6 a 5-8)"
---

> **TL;DR** — For a binomial, skip the general sums: $\mu=np$, $\sigma^2=npq$, $\sigma=\sqrt{npq}$ — and the real payoff is using $np \pm 2\sqrt{npq}$ to judge whether an observed count is unusual.

---

## Intuition

If 75% of pea offspring have green pods and you grow 5, how many green do you *expect*? Obviously about $5 \times 0.75 = 3.75$. That's the whole idea of the binomial mean: **expected count = fraction × number of trials**, i.e. $\mu = np$. No summation needed.

The spread ($\sigma$) is less obvious, but its *use* is the point of this section: it turns a single "expected" number into a **range of normal results**. Real experiments don't hit the mean exactly — sample results vary. So instead of asking "did I get exactly $np$?", you ask "did I land inside $np \pm 2\sigma$?" If yes, the outcome is consistent with $p$; if it falls outside, $p$ is suspect. That reasoning — a claim survives if the data lands in its usual range — is the seed of [[statistical-significance|hypothesis testing]].

## Mechanics

A binomial is a [[discrete-probability-distribution|discrete distribution]], so the general [[mean-and-variance-of-a-probability-distribution|formulas]] ($\mu=\sum xP(x)$, etc.) work — but these shortcuts are far easier ($q = 1-p$):

| Quantity | General (§5-2) | **Binomial shortcut** |
|----------|----------------|----------------------|
| Mean | $\sum[xP(x)]$ | $\mu = np$ |
| Variance | $\sum[x^2P(x)]-\mu^2$ | $\sigma^2 = npq$ |
| Std. dev. | $\sqrt{\sum[x^2P(x)]-\mu^2}$ | $\sigma = \sqrt{npq}$ |

**Why they work (the derivation Triola skips).** A binomial $X$ is the **sum of $n$ independent [[bernoulli-distribution|Bernoulli]]$(p)$ trials**, each with mean $p$ and variance $pq$. Means always add (linearity): $\mu = \underbrace{p+\dots+p}_{n} = np$. Variances add *because the trials are [[multiplication-rule|independent]]*: $\sigma^2 = \underbrace{pq+\dots+pq}_{n} = npq$. Independence is exactly what lets the variances sum — dependent trials would need covariance terms.

**Interpretation — the range rule** ([[identifying-unusual-results]]): usual values lie in
$$[\,\mu - 2\sigma,\ \mu + 2\sigma\,] = [\,np - 2\sqrt{npq},\ np + 2\sqrt{npq}\,].$$

**Worked (Mendel).** $n=580$, $p=0.75$: $\mu = 580(0.75) = 435$, $\sigma = \sqrt{580(0.75)(0.25)} = 10.4$. Usual range $435 \pm 20.9 = [414,\,456]$. Mendel observed **428** → *inside* the range → consistent with the 75% claim, not unusual.

```python
from scipy.stats import binom
n, p = 580, 0.75
mu, sd = binom.mean(n, p), binom.std(n, p)   # 435.0, 10.43
lo, hi = mu - 2*sd, mu + 2*sd                 # 414.1, 455.9  → 428 is inside
```

## In ML

**Standard error of a proportion.** The sample proportion $\hat p = X/n$ has $\text{Var}(\hat p) = pq/n$, so $\text{SE} = \sqrt{pq/n}$ — this is $\sigma$ of the binomial rescaled by $n$. It's the engine behind confidence intervals for conversion rates and the two-proportion A/B test.

**Error bars on accuracy.** A model's correct-count on $n$ test cases is [[binomial-distribution|Binomial]]$(n, p)$ with $p$ = true accuracy. So reported accuracy carries $\text{SE}=\sqrt{p(1-p)/n}$ — the reason small test sets give untrustworthy accuracy and why you report intervals, not point estimates.

## Exercises

**Basic** — For $n=100$, $p=0.2$, compute $\mu$, $\sigma$, and the usual range $\mu \pm 2\sigma$.

**Intermediate** — A coin is flipped 100 times, giving 68 heads. Using $np \pm 2\sqrt{npq}$ for a fair coin, is 68 unusual? What would you conclude about the coin?

**Advanced** — Prove $\sigma^2 = npq$ by writing $X = \sum_{i=1}^n B_i$ with $B_i \sim$ Bernoulli$(p)$ independent, using $\text{Var}(B_i)=pq$ and the additivity of variance under independence. Where exactly does independence enter?
