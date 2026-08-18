---
tags:
  - status/seed
  - ml
related:
  - "[[data-types-and-levels-of-measurement]]"
  - "[[feature-engineering]]"
  - "[[linear-regression]]"
  - "[[feature-scaling]]"
  - "[[platzi-fundamentos-machine-learning]]"
domain: ml
sources:
  - "James et al., An Introduction to Statistical Learning, §3.3.1 (qualitative predictors / dummy variables)."
  - "Platzi — Fundamentos de Machine Learning, Clase 5 (implementation companion: pandas.get_dummies)."
---

> **TL;DR** — One-hot encoding turns a [[data-types-and-levels-of-measurement|nominal]] category with *k* levels into *k* binary (0/1) columns, so a model can consume categories as numbers **without inventing a fake order** between them.

---

## Intuition

A model does arithmetic; it can't read `"Cebollitas Juniors"` or `"Real Patacón"`. The naive fix — map teams to 1, 2, 3 — is *wrong for nominal data*: it secretly claims team 3 is "greater than" team 1 and that the gap 1→2 equals 2→3, an order that doesn't exist. One-hot encoding avoids this by giving each category its **own** column: a 1 marks "this row is that category," 0 otherwise. No category is numerically larger than another — they're just present or absent.

## Mechanics

For a categorical feature with levels $\{c_1,\dots,c_k\}$, create $k$ indicator columns; row $i$ gets a 1 in the column of its category and 0 elsewhere (exactly one 1 per row — hence "one-hot").

| Team | → | is_Juniors | is_Patacón | is_Cebollitas |
|------|---|-----------|-----------|--------------|
| Juniors | | 1 | 0 | 0 |
| Patacón | | 0 | 1 | 0 |

**The dummy-variable trap.** The $k$ columns are linearly dependent — they always sum to 1, so any one is perfectly predictable from the others (perfect multicollinearity). For models with an intercept (linear/logistic regression) this makes the design matrix singular. Fix: **drop one column** (`drop_first=True`), using $k-1$ columns with the dropped level as the implicit *baseline*. Tree-based models don't need the drop.

```python
import pandas as pd
# Platzi Clase 5 — get_dummies is the implementation companion
datos = pd.get_dummies(
    datos_cebollitas,
    columns=["equipo_local", "equipo_visitante"],
    drop_first=True,   # avoid the dummy-variable trap for linear models
)
```

**Cost — cardinality.** $k$ levels add $k$ (or $k-1$) columns. High-cardinality features (zip codes, user IDs) explode dimensionality and sparsity — a signal to use an alternative (below).

| Encoding | Use when |
|----------|----------|
| **One-hot** | nominal, low cardinality |
| **Ordinal/label** | genuinely *ordered* categories ([[data-types-and-levels-of-measurement\|ordinal]]) |
| **Target/mean** | high cardinality, supervised |
| **Embeddings** | very high cardinality / deep learning |

## In ML

**It encodes the measurement level, not just the text.** Choosing one-hot vs. ordinal encoding *is* the [[data-types-and-levels-of-measurement|nominal-vs-ordinal]] decision made operational — encode order only when order truly exists, else one-hot.

**It interacts with scaling and regularization.** One-hot columns are already 0/1, so they usually bypass [[feature-scaling|standardization]]; but L1/L2 penalties treat each dummy as a separate feature, which is why grouped penalties (group lasso) exist for one categorical variable's dummies.

**It's the classic baseline vs. learned embeddings.** One-hot is a sparse, orthogonal, *untrained* representation (every category equidistant); embeddings replace it with dense, *learned* vectors where similar categories sit close — the same leap as bag-of-words → word2vec.

## Exercises

**Basic** — A `stadium` column has 3 values. How many columns does plain one-hot create? How many with `drop_first=True`, and what does the dropped level become?

**Intermediate** — Explain, using the "columns sum to 1" fact, why feeding all $k$ dummies plus an intercept into linear regression breaks. Why don't decision trees care?

**Advanced** — A `user_id` feature has 50,000 unique values. Argue why one-hot is a poor choice here and name two alternatives, stating what each assumes about the data or the model.
