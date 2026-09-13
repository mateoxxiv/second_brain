---
tags:
  - status/seed
  - ml
related:
  - "[[odds]]"
  - "[[bernoulli-distribution]]"
  - "[[supervised-learning-algorithms]]"
  - "[[linear-regression]]"
  - "[[gradient-descent]]"
  - "[[cross-entropy]]"
domain: ml
sources:
  - "James, Witten, Hastie & Tibshirani. An Introduction to Statistical Learning, Ch. 4."
  - "https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression"
---

> **TL;DR** — **Logistic regression** predicts a *probability* by fitting a straight line to the **[[odds|log-odds]]** and squashing it back to (0,1) with the sigmoid; despite the name it's a *classifier*, and its loss is exactly the [[bernoulli-distribution|Bernoulli]] likelihood.

---

## Intuition

You want to predict a probability — "how likely is this email to be spam?" — as a linear function of features. But a line runs off to ±∞, while a probability must stay in [0,1]. Linear regression can't respect that boundary. The fix is to *change what the line predicts*: not the probability directly, but the **[[odds|log-odds]]** (the logit), which legitimately lives on the whole real line. Fit a line there, then map back to a probability with the sigmoid. That single move — model the log-odds linearly — is all logistic regression is.

So the name is a historical trap: it's built on regression machinery (a linear combination inside), but the *output is a class probability*, which you threshold into a decision. It's a **classifier**.

## Mechanics

Model the log-odds as linear, then invert:

$$\ln\frac{p}{1-p} = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k \;=\; z
\qquad\Longrightarrow\qquad
p = \sigma(z) = \frac{1}{1+e^{-z}}$$

- The **[[odds|logit]]** $\ln\frac{p}{1-p}$ turns a bounded probability into an unbounded quantity a line can safely predict.
- The **sigmoid** $\sigma$ is its inverse, squashing $(-\infty,\infty)\to(0,1)$. At $z=0$, $p=0.5$ (odds 1:1) — the decision boundary.
- Each coefficient $\beta_j$ is a **log-odds-ratio**: $e^{\beta_j}$ is the multiplicative change in odds per unit of $x_j$.

**Loss.** With label $y\in\{0,1\}$ and prediction $p$, the negative log-likelihood of one [[bernoulli-distribution|Bernoulli]] observation is **binary [[cross-entropy]]**:

$$\mathcal{L} = -\big[\,y\log p + (1-y)\log(1-p)\,\big]$$

This isn't a design choice — it *falls out* of maximizing the Bernoulli likelihood. There's no closed-form solution (unlike [[linear-regression]]), so coefficients are fit by [[gradient-descent]].

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(X, y)   # y in {0,1}
clf.predict_proba(X_new)[:, 1]          # P(class 1) — the sigmoid output
```

## In ML

**The workhorse baseline for classification.** Fast, interpretable (coefficients = log-odds-ratios), and calibrated (outputs are real probabilities, not just scores). Reach for trees/nets only when it underfits — see [[supervised-learning-algorithms]].

**The building block of neural nets.** A single sigmoid neuron with cross-entropy loss *is* logistic regression. Stack and add hidden layers and you get a deep classifier; the final layer of a binary net is still exactly this.

## Exercises

**Basic** — A model gives $z = \beta_0+\beta_1 x = -1 + 0.5x$. Compute $p$ at $x=2$ and $x=4$. At what $x$ is the decision boundary ($p=0.5$)?

**Intermediate** — A coefficient is $\beta_j = 0.7$. By what factor do the odds of the positive class change per unit increase in $x_j$? (Hint: $e^{0.7}$.) Why is this stated in *odds*, not probability?

**Advanced** — Show that maximizing the [[bernoulli-distribution|Bernoulli]] log-likelihood over a dataset is equivalent to minimizing mean binary cross-entropy. Then explain why squared error is a poor loss for this model (hint: non-convexity in the parameters, weak gradients when $p$ is confidently wrong).
