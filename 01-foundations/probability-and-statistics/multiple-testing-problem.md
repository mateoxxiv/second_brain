---
tags:
  - status/seed
  - probability
related:
  - "[[p-value]]"
  - "[[addition-rule]]"
  - "[[one-tailed-vs-two-tailed-tests]]"
  - "[[statistical-significance]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §8-2 (Detectores de mentiras y leyes; Recuadro: La aspirina no es útil para las personas de los signos Géminis y Libra)"
---

> **TL;DR** — Run enough tests and some will look significant by chance. With 12 independent tests at α = 0.05, the chance of at least one false positive is about 46%.

---

## Intuition

Triola's aspirin example: a researcher split heart-attack patients into 12 zodiac groups and found aspirin "useless" for two of them. With enough groups, some will look different purely by luck. Each subgroup test has a 5% false-alarm rate, and the false alarms add up.

## Mechanics

For $m$ independent tests, each at level α:

$$P(\text{at least one false positive}) = 1 - (1-\alpha)^m$$

With $m = 12$ and α = 0.05: $1 - 0.95^{12} \approx 0.46$.

The union bound from [[addition-rule]] gives a quick upper bound that does not need independence: $P(\text{at least one}) \le m\alpha$.

A common fix is the Bonferroni correction: test each hypothesis at $\alpha / m$. Triola's §8-2 states the problem only. The correction below is an outside addition, not from the book.

```python
alpha, m = 0.05, 12
print(round(1 - (1 - alpha) ** m, 3))   # P(at least one false positive): 0.46
print(round(alpha / m, 4))              # Bonferroni per-test level: 0.0042
```

## In ML

**Hyperparameter search** — trying 200 configurations and reporting the best validation score overstates performance. The winner is partly luck. Keep a held-out test set that the search never sees.

**Many A/B metrics** — checking 20 metrics at α = 0.05, one will often look significant by chance. Pre-register a primary metric or correct for the family of tests.

## Exercises

**Basic** — Five independent tests, each at α = 0.05. What is the probability of at least one false positive?

**Intermediate** — How many independent tests at α = 0.05 are needed before the chance of at least one false positive exceeds 0.5?

**Advanced** — Bonferroni controls the family error rate but lowers power for each test. Connect this to [[statistical-power]]: which quantity does the correction shrink, and what does that cost?
