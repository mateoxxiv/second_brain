# Study Roadmap

**Created**: 2026-02-24
**Last updated**: 2026-10-03 (re-audit. Vault grew 155 → **190 domain notes** + 8 literature notes. **T3 Probability 49 → 76**: Triola Ch. 4 (probability rules, Bayes, counting, simulation), all of Ch. 5 (discrete distributions) and Ch. 6 §6-1–6-3 (PDF, uniform, standard normal, critical values, standardization, inverse normal) landed. **First theory-sourced T4 algorithm note**: logistic-regression (ISLR Ch. 4). **B2 Prompt Engineering STARTED** (3 notes, from Claude 101). **B6/B7 Fabric + Medallion STARTED** (4 notes, Udemy Fabric course). New sections this audit: **Course Progress**, **T4b Evaluation**, **T11 Reinforcement Learning**, **T12 Generative Models**, **F1 Algorithms & DS**, **F2 Databases**, **B10–B12 fleshed out**, **B13 AI Safety & Security**. Prior audit 2026-09-10: Since 2026-08-09 the vault grew 116 → 155 domain notes. **T3 Probability jumped 23 → 49**: the entire Triola Ch. 2-3 descriptive-statistics block landed — frequency distributions, all graph types (histogram, ogive, stem-and-leaf, Pareto, boxplots, etc.), measures of center/variation, z-scores, percentiles, quartiles/IQR, Chebyshev, skewness, coefficient of variation. **T4 Supervised/Unsupervised ML has actually STARTED (0 → 7 notes)** from the Platzi "Fundamentos de ML" course — types-of-machine-learning, supervised + algorithms, unsupervised, and a feature-engineering trio (feature-engineering, feature-scaling, one-hot-encoding); note these are *practical-course-derived companion notes*, not the deep theory notes T4 ultimately needs. **Constitutional AI** note added to the LLM track (04/architectures). **MLOps opened (0 → 1)**: python-and-jupyter-environment-setup. Literature notes grew 2 → 7 (Anton LA, Platzi LA, Triola, Platzi ML, Platzi People Analytics, Claude 101, AI frontier-models landscape). **Still unresolved from every prior audit**: matrix-transpose is still 3 competing drafts in `00-inbox/proposals/` with no promoted note; `code/` is still 100% empty — zero runnable `.py` files despite 155 notes. Prior 2026-08-09: added T3 "Data skepticism & study design" reading block.)
**Goal**: Become an expert AI architect and engineer — design, implement, and orchestrate intelligent systems end-to-end.

> **2026-09-14 addition**: Added a third **Human Skills Track (H1–H6)** — soft, social & leadership skills — as a co-equal complement to the Theory and Builder tracks. Rationale: the "architect / orchestrate end-to-end" goal is inherently a *team* role, so communication, collaboration, and leadership are load-bearing, not optional. Notes will live in a new `09-professional-skills/` folder once the first one is written.

---

## Dual-Track Approach

Two parallel tracks that reinforce each other:

```
THEORY TRACK (left)              BUILDER TRACK (right)
Deep understanding               Real tools, real projects

Linear Algebra ──────────────── → Embeddings & Vector Search
Calculus ─────────────────────── → Gradient Descent in practice
Probability ──────────────────── → Evaluation, A/B testing
Supervised ML ────────────────── → Scikit-learn, Kaggle
Neural Networks ──────────────── → PyTorch, HuggingFace
Transformers ─────────────────── → LLM APIs (OpenAI, Anthropic)
Attention Mechanism ──────────── → RAG, agents
                                    ↓
                         Cloud: AWS / Azure Fabric / GCP
                         ETL pipelines + model serving
                                    ↓
                    Data Engineering (medium-high level)
              SQL → Spark → Kafka → dbt → Lakehouse → Streaming
                                    ↓
                    Low-Level ML: C++ & Systems Programming
              Memory model → Pointers → CUDA → TensorRT → custom ops
                                    ↓
              Software Engineering & System Design for DS/AI
         Clean code → Testing → APIs → Distributed systems → ML design

Theory explains WHY things work.
Building shows HOW they work in practice.
DE + C++ + SWE + System Design = production-grade AI architect.

        ┌─────────────────────────────────────────────┐
        │  HUMAN SKILLS TRACK (wraps both tracks)       │
        │  Communication · Collaboration · Leadership   │
        │  = how technical skill turns into team impact │
        └─────────────────────────────────────────────┘
```

---

## Progress Overview

| Area | Notes | Status |
|------|-------|--------|
| 01-foundations/linear-algebra | 60 | **Essentially complete** (8 evergreen / 10 growing / 42 seed). Transpose, matrix calculus, pseudoinverse, matrix norms, quadratic forms remain |
| 01-foundations/calculus | 9 | Core complete (6 growing / 3 seed) — no change since last audit |
| 01-foundations/probability | 76 | **+27** — Triola Ch. 4 (12), Ch. 5 (12), Ch. 6 §6-1–6-3 (8). Descriptive + probability + discrete/normal distributions done. **Inferential half (sampling distributions, CLT, CIs, hypothesis testing, MLE) still entirely open** |
| 01-foundations/algorithms | 0 | Not started — now has a track (F1) |
| 01-foundations/databases | 0 | Not started — now has a track (F2) |
| 02-machine-learning | 8 | 7 Platzi orientation notes + **logistic-regression** (first ISLR-derived algorithm note). All seed |
| 03-deep-learning | 0 | Not started |
| 04-llms-and-agents | 15 | **+3** — prompt-engineering-fundamentals, claude-context-layers, iterative-prompt-refinement (B2 opened) |
| 05-mlops | 5 | **+4** — microsoft-fabric, fabric-access-and-trial, fabric-workspace, medallion-architecture |
| 08-applied-domains/people-analytics | 17 | **Side track, outside core path** — full course captured. All 17 still `status/seed` |

**Total notes**: 190 domain notes + 8 literature notes | **8 evergreen** | **26 growing** | **156 seed**

**Vault hygiene gaps** (carried over unresolved from prior audits):
1. `00-inbox/proposals/` still has three unresolved template drafts for `matrix-transpose` — **open for 4+ audits**. Promote one to `linear-algebra/matrix-transpose.md` or delete the drafts.
2. `code/` is entirely empty. Per CLAUDE.md, `.py` files are created only on explicit request, so this is a choice, not an oversight — but no "build from scratch" item has been exercised yet.
3. **156 of 190 notes are `status/seed`** (was 121/155). **Zero notes were promoted this cycle** — 35 new notes, 0 maturations. 82% of the vault is seed. The `/review` pass is now the single most overdue maintenance item.
4. Literature-note gap lists drift from reality: `udemy-microsoft-fabric` still lists [[medallion-architecture]] as a gap though the note now exists; `platzi-fundamentos-machine-learning` Class 4 row doesn't link [[python-and-jupyter-environment-setup]].

---

## Course Progress (literature sources)

| Source | Type | Progress | Notes | What's left |
|---|---|---|---|---|
| **Anton — Álgebra Lineal** | Theory (textbook) | ✅ Ch. 1–7 covered (~100%) | 58 | [[quadratic-forms]] (only listed gap) |
| **Platzi — Álgebra Lineal** | Practical companion | ✅ Complete | 2 own + links | — |
| **Triola — Estadística** | Theory (textbook) | 🟡 Ch. 1–5 done, **Ch. 6 §6-1–6-3 done** → ~5.4 / 12 ch. (**~45%**) | 76 | §6-4 sampling distributions, §6-5 **CLT**, §6-6 assessing normality, §6-7 normal approx. to binomial; then Ch. 7–12 |
| **Platzi — Fundamentos de ML** | Practical companion | 🟡 8 / 20 classes mapped (**40%**) | 7 | Classes 9–20: feature selection, train-test split, linear regression, metrics, R², trees, K-Means, PCA, pipeline, MLP, sentiment |
| **Platzi — People Analytics con Excel** | Practical | ✅ 13 / 13 classes | 17 | — (side track) |
| **Claude Academy — Claude 101** | Product course | 🟡 Lessons 1–2 done, 3 partial → ~2.5 / 13 (**~20%**) | 3 | ai-fluency-framework, claude-work-modes, projects, artifacts, skills, connectors, research-mode |
| **Udemy — Microsoft Fabric** | Practical (vendor) | 🟡 Modules 1–2 + medallion (part of 7) → ~2.5 / 9 (**~28%**) | 4 | Data Factory, Lakehouse + Spark, Warehouse, storage comparison, Power BI, DP-600/700 prep |
| **AI Frontier Models Landscape 2026-09** | News snapshot | — | 0 | gemini-api, grok-api, deepseek-api, open-weight-vs-closed-models |

**Reading:** the only *theory* source actively in progress is Triola — keep it as the main line. Anton is finished. Three practical courses (Platzi ML, Claude 101, Fabric) are open in parallel; that's fine as long as they stay companions, but **don't open a 4th practical course** until one of them closes.

---

## THEORY TRACK

### T1: Linear Algebra — ESSENTIALLY COMPLETE (60/~63 notes)

> *Why*: Every ML algorithm is a matrix operation. You can't understand neural nets, PCA, or embeddings without this.

**Done:**
- [x] Vectors and Vector Spaces
- [x] Vector Operations
- [x] Vector Norms
- [x] Dot Product
- [x] Cross Product + Lagrange Identity
- [x] Cosine Similarity
- [x] Linear Combination
- [x] Linear Independence
- [x] Basis and Dimension
- [x] Projection (single vector)
- [x] Projection onto Subspaces
- [x] Gaussian Elimination
- [x] Determinant
- [x] Cofactor
- [x] Adjugate Matrix
- [x] Sarrus' Rule
- [x] Cramer's Rule
- [x] Matrix Operations (+ scalar multiplication)
- [x] Matrix Inverse
- [x] Special Matrices
- [x] Eigenvalues and Eigenvectors
- [x] Spectral Decomposition
- [x] Singular Value Decomposition
- [x] Gram-Schmidt
- [x] Linear Transformations
- [x] Planes as Linear Systems
- [x] Plane Equation
- [x] Point-to-Plane Distance
- [x] Line Equation in 3D
- [x] Euclidean N-Space
- [x] General Vector Spaces (10 axioms, certification → toolkit)
- [x] Inner Product Spaces
- [x] Subspaces ← new
- [x] Angles and Orthogonality ← new
- [x] Cauchy-Schwarz Inequality ← new
- [x] Induced Norm and Distance ← new
- [x] Orthogonal Matrix ← new
- [x] Orthonormal Bases ← new
- [x] Change of Basis ← new
- [x] Coordinate Vector ← new
- [x] Kernel and Range ← new
- [x] Row and Column Spaces ← new
- [x] Rank-Nullity Theorem ← new
- [x] Eigenspace ← new (geometric vs. algebraic multiplicity)
- [x] Complex Eigenvalues ← new
- [x] Synthetic Division ← new (root-finding for characteristic polynomials)
- [x] Block-Diagonal Matrices ← new
- [x] Diagonalization ← new (§6.2 — Theorem 2, distinct-eigenvalues shortcut)
- [x] Orthogonal Diagonalization ← new (§6.3 — symmetric ⟺ orthogonally diagonalizable, guaranteed spectrum)
- [x] Matrix Similarity ← new
- [x] Elementary Matrices as Geometric Transformations ← new
- [x] Geometry of Planar Linear Transformations ← new
- [x] Inverse Linear Transformations ← new
- [x] Linear Transformations Map Lines to Lines ← new
- [x] Matrix of Linear Transformation (+ general spaces) ← new

**Remaining:**
- [ ] Matrix Transpose — surprising gap: no permanent note exists, only 3 unresolved template drafts sitting in `00-inbox/proposals/`. Resolve before anything else in this track.
- [ ] Matrix Calculus (Jacobians, Hessians, dL/dW) — needs calculus track first, CRITICAL for backprop
- [ ] Pseudoinverse (Moore-Penrose) — via SVD, for least-squares
- [ ] Matrix Norms and Condition Number — numerical stability
- [ ] Quadratic Forms and Positive Definiteness ← added 2026-10-03 (Anton gap) — xᵀAx, PD/PSD, the bridge to Hessians, covariance matrices, and convexity
- [ ] Low-Rank Approximation (Eckart–Young) ← added 2026-10-03 — the theorem behind PCA, LoRA, and embedding compression

**Estimated remaining**: ~6 notes — the eigenvalue chapter (Anton §6.1-6.3) is now fully covered end-to-end. Once matrix transpose and matrix calculus land, this track is done and T4 (Supervised ML) is fully unblocked.

---

### T2: Calculus — IN PROGRESS (9/~12 notes)

> *Why*: Optimization IS calculus. Gradient descent, backpropagation, loss functions — all calculus.

**Done:**
- [x] Derivatives and Partial Derivatives
- [x] Derivative Rules
- [x] Chain Rule
- [x] Polynomial Factorization
- [x] Gradient Descent
- [x] Optimization (convexity, second derivative test, saddle points)
- [x] Algebraic Operation Properties (commutativity, associativity, distributivity)
- [x] Exponent, Log, and Root Properties
- [x] Trigonometric Identities ← new

**Remaining:**
- [ ] Matrix Calculus (Jacobians, Hessians) — CRITICAL before deep learning, shared gate with T1
- [ ] Taylor Series and Approximations — explains why gradient descent works
- [ ] Integration Basics — needed for probability density derivations (now urgent: Triola Ch. 6 PDFs already use areas-under-curves)
- [ ] Lagrange Multipliers (constrained optimization) ← added 2026-10-03 — needed for SVM dual, PCA derivation, max-entropy
- [ ] Multivariable Integration and Change of Variables ← added 2026-10-03 — joint densities, the Gaussian integral, normalizing flows

**Estimated remaining**: ~5 notes

---

### T3: Probability and Statistics — IN PROGRESS (76/~100 notes)

> *Why*: ML is applied statistics. Bayesian thinking, distributions, hypothesis testing.

**Done — distributions (10):**
- [x] Probability Fundamentals (Bayes, conditional, independence)
- [x] Probability Distributions (overview + selection guide)
- [x] Bernoulli Distribution
- [x] Binomial Distribution
- [x] Normal Distribution (CLT, MSE derivation)
- [x] Poisson Distribution
- [x] Exponential Distribution (memoryless property)
- [x] Beta Distribution (conjugate prior, Bayesian A/B testing)
- [x] Dirichlet Distribution (LDA connection)
- [x] CDF and Quantile Function

**Done — statistical thinking, Triola Ch. 1 (13):**
- [x] Population and Sample (why collection method beats sample size)
- [x] Parameter vs. Statistic (μ/σ/p vs. x̄/s/p̂)
- [x] Data Types and Levels of Measurement (nominal→ordinal→interval→ratio)
- [x] Principles of Statistical Thinking (the four-factor checklist) — *growing*
- [x] Statistical Significance (statistical vs. practical)
- [x] Common Misuses of Statistics (§1-4 taxonomy of pitfalls)
- [x] Sampling Methods (§1-5: SRS, systematic, convenience, stratified, cluster, multistage)
- [x] Random Sample vs. Simple Random Sample (§1-5: the A/B/C/D example)
- [x] Observational Study vs. Experiment (§1-5: data sources, causation)
- [x] Types of Observational Studies (§1-5: cross-sectional / retrospective / prospective)
- [x] Experimental Design Principles (§1-5: randomization, replication, control/blinding)
- [x] Experimental Designs for Controlling Variables (§1-5: completely randomized, randomized block, rigorously controlled, matched pairs)
- [x] Sampling Error vs. Nonsampling Error (§1-5: random wobble vs. fixable bias)

**Done — descriptive statistics, Triola Ch. 2-3 (26) ← NEW this audit:**
- [x] Characteristics of Data (CVDOT: center, variation, distribution, outliers, time)
- [x] Frequency Distribution · Relative Frequency Distribution · Cumulative Frequency Distribution
- [x] Histogram · Frequency Polygon · Ogive · Dot Plot · Stem-and-Leaf Plot
- [x] Bar Graph · Pareto Chart · Pie Chart · Scatterplot · Time-Series Graph
- [x] Principles of Effective Graphs · Misleading Graphs
- [x] Measures of Center · Weighted Mean
- [x] Measures of Variation · Coefficient of Variation · Chebyshev's Theorem
- [x] z-Score · Percentiles · Quartiles and IQR · Five-Number Summary and Boxplots
- [x] Skewness

**Done — probability, Triola Ch. 4 (11 new) ← NEW this audit:**
- [x] Sample Space and Events · Three Methods of Assigning Probability · Law of Large Numbers
- [x] Complementary Events · Addition Rule · Multiplication Rule · Conditional Probability
- [x] Law of Total Probability · Bayes' Theorem · Odds
- [x] Counting and Combinatorics · Monte Carlo Simulation

**Done — discrete distributions, Triola Ch. 5 (9 new) ← NEW this audit:**
- [x] Random Variable · Discrete Probability Distribution · Mean and Variance of a Probability Distribution · Expected Value
- [x] Identifying Unusual Results (range rule of thumb, probability criterion)
- [x] Binomial Distribution Requirements · Binomial Mean and Variance · Hypergeometric Distribution · Poisson Approximation to Binomial

**Done — normal distributions, Triola Ch. 6 §6-1–6-3 (6 new) ← NEW this audit:**
- [x] Probability Density Function · Uniform Distribution · Standard Normal Distribution
- [x] Critical Values and z_α · Normal Probabilities via Standardization · Finding Values from Normal Areas

**Remaining — Triola Ch. 6 rest (the gateway to inference) ← NEXT:**
- [x] Sampling Distributions and Estimators (§6-4) — [[sampling-distribution]] + [[unbiased-and-biased-estimators]] ← done 2026-10-04
- [ ] Central Limit Theorem (§6-5) — **the most important missing note in T3**; justifies every z/t interval and test that follows
- [ ] Assessing Normality / Normal Quantile Plots (§6-6) — QQ plots, the residual-diagnostics tool of regression
- [ ] Normal Approximation to the Binomial (§6-7) — continuity correction

**Remaining — Triola Ch. 7–12 (the inferential half) ← added 2026-10-03 from the Triola gap list:**
- [ ] Point Estimates and Confidence Intervals for a Proportion / Mean (Ch. 7) — margin of error, sample size determination
- [ ] Student's t Distribution (Ch. 7) · Chi-Squared Distribution (Ch. 7, CI for σ)
- [ ] Hypothesis Testing and p-values (Ch. 8) — H₀/H₁, Type I/II errors, power
- [ ] Inferences from Two Samples (Ch. 9) — two-proportion z-test (= the A/B test), paired vs. independent t-test
- [ ] Correlation and Regression (Ch. 10) — Pearson r, least-squares line, residuals; **bridge to T4 linear regression**
- [ ] Chi-Squared Goodness-of-Fit and Contingency Tables (Ch. 11)
- [ ] ANOVA and the F Distribution (Ch. 12)

**Remaining — beyond Triola (needs Wasserman / Bishop / MacKay):**
- [ ] Maximum Likelihood Estimation (MLE) — derives ALL loss functions from distributions
- [ ] Cross-Entropy and KL Divergence (+ Entropy) — information theory, classification losses (logistic-regression already links [[cross-entropy]] → dangling)
- [ ] Joint, Marginal, and Conditional Distributions · Covariance and Correlation of Random Variables
- [ ] Multivariate Normal Distribution — VAEs, Gaussian processes
- [ ] Maximum A Posteriori (MAP) — = regularization in disguise
- [ ] Bootstrap and Empirical Distributions
- [ ] Log-Normal, Gamma distributions
- [ ] **Causal inference basics** ← added 2026-10-03 — confounding, DAGs, potential outcomes; the formal follow-up to [[observational-study-vs-experiment]] and essential for A/B testing and uplift modeling

**Estimated remaining**: ~25 notes (≈ 4 Ch. 6 + 12 Triola Ch. 7–12 + 9 beyond)

**Reading resources (optional / enrichment — not critical path):**
- ✅ **How to Lie with Statistics** — Darrell Huff (1954). Short (~1 hr), foundational data-literacy classic; still the best "spot the misuse" primer. Pairs directly with [[common-misuses-of-statistics]]. Referenced in Triola Ch. 1 §1-4.
- ⚠️ **Tainted Truth** — Cynthia Crossen. Good on sponsored-study / conflict-of-interest bias, but dated and journalistic. Optional. Referenced in Triola Ch. 1 §1-4.
- *(Critical-path source for the rigorous inferential half of T3 remains Triola Ch. 7-12, then Wasserman's* All of Statistics *— these two books are literacy enrichment, not stepping stones.)*

**Books to understand *experimental design* (diseño de experimentos) — deeper than Triola §1-5:**
- 📘 **Design and Analysis of Experiments** — Douglas C. Montgomery. The standard textbook. Covers completely randomized, randomized block, factorial, and response-surface designs rigorously. Start here for [[experimental-designs-for-controlling-variables]].
- 📗 **Statistics for Experimenters** — Box, Hunter & Hunter. Famously intuitive, hands-on treatment of design + analysis; best for *building intuition* before Montgomery's formalism.
- 📙 **Trustworthy Online Controlled Experiments** — Kohavi, Tang & Xu ("the A/B testing book"). Bridges classical design straight to tech-industry A/B testing — the direct link from [[experimental-design-principles]] to the Builder track's evaluation/A-B-testing work.
- 🎥 *Free*: MIT 18.05 / Khan Academy "Study design" unit, and StatQuest's design-of-experiments videos — quick visual primers before committing to Montgomery.

**Data skepticism & study design (complements Ch. 1 §1-4 misuses + §1-5 collection) — "half the work" of statistics + ML:**
- ⭐ **Calling Bullshit** — Bergstrom & West (Univ. of Washington). *The* modern companion to Triola §1-4. **Free full course** (syllabus, readings, case studies, videotaped lectures) at [callingbullshit.org](https://www.callingbullshit.org/) + [syllabus](https://www.callingbullshit.org/syllabus.html); also a 2020 book. Rigorous about *reasoning* (not a shallow technical course), so it qualifies as a real source, not just a complement. **Candidate for its own `/literature` note.** Pairs with [[common-misuses-of-statistics]].
- 📄 [Misuse of statistics — Wikipedia](https://en.wikipedia.org/wiki/Misuse_of_statistics) — well-organized taxonomy to cross-check [[common-misuses-of-statistics]] against.
- 📄 [The misuse and abuse of statistics in biomedical research (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4401313/) — peer-reviewed examples of these errors in real published science.
- 🌐 [Statistics By Jim — Observational Study vs Experiment](https://statisticsbyjim.com/basics/observational-study-vs-experiment/) — clearest free explainer; pairs with [[observational-study-vs-experiment]].
- 🌐 [Columbia Irving Institute — Choosing a Study Design](https://irvinginstitute.columbia.edu/choosing-study-design) (with video) and [IWH — Observational vs. experimental](https://www.iwh.on.ca/what-researchers-mean-by/observational-vs-experimental-studies) — design-selection + why randomization licenses causal claims; pair with [[types-of-observational-studies]].
- *Framing:* Ch. 1 (design + misuse) is **half the discipline** — it decides whether the inferential half means anything. Same law as data-centric AI: data quality beats model cleverness ("garbage in, garbage out").

---

### T4: Supervised ML — STARTED (8/~16 notes)

> *Why*: The core of predictive modeling. Build from scratch before using libraries.

> ⚠️ **Source caveat**: 7 of the 8 notes come from the **Platzi "Fundamentos de ML" course** (practical companion → orientation, not mastery). [[logistic-regression]] is the first note derived from a theory source (ISLR Ch. 4). The remaining algorithm notes need ISLR/ESL/Bishop as origin.

**Done — orientation (Platzi companion, all seed):**
- [x] Types of Machine Learning (supervised / unsupervised / RL taxonomy)
- [x] Supervised Learning (overview)
- [x] Supervised Learning Algorithms (survey)
- [x] Feature Engineering · Feature Scaling · One-Hot Encoding

**Done — theory-derived:**
- [x] Logistic Regression ← NEW (ISLR Ch. 4; links forward to the not-yet-written [[cross-entropy]] and [[linear-regression]])

**Remaining — the deep, derive-and-implement notes:**
- [ ] Linear Regression (closed-form + gradient descent, normal equations) ← NEXT — [[least-squares]] already exists; [[logistic-regression]] links to it
- [ ] Bias-Variance Tradeoff
- [ ] Regularization (L1/L2, Ridge, Lasso)
- [ ] Decision Trees (Gini / entropy splits)
- [ ] K-Nearest Neighbors
- [ ] Naive Bayes — direct application of [[bayes-theorem]]
- [ ] Support Vector Machines (needs Lagrange multipliers from T2)
- [ ] Generalized Linear Models ← added 2026-10-03 — unifies linear/logistic/Poisson regression under one MLE framework

**Remaining — data preparation (Platzi gaps, theory-first):**
- [ ] Missing Data Imputation (MCAR / MAR / MNAR)
- [ ] Data Preprocessing pipeline
- [ ] Feature Selection (filter / wrapper / embedded)

---

### T4b: Model Evaluation — NOT STARTED (0/~8 notes) ← NEW TRACK 2026-10-03

> *Why*: The vault has a `02-machine-learning/evaluation/` folder but the roadmap never had a track for it. Evaluation is how you know whether *any* model works — and it's the direct application of T3's sampling and inference notes.

- [ ] Train / Validation / Test Split — the generalization contract (ties to [[random-sample-vs-simple-random-sample]])
- [ ] Cross-Validation (k-fold, stratified, time-series split)
- [ ] Data Leakage — target leakage, train/test contamination (already mentioned in [[feature-scaling]] and [[feature-engineering]])
- [ ] Regression Metrics (MAE, MSE, RMSE, R²)
- [ ] Confusion Matrix, Precision, Recall, F1
- [ ] ROC-AUC and PR-AUC — threshold-independent evaluation
- [ ] Probability Calibration (reliability diagrams, Brier score)
- [ ] Class Imbalance (resampling, class weights, threshold tuning)

---

### T5: Unsupervised ML — STARTED, ORIENTATION ONLY (1/~6 notes)

**Done:** [x] Unsupervised Learning (overview — Platzi companion, seed)

- [ ] K-Means Clustering
- [ ] Hierarchical Clustering and DBSCAN
- [ ] Principal Component Analysis (PCA) — derive from [[spectral-decomposition]] / [[singular-value-decomposition]]
- [ ] t-SNE and UMAP
- [ ] Anomaly Detection
- [ ] Gaussian Mixture Models and EM ← added 2026-10-03 — soft clustering; EM is a core latent-variable algorithm

---

### T6: Ensemble Methods — NOT STARTED (0/~4 notes)

- [ ] Bagging, Bootstrap, Random Forests
- [ ] Boosting (AdaBoost, Gradient Boosting)
- [ ] XGBoost / LightGBM / CatBoost
- [ ] Stacking and Blending

---

### T6b: Time Series — NOT STARTED (0/~4 notes) ← NEW TRACK 2026-10-03

> *Why*: Most business data (sales, HR attrition, sensors, finance) is temporal, and the i.i.d. assumption behind T4 breaks here. [[time-series-graph]] exists, but there's no modeling yet.

- [ ] Stationarity, Trend, Seasonality, Autocorrelation
- [ ] ARIMA / Exponential Smoothing
- [ ] Forecasting with ML (lag features, time-series CV)
- [ ] Forecast Evaluation (MAPE, backtesting)

---

### T7: Deep Learning Fundamentals — NOT STARTED (0/~7 notes)

> *Why*: Build neural networks from scratch before using frameworks.

- [ ] Perceptron and Multilayer Perceptron
- [ ] Activation Functions (ReLU, Sigmoid, Tanh, GELU)
- [ ] Forward and Backpropagation
- [ ] Loss Functions (MSE, Cross-Entropy, Focal Loss)
- [ ] Optimizers (SGD, Adam, AdaGrad)
- [ ] Batch Normalization, Dropout, Weight Init
- [ ] Vanishing/Exploding Gradients

---

### T8: CNNs and RNNs — NOT STARTED (0/~5 notes)

- [ ] Convolution Operation and Pooling
- [ ] CNN Architectures (LeNet → ResNet)
- [ ] Transfer Learning
- [ ] Vanilla RNN, LSTM, GRU
- [ ] Sequence-to-Sequence Models

---

### T9: Transformers and Attention — NOT STARTED (0/~6 notes)

> *Why*: THE architecture behind modern AI. Everything leads here.

- [ ] Attention Mechanism (Scaled Dot-Product)
- [ ] Self-Attention and Multi-Head Attention
- [ ] Positional Encoding
- [ ] Transformer Architecture (Encoder-Decoder)
- [ ] BERT, GPT, and the Encoder/Decoder Split
- [ ] Vision Transformers (ViT)

---

### T10: LLM Internals — BARELY STARTED (1/~10 notes)

- [x] Constitutional AI (HHH + RLAIF) — from Claude 101 Lesson 1, theory-first (Bai et al. 2022)
- [ ] Language Modeling (autoregressive vs masked)
- [ ] Tokenization (BPE, WordPiece, SentencePiece)
- [ ] Decoding and Sampling (temperature, top-k, top-p) ← added 2026-10-03 — what every API `temperature` parameter actually does
- [ ] Scaling Laws
- [ ] Context Windows and KV-Cache
- [ ] Mixture of Experts ← added 2026-10-03 — the frontier-models landscape note mentions MoE for Grok / DeepSeek
- [ ] RLHF and DPO (alignment) — needs T11 RL basics for the PPO half
- [ ] Fine-Tuning: Full vs LoRA/QLoRA
- [ ] Quantization and Distillation ← added 2026-10-03 — how open-weight models run on real hardware

---

### T11: Reinforcement Learning — NOT STARTED (0/~5 notes) ← NEW TRACK 2026-10-03

> *Why*: [[types-of-machine-learning]] names RL as one of the three paradigms, and RLHF / PPO / GRPO (T10) is how frontier LLMs are aligned and trained to reason — yet the roadmap had no RL track at all. Source: Sutton & Barto (free PDF).

- [ ] Markov Decision Processes (states, actions, rewards, discount)
- [ ] Value Functions and the Bellman Equation
- [ ] Q-Learning and Exploration vs. Exploitation (multi-armed bandits)
- [ ] Policy Gradients (REINFORCE)
- [ ] PPO and GRPO — the algorithms behind RLHF and reasoning models

---

### T12: Generative Models — NOT STARTED (0/~4 notes) ← NEW TRACK 2026-10-03

> *Why*: Transformers cover text generation, but image/audio/video generation runs on different math. The multivariate normal and KL divergence (T3) are the prerequisites.

- [ ] Autoencoders and Variational Autoencoders (ELBO, reparameterization trick)
- [ ] Generative Adversarial Networks
- [ ] Diffusion Models (forward noise, reverse denoising, score matching)
- [ ] Multimodal Models (CLIP, vision-language models)

---

## FOUNDATIONS GAP TRACKS ← NEW 2026-10-03

> The vault structure has `01-foundations/algorithms-and-data-structures/` and `01-foundations/databases/`, but the roadmap never gave them a track. They are prerequisites for B7 (data engineering), B9 (system design), and technical interviews.

### F1: Algorithms & Data Structures — NOT STARTED (0/~8 notes)

- [ ] Big-O and Complexity Analysis
- [ ] Arrays, Hash Tables, and Sets (why dict lookup is O(1))
- [ ] Trees and Heaps (BSTs, priority queues — used in beam search, k-NN)
- [ ] Graphs: BFS, DFS, shortest paths (knowledge graphs, agent planning, ONA)
- [ ] Sorting and Searching (binary search)
- [ ] Dynamic Programming (Viterbi, edit distance, sequence alignment)
- [ ] Approximate Nearest Neighbors (HNSW, IVF, LSH) — **the algorithm inside every vector DB** (B4)
- [ ] Recursion and Divide-and-Conquer

### F2: Databases — NOT STARTED (0/~6 notes)

- [ ] Relational Model and SQL Fundamentals (joins, group by)
- [ ] Normalization (1NF → 3NF) vs. Denormalization
- [ ] Indexes (B-trees) and Query Plans
- [ ] Transactions and ACID
- [ ] NoSQL Families (document, key-value, column, graph)
- [ ] Vector Databases as a database category (bridge to B4)

---

## BUILDER TRACK

### B1: LLM APIs & Claude Platform — CORE DONE, Claude 101 gaps open

- [x] Anthropic Claude API
- [x] OpenAI API
- [x] Claude Code
- [x] Claude Code Agent Teams
- [x] Claude Code Hooks
- [x] Claude Code Cron Jobs
- [x] Claude Code + Chrome
- [x] Model Context Protocol
- [x] Claude Agent SDK
- [x] OpenAI Codex
- [x] OpenAI Agents SDK

**Remaining — Claude 101 gaps (product-course companions):**
- [ ] AI Fluency Framework (Lesson 3)
- [ ] Claude Work Modes: Chat / Cowork / Code (Lesson 4)
- [ ] Claude Projects (Lesson 5) · Claude Artifacts (Lesson 6) · Claude Skills (Lesson 7)
- [ ] Claude Connectors + Enterprise Search (Lessons 8–9)
- [ ] Claude Research Mode (Lesson 10)

---

### B2: Prompt Engineering — STARTED (3/~7 notes)

- [x] Prompt Engineering Fundamentals (stage → task → rules) ← NEW
- [x] Claude Context Layers (stateless model, five context scopes) ← NEW
- [x] Iterative Prompt Refinement ← NEW (uncommitted)
- [ ] Prompt Design Patterns (zero-shot, few-shot, chain-of-thought)
- [ ] Structured Output (JSON mode, function calling)
- [ ] System Prompts and Guardrails
- [ ] Context Engineering ← added 2026-10-03 — managing what goes in the window for long-running agents (compaction, retrieval, memory)
- [ ] **Project**: Structured data extractor

---

### B3: LLM Providers Landscape — NOT STARTED (0/~6 notes)

- [ ] Provider Comparison (Claude vs GPT vs Gemini vs Mistral vs LLaMA)
- [ ] Google Gemini API · xAI Grok API · DeepSeek API ← from the frontier-models landscape gaps
- [ ] Open-Weight vs Closed Models (cost, privacy, control vs. capability)
- [ ] Pricing and Cost Optimization (prompt caching, batching, model tiering)
- [ ] Model Selection Framework
- [ ] **Project**: Multi-provider router

---

### B4: Embeddings & Vector Search — NOT STARTED

- [ ] Embedding Models (OpenAI, Cohere, open-source)
- [ ] Vector Databases (Chroma, Pinecone, Qdrant)
- [ ] **Project**: Semantic search over your own vault

---

### B5: RAG Pipeline — NOT STARTED

- [ ] RAG Architecture
- [ ] Chunking Strategies
- [ ] Retrieval (dense, sparse, hybrid)
- [ ] Reranking and Evaluation
- [ ] **Project**: RAG chatbot over this vault

---

### B6: Cloud Infrastructure for AI & Data — STARTED via Microsoft Fabric (3 notes)

> *Why*: Knowing the math and code is not enough — you need to ship. Cloud platforms are where ETL pipelines run, models get served, and AI systems live in production.

#### AWS
- [ ] Core services overview (S3, EC2, IAM, VPC)
- [ ] AWS Glue — managed ETL, PySpark, crawlers, data catalog
- [ ] AWS Lambda — serverless functions, event-driven ETL triggers
- [ ] AWS SageMaker — training jobs, endpoints, model registry, pipelines
- [ ] Amazon Bedrock — managed LLM APIs (Claude, Llama, Titan) in AWS
- [ ] Amazon Redshift + Athena — data warehousing and S3 querying
- [ ] AWS Step Functions — orchestrating multi-step ML workflows
- [ ] ECR + ECS / EKS — containerized model serving
- [ ] **Project**: Deploy a FastAPI model endpoint on SageMaker

#### Microsoft Azure / Fabric (companion: Udemy *Microsoft Fabric — La formación completa*, ~28%)
- [x] Microsoft Fabric overview — unified analytics: Data Engineering, Data Science, Data Warehouse, Real-Time Analytics ← NEW
- [x] Fabric Access and Trial (Entra ID identity + capacity) ← NEW
- [x] Fabric Workspace (items, roles, license modes) ← NEW
- [ ] Fabric Lakehouses and OneLake — Delta Lake-based unified storage
- [ ] Fabric Pipelines and Dataflows Gen2 — ETL/ELT with drag-and-drop + PySpark
- [ ] Fabric Data Warehouse + SQL analytics endpoint
- [ ] Power BI semantic models + DirectLake
- [ ] 🎯 **Milestone**: DP-600 (Fabric Analytics Engineer) / DP-700 (Fabric Data Engineer) certification ← added 2026-10-03
- [ ] Azure Machine Learning — experiment tracking, model registry, endpoints
- [ ] Azure OpenAI Service — GPT-4, embeddings, DALL-E on Azure
- [ ] Azure Data Factory — enterprise ETL orchestration
- [ ] **Project**: Build an ETL pipeline in Microsoft Fabric from raw data to gold layer

#### GCP (Google Cloud)
- [ ] BigQuery — serverless data warehouse, SQL + ML
- [ ] BigQuery ML — train models directly in SQL
- [ ] Vertex AI — unified ML platform (training, tuning, serving, pipelines)
- [ ] Cloud Functions + Pub/Sub — event-driven data pipelines
- [ ] **Project**: Train and serve a model on Vertex AI

#### Cross-Platform Tools
- [ ] Docker — containerize ML models and ETL jobs
- [ ] Apache Airflow — workflow orchestration for data pipelines
- [ ] dbt (data build tool) — SQL transformations, testing, lineage
- [ ] MLflow — experiment tracking, model registry (works on any cloud)
- [ ] Terraform — infrastructure as code (provision cloud resources)
- [ ] **Project**: Containerize a model + Airflow DAG for automated retraining

---

### B7: Data Engineering — NOT STARTED ← NEW (medium-high level)

> *Why*: AI systems run on data pipelines. An AI architect who can't build and debug a data pipeline is blocked at the first step. Medium-high means: beyond basic SQL, into distributed processing, real-time systems, and production-grade pipeline design.

#### Foundations
- [ ] Advanced SQL — window functions, CTEs, query optimization, execution plans
- [ ] Data modeling — star schema, dimensional modeling, data vault 2.0
- [ ] OLAP vs OLTP — when each applies and why
- [ ] Columnar storage — Parquet, ORC, why they're faster for analytics
- [x] Medallion architecture — Bronze / Silver / Gold layers, data quality tiers ← NEW (uncommitted)
- [ ] Lakehouse vs. Data Warehouse — schema-on-read vs. schema-on-write (Fabric course gap)
- [ ] Data Lake (and OneLake as one implementation) (Fabric course gap)
- [ ] ETL vs. ELT (Fabric course gap)

#### Batch Processing
- [ ] Apache Spark fundamentals — RDDs, DataFrames, lazy evaluation, DAG
- [ ] PySpark — data transformations, joins, aggregations, UDFs
- [ ] dbt (data build tool) — SQL transformations, testing, lineage, docs
- [ ] Airflow — DAGs, operators, sensors, XComs, production scheduling
- [ ] **Project**: Build a full Bronze→Gold pipeline with PySpark + dbt + Airflow

#### Streaming & Real-Time
- [ ] Apache Kafka fundamentals — topics, partitions, producers, consumers, offsets
- [ ] Kafka Connect + Schema Registry — integrating data sources
- [ ] Spark Structured Streaming — micro-batch, watermarking, stateful ops
- [ ] Real-time vs near-real-time vs batch — design trade-offs
- [ ] **Project**: Real-time feature store ingestion pipeline with Kafka + Spark Streaming

#### Lakehouse & Storage
- [ ] Delta Lake — ACID transactions on data lakes, time travel, schema evolution
- [ ] Apache Iceberg — table format, partition evolution, hidden partitioning
- [ ] Data contracts — schema agreements between producers and consumers
- [ ] Data quality — Great Expectations, Soda, unit testing pipelines
- [ ] **Project**: Migrate a raw S3 / ADLS lake to Delta Lake with data quality checks

#### Data Warehousing
- [ ] Snowflake architecture — virtual warehouses, clustering, micro-partitions
- [ ] BigQuery internals — Dremel, columnar storage, slot-based billing
- [ ] Redshift — distribution keys, sort keys, VACUUM, ANALYZE
- [ ] Query optimization — explain plans, materialized views, partitioning

---

### B8: C++ and Low-Level ML — NOT STARTED ← NEW

> *Why*: Python is a thin wrapper over C/C++. Understanding what happens at the machine level makes you a better ML engineer — you understand why CUDA kernels matter, what memory layout means for performance, and how to write custom ops for PyTorch or TensorFlow.

#### C++ Fundamentals
- [ ] Types, variables, functions, control flow — the basics vs Python differences
- [ ] Pointers and references — the core of C++ memory model
- [ ] Stack vs heap — where data lives, when to use which
- [ ] Manual memory management — `new`/`delete`, memory leaks, valgrind
- [ ] Smart pointers — `unique_ptr`, `shared_ptr`, `weak_ptr` (RAII pattern)
- [ ] **Project**: Implement a dynamic array (std::vector clone) from scratch

#### Intermediate C++
- [ ] Classes and OOP — constructors, destructors, copy/move semantics
- [ ] Templates — generic programming, type traits
- [ ] STL containers — vector, map, unordered_map, deque — when to use each
- [ ] Concurrency — `std::thread`, mutexes, atomics, race conditions
- [ ] **Project**: Thread-safe matrix multiplication with manual memory layout

#### Performance C++
- [ ] Cache hierarchy — L1/L2/L3, cache lines, false sharing
- [ ] Memory layout — row-major vs column-major, struct of arrays vs array of structs
- [ ] SIMD intrinsics — AVX/SSE, vectorized operations
- [ ] Profiling — perf, gprof, Valgrind/cachegrind, Instruments
- [ ] **Project**: Hand-optimized GEMM (matrix multiply) beating naive implementation

#### C++ for ML
- [ ] ONNX Runtime — load and run model inference in C++
- [ ] LibTorch (PyTorch C++ API) — tensors, autograd, custom ops
- [ ] TensorRT — NVIDIA inference optimizer, layer fusion, INT8 quantization
- [ ] Writing custom CUDA kernels — threads, blocks, shared memory, warps
- [ ] **Project**: Custom attention kernel in CUDA faster than naive PyTorch

---

### B9: Software Engineering & System Design for DS/AI — NOT STARTED ← NEW

> *Why*: Knowing the math and the tools is not enough — you need to write production-quality code and design systems that scale. This track covers the engineering practices that separate a data scientist who can prototype from one who can build and own a production AI system.

#### Software Engineering for DS/AI
- [ ] Python best practices — type hints, dataclasses, virtual environments, packaging (`pyproject.toml`)
- [ ] Clean code for data science — naming, modularity, avoiding notebook anti-patterns
- [ ] Testing ML code — unit tests (pytest), data validation tests, model behavior tests
- [ ] API design with FastAPI — REST endpoints, request/response schemas, async handlers
- [ ] Design patterns for ML — pipeline pattern, strategy pattern, factory pattern applied to models
- [ ] Git workflows for ML — branching, versioning models + data, PR practices
- [ ] Documentation — docstrings, mkdocs, auto-generated API docs
- [ ] **Project**: Refactor a notebook-based ML project into a clean, tested Python package

#### System Design for AI/ML
- [ ] Distributed systems basics — CAP theorem, consistency vs availability, partitioning
- [ ] Database selection — SQL vs NoSQL vs Vector DB — when to use each
- [ ] Caching strategies — Redis, cache invalidation, TTL, write-through vs write-back
- [ ] Message queues — Kafka vs RabbitMQ vs SQS — event-driven architectures
- [ ] Microservices vs monolith — trade-offs for AI systems, service boundaries
- [ ] Load balancing and horizontal scaling — stateless services, session management
- [ ] **Project**: Design a scalable ML prediction service — handle 10K requests/second

#### ML System Design (interviews + production)
- [ ] Feature stores — online vs offline, point-in-time correctness (Feast, Tecton, Hopsworks)
- [ ] Model serving architectures — REST vs gRPC, batch vs real-time, shadow mode
- [ ] A/B testing infrastructure — traffic splitting, experiment tracking, statistical significance
- [ ] Data versioning — DVC, Delta Lake time travel, reproducible pipelines
- [ ] Experiment tracking — MLflow, Weights & Biases, managing runs at scale
- [ ] ML system design interview framework — requirements → data → model → serving → monitoring
- [ ] **Project**: Design an end-to-end recommendation system (design doc + implementation skeleton)

---

### B10: Tool Use & Agents — NOT STARTED (0/~8 notes) ← fleshed out 2026-10-03

> *Why*: This was an empty stub, yet "orchestrate intelligent systems" is the core of the stated goal. The SDK notes in B1 explain *which tool*; this track explains *how agents work and how to design them*. Sources: Anthropic's "Building Effective Agents", the ReAct paper, Lilian Weng's "LLM Powered Autonomous Agents".

- [ ] Tool Use / Function Calling — the request → tool call → result loop
- [ ] The Agent Loop (ReAct: reason → act → observe)
- [ ] Workflow Patterns vs. Agents (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer)
- [ ] Agent Memory (short-term context, long-term stores, summarization)
- [ ] Planning and Task Decomposition
- [ ] Multi-Agent Orchestration (supervisor, handoffs, shared state) — links [[claude-code-agent-teams]], [[openai-agents-sdk]]
- [ ] LangGraph (stateful agent graphs) — named in CLAUDE.md's stack, no note yet
- [ ] Human-in-the-Loop and Permissioning
- [ ] **Project**: A research agent over this vault with tool use + memory

### B11: LLM Evaluation & Observability — NOT STARTED (0/~5 notes)

- [ ] LLM Evaluation Fundamentals (offline evals, golden datasets, regression suites)
- [ ] LLM-as-a-Judge (and its biases)
- [ ] RAG Evaluation (faithfulness, context precision/recall — RAGAS)
- [ ] Agent Evaluation (task success, trajectory evals)
- [ ] Tracing and Observability (LangSmith, Langfuse, OpenTelemetry)

### B12: MLOps — STARTED (1/~6 notes)

- [x] Python and Jupyter Environment Setup
- [ ] Model Packaging and Serving (FastAPI, batch vs. online)
- [ ] Model Monitoring (data drift, concept drift, performance decay)
- [ ] CI/CD for ML (tests on data + model, automated retraining)
- [ ] Model Registry and Versioning (MLflow)
- [ ] LLMOps differences (prompt versioning, cost/latency monitoring)

### B13: AI Safety, Security & Responsible AI — NOT STARTED (0/~5 notes) ← NEW TRACK 2026-10-03

> *Why*: Anyone shipping agents that read untrusted input and call tools needs this — it's a design constraint, not an afterthought. [[constitutional-ai]] covers training-time alignment; this covers deploy-time risk.

- [ ] Prompt Injection (direct and indirect) and Defenses
- [ ] Jailbreaks and Guardrails (input/output filtering)
- [ ] Hallucination — causes, detection, and mitigation (grounding, citations)
- [ ] Fairness and Bias in ML (generalizes [[bias-in-people-analytics]])
- [ ] Data Privacy (PII handling, GDPR basics) and the AI Regulation landscape (EU AI Act)

---

## HUMAN SKILLS TRACK (soft, social & leadership) — NOT STARTED ← NEW

> *Why*: The title is **AI architect and engineer** — and "architect" is a role played *on a team*. The hardest part of shipping intelligent systems end-to-end is rarely the math; it's aligning people, communicating trade-offs to non-experts, earning trust, and leading without authority. These skills compound over a career the way linear algebra compounds over the theory track — and unlike a framework, they never get deprecated. This track wraps *around* Theory + Builder: every technical skill is amplified or bottlenecked by how well you can explain it, collaborate on it, and lead with it.
>
> *Where these notes live*: a new **`09-professional-skills/`** folder (to be created when the first note lands). These are permanent notes like any other — atomic, linked, with a TL;DR and exercises (here "exercises" = concrete practice: run a retro, give a code review, present a design). Sources will be books/talks, not textbooks. This track is **deliberately lighter-weight** than T1–T10: read, reflect, practice on the job — not derive-from-scratch.

### H1: Communication
- [ ] Technical writing — design docs, RFCs, clear PR descriptions, writing for skimmers
- [ ] Explaining complex ideas to non-experts — the "explain it to a PM / exec" skill (analogy-first, like this vault's own notes)
- [ ] Presenting and public speaking — structuring a talk, slides that don't distract, handling Q&A
- [ ] **Meeting presence & speaking up** — "executive presence" (gravitas): being heard in meetings without dominating. High-leverage tactics: speak in the first 5 min, walk in with one prepared point, ask a sharp question, slow down + pause, "build on" others. *(Personal priority — flagged as a current gap.)*
- [ ] Asynchronous communication — writing so a distributed/remote team stays unblocked without a meeting
- [ ] **Practice**: write a one-page design doc for a real feature and get it reviewed; commit to speaking once in the first 5 minutes of your next 3 meetings

### H2: Collaboration & Teamwork
- [ ] Code review etiquette — giving and receiving feedback without ego (both sides of the PR)
- [ ] Pair / mob programming — thinking out loud, sharing the keyboard
- [ ] Cross-functional work — collaborating with product, design, data, and non-technical stakeholders
- [ ] Working agreements & team norms — how healthy teams decide how they work
- [ ] **Practice**: run or actively participate in a sprint retrospective

### H3: Leadership & Influence
- [ ] Leading without authority — influence, persuasion, building consensus as an IC
- [ ] Technical decision-making — trade-off analysis, disagree-and-commit, documenting the "why"
- [ ] Mentoring and coaching — growing more junior engineers, the Socratic teaching style
- [ ] Ownership and accountability — taking responsibility for outcomes, not just tasks
- [ ] Driving alignment — getting a group to a shared goal when opinions diverge
- [ ] **Practice**: mentor someone on one concept from this vault; own a small project end-to-end

### H4: Emotional Intelligence & Social Skills
- [ ] Active listening — understanding before responding, asking better questions
- [ ] Empathy and perspective-taking — reading the room, understanding others' constraints
- [ ] Giving and receiving feedback — SBI (Situation-Behavior-Impact), radical candor
- [ ] Conflict resolution — disagreeing productively, de-escalation, finding shared interests
- [ ] Self-awareness & regulation — knowing your triggers, staying calm under pressure
- [ ] **Practice**: give one piece of structured feedback using SBI this week

### H5: Business & Stakeholder Acumen
- [ ] Translating technical work into business value — outcomes and ROI, not features
- [ ] Product thinking — user needs, MVPs, why-before-what
- [ ] Managing expectations — scoping, estimating honestly, saying no well
- [ ] Working with leadership — reporting up, making the ask, surfacing risk early
- [ ] **Practice**: reframe one vault project as a business case (problem → value → cost)

### H6: Personal Effectiveness
- [ ] Time management & prioritization — deep work, Eisenhower matrix, saying no to protect focus
- [ ] Learning how to learn — spaced repetition, deliberate practice (this vault *is* this skill)
- [ ] Handling ambiguity — making progress without complete information
- [ ] Growth mindset & resilience — treating failures as data, sustainable pace over burnout
- [ ] **Practice**: run a weekly personal review; timebox one deep-work block daily

**Reading resources (this track's "textbooks"):**
- 📘 **Crucial Conversations** — Patterson et al. — the standard for high-stakes discussions (pairs with H4).
- 📘 **Radical Candor** — Kim Scott — care personally + challenge directly; feedback and management (H3, H4).
- 📘 **The Manager's Path** — Camille Fournier — the tech IC→lead→manager progression; excellent even if you stay IC (H3).
- 📘 **Made to Stick** — Chip & Dan Heath — why some ideas land; the communication craft (H1).
- 📘 **Executive Presence** — Sylvia Ann Hewlett — the definitive book on *meeting presence / gravitas*: how you're perceived, how you speak, how you show up (H1). Direct fit for the "speaking up in meetings" gap.
- 🎥 **Think Fast, Talk Smart** — Matt Abrahams (Stanford GSB podcast + videos) — speaking spontaneously under pressure; *the* resource for the meeting-presence problem (H1).
- 🎥 **"How to Speak" — Patrick Winston (MIT, full lecture on YouTube)** — commanding a room, engineer-friendly and tactical (H1).
- 🎥 **Amy Cuddy — "Your body language may shape who you are"** (TED) — posture/presence and confidence (H1, H4).
- 📘 **Thinking, Fast and Slow** — Kahneman — cognitive biases; foundational for decision-making and EQ (H4, H5).
- 📘 **The Staff Engineer's Path** — Tanya Reilly — leading and influencing as a senior IC (H3, H5).
- 🎥 *Free*: MIT 6.UAR / "Patterns for Effective Communication"; conference talks on staff-engineering archetypes; LeadDev talks (leadership for engineers).

---

## SIDE TRACK (outside core AI architect path)

### S1: Applied Domains — People Analytics (17 notes, all seed) — course complete

> Not part of the theory or builder tracks above — this is domain knowledge (HR/people analytics) tied to the Platzi "People Analytics con Excel" course. Tracked here so it doesn't get lost, but it shouldn't compete with T1–T10 for study time unless there's a specific reason (e.g., a work project applying ML to HR data). The course (13 classes) is now fully captured in [[platzi-people-analytics-excel]].

**Fundamentals & culture:**
- [x] People Analytics (overview)
- [x] People Analytics — Employee Lifecycle
- [x] Data-Driven Culture
- [x] HR Data Types
- [x] HR Data Ethics

**Running a project:**
- [x] People Analytics — Project Framework (8 steps, 4 analytics levels, knowledge map)
- [x] Impact Evaluation in People Analytics
- [x] Bias in People Analytics
- [x] Data Cleaning for People Analytics

**Data, KPIs, and dashboards (Excel-heavy):**
- [x] KPI Design
- [x] HR Dashboard in Excel

**Qualitative & survey analysis:**
- [x] Employee Satisfaction Survey Analysis (VLOOKUP, pivot tables, NPS)
- [x] Likert Scale (ordinal scale, Cronbach's alpha)
- [x] Exit Interview NLP Analysis (4-phase pipeline: clean → quantitative → NLP → sentiment)

**Long-term strategy:**
- [x] People Analytics Strategy Pillars (David Green — bases/resources/added-value)
- [x] AI in HR Applications (ATS, text analysis, ONA)
- [x] People Analytics Best Practices (peer monitoring, sharing, feedback)

**Open question, now more concrete**: several notes already draw the bridge back to core ML — [[exit-interview-nlp-analysis]] connects to embeddings/clustering/sentiment classifiers, [[ai-in-hr-applications]]'s ONA section is applied graph theory, and [[likert-scale]]'s Cronbach's-alpha code is a real feature-reliability check. A natural next step is a **06-projects capstone**: an attrition-prediction or exit-interview-sentiment mini-project in `06-projects/` that actually implements one of these (e.g. the ONA networkx example, or a lexicon/transformer sentiment classifier on synthetic exit-interview text) — this would also start filling the empty `code/` directory (see hygiene gap above) and double as the first T4/T5 bridge project once supervised/unsupervised ML notes exist.

---

## Parallel Schedule

```
Weeks 1-3   | Linear Algebra (✓ done)          | B1: APIs (✓ done)
Weeks 4-5   | Calculus (✓ core done)            | B2: Prompt engineering (started)
Weeks 6-12  | Probability: Triola Ch.1-6 (now)  | B6: Fabric course (started, ~28%)
Weeks 13-15 | Triola Ch.6 rest + Ch.7-8 (CLT, CIs, tests) + MLE | B3: Providers landscape
Weeks 16-17 | Info theory + Triola Ch.9-10       | B4: Embeddings + vector DBs (+F1 ANN)
Weeks 18-20 | Supervised ML + T4b Evaluation    | B5: RAG pipeline
Weeks 21-22 | Unsupervised + Ensemble           | B10: Tool use & agents
Weeks 23-25 | Deep Learning Fundamentals        | B11: LLM evals + B7-DE: SQL/Spark/dbt
Weeks 26-27 | CNNs + RNNs                       | B7-DE: Kafka + streaming
Weeks 28-29 | Transformers                      | B12: MLOps + B13 safety
Weeks 30-31 | LLM Internals + RL basics (T11)   | B8-C++: Fundamentals + memory
Weeks 32-34 | Fine-tuning + RLHF + Generative   | B8-C++: Performance + CUDA
Weeks 35+   | Capstone projects                 | B9: System design
```

---

## What to Do Right Now

**Immediate priorities (theory):**

1. **Finish Triola Ch. 6** — `/note sampling-distributions-and-estimators` (§6-4), then `/note central-limit-theorem` (§6-5). The CLT is the single most important missing note: every confidence interval and hypothesis test in Ch. 7–12 rests on it. Then §6-6 (normal quantile plots) and §6-7 (normal approximation to the binomial). ~4 notes, closes the chapter you're in the middle of.
2. **`/review` pass on the probability cluster** — 0 notes were promoted this cycle while 35 were added. Before building inference on top, promote the load-bearing ones (conditional-probability, bayes-theorem, random-variable, expected-value, standard-normal-distribution) from seed → growing.
3. **Triola Ch. 7–8** — confidence intervals, t distribution, hypothesis testing and p-values. This finally gives [[statistical-significance]] its formal machinery.
4. `/note maximum-likelihood-estimation` + `/note cross-entropy-and-kl-divergence` — the bridge from probability to ML losses. [[logistic-regression]] already links to `[[cross-entropy]]`, which doesn't exist yet.
5. `/session linear-regression` — derive the normal equations from [[least-squares]] and the MLE/Gaussian-noise view; ideally after Triola Ch. 10 (correlation and regression).
6. Housekeeping: resolve the `matrix-transpose` inbox drafts (open for 4+ audits); write `matrix-calculus` before T7.

**Immediate priorities (builder):**

1. **Finish one open practical course before starting another** — Claude 101 (~20%) is the shortest: 7 small notes (AI fluency, work modes, projects, artifacts, skills, connectors, research).
2. Continue the Fabric course — next: lakehouse-vs-data-warehouse and etl-vs-elt (theory-first), with DP-600/DP-700 as the milestone.
3. `/note prompt-design-patterns` — zero-shot, few-shot, CoT (B2).
4. Then B4 embeddings → B10 agents (the stub that's now a full track).

**Cloud track entry points (B6):**

1. **Docker** first — language-agnostic container skill needed everywhere
2. **AWS Glue + S3** or **Microsoft Fabric Pipelines** depending on job target
3. **SageMaker** or **Azure ML** for model deployment

**Data engineering entry points (B7):**

1. **Advanced SQL** — window functions, CTEs, execution plans (1-2 weeks)
2. **PySpark** — distributed data processing (2-3 weeks, run locally with Docker)
3. **dbt** — SQL transformations and testing on top of any warehouse (1 week)
4. **Apache Kafka** — streaming fundamentals (2 weeks)
5. **Delta Lake** — lakehouse storage layer (1 week)

**C++ entry points (B8):**

1. **Pointers and memory** — start here, everything else depends on it
2. **Smart pointers + RAII** — modern C++ memory safety
3. **Cache and memory layout** — why matrix layout affects ML speed
4. **LibTorch / ONNX Runtime** — run ML models in C++ before writing CUDA
5. **CUDA basics** — GPU threads, blocks, shared memory

**Quality improvements:**
- Promote `singular-value-decomposition` from seed to growing — still the biggest quality gap given how central SVD is to ML (PCA, pseudoinverse, low-rank approximation)
- `spectral-decomposition` promoted seed → growing since last update ✓
- **156 of 190 content notes are still `status/seed`** (was 121/155, before that 78/111) — the seed backlog grew by 35 this cycle and nothing was promoted. Worth a `/review` pass on the load-bearing linear-algebra seeds (subspaces, kernel-and-range, rank-nullity-theorem, diagonalization) and on the new descriptive-statistics cluster before building on top of them
- All 17 people-analytics notes are `status/seed` with zero code — lowest priority for now (side track), but if a 06-projects capstone gets built from this material (see S1 above), promote the notes it exercises to `growing`
- **Vault-wide**: write at least one runnable file in `code/` — right now every single implementation described in every note (Gauss-Jordan, Gram-Schmidt, Cronbach's alpha, ONA centrality, sentiment scoring) exists only as an inline snippet, never as an actual tested `.py` file
