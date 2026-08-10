---
tags:
  - status/seed
  - ml
related:
  - "[[types-of-machine-learning]]"
  - "[[supervised-learning]]"
  - "[[k-means-clustering]]"
  - "[[principal-component-analysis]]"
  - "[[characteristics-of-data]]"
domain: ml
sources:
  - "James, Witten, Hastie & Tibshirani. An Introduction to Statistical Learning. Ch. 10/12 (theory)"
  - "https://scikit-learn.org/stable/unsupervised_learning.html"
  - "[[platzi-fundamentos-machine-learning]] — Class 3 (practical companion)"
---

> **TL;DR** — Unsupervised learning finds structure in data that has **no labels** — grouping similar points (clustering) or compressing many variables into few (dimensionality reduction) — so there is no "right answer" to predict, only patterns to discover and interpret.

---

## Intuition

You have stats on hundreds of players but *no one told you* who is good or what role each plays. There's nothing to predict — instead you want the data to *reveal* its own structure: which players behave alike, which variables carry the real signal. That's unsupervised learning: no teacher, no labels ([[supervised-learning|the supervised opposite]]), just "here's the data, find what's in it." Because there's no target, *you* interpret what emerges — the algorithm surfaces groups or axes; you name them ("tireless wingbacks," "ghost strikers").

The catch that defines the whole paradigm: **with no labels, there's no ground truth to score against**, so both *how you find* structure and *how you judge* it are fundamentally different from supervised learning.

## Mechanics

Only **X** exists (no y). Two dominant task families:

| Task | Goal | Methods | Note |
|------|------|---------|------|
| **Clustering** | group similar points | K-Means, DBSCAN, hierarchical | [[k-means-clustering]] |
| **Dimensionality reduction** | compress variables, keep signal | PCA, t-SNE, UMAP | [[principal-component-analysis]] |

**Clustering — three tools, different assumptions:**
- **K-Means** — split into *K* groups by minimizing distance to each group's center; assumes roughly round, similar-size clusters and *you pick K*. Iterates: assign points → recompute centers → repeat.
- **DBSCAN** — groups by **density**; finds arbitrary shapes and labels sparse points as **noise**; no need to preset the number of clusters.
- **Hierarchical** — builds a tree (**dendrogram**) merging similar items into ever-broader groups; explore relationships at *any* level.

**Dimensionality reduction — summarize vs. explore:**
- **PCA** — new axes (principal components) capturing the most **variance**, *linearly*; the "view from a drone" — less detail, more overview. Ties to [[singular-value-decomposition|SVD]].
- **t-SNE / UMAP** — nonlinear, built to **visualize** local neighborhoods in 2D/3D; reveal clusters PCA's linear view misses.

**Evaluation without labels** — the hard part. Use *internal* metrics:
- **Inertia** — how *compact* clusters are (lower = tighter); K-Means minimizes it.
- **Silhouette coefficient** — how well-separated each point's cluster is, in **[−1, 1]**; near **1** = well-matched to its own cluster and far from others.

These don't *prove* the grouping is "true" — they only tell you whether the structure is compact/separated or just an optical illusion.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
km = KMeans(n_clusters=3).fit(X)     # note: fit(X) only — no labels y
print(km.inertia_)                    # compactness (lower = tighter)
print(silhouette_score(X, km.labels_))# separation quality in [-1, 1]
```

## In ML

**Unsupervised = the exploratory / representation-learning half of ML** — clustering powers customer/player segmentation and anomaly detection; dimensionality reduction powers visualization, denoising, and feature compression before a supervised model. It profiles the [[characteristics-of-data|structure]] of data no one has labeled.

**Evaluation is the core difficulty** — with no ground truth, metrics like silhouette are *heuristics*, not verdicts; choosing K or judging a projection always needs human interpretation. This is exactly why it's harder to validate than [[supervised-learning]].

**It underlies modern representation learning** — self-supervised pretraining (word/image embeddings) is unsupervised structure-finding at scale, learning representations later reused by supervised tasks.

## Exercises

**Basic** — For each, name the task (clustering or dimensionality reduction): (a) segment players into style groups; (b) squeeze 20 features into 2 for a scatter plot; (c) flag unusual, isolated data points.

**Intermediate** — You must cluster data with irregular shapes and some noise, and you don't know how many groups exist. Would you choose K-Means or DBSCAN? Justify using each method's assumptions.

**Advanced** — A clustering has low inertia but also a low silhouette score. Explain how both can happen at once, and what it tells you about the quality of the clusters (hint: inertia always drops as K rises).
