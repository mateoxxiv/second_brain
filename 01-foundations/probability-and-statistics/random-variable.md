---
tags:
  - status/seed
  - probability
related:
  - "[[discrete-probability-distribution]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[sample-space-and-events]]"
  - "[[probability-distributions]]"
domain: probability
sources:
  - "Triola, Estadística 11e, §5-2 (Variables aleatorias)"
---

> **TL;DR** — A random variable is a rule (usually called $x$) that pins a single number to each outcome of a random procedure; whether that number is *counted* or *measured* makes it discrete or continuous.

---

## Intuition

A random procedure spits out outcomes — a coin lands, a cow gives milk, five pea plants grow. A **random variable** is the translator that turns each messy outcome into *one number*. It's the bridge from the [[sample-space-and-events|sample space]] (the raw events) to the number line (where math can happen).

The word "random" doesn't mean the *rule* is random — the rule is fixed. What's random is which outcome occurs, and therefore which number you get. Same distinction as [[data-types-and-levels-of-measurement|discrete vs. continuous data]], now lifted from *observed data* to the *variable itself*: if you get the number by **counting**, it's discrete; if you get it by **measuring** on a continuous scale, it's continuous.

## Mechanics

**Definition.** A random variable $X$ (values written $x$) assigns exactly one real number to each outcome of a procedure, determined by chance.

| Type | Values | How you get them | Example |
|------|--------|------------------|---------|
| **Discrete** | Finite or *countable* (0, 1, 2, …), possibly infinite but listable | **Counting** | # of eggs a hen lays; # of students in class |
| **Continuous** | Infinitely many, on an unbroken scale — no gaps | **Measuring** | liters of milk per day; battery voltage $\in[0,9]$ |

"Countable" is the subtle part: a discrete variable *can* have infinitely many values (0, 1, 2, … forever), as long as they can be put in a counting list. Continuous variables can't — between any two values there's always another (4.123456 L is allowed).

```python
# Discrete: outcomes map to integer counts you can enumerate
green_pods = [0, 1, 2, 3, 4, 5]          # countable — a list
# Continuous: any real value in a range; enumeration is impossible
voltage = "any x in [0.0, 9.0]"           # measured, not counted
```

This chapter (Triola Ch. 5) is *only* discrete; continuous variables wait for the [[normal-distribution|normal]] and other continuous distributions.

## In ML

**Every feature and label is a random variable.** A column in a dataset is a realization of a random variable. Knowing discrete vs. continuous decides everything downstream: a discrete target → classification (cross-entropy, [[binomial-distribution|Bernoulli/Binomial]] likelihood); a continuous target → regression (MSE, [[normal-distribution|Gaussian]] likelihood). Mislabeling the type is a modeling bug, not a cosmetic one.

**Discreteness controls the math.** Discrete variables use sums ($\sum$) over their [[discrete-probability-distribution|probability distribution]]; continuous ones use integrals over a density. The whole `PMF vs. PDF` split — and why you can never ask $P(X = 3.14)$ for a continuous variable — traces straight back to this definition.

## Exercises

**Basic** — Classify each as discrete or continuous: (a) number of emails you get today, (b) your exact reaction time in ms, (c) shoe size (US), (d) rainfall in mm tomorrow.

**Intermediate** — "Number of coin flips until the first head" can be 1, 2, 3, … with no upper bound. Is it discrete or continuous? Justify using the *countable* criterion.

**Advanced** — Temperature is continuous, but a thermometer reports it to 0.1°. Is the *reported* value a discrete or continuous random variable? What does this say about the difference between a quantity and its measurement?
