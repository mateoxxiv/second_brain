---
tags:
  - status/seed
  - probability
related:
  - "[[mean-and-variance-of-a-probability-distribution]]"
  - "[[binomial-mean-and-variance]]"
  - "[[discrete-probability-distribution]]"
  - "[[statistical-significance]]"
  - "[[measures-of-variation]]"
  - "[[z-score]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-2 (Resultados inusuales)"
---

> **TL;DR** — An outcome is "unusual" either if it lands more than 2 standard deviations from the mean (range rule of thumb) or if the probability of a result *that extreme or more* is $\le 0.05$ (rare event rule).

---

## Intuition

When a result surprises you, you want a rule for "is this actually weird, or just normal randomness?" Two rules, two viewpoints. The **range rule of thumb** looks at *distance*: most values huddle within 2 SDs of the mean, so anything beyond that is uncommon. The **rare event rule** looks at *probability*: if getting a result this extreme (or more) would almost never happen by chance, then chance probably isn't the explanation — your assumption is likely wrong.

This is the seed of all inferential statistics: assume something (a coin is fair), observe data, and if the data is too improbable under that assumption, reject the assumption. It's the same logic as [[statistical-significance|statistical significance]], here in its most basic form.

## Mechanics

**Range rule of thumb** (distance-based, builds on the [[measures-of-variation|SD]] and the [[z-score|2-SD rule]]):
$$\text{max usual} = \mu + 2\sigma, \qquad \text{min usual} = \mu - 2\sigma$$
Values outside $[\mu-2\sigma,\ \mu+2\sigma]$ are unusual. The "2" is a guideline, not sacred — 3 is sometimes used.

**Rare event rule** (probability-based). Under a stated assumption, if the probability of the *observed event or a more extreme one* is very small, doubt the assumption. Using probabilities to flag counts:

| Direction | Unusually **high** | Unusually **low** |
|-----------|--------------------|--------------------|
| Criterion | $P(x \text{ or more}) \le 0.05$ | $P(x \text{ or fewer}) \le 0.05$ |

**Key subtlety — use "or more/or fewer", not exactly $x$.** With 1000 coin flips, $P(\text{exactly }501)=0.0252$ is tiny, yet 501 heads is *not* unusual, because $P(501\text{ or more})=0.487$ is huge. Any single exact count is rare when there are many possibilities; what matters is the *cumulative tail*.

**Worked example (peas: $\mu=3.8,\ \sigma=1.0$).** Range rule: usual values lie in $[1.8, 5.8]$, so getting only **1** green pod is unusual. Probability rule: $P(1\text{ or fewer}) = P(1)+P(0) = 0.015+0.001 = 0.016 \le 0.05$ → unusually low. Both agree.

```python
# Rare event rule: is 1 green pod (of 5) unusually low?
P = {0:0.001, 1:0.015}
p_one_or_fewer = P[0] + P[1]          # 0.016  ≤ 0.05  → unusual
```

## In ML

**This is hypothesis testing in miniature.** The rare event rule — assume a null, compute the tail probability, reject if $\le 0.05$ — is exactly the p-value logic behind A/B tests and model-comparison significance checks. The 0.05 threshold you'll meet everywhere starts right here.

**Anomaly and outlier detection.** The range rule ($|x-\mu| > 2\sigma$, i.e. $|z|>2$) is the textbook z-score outlier filter used to flag anomalies, clean training data, and trigger monitoring alerts when a production metric drifts into the tail.

## Exercises

**Basic** — A distribution has $\mu = 20,\ \sigma = 3$. Give the range of usual values. Is 27 unusual?

**Intermediate** — For a variable where $P(8\text{ or more}) = 0.03$, is observing 8 unusually high? What if instead $P(\text{exactly }8) = 0.03$ but $P(8\text{ or more}) = 0.20$ — is 8 unusual then? Explain the difference.

**Advanced** — A coin gives 990 heads in 1000 flips. Sketch how you'd use the rare event rule to argue the coin is biased. Which probability do you compute, and why "or more" rather than "exactly 990"?
