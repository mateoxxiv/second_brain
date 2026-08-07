---
tags:
  - status/seed
  - probability
related:
  - "[[population-and-sample]]"
  - "[[principles-of-statistical-thinking]]"
  - "[[probability-distributions]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 1, §1-3."
---

> **TL;DR** — Before you compute anything, classify the data: whether it counts/measures or just labels, and *what kind of arithmetic its scale actually supports* — because that, not the numbers themselves, decides which statistical methods are valid.

---

## Intuition

A number on a page tells you nothing about what you're allowed to do with it. The `23` on a basketball jersey and the `23` years of a survey respondent look identical, but averaging the first is nonsense and averaging the second is routine. The whole point of classifying data is to stop yourself from running an operation the data can't support — like the NASA Mars Climate Orbiter that crashed because one team's numbers were in pounds-force and another's in newtons.

So ask two questions of any dataset: **do these values measure/count something, or are they just labels?** And if numeric, **how much structure does the scale really have** — order? meaningful gaps? a true zero? Each "yes" unlocks more arithmetic.

## Mechanics

**First split — what the values *are*:**

| Type | Definition | Example |
|---|---|---|
| Categorical (qualitative) | Names, labels, categories — no arithmetic meaning | Eye color; party affiliation; jersey numbers |
| Quantitative (numerical) | Numbers that genuinely count or measure | Ages in years; heights in cm |

**Quantitative splits further — how many values are possible:**

| Type | Definition | Example |
|---|---|---|
| Discrete | Countable set of values (0, 1, 2, …), possibly finite | Number of eggs a hen lays |
| Continuous | Infinitely many values over a range, no gaps | Litres of milk a cow produces (5678.1234 is fine) |

**The four levels of measurement** — a ladder where each rung adds one capability:

| Level | Ordered? | Meaningful differences? | True zero (ratios)? | Example |
|---|---|---|---|---|
| Nominal | ✗ | ✗ | ✗ | Eye color, yes/no/undecided |
| Ordinal | ✓ | ✗ | ✗ | Course grades A–F; university rankings |
| Interval | ✓ | ✓ | ✗ | Temperature °F/°C; calendar years |
| Ratio | ✓ | ✓ | ✓ | Distance, price, weight |

**The "twice" test for ratio** (Triola's shortcut): pick two values where one is double the other and ask if *"twice as much"* is literally true. 400 km really is twice 200 km → ratio. But 50 °F is **not** twice as hot as 25 °F (the zero is arbitrary, not "no heat") → only interval.

```python
# Why level matters: the same numbers, a valid vs. a meaningless operation
grades   = [4, 3, 3, 2]          # A,B,B,C coded as numbers -> ordinal
distances = [200, 400, 100]      # km -> ratio

sum(distances) / len(distances)  # 233.3 km -- meaningful average
sum(grades) / len(grades)        # 3.0 -- a GPA: common, but technically abusing ordinal data
```

## In ML

**Feature encoding is a levels-of-measurement decision** — nominal features need one-hot encoding (no false order imposed); ordinal features can be integer-encoded because their order is real. Silently label-encoding a nominal column injects a fake ordering a model will happily, wrongly, exploit. See [[population-and-sample]] for the data-collection half of getting features right.

**The task type follows the data type** — a categorical target means classification; a quantitative target means regression. Discrete counts often call for count models (Poisson-style), while continuous targets suit ordinary regression — the [[probability-distributions]] you reach for are dictated by this classification.

**Metrics must respect the level** — averaging star ratings (ordinal) or reporting a "mean survey category" repeats exactly the mistake of computing an average of jersey numbers: an operation the scale doesn't license.

## Exercises

**Basic** — Classify each: (a) ZIP codes, (b) number of siblings, (c) restaurant star ratings 1–5, (d) body temperature in °C, (e) reaction time in ms. Give the data type *and* the level of measurement for each.

**Intermediate** — A survey codes political party as 1 = Democrat, 2 = Republican, 3 = Independent and reports a "mean party of 1.8." Explain precisely what level this data is and why that statistic is meaningless — then name the one arithmetic property the scale is missing.

**Advanced** — Temperature in °C is interval, but temperature in **kelvin** is ratio. Explain what changes between the two scales, apply the "twice" test to 200 K vs. 400 K, and state the general rule for when a shift of origin turns an interval variable into a ratio one.
