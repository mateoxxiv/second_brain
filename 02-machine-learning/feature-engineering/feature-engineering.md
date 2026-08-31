---
tags:
  - status/seed
  - ml
related:
  - "[[feature-scaling]]"
  - "[[one-hot-encoding]]"
  - "[[feature-selection]]"
  - "[[correlation]]"
  - "[[linear-regression]]"
  - "[[principal-component-analysis]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[platzi-fundamentos-machine-learning]]"
domain: ml
sources:
  - "Kuhn & Johnson, Feature Engineering and Selection (2019), Ch. 1–6."
  - "Platzi — Fundamentos de Machine Learning, Clase 8 (implementation companion: pandas-derived columns)."
---

> **TL;DR** — Feature engineering is constructing new, more *informative* predictors from raw data so the model can express a pattern it otherwise couldn't — often a bigger win than swapping the algorithm.

---

## Intuition

A model learns a function *of the features you give it*: the input representation sets a ceiling on what is learnable. Handing it `goals_home` and `possession` separately forces it to discover, on its own, that *efficiency* — shots relative to possession — is what matters. But you, the analyst, already know that. Feature engineering is the act of **writing your domain knowledge into the columns**: instead of two raw numbers you supply the *goal difference* (which directly encodes the result) or the *shots/possession ratio* (which encodes offensive efficiency). This is why a single well-chosen feature often moves the needle more than a fancier model — you've handed the algorithm a pattern it can't perceive by itself.

## Mechanics

Feature engineering is a small vocabulary of operations on raw columns:

| Operation | Example (Cebollitas) | Encodes |
|-----------|----------------------|---------|
| **Difference** | `goles_local − goles_visitante` | match outcome (win/draw/loss) |
| **Ratio / rate** | `tiros_local / posesion_local` | efficiency, not raw volume |
| **Interaction** | `shots × on_target_pct` | combined effect |
| **Aggregation** | rolling mean of last-5 goals | recent form |
| **Decomposition** | date → weekday, month | seasonality |
| **Encoding / scaling** | see [[one-hot-encoding]], [[feature-scaling]] | model-readable form |

```python
import pandas as pd  # Platzi Clase 8 — derived columns
df["goal_diff"] = df["goles_local"] - df["goles_visitante"]
df["ratio_shots_home_possession"] = df["tiros_local"] / df["posesion_local"]
```

**Validate, don't just create.** A new column earns its place only if it carries signal. Two cheap checks:
- **Distribution** (`histplot`) — is `goal_diff` mostly wins, draws, or losses? Reveals class balance and shape.
- **[[correlation|Correlation]] matrix / heatmap** — Pearson $r \in [-1,1]$. A moderate $r=0.67$ between `goles_local` and `goal_diff` confirms the new feature tracks real performance. But read it two ways: high feature↔target $r$ is *useful*; high feature↔feature $r$ is *redundancy* (multicollinearity) — a target for [[feature-selection]].

**The leakage trap.** A feature that secretly contains the answer inflates offline scores and collapses in production. `goal_diff` *is* the result, so it's a fine **target** — but never a *predictor* of that same result. Always ask: would this value be knowable *before* the moment I'm predicting?

## In ML

**Correlation only sees straight lines.** Pearson $r$ measures *linear* association; a U-shaped but strongly predictive feature can score $r\approx0$. And $r$ never implies causation — validate features, but don't trust the heatmap as ground truth.

**Representation > algorithm for tabular data.** On structured problems, gains from good features routinely dwarf gains from a better model class. This is the practitioner's leverage point that [[feature-selection]] then prunes.

**Deep learning automates it.** CNNs/transformers *learn* their features (representation learning), which is exactly why they dominate images and text — domains where hand-crafting features is hopeless. Tabular ML still leans on human feature engineering; that's the frontier the two paradigms divide.

## Exercises

**Basic** — Given `shots=12` and `possession=55`, compute `ratio_shots_home_possession`. What does a *high* value say about the team, in one sentence?

**Intermediate** — You build `points = 3·wins + draws` and use it to predict whether the team won a given match. Explain why this is target leakage and how the model would fail on new games.

**Advanced** — A feature has near-zero Pearson correlation with the target yet a decision tree finds it highly predictive. Give a concrete relationship (with numbers) that produces this, and explain what it reveals about the limits of correlation-based feature screening.
