---
tags:
  - status/seed
  - ml
related:
  - "[[supervised-learning]]"
  - "[[unsupervised-learning]]"
  - "[[reinforcement-learning]]"
  - "[[data-types-and-levels-of-measurement]]"
domain: ml
sources:
  - "Platzi — Curso de Fundamentos de Machine Learning, Class 1 (practical companion)"
  - "Goodfellow, Bengio & Courville. Deep Learning. Ch. 5 (theory)"
  - "https://scikit-learn.org/stable/"
---

> **TL;DR** — The three ML paradigms are distinguished by *what feedback signal the data carries*: **supervised** learns from labeled input→output pairs, **unsupervised** finds structure in unlabeled data, and **reinforcement** learns from delayed reward through trial and error.

---

## Intuition

The whole taxonomy comes down to **one question: what does the learner get told about whether it's right?**

- **Supervised** — a teacher gives the answer for every example. You're shown matches Cebollitas *won* and *lost* (labels) and learn what separates them. Feedback is *immediate and exact*.
- **Unsupervised** — no teacher, no answers. You get a pile of data and must find patterns yourself: which players train at similar rhythms, which cluster tends to get injured. Feedback is *nonexistent* — success is structure you discover.
- **Reinforcement** — no answer given, only a *reward* after acting. A match simulator tries strategies and gets points when it wins, improving over many tries. Feedback is *delayed and evaluative* (good/bad, not "here's the right move").

So the axis is the **richness and timing of the feedback signal**: full answers (supervised) → no answers (unsupervised) → scalar rewards after action (reinforcement). Picking the wrong paradigm means answering the wrong question about your problem.

## Mechanics

Each paradigm is defined by the *form of the training data*:

| Paradigm | Data available | Goal | Learns |
|----------|---------------|------|--------|
| **Supervised** | features **X** + labels **y** (pairs) | predict y for new X | a mapping f: X → y |
| **Unsupervised** | features **X** only (no y) | find structure | groups / low-dim representation / density |
| **Reinforcement** | states, actions, **rewards** (from an environment) | maximize cumulative reward | a policy π: state → action |

**Supervised** splits by label type: **classification** (categorical y — win/lose) vs. **regression** (continuous y — goals scored). Needs [[data-types-and-levels-of-measurement|labeled data]], which is often the expensive bottleneck. → [[supervised-learning]].

**Unsupervised** has no target to check against, so "correct" is ill-defined; you evaluate by usefulness of the structure. Main tasks: **clustering** (K-Means), **dimensionality reduction** (PCA), density estimation. → [[unsupervised-learning]].

**Reinforcement** optimizes a *sequence* of decisions under delayed feedback; the core tension is **exploration vs. exploitation**. → [[reinforcement-learning]].

```python
# the paradigms differ only in what the fit() call receives
supervised.fit(X, y)          # inputs AND labels
unsupervised.fit(X)           # inputs only — no y exists
# reinforcement: no static X/y — an agent loops with an environment
for state in episode:
    action = policy(state)
    reward = env.step(action) # signal arrives only AFTER acting
    policy.update(reward)
```

*(A fourth paradigm, **semi-supervised**, mixes a little labeled data with lots of unlabeled — practically important when labels are scarce.)*

## In ML

**The paradigm dictates the entire pipeline** — supervised needs a [[train-test-split|labeled split]] and error metrics vs. ground truth; unsupervised needs internal validity measures (silhouette, explained variance) because there *is* no ground truth; reinforcement needs an environment/simulator and reward shaping. Choosing wrong wastes the whole project.

**Most production ML today is supervised** — spam filters, fraud detection, recommendation ranking, and the goal-prediction model in the Cebollitas project are all supervised, because labeled outcomes exist and the objective is prediction.

**The line blurs at the frontier** — LLMs are pretrained *self-supervised* (labels manufactured from the text itself: predict the next token), then aligned with *reinforcement* (RLHF). Real systems chain paradigms rather than picking one.

## Exercises

**Basic** — Classify each as supervised, unsupervised, or reinforcement: (a) predicting house price from features; (b) grouping customers by behavior with no labels; (c) a bot learning chess by playing itself.

**Intermediate** — Cebollitas wants to (i) predict next match result and (ii) discover natural player "types." Which paradigm fits each, and what data shape (X only? X+y?) does each require?

**Advanced** — Explain why unsupervised learning is *harder to evaluate* than supervised, and why "no labels" does not mean "no way to measure quality." Name one internal metric for clustering and one for dimensionality reduction.
