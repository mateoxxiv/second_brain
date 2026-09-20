---
tags:
  - status/seed
  - probability
related:
  - "[[binomial-distribution]]"
  - "[[multiplication-rule]]"
  - "[[counting-and-combinatorics]]"
  - "[[discrete-probability-distribution]]"
  - "[[mean-and-variance-of-a-probability-distribution]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-4 (Distribución hipergeométrica) / §5-2 Ejercicio 32"
---

> **TL;DR** — The hypergeometric distribution counts how many "special" items you get when you draw $n$ from a finite population **without replacement** — the without-replacement cousin of the [[binomial-distribution|binomial]].

---

## Intuition

You have a finite pile with two kinds of things — say 2 defective altimeters and 8 good ones. You grab a handful (3) *without putting any back* and ask: "how many defective ones did I catch?" Because you don't replace, every draw changes the pile, so the draws are **dependent** — this is the [[multiplication-rule|multiplication rule]] with a shrinking pool, packaged into a formula.

Contrast with the [[binomial-distribution|binomial]]: there, each trial is independent (you replace, or the pool is effectively infinite). Same question — "how many successes in $n$ draws?" — the *only* difference is replacement. When the population is huge relative to your sample, the two nearly coincide (the pool barely shrinks); when it's small, you must use hypergeometric.

## Mechanics

Population of $N$ items, of which $K$ are "successes." Draw $n$ without replacement; $x$ = number of successes drawn:

$$P(x) = \frac{\binom{K}{x}\binom{N-K}{\,n-x\,}}{\binom{N}{n}}$$

Read it as: **(ways to pick $x$ of the $K$ good) × (ways to pick the rest from the $N-K$ others), over all ways to pick $n$ of $N$** — pure [[counting-and-combinatorics|combinations]], which absorb the ordering automatically.

| Quantity | Formula |
|----------|---------|
| Mean | $\mu = n\dfrac{K}{N}$ |
| Variance | $\sigma^2 = n\dfrac{K}{N}\dfrac{N-K}{N}\dfrac{N-n}{N-1}$ |

The last factor $\frac{N-n}{N-1}$ is the **finite population correction** — it's what shrinks the variance below the binomial's $np(1-p)$, and it vanishes (→1) as $N$ grows.

**Worked (Sky Ranch, §5-2 Ex. 32).** $N=10$ altimeters, $K=2$ miscalibrated, draw $n=3$. Total ways $\binom{10}{3}=120$:

```
x=0:  C(2,0)C(8,3)/120 = 56/120 = 0.4667
x=1:  C(2,1)C(8,2)/120 = 56/120 = 0.4667
x=2:  C(2,2)C(8,1)/120 =  8/120 = 0.0667   (sum = 1 ✓)
```

Then $\mu = 3\cdot\frac{2}{10} = 0.6$ and $\sigma \approx 0.6$ via the [[mean-and-variance-of-a-probability-distribution|distribution formulas]].

```python
from scipy.stats import hypergeom
rv = hypergeom(M=10, n=2, N=3)      # M=pop, n=successes in pop, N=draws
print(rv.pmf([0,1,2]))              # [0.4667 0.4667 0.0667]
print(rv.mean(), rv.std())          # 0.6 0.611
```

## In ML

**Sampling without replacement is everywhere.** Building a train/test split, drawing a mini-batch without repeats, or selecting $k$ features from $p$ are all without-replacement draws — the *count* of any subgroup follows a hypergeometric law. It's the correct model whenever the population is finite and you don't put items back.

**Fisher's exact test is hypergeometric.** The p-value for a 2×2 contingency table (used in A/B tests with small counts and in gene-set enrichment analysis) is computed directly from hypergeometric tail probabilities — the exact, small-sample alternative to the chi-squared approximation.

## Exercises

**Basic** — A box has 5 red and 7 blue chips. Draw 4 without replacement. Write $P(x=2\text{ red})$ using the formula (don't simplify).

**Intermediate** — For the Sky Ranch problem, verify $\mu=0.6$ two ways: (a) the shortcut $\mu=nK/N$, and (b) $\sum x\,P(x)$ from the table. Why must they agree?

**Advanced** — Show that as $N,K\to\infty$ with $K/N\to p$ fixed, the hypergeometric PMF approaches the [[binomial-distribution|binomial]] $\binom{n}{x}p^x(1-p)^{n-x}$. What happens to the finite population correction, and what does that say about the 5% guideline in [[multiplication-rule]]?
