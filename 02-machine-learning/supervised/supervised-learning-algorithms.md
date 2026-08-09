---
tags:
  - status/seed
  - ml
related:
  - "[[supervised-learning]]"
  - "[[types-of-machine-learning]]"
  - "[[linear-regression]]"
  - "[[decision-trees]]"
  - "[[bias-variance-tradeoff]]"
domain: ml
sources:
  - "https://scikit-learn.org/stable/supervised_learning.html"
  - "https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares"
  - "James, Witten, Hastie & Tibshirani. An Introduction to Statistical Learning (theory)"
  - "[[platzi-fundamentos-machine-learning]] — Class 2 (practical companion)"
---

> **TL;DR** — There is no single best supervised algorithm; you choose based on *what you predict* (number vs. category) and *how complex the pattern is*, trading interpretability against flexibility.

---

## Intuition

Given labeled data ([[supervised-learning]]), many algorithms can learn the mapping — but they differ in the *shape of relationship* they can capture and how *readable* their logic is. Picking one is like a coach choosing a tactic: a simple, clear play (linear model) when the situation is straightforward; a complex, powerful scheme (neural net) when the game is tangled but you have the resources. The guiding law is the **No Free Lunch theorem**: no model is best on *all* problems, so the skill is matching the model to the problem, not memorizing one favorite.

Two axes organize the whole choice:
- **What is the label?** continuous number → *regression*; category → *classification*.
- **How complex & how much data?** simple/linear + little data → simple models; nonlinear + lots of data → flexible models.

## Mechanics

| Algorithm | Predicts | Use when | Main weakness | Note |
|-----------|----------|----------|---------------|------|
| **Linear regression** | continuous number | relationship is roughly linear, few features | misses nonlinearity | [[linear-regression]] |
| **Logistic regression** | class probability (0–1) | binary/multi-class with ~linear boundary | linear boundary only | [[logistic-regression]] |
| **Decision tree** | number or class | you need clear, explainable `if/then` rules | overfits easily | [[decision-trees]] |
| **Random forest** | number or class | one tree underfits/overfits; want accuracy | less interpretable, slower | [[random-forests]] |
| **SVM** | class (or number) | clear margin between classes, medium data | poor on huge/noisy data, tuning | [[support-vector-machines]] |
| **Neural network** | number or class | nonlinear patterns, lots of data + compute | data/compute hungry, opaque | [[neural-networks]] |

**Two clarifications the names hide:**
- **Logistic regression is *classification*, not regression** — despite the name, it outputs a *probability* of class membership (e.g. 80% win), then thresholds it. The "regression" refers to the linear combination inside, not the output type.
- **Random forest is an [[ensemble-methods|ensemble]]** — it grows many decorrelated trees and lets them *vote*, which averages away the overfitting of a single tree (bagging). This is the [[bias-variance-tradeoff|variance-reduction]] idea in action.

**The selection heuristic (from simple → complex):**
1. Continuous target, direct relationship → **linear regression**.
2. Two categories → **logistic regression**.
3. Need explainable rules → **decision tree**.
4. Tree not accurate enough → **random forest**.
5. Well-separated classes, moderate data → **SVM**.
6. Nonlinear, big data, compute available → **neural network**.

Cross-cutting rule that no algorithm forgives: **quality labeled data beats a fancier model.** Garbage labels sink any of these.

```python
# same labeled (X, y); swapping the model is a one-line change
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
reg = LinearRegression().fit(X, goals)          # predict a number
clf = LogisticRegression().fit(X, won)          # predict P(win)
rf  = RandomForestClassifier().fit(X, won)      # ensemble of voting trees
```

## In ML

**Start simple, add complexity only if needed** — a linear/logistic baseline is fast, interpretable, and often "good enough"; reach for random forests or nets only when the baseline underfits. Jumping straight to a neural network on small tabular data usually *loses* to a tree ensemble.

**Interpretability vs. accuracy is a real tradeoff** — trees and linear models explain *why* they predicted; forests and nets predict better but are harder to justify. In regulated domains (credit, medicine) the explainable model may win despite lower accuracy.

**Tabular data still favors tree ensembles** — for structured/tabular problems like the Cebollitas match data, gradient-boosted trees and random forests routinely beat neural nets, which shine mainly on unstructured data (images, text, audio).

## Exercises

**Basic** — Match each task to a first-choice algorithm: (a) predict continuous goals from shots; (b) predict win/lose with a clear class margin; (c) need a rule a coach can read aloud.

**Intermediate** — Explain why logistic regression is classified as a *classification* method even though "regression" is in its name. What does it actually output, and how does that become a class?

**Advanced** — Using the No Free Lunch idea and the [[bias-variance-tradeoff]], argue when a single decision tree would *beat* a random forest, and when it would lose badly.
