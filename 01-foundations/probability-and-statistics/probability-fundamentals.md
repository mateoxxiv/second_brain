**Related**: [[derivatives-and-partial-derivatives]]
**Tags**: #status/growing

## Core Idea

Probability measures **how likely** something is, on a scale from 0 (impossible)
to 1 (certain). In ML, everything is uncertain — predictions, data, parameters.
Probability gives you the language to reason about that uncertainty.

## Details

### Basic Probability

```
P(A) = favorable outcomes / total outcomes
```

```
P = 0    → impossible
P = 0.5  → equally likely either way
P = 1    → certain
```

### Three Rules

**Complement** — probability of NOT A:

```
P(not A) = 1 - P(A)
```

**OR (union)** — probability of A or B:

```
P(A or B) = P(A) + P(B) - P(A and B)
```

Subtract the overlap to avoid double-counting. If A and B can't happen
together (mutually exclusive), the overlap is 0.

**AND (joint)** — probability of both A and B:

```
P(A and B) = P(A) * P(B|A)
```

If A and B are independent: P(A and B) = P(A) * P(B).

### Worked Example

200 employees:

```
Engineering (100):  70 above $5000,  30 below
Sales (100):        20 above $5000,  80 below
```

```
P(above 5000) = 90/200 = 0.45
P(below 5000) = 110/200 = 0.55
P(engineering) = 100/200 = 0.5
P(below 5000 OR above 10000) = P(below) + P(above) - 0  (no overlap)
```

### Conditional Probability — P(A|B)

Probability of A **given that** B happened. Knowing B changes the picture.

```
P(A|B) = P(A and B) / P(B)
```

```
P(above 5000 | engineering) = 70/100 = 0.70
P(above 5000 | sales) = 20/100 = 0.20
P(above 5000 | overall) = 90/200 = 0.45
```

The department completely changes the prediction. This is why **features
matter** in ML — they're the conditions that shift probabilities.

### Bayes' Theorem

Flips the conditional around. The most important formula in ML.

```
P(A|B) = P(B|A) * P(A) / P(B)
```

### Conditional vs Bayes — What's the Difference?

They answer **opposite** questions:

```
Conditional:  I KNOW the group   → what's P(outcome)?
Bayes:        I KNOW the outcome → what's P(group)?
```

```
Conditional:  "This person is in engineering. P(above 5k)?"
              → Easy. Look at engineering, count: 70/100 = 0.70

Bayes:        "This person earns above 5k. P(engineering)?"
              → Harder. Need info from ALL groups to figure out.
```

In ML:
- You CAN compute P(data | class) — just count things in each group (easy)
- You WANT P(class | data) — this is prediction (hard)
- Bayes flips easy → hard

```
EASY direction:   P(data | class)    ← count things in each group
HARD direction:   P(class | data)    ← this is prediction!
Bayes:            turns easy into hard
```

### Bayes Worked Example

```
Observe: employee earns above $5000
Want:    probability they're in engineering

P(eng | above5k) = P(above5k | eng) * P(eng) / P(above5k)
                 = 0.70 * 0.5 / 0.45
                 = 0.778
```

**In ML terms:**

```
P(class | data) = P(data | class) * P(class) / P(data)
  posterior        likelihood        prior      evidence
```

- **Prior** P(class) — what you believed before seeing data
- **Likelihood** P(data|class) — how well the data fits each class
- **Posterior** P(class|data) — updated belief after seeing data
- **Evidence** P(data) — normalizing constant

This is how Naive Bayes classifiers work: compute P(spam|text) using
P(text|spam) * P(spam) / P(text).

### Independence

Two events are independent when knowing one doesn't change the other:

```
Independent:     P(A|B) = P(A)       ← B is irrelevant
Not independent: P(A|B) ≠ P(A)       ← B changes things
```

When independent, the AND rule simplifies:

```
P(A and B) = P(A) * P(B)
```

**ML connections:**
- **Naive Bayes** assumes features are independent (the "naive" assumption)
- **Feature correlation** = features are NOT independent
- **i.i.d.** = training samples are Independent and Identically Distributed
  (common assumption in ML)

### Summary Table

| Concept | Formula | When to use |
|---------|---------|-------------|
| Complement | P(not A) = 1 - P(A) | "What's the chance it DOESN'T happen?" |
| Union (OR) | P(A or B) = P(A) + P(B) - P(A and B) | "Either this or that" |
| Joint (AND) | P(A and B) = P(A) * P(B\|A) | "Both this and that" |
| Conditional | P(A\|B) = P(A and B) / P(B) | "Given B happened, what about A?" |
| Bayes | P(A\|B) = P(B\|A)*P(A)/P(B) | "Flip the condition around" |
| Independence | P(A and B) = P(A)*P(B) | "They don't affect each other" |

## Code Example

```python
import numpy as np

# Employee data
eng_above = 70
eng_below = 30
sales_above = 20
sales_below = 80
total = 200

# Basic probability
p_above = (eng_above + sales_above) / total       # 0.45
p_eng = (eng_above + eng_below) / total            # 0.5

# Conditional
p_above_given_eng = eng_above / (eng_above + eng_below)    # 0.70
p_above_given_sales = sales_above / (sales_above + sales_below)  # 0.20

# Bayes: P(eng | above 5000)
p_eng_given_above = (p_above_given_eng * p_eng) / p_above  # 0.778

print(f"P(above 5k) = {p_above}")
print(f"P(above 5k | eng) = {p_above_given_eng}")
print(f"P(above 5k | sales) = {p_above_given_sales}")
print(f"P(eng | above 5k) = {p_eng_given_above:.3f}")

# Independence check
print(f"\nIndependent? P(above|eng)={p_above_given_eng} vs P(above)={p_above}")
print(f"Not equal → NOT independent (department affects salary)")
```

## Connections

- Forward link: probability distributions — Normal, Bernoulli, Poisson
- Forward link: expectation and variance — summarizing distributions
- Forward link: MLE — finding best parameters using likelihood
- Forward link: Naive Bayes — classifier built directly on Bayes' theorem
- Forward link: cross-entropy loss — comes from information theory + probability

## Sources

- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — practical ML statistics
- [3Blue1Brown — Bayes' Theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM) — best visual explanation
- [Khan Academy — Probability](https://www.khanacademy.org/math/statistics-probability) — interactive exercises
- [Think Stats — Allen Downey](https://greenteapress.com/thinkstats2/) — computational approach to probability
- [Mathematics for Machine Learning — Chapter 6](https://mml-book.github.io/book/mml-book.pdf)
