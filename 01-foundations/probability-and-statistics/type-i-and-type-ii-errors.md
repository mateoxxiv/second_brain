---
tags:
  - status/seed
  - probability
related:
  - "[[statistical-power]]"
  - "[[critical-region-and-significance-level]]"
  - "[[sample-size-for-proportion]]"
  - "[[null-and-alternative-hypotheses]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Errores en las pruebas de hipótesis; Tabla 8-1; Ejemplo 10)"
---

> **TL;DR** — A type I error rejects a true H0 (probability α); a type II error fails to reject a false H0 (probability β). At fixed n, lowering one raises the other.

---

## Intuition

Any decision rule can be wrong in two ways. Convict an innocent person, or let a guilty one go. A test sets the first risk directly (α) and inherits the second (β). Only more data reduces both at once.

## Mechanics

| Decision | H0 true | H0 false |
|---|---|---|
| Reject H0 | **type I error**, probability α | correct (power = 1 − β) |
| Do not reject H0 | correct | **type II error**, probability β |

Mnemonics from the text:
- **RNV** (Rechazar Nula Verdadera) = type I.
- **NRNF** (No Rechazar Nula Falsa) = type II.

Triola's XSORT example (H1: $p > 0.5$):
- Type I: concluding the method works when it does nothing.
- Type II: concluding the method has no effect when it does work.

**Choosing the three quantities.** α, β and n are linked: fix two and the third follows. Triola's common practice is to pick α, then a practical n, which determines β. Use the largest α you can tolerate, and smaller α when a type I error is costly. Choose n from time and cost.

Trade-off at fixed n. Here is a quick check with $n = 14$, rejecting when $X \ge 13$:

```python
from scipy.stats import binom

alpha = binom.sf(12, 14, 0.5)     # P(X >= 13 | p = 0.5): type I error rate of this rule
beta = binom.cdf(12, 14, 0.6)     # P(X <= 12 | p = 0.6): type II error if the true p is 0.6
print(round(alpha, 4), round(beta, 3))   # 0.0009  0.992
```

The rule is very strict, so α is tiny and β is huge. Loosen the cutoff and β drops, but α rises.

## In ML

**Precision vs. recall** — moving a classifier threshold trades false positives (type I) against false negatives (type II). See [[conditional-probability]] for the precision/recall link.

**Peeking at A/B tests** — checking results repeatedly and stopping at the first significant result raises the real type I error above the nominal α.

## Exercises

**Basic** — A drug trial has H0: the drug has no effect. Describe a type I error and a type II error in plain words.

**Intermediate** — A fraud detector wrongly blocks 1% of legitimate transactions, and misses 20% of frauds. Which number is α, which is β, and what is the power against fraud?

**Advanced** — With n fixed, argue why α and β move in opposite directions when you change the rejection cutoff. What single change lowers both?
