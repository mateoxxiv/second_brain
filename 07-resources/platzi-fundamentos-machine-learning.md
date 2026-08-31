---
tags:
  - status/seed
  - literature
type: course
domain: ml
sources:
  - "https://platzi.com/cursos/machine-learning/"
author: "Juan Carlos Osorio (AI/ML Engineer, AWS Instructor)"
date_read: "2026-08-08 (in progress)"
---

## Summary

*Curso de Fundamentos de Machine Learning* (Platzi) is a beginner, project-driven introduction to the end-to-end ML workflow in Python, taught through a single **sports-analytics** case study (predicting football/soccer match outcomes and scouting players). Across 20 short classes it walks from choosing a learning paradigm, through data cleaning, scaling, and feature engineering, into supervised regression and unsupervised clustering/PCA, and finishes with a first taste of PyTorch neural nets and NLP sentiment analysis. It exercises `pandas`, `numpy`, `scikit-learn`, and Jupyter on a real dataset.

> **Role in the vault — read this before deriving notes.** This is a **technical/practical complement, NOT a source of conceptual mastery.** Platzi teaches the *how* (which sklearn call, in what order) at a technical level and deliberately **skips the mathematical rigor** — no derivations, no proofs, no "why this works." So it does **not** "cover" topics like linear regression or PCA. The permanent notes for those concepts must be **theory-derived** (Triola, ISLR/ESL, textbooks, first-principles math); Platzi contributes only the *runnable code layer* and the sports examples that make the theory concrete. When a class maps to a note below, treat the class as the **implementation companion** to a theory-first note, never its origin.

---

## Chapter / Class Map

| Module | Class | Topic | Vault notes |
|---|---|---|---|
| 1 — Foundations & context | 1 | Supervised vs. unsupervised vs. reinforcement — which to choose | [[types-of-machine-learning]] |
| | 2 | Supervised models to predict matches | [[supervised-learning]], [[supervised-learning-algorithms]] |
| | 3 | Clustering and PCA on unlabeled data | [[unsupervised-learning]] |
| | 4 | Python + Jupyter setup for analysis | |
| 2 — Data prep & exploration | 5 | Cleaning CSV data with Pandas | [[one-hot-encoding]], [[missing-data-imputation]], [[data-preprocessing]] |
| | 6 | Descriptive statistics to analyze matches | [[data-types-and-levels-of-measurement]] |
| | 7 | MinMaxScaler and StandardScaler | [[feature-scaling]] |
| 3 — Feature engineering | 8 | Feature engineering with pandas | [[feature-engineering]] |
| | 9 | Feature selection: SelectKBest & decision trees | [[feature-selection]] |
| 4 — Supervised modeling | 10 | Splitting data with train_test_split | [[train-test-split]] |
| | 11 | Linear regression to predict goals | [[linear-regression]] |
| | 12 | Is your regression model any good? | [[regression-evaluation-metrics]] |
| | 13 | R² metric in sports regression | [[r-squared]] |
| | 14 | Decision tree vs. linear regression | [[decision-trees]] |
| 5 — Unsupervised learning | 15 | Clustering players with K-Means | [[k-means-clustering]] |
| | 16 | Interpreting K-means clusters | [[k-means-clustering]] |
| | 17 | Visualizing player profiles with PCA | [[principal-component-analysis]] |
| 6 — Pipeline & final project | 18 | ML pipeline joining prediction + scouting | [[ml-pipeline]] |
| 7 — Intro to deep learning | 19 | Neural networks with PyTorch, step by step | [[perceptron-and-mlp]] |
| 8 — NLP use case | 20 | Fan sentiment analysis with NLP | [[sentiment-analysis]] |

---

## All Topics at a Glance

**Module 1 — Foundations & sports context**
- [[types-of-machine-learning]] — the supervised / unsupervised / reinforcement split and how to pick one for a problem
- [[supervised-learning]] — learning a mapping from labeled examples (predicting match results)
- [[supervised-learning-algorithms]] — the algorithm selection map (linear/logistic regression, trees, RF, SVM, NN) and when to use each
- [[unsupervised-learning]] — finding structure without labels (clustering, PCA)

**Module 2 — Data preparation & exploration**
- [[one-hot-encoding]] — *(Class 5, companion)* nominal categories → k binary columns; the dummy-variable trap and `get_dummies`
- [[missing-data-imputation]] — *(Class 5, companion, gap)* fill nulls with mean/median instead of dropping rows
- [[data-preprocessing]] — *(Class 5, companion, gap)* the load→inspect→impute→encode→dedupe→parse cleaning pipeline
- [[feature-scaling]] — MinMax vs. Standard scaling and why distance/gradient methods need it
- [[data-types-and-levels-of-measurement]] — *(exists)* the descriptive-stats vocabulary reused here

**Module 3 — Feature engineering**
- [[feature-engineering]] — constructing informative inputs from raw match data
- [[feature-selection]] — SelectKBest and tree-based importance to drop noise

**Module 4 — Supervised modeling**
- [[train-test-split]] — holding out data to estimate generalization (ties to [[random-sample-vs-simple-random-sample]])
- [[linear-regression]] — the first predictive model, closed-form + fit in sklearn
- [[regression-evaluation-metrics]] — MAE/MSE/RMSE and what "good" means
- [[r-squared]] — variance-explained metric and its traps
- [[decision-trees]] — nonlinear alternative; tree vs. linear comparison

**Module 5 — Unsupervised learning**
- [[k-means-clustering]] — grouping players into profiles; choosing k and interpreting centroids
- [[principal-component-analysis]] — dimensionality reduction to visualize clusters

**Module 6-8 — Pipeline, DL, NLP**
- [[ml-pipeline]] — chaining preprocessing → model into one reproducible object
- [[perceptron-and-mlp]] — first neural net in PyTorch
- [[sentiment-analysis]] — NLP classification of fan text

---

## Key Takeaways

1. **The ML workflow is a fixed pipeline, not a single model** — choose paradigm → clean → explore → scale → engineer features → split → train → evaluate → (cluster/reduce) → deploy as a pipeline. The course's value is drilling this *sequence* on one dataset.
2. **Preprocessing and feature work dominate the effort** — of the modeled 16 practical hours, cleaning, scaling, and feature engineering (Modules 2–3) come *before* any model is fit; the modeling itself (Module 4) is comparatively quick.
3. **Scaling is a prerequisite for many algorithms, not a nicety** — `MinMaxScaler`/`StandardScaler` appear early because distance-based (K-Means) and gradient-based methods are distorted by unscaled features.
4. **Supervised and unsupervised solve different questions on the same data** — regression *predicts goals* (labeled), while K-Means/PCA *profile players* (unlabeled); the final pipeline fuses both (prediction + scouting).
5. **The course is a bridge, not a destination** — it ends by *touching* PyTorch and NLP, signaling where the roadmap's T7 (deep learning) and later NLP work continue.

## Quotes / Important Passages

> *(Course in progress — quotes/timestamps to be added as classes are watched.)*

## My Thoughts

This is a useful **Builder-track implementation companion** to run alongside the theory notes: it turns the abstract T4/T5 roadmap items (linear regression, decision trees, K-Means, PCA) into runnable `scikit-learn` code on a concrete dataset. But it is *only* that — the math rigor is absent by design, so it must not be mistaken for coverage of the concepts. The deep derivations (why least-squares minimizes squared error, what R² actually measures, the K-Means objective and its convergence) come from the **theory track**, and the permanent notes stay theory-first. The tightest connection to what we've just studied is Class 10 (`train_test_split`) — that's [[random-sample-vs-simple-random-sample]] and [[sampling-error-vs-nonsampling-error]] in practice — and Class 6 (descriptive statistics) reuses [[data-types-and-levels-of-measurement]]. Its real, concrete value: **concrete, runnable examples** — every class produces working `scikit-learn` code that grounds the theory notes as short inline snippets (per vault policy, no standalone `.py` files unless explicitly requested). Where to get the *why* it skips: ISLR (*An Introduction to Statistical Learning*, free PDF) and StatQuest videos, class by class.

---

## Permanent Notes Created

- [[types-of-machine-learning]] — from Class 1: the supervised / unsupervised / reinforcement split, organized by the feedback signal each paradigm receives (theory-first, Cebollitas as illustration)
- [[supervised-learning]] — from Class 2: learning f: X→y from labeled pairs; regression vs. classification, overfitting, generalization as the goal
- [[supervised-learning-algorithms]] — from Class 2: the algorithm selection map (linear/logistic regression, trees, random forest, SVM, neural nets) and when to use each
- [[unsupervised-learning]] — from Class 3: finding structure without labels; clustering (K-Means/DBSCAN/hierarchical), dimensionality reduction (PCA/t-SNE/UMAP), and evaluation via inertia + silhouette
- [[one-hot-encoding]] — from Class 5 (companion): theory-first (ISLR §3.3.1 dummy variables) with `get_dummies` as the implementation layer — nominal→binary columns, the dummy-variable trap, cardinality cost, and encoding alternatives
- [[feature-scaling]] — from Class 7 (companion): theory-first (ESL §14.5.1) with `MinMaxScaler`/`StandardScaler` as the implementation layer — min-max vs. z-score, when each fits, the fit-on-train-only leakage trap, and why distance/gradient/PCA methods require it
- [[feature-engineering]] — from Class 8 (companion): theory-first (Kuhn & Johnson) with pandas-derived columns as the implementation layer — the operation vocabulary (difference/ratio/interaction/aggregation), correlation-and-distribution validation, and the target-leakage trap

## Gaps — Notes Still to Create

- [[missing-data-imputation]] — from Class 5's `fillna(mean)`; theory-first (mean/median/mode imputation, when it biases variance, MCAR/MAR/MNAR)
- [[data-preprocessing]] — from Class 5; the umbrella cleaning pipeline note tying together imputation, encoding, deduplication, and type parsing
- [[linear-regression]] — the course's core model; already the #1 item in roadmap T4, derive closed-form + gradient-descent + sklearn
- [[k-means-clustering]] — roadmap T5's first clustering algorithm, exercised on player profiles
- [[principal-component-analysis]] — roadmap T5; note the link back to [[singular-value-decomposition]] already in the linear-algebra track
