---
tags:
  - status/seed
  - probability
related:
  - "[[one-proportion-z-test]]"
  - "[[binomial-distribution]]"
  - "[[p-value]]"
  - "[[normal-approximation-to-binomial]]"
  - "[[identifying-unusual-results]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-3 Parte 2 (Ejemplo 4)"
---

> **TL;DR** — Skip the normal approximation: compute the P-value directly as a binomial tail probability under H0. It is exact and needs no $np \ge 5$ condition.

---

## Intuition

The [[one-proportion-z-test]] approximates a binomial with a normal curve because tail sums used to be hard by hand. Software makes the sums trivial, so you can ask the exact question: "if $p$ really is $p_0$, how likely is a count this extreme?" This is the rare-event rule from [[identifying-unusual-results]], made formal.

## Mechanics

Requirements: only simple random sample + binomial conditions. Under H0, $X \sim \text{Bin}(n, p_0)$.

| Test | P-value |
|---|---|
| Left-tailed | $P(X \le x)$ |
| Right-tailed | $P(X \ge x)$ |
| Two-tailed, $\hat p > p_0$ | $2\,P(X \ge x)$ |
| Two-tailed, $\hat p < p_0$ | $2\,P(X \le x)$ |

Each tail is a sum of [[binomial-distribution]] terms: $P(X \ge x) = \sum_{k=x}^{n} \binom{n}{k} p_0^k q_0^{\,n-k}$.

**Worked, pregnancy guesses** (57 of 104, H0: $p = 0.5$, two-tailed, α = 0.05): $\hat p = 0.548 > 0.5$, so
$$P = 2\,P(X \ge 57) = 2(0.18879) = 0.3776 > 0.05 \Rightarrow \text{fail to reject}$$

| Method | P-value |
|---|---|
| Normal approximation ($z = 0.98$) | 0.3268 |
| Exact binomial | 0.3776 |

Same decision, but the approximation understates $P$ by 0.05 here. Almost all of the gap is the dropped [[continuity-correction]]: using $x - 0.5 = 56.5$ gives $P = 0.3775$.

```python
from scipy import stats

n, x, p0 = 104, 57, 0.5
right = stats.binom.sf(x - 1, n, p0)     # P(X >= x): sf is P(X > x-1)
print(round(right, 5), round(2 * right, 4))         # 0.18879 0.3776
print(round(stats.binomtest(x, n, p0).pvalue, 4))   # 0.3776
```

Caveat: doubling one tail can push $P$ above 1 when $x$ is near $np_0$; cap it at 1. With $p_0 \ne 0.5$ the binomial is asymmetric, and `binomtest` uses a different two-sided rule (sum all outcomes no more likely than the observed one), so its answer can differ from Triola's doubling.

## In ML

**Small test sets** — 9 of 10 correct on a hand-labeled set fails $nq \ge 5$ for $p_0 = 0.5$. The exact test is the right tool.

**McNemar's test** — comparing two classifiers on the same items reduces to an exact binomial test on the disagreements, with $p_0 = 0.5$.

## Exercises

**Basic** — 8 heads in 10 flips, right-tailed, H0: $p = 0.5$. Compute $P(X \ge 8)$ by hand.

**Intermediate** — 3 defects in 50 items, H0: $p = 0.01$, H1: $p > 0.01$. Why is the z test invalid? Compute the exact P-value.

**Advanced** — For $p_0 = 0.3$, $n = 20$, $x = 2$, compare Triola's doubling rule with `binomtest`. Explain the difference.
