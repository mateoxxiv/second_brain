---
tags:
  - status/seed
  - ml
related:
  - "[[types-of-machine-learning]]"
  - "[[unsupervised-learning]]"
  - "[[linear-regression]]"
  - "[[train-test-split]]"
  - "[[data-types-and-levels-of-measurement]]"
domain: ml
sources:
  - "James, Witten, Hastie & Tibshirani. An Introduction to Statistical Learning. Ch. 2 (theory)"
  - "Platzi — Curso de Fundamentos de Machine Learning, Class 2 (practical companion)"
---

> **TL;DR** — Supervised learning fits a function **f: X → y** from labeled example pairs, so that it predicts the label **y** for unseen inputs **X** — its whole premise is that a *teacher* provided the right answers to learn from.

---

## Intuition

You learn a language faster with a tutor correcting every sentence than by guessing alone. Supervised learning is the tutored case: for every training example you have both the **question (X)** and the **correct answer (y)**, and the algorithm's job is to discover the rule connecting them so it can answer *new* questions.

Shown enough Cebollitas matches labeled *won* or *lost* — each with features like possession, shots, rest days — the model learns which patterns separate wins from losses, then predicts the next match. The label is the "supervision." No labels, no supervision — that's a different paradigm ([[unsupervised-learning]]). Supervised learning is the workhorse of ML precisely because "predict a known target" is the most common business question.

## Mechanics

**Setup.** Given training pairs $(x_i, y_i)$ for $i = 1..n$, assume some true relationship $y = f(x) + \varepsilon$ (with irreducible noise $\varepsilon$). Learn an estimate $\hat{f}$ that minimizes a **loss** measuring the gap between predictions $\hat{f}(x)$ and true $y$.

**Two families, split by the label's type** (this is where [[data-types-and-levels-of-measurement]] decides the method):

| Task | Label y | Example | Typical loss |
|------|---------|---------|--------------|
| **Regression** | continuous | goals scored (2.7) | squared error (MSE) |
| **Classification** | categorical | win / lose | cross-entropy / 0-1 loss |

**The learning loop:** (1) pick a model family $\hat{f}_\theta$ (linear, tree, net); (2) define a loss $L(\theta)$; (3) find parameters $\theta$ that minimize average loss on the training data; (4) **evaluate on held-out data** to estimate generalization — this is why you need a [[train-test-split]]. Fitting the training data perfectly while failing on new data is **overfitting**: the model memorized noise instead of learning $f$.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# X = match features, y = goals scored (a labeled target -> supervised)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression().fit(X_tr, y_tr)   # learn f from labeled pairs
preds = model.predict(X_te)                  # predict y for unseen X
print(model.score(X_te, y_te))               # R^2 on held-out data
```

## In ML

**Generalization, not memorization, is the goal** — a supervised model is judged only on data it never saw in training. The central obstacle is the [[bias-variance-tradeoff|bias–variance tradeoff]]: too simple a model underfits (high bias), too flexible overfits (high variance). Everything — regularization, cross-validation, early stopping — exists to manage this.

**Labels are the expensive bottleneck** — supervised learning's power depends on labeled data, and labeling is often costly or slow (human annotation, waiting for outcomes). This constraint motivates semi-supervised learning, active learning, and the *self-supervised* pretraining behind modern LLMs (labels manufactured from the data itself).

**It underlies most deployed ML** — spam detection, credit scoring, medical diagnosis, recommendation ranking, and the Cebollitas match predictor are all supervised. The dominant workflow (features → labeled split → fit → evaluate) is the backbone of the practical ML pipeline.

## Exercises

**Basic** — For each, state whether it's regression or classification: (a) predict tomorrow's temperature; (b) predict whether an email is spam; (c) predict a player's minutes played next match.

**Intermediate** — You fit a model that scores 99% accuracy on training data but 62% on the test set. Name what's happening, explain *why* the two numbers diverge, and give one concrete fix.

**Advanced** — Explain why minimizing training loss is *not* the true objective of supervised learning, and formalize what we actually want to minimize (hint: expected loss over the true data distribution — the "generalization error").
