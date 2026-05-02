---
tags:
  - status/growing
  - probability
related:
  - "[[probability-distributions]]"
domain: probability
sources:
  - "https://www.packtpub.com/"
  - "https://www.youtube.com/watch?v=HZGCoVF3YvM"
  - "https://www.khanacademy.org/math/statistics-probability"
  - "https://greenteapress.com/thinkstats2/"
  - "https://mml-book.github.io/book/mml-book.pdf"
---

> **TL;DR** — Probability measures likelihood on [0,1]. Three rules: complement, OR, AND. Conditional P(A|B) = P(A and B)/P(B). Bayes flips the condition.

---

## Intuition

Probability answers: "how likely is this to happen?" on a scale from 0 (impossible) to 1 (certain). In ML, everything is uncertain — predictions, data, parameters — and probability is the language for reasoning about that uncertainty.

Bayes' theorem is the most important formula: it flips the question. You can easily measure P(data | class) by counting. What you want is P(class | data). Bayes converts easy into hard.

## Mechanics

**Three rules:**

| Rule | Formula |
|------|---------|
| Complement | P(not A) = 1 − P(A) |
| OR | P(A or B) = P(A) + P(B) − P(A and B) |
| AND | P(A and B) = P(A) · P(A\|B) |

**Conditional probability:** P(A|B) = P(A and B) / P(B)

**Bayes' theorem:** P(A|B) = P(B|A) · P(A) / P(B)

**Law of total probability:** P(A) = Σᵢ P(A|Bᵢ) · P(Bᵢ)

**Worked example** — 200 employees: 100 engineering (70 above $5k), 100 sales (20 above $5k):
```
P(above 5k | eng)   = 70/100 = 0.70
P(eng | above 5k)   = 0.70 × 0.5 / 0.45 = 0.778  ← Bayes
```

```python
p_above_given_eng   = 70 / 100        # 0.70
p_eng               = 100 / 200       # 0.50
p_above             = 90 / 200        # 0.45  (law of total probability)
p_eng_given_above   = (p_above_given_eng * p_eng) / p_above
print(f"P(eng | above 5k) = {p_eng_given_above:.3f}")  # 0.778
```

> Runnable: [[code/foundations/probability_fundamentals.py]]

## In ML

**Bayes flips easy → hard.** P(data | class) is easy to compute by counting in each class. P(class | data) is what you need for prediction. Bayes converts one into the other: P(class|data) = P(data|class) · P(class) / P(data).

**Naive Bayes assumes independence.** The "naive" assumption is P(feature1 and feature2 | class) = P(feature1|class) · P(feature2|class). This is almost never true in reality (words in a sentence are correlated), but the classifier works well despite it.

**i.i.d. assumption.** Training samples are assumed Independent and Identically Distributed. This is the foundation of most ML theory — it allows treating each sample as a fresh draw from the same distribution.

## Exercises

**Basic** — Compute P(sales | above 5k) using Bayes' theorem with the employee example above. Verify it equals 1 − P(eng | above 5k).

**Intermediate** — Verify the law of total probability for P(above 5k) using the engineering and sales conditional probabilities.

**Advanced** — Explain why the Naive Bayes independence assumption is "naive" in practice. Give a concrete NLP example where the assumption badly fails, yet the classifier still works.
