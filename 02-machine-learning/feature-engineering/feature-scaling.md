---
tags:
  - status/seed
  - ml
related:
  - "[[measures-of-variation]]"
  - "[[measures-of-center]]"
  - "[[normal-distribution]]"
  - "[[coefficient-of-variation]]"
  - "[[feature-engineering]]"
  - "[[one-hot-encoding]]"
  - "[[k-means-clustering]]"
  - "[[principal-component-analysis]]"
  - "[[linear-regression]]"
  - "[[train-test-split]]"
  - "[[platzi-fundamentos-machine-learning]]"
domain: ml
sources:
  - "Hastie, Tibshirani & Friedman, The Elements of Statistical Learning, §14.5.1 (standardization before distance/PCA)."
  - "Platzi — Fundamentos de Machine Learning, Clase 7 (implementation companion: MinMaxScaler / StandardScaler)."
---

> **TL;DR** — Feature scaling rewrites every column onto a common scale so that distance- and gradient-based models weigh features by their *information*, not by the accident of their **units**.

---

## Intuition

A striker took 12 shots and the team held 55% possession. To a model that measures similarity by raw distance, a 1-unit change in shots looks 55× smaller than a 1-unit change in possession — purely because of the numbers' magnitudes, not their importance. The larger-ranged feature silently dominates. Scaling levels the field: it strips the units so no feature wins just for being counted in bigger numbers. Note this only matters for models that compare feature magnitudes — **distance-based** ([[k-means-clustering|K-Means]], KNN, SVM) and **gradient-based** (linear/logistic regression, neural nets); tree-based models split one feature at a time and are scale-invariant, so they don't need it.

## Mechanics

Two dominant transforms, both fit column-by-column:

| | Formula | Output | Best when |
|---|---------|--------|-----------|
| **Min-max (normalization)** | $x' = \dfrac{x - \min}{\max - \min}$ | bounded $[0,1]$ | bounded range wanted; non-normal data; no extreme outliers |
| **Standardization (z-score)** | $x' = \dfrac{x - \bar{x}}{s}$ | mean 0, [[measures-of-variation\|std]] 1, unbounded | data ~[[normal-distribution\|normal]] or centered assumed (PCA, linear models) |

- **Min-max** preserves the distribution's *shape* exactly (it's a linear rescale) but is **fragile to outliers**: one huge max squashes everyone else toward 0.
- **Standardization** re-centers on the [[measures-of-center|mean]] and divides by the [[measures-of-variation|standard deviation]] — the [[coefficient-of-variation|z-score]] machinery — so it doesn't bound the range but is less distorted by a single extreme. For heavy outliers, `RobustScaler` (median / IQR) beats both.

**The leakage trap — fit on train only.** Scalers *learn* parameters (min/max, or mean/std) from data. Those must be learned from the **training set alone**, then applied to test/new data — otherwise test-set statistics leak into training and inflate your score. The course's `fit_transform(df)` on the whole frame is fine for a demo but wrong for real modeling; see [[train-test-split]].

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler  # Platzi Clase 7
# fit ONLY on train, then transform both
norm = MinMaxScaler().fit(X_train[["tiros_local", "tiros_visitante"]])
std  = StandardScaler().fit(X_train[["posesion_local", "posesion_visitante"]])
X_train[cols_n] = norm.transform(X_train[["tiros_local", "tiros_visitante"]])
X_test[cols_n]  = norm.transform(X_test[["tiros_local", "tiros_visitante"]])
```

`fit` computes the parameters; `transform` applies the formula; `fit_transform` chains them — use it only on the training split.

## In ML

**Distance methods are useless without it.** [[k-means-clustering|K-Means]] and KNN sum squared differences across features; an unscaled large-range feature *is* the distance. Scaling is a prerequisite, not a polish step.

**PCA chases variance, so scale first.** [[principal-component-analysis|PCA]] keeps directions of maximum variance — on unscaled data the top component just tracks the largest-unit feature. Standardizing first makes "variance" mean *shape*, not *units*.

**Gradient descent converges faster on scaled inputs.** Unscaled features stretch the loss surface into a narrow ravine; scaling rounds it out, so a single learning rate works across all weights ([[linear-regression]], neural nets).

## Exercises

**Basic** — A player has 12 shots; the column ranges 3–15. Give the min-max value. Separately, if possession has mean 50 and std 8, give the z-score of a 66% game.

**Intermediate** — You min-max scale using the full dataset's min and max, then split into train/test. Explain precisely how this leaks information and why the leak flatters your test metric.

**Advanced** — One feature has a lone 100× outlier. Show what min-max does to the other 99 values, contrast with standardization, and argue why `RobustScaler` (median/IQR) is preferable — tie it back to why the [[measures-of-variation|std deviation]] itself is outlier-sensitive.
