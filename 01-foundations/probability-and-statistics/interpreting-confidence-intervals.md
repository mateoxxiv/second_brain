---
tags:
  - status/seed
  - probability
related:
  - "[[confidence-interval]]"
  - "[[point-estimate]]"
  - "[[sampling-distribution]]"
  - "[[statistical-significance]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §7-2 (Interpretación de un intervalo de confianza; Figura 7-1; Advertencia)"
---

> **TL;DR** — The 95% belongs to the method: across many samples, 95% of the intervals built this way contain the fixed parameter p. It is not the probability that p lies in one particular interval.

---

## Intuition

The population value p is fixed, like a baby whose sex is already determined. It is not random, so it can't have a 95% probability of being in a range. The interval is the random part, because it depends on the sample. So the 95% describes how often the procedure catches p, and the question "is p in this interval?" has a yes-or-no answer, with no probability attached.

## Mechanics

**Correct:** "We are 95% confident that the interval 0.677 to 0.723 contains the true proportion p." Unpacked, this means: if we repeated the sampling many times and built an interval each time, about 95% of those intervals would contain p.

**Incorrect:**

| Claim | Why it's wrong |
|-------|----------------|
| "There is a 95% probability that p is between 0.677 and 0.723." | p is fixed; the interval is what's random. |
| "95% of sample proportions fall between 0.677 and 0.723." | The interval is about p, not about the spread of p̂. Most p̂ values sit near 0.70 with SD ≈ 0.012, so they are much more concentrated. |

**Coverage simulation.** The 95% is a long-run rate, which we can check by simulating the procedure:

```python
import numpy as np
rng = np.random.default_rng(1)
p, n, z = 0.75, 1501, 1.96
hits = 0
for _ in range(10_000):
    p_hat = rng.binomial(n, p) / n
    E = z * np.sqrt(p_hat * (1 - p_hat) / n)
    hits += (p_hat - E <= p <= p_hat + E)
print(hits / 10_000)   # ≈ 0.95
```

Some of the 10,000 intervals miss p = 0.75, and that's expected. Triola's Figure 7-1 shows the same thing with 20 samples: 19 intervals contain p, and one misses it.

**Confidence level = success rate of the procedure.** Triola's phrase for 1 − α is "la tasa de éxitos del procedimiento." A 95% level means a 5% failure rate, which is why α is called the error rate.

## In ML

**Reporting an interval for a metric.** "Accuracy is 0.92, 95% CI [0.90, 0.94]" means the procedure of building this interval captures the true accuracy 95% of the time. It does not mean the true accuracy has a 95% chance of being in that range.

**Overlap is not a test.** Triola warns that overlapping intervals shouldn't be used to decide whether two proportions are equal. The same caution applies to comparing model metrics by eye.

**Miscalibrated intervals.** If a reported interval misses the truth far more often than its stated level (say, 50% of the time for a 95% claim), the method is wrong, even if each interval looks reasonable.

## Exercises

**Basic** — Label each statement correct or incorrect: (a) "95% of the sample proportions are in the interval." (b) "The method captures p in 95% of repeated samples." (c) "The probability that p is in the interval is 0.95."

**Intermediate** — Suppose the true p = 0.75. Does the interval 0.677 to 0.723 contain p? Does that contradict the 95% claim? Explain why not.

**Advanced** — Change z to 2.575 in the simulation. What coverage do you expect, and why does the width matter? Explain why the procedure, not the interval, carries the probability.
