---
tags:
  - status/seed
  - probability
related:
  - "[[principles-of-statistical-thinking]]"
  - "[[binomial-distribution]]"
  - "[[probability-fundamentals]]"
  - "[[population-and-sample]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[law-of-large-numbers]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-2, Ejemplos 6-8."
---

> **TL;DR** — A result is statistically significant when it's too unlikely to have happened by pure chance under a "no real effect" assumption — but statistically significant is not the same as practically significant.

---

## Intuition

Suppose a fertility technique is followed by 13 girls out of 14 births. Two explanations compete: pure chance, or the technique actually works. Statistical significance formalizes the question "how surprising would this outcome be if chance alone were responsible?" If the answer is *very* surprising, chance stops being a convincing explanation. If it's not that surprising, chance stays fully plausible — and the result tells you nothing.

## Mechanics

**Definition** — a result is statistically significant when its probability of occurring, *assuming the treatment or method has no real effect*, is low enough that "pure chance" is no longer a convincing explanation. This is Triola's **rare-event rule** — the same "how likely under no effect?" reasoning that a small probability ([[three-methods-of-assigning-probability|estimated by relative frequency or the classical method]]) flags as *unusual*.

**Worked contrast — the MicroSort gender-selection technique**, tested on 14 births, assuming a fair 50/50 chance per birth if the technique does nothing:

| Example | Observed result | P(result \| technique has no effect) | Significant? | Conclusion |
|---|---|---|---|---|
| 7 | 13 girls of 14 | ≈ 1 in 1000 | Yes | Chance is an unconvincing explanation — technique likely works |
| 8 | 8 girls of 14 | ≈ 2 in 5 | No | Easily happens by chance alone — can't conclude the technique works |

Both results exceed the "expected" 7 of 14, but only the first is rare enough to move the needle — the second is well within what chance alone regularly produces.

```python
from scipy.stats import binom

n, p = 14, 0.5   # 14 births, "no effect" = fair 50/50 chance of a girl each time

p_13_or_more = 1 - binom.cdf(12, n, p)   # P(X >= 13)
p_8_or_more  = 1 - binom.cdf(7, n, p)    # P(X >= 8)

print(f"{p_13_or_more:.4f}")   # ~0.0009 -- matches the book's "1 in 1000"
print(f"{p_8_or_more:.4f}")    # ~0.395  -- matches the book's "2 in 5"
```

**Statistical significance ≠ practical significance** — a result can be statistically significant while being practically worthless. In an Atkins-diet trial, 40 subjects lost an average of 2.1 lb over a year — a real, statistically significant effect (not due to chance). But common sense says nobody starting a weight-loss program wants just 2.1 lb: the effect is real yet too small to matter. Statistically significant means *probably a real effect*; practically significant means *an effect large enough to act on* — a result can have either without the other.

## In ML

**This is p-value reasoning before the formal name** — "how likely is this result if there's really no effect?" is exactly what a p-value quantifies. This note is the intuitive seed for the formal hypothesis-testing machinery — flagged as the study roadmap's next T3 priority.

**Statistically significant but practically useless lifts** — an A/B test can find a real, statistically significant +0.01% click-through-rate improvement on 10 million users that's still too small to justify shipping. This is the Atkins-diet trap in production ML experimentation.

**Effect size, not p-value alone, drives decisions** — reporting only "p < 0.05" without the size of the effect is a widely recognized reporting failure, for precisely the reason the Atkins example demonstrates: significance answers "is this real?", not "does this matter?".

## Exercises

**Basic** — A coach claims a "lucky coin" wins more overtime tosses. In 14 tosses it comes up heads 13 times. Using the MicroSort reasoning (and table above), is this statistically significant? What would you conclude, and why?

**Intermediate** — Extend the code above to n = 20 births. If a technique produces 16 girls out of 20, is that more or less surprising, in probability terms, than 13 out of 14? Compute both probabilities and compare.

**Advanced** — A recommender algorithm increases average session length by 4 seconds, statistically significant at p < 0.001 across 10 million users. Argue both sides of whether this is practically significant, and specify exactly what additional information (beyond significance) you'd need to decide whether to ship it.
