# Study Roadmap

**Created**: 2026-02-24
**Last updated**: 2026-05-02
**Goal**: Become an expert AI architect and engineer — design, implement, and orchestrate intelligent systems end-to-end.

---

## Dual-Track Approach

Two parallel tracks that reinforce each other:

```
THEORY TRACK (left)              BUILDER TRACK (right)
Deep understanding               Real tools, real projects

Linear Algebra ──────────────── → Embeddings & Vector Search use vectors
Calculus ─────────────────────── → Gradient Descent in practice
Probability ──────────────────── → Evaluation metrics, A/B testing
Supervised ML ────────────────── → Scikit-learn pipelines, Kaggle
Neural Networks ──────────────── → PyTorch, HuggingFace models
Transformers ─────────────────── → LLM APIs (OpenAI, Anthropic, Gemini)
Attention Mechanism ──────────── → RAG, prompt engineering, agents

Theory explains WHY things work.
Building shows HOW they work in practice.
Both together = architect.
```

---

## Progress Overview

| Area | Notes | Status |
|------|-------|--------|
| 01-foundations/linear-algebra | 25 | Strong — determinants cluster complete, dot/cross product added |
| 01-foundations/calculus | 6 | Core complete — matrix calculus remaining |
| 01-foundations/probability | 10 | Distributions done — MLE, entropy, multivariate Normal next |
| 01-foundations/algorithms | 0 | Not started |
| 01-foundations/databases | 0 | Not started |
| 02-machine-learning | 0 | Not started |
| 03-deep-learning | 0 | Not started |
| 04-llms-and-agents | 8 | Anthropic + OpenAI ecosystems covered |
| 05-mlops | 0 | Not started |

**Total notes**: 49 | **8 evergreen** | **25 growing** | **16 seed**

**All 49 notes** are on the new layered structure (TL;DR → Intuition → Mechanics → In ML → Exercises).

---

## THEORY TRACK

### T1: Linear Algebra — NEAR COMPLETE (25/~28 notes)

> *Why*: Every ML algorithm is a matrix operation. You can't understand neural nets, PCA, or embeddings without this.

**Done:**
- [x] Vectors and Vector Spaces
- [x] Vector Operations
- [x] Vector Norms
- [x] Dot Product ← new
- [x] Cross Product + Lagrange Identity ← new
- [x] Cosine Similarity
- [x] Linear Combination
- [x] Linear Independence
- [x] Basis and Dimension
- [x] Projection (single vector)
- [x] Projection onto Subspaces
- [x] Gaussian Elimination
- [x] Determinant
- [x] Cofactor ← new
- [x] Adjugate Matrix ← new
- [x] Sarrus' Rule ← new
- [x] Cramer's Rule ← new
- [x] Matrix Operations
- [x] Matrix Inverse
- [x] Special Matrices
- [x] Eigenvalues and Eigenvectors
- [x] Spectral Decomposition
- [x] Singular Value Decomposition
- [x] Gram-Schmidt
- [x] Linear Transformations

**Remaining:**
- [ ] Matrix Calculus (Jacobians, Hessians, dL/dW) — needs calculus track first, CRITICAL for backprop
- [ ] Pseudoinverse (Moore-Penrose) — via SVD, for least-squares
- [ ] Matrix Norms and Condition Number — numerical stability

**Estimated remaining**: ~3 notes

---

### T2: Calculus — CORE COMPLETE (6/~9 notes)

> *Why*: Optimization IS calculus. Gradient descent, backpropagation, loss functions — all calculus.

**Done:**
- [x] Derivatives and Partial Derivatives
- [x] Derivative Rules
- [x] Chain Rule
- [x] Polynomial Factorization
- [x] Gradient Descent
- [x] Optimization (convexity, second derivative test, saddle points)

**Remaining:**
- [ ] Matrix Calculus (Jacobians, Hessians) — CRITICAL before deep learning
- [ ] Taylor Series and Approximations — explains why gradient descent works
- [ ] Integration Basics — needed for probability density derivations

**Estimated remaining**: ~3 notes

---

### T3: Probability and Statistics — IN PROGRESS (10/~18 notes)

> *Why*: ML is applied statistics. Bayesian thinking, distributions, hypothesis testing.

**Done:**
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

**Remaining (priority order):**
- [ ] Maximum Likelihood Estimation (MLE) ← NEXT — derives ALL loss functions from distributions
- [ ] Cross-Entropy and KL Divergence — information theory, classification losses
- [ ] Joint, Marginal, and Conditional Distributions
- [ ] Multivariate Normal Distribution — used in VAEs, Gaussian processes
- [ ] Maximum A Posteriori (MAP)
- [ ] Hypothesis Testing and p-values
- [ ] Bootstrap and Empirical Distributions
- [ ] Tier 2 distributions: Gamma, Chi-Squared, Student's t, Log-Normal

**Estimated remaining**: ~8 notes

---

### T4: Supervised ML — NOT STARTED (0/~8 notes)

> *Why*: The core of predictive modeling. Build from scratch before using libraries.

- [ ] Linear Regression (closed-form + gradient descent, normal equations)
- [ ] Logistic Regression
- [ ] Decision Trees
- [ ] Support Vector Machines
- [ ] K-Nearest Neighbors
- [ ] Naive Bayes
- [ ] Bias-Variance Tradeoff
- [ ] Regularization (L1/L2, Ridge, Lasso)

**Estimated**: ~8 notes, 3 code files

---

### T5: Unsupervised ML — NOT STARTED (0/~5 notes)

- [ ] K-Means Clustering
- [ ] Hierarchical Clustering and DBSCAN
- [ ] Principal Component Analysis (PCA)
- [ ] t-SNE and UMAP
- [ ] Anomaly Detection

---

### T6: Ensemble Methods — NOT STARTED (0/~4 notes)

- [ ] Bagging, Bootstrap, Random Forests
- [ ] Boosting (AdaBoost, Gradient Boosting)
- [ ] XGBoost / LightGBM / CatBoost
- [ ] Stacking and Blending

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

### T10: LLM Internals — NOT STARTED (0/~6 notes)

- [ ] Language Modeling (autoregressive vs masked)
- [ ] Tokenization (BPE, WordPiece, SentencePiece)
- [ ] Scaling Laws
- [ ] Context Windows and KV-Cache
- [ ] RLHF and DPO (alignment)
- [ ] Fine-Tuning: Full vs LoRA/QLoRA

---

## BUILDER TRACK

### B1: LLM APIs — DONE

- [x] Anthropic Claude API
- [x] OpenAI API
- [x] Claude Code
- [x] Claude Code Agent Teams
- [x] Model Context Protocol
- [x] Claude Agent SDK
- [x] OpenAI Codex
- [x] OpenAI Agents SDK

### B2: Prompt Engineering — NOT STARTED

- [ ] Prompt Design Patterns (zero-shot, few-shot, chain-of-thought)
- [ ] Structured Output (JSON mode, function calling)
- [ ] System Prompts and Guardrails
- [ ] **Project**: Structured data extractor

### B3: LLM Providers Landscape — NOT STARTED

- [ ] Provider Comparison (Claude vs GPT vs Gemini vs Mistral vs LLaMA)
- [ ] Pricing and Cost Optimization
- [ ] Model Selection Framework
- [ ] **Project**: Multi-provider router

### B4: Embeddings & Vector Search — NOT STARTED

- [ ] Embedding Models (OpenAI, Cohere, open-source)
- [ ] Vector Databases (Chroma, Pinecone, Qdrant)
- [ ] **Project**: Semantic search over your own vault

### B5: RAG Pipeline — NOT STARTED

- [ ] RAG Architecture
- [ ] Chunking Strategies
- [ ] Retrieval (dense, sparse, hybrid)
- [ ] Reranking and Evaluation
- [ ] **Project**: RAG chatbot over this vault

### B6–B10: Tool Use, Agents, Evaluation, Production, MLOps — NOT STARTED

---

## Parallel Schedule

```
Weeks 1-3   | Linear Algebra (✓ done)     | B1: APIs (✓ done)
Weeks 4-5   | Calculus (✓ done)            | B2: Prompt engineering
Weeks 6-8   | Probability (in progress)    | B3: Providers landscape
Weeks 9-10  | MLE + Information Theory     | B4: Embeddings + vector DBs
Weeks 11-13 | Supervised ML                | B5: RAG pipeline
Weeks 14-15 | Unsupervised + Ensemble      | B6: Tool use
Weeks 16-18 | Deep Learning Fundamentals   | B7: Agent frameworks
Weeks 19-21 | CNNs + RNNs                  | B8: Evaluation
Weeks 22-24 | Transformers                 | B9: Production patterns
Weeks 25+   | LLM Internals                | B10: MLOps + Capstones
```

---

## What to Do Right Now

**Immediate priorities (theory):**

1. `/note maximum-likelihood-estimation` — derives ALL loss functions (MSE, cross-entropy, etc.) from probability. The single most important missing concept.
2. `/note cross-entropy-and-kl-divergence` — information theory, connects to classification losses and VAEs.
3. `/note matrix-calculus` — Jacobians, Hessians, dL/dW. Required before any deep learning.
4. `/session linear-regression` — first ML model, bridges all of foundations → ML.

**Immediate priorities (builder):**

1. Complete Anthropic Skilljar courses
2. `/note prompt-design-patterns` — zero-shot, few-shot, CoT
3. Start B4: embeddings project using this vault

**Quality improvements:**
- Promote `singular-value-decomposition` from seed to growing (add exercises to code file)
- Promote `spectral-decomposition` to evergreen
