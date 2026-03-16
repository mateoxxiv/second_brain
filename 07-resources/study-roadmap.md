# Study Roadmap

**Created**: 2026-02-24
**Last updated**: 2026-03-15
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

| Area | Notes | Code | Status |
|------|-------|------|--------|
| 01-foundations/linear-algebra | 19 | 3 | Near complete (8 evergreen, 9 growing, 2 seed — only matrix calculus remains) |
| 01-foundations/calculus | 0 | 0 | Not started |
| 01-foundations/probability | 0 | 0 | Not started |
| 01-foundations/algorithms | 0 | 0 | Not started |
| 01-foundations/databases | 0 | 0 | Not started |
| 02-machine-learning | 0 | 0 | Not started |
| 03-deep-learning | 0 | 0 | Not started |
| 04-llms-and-agents | 8 | 2 | In progress (Anthropic + OpenAI ecosystems done) |
| 05-mlops | 0 | 0 | Not started |
| 06-projects | 0 | 0 | Not started |

### Linear Algebra Notes Completed

- [x] Vectors and Vector Spaces
- [x] Vector Operations
- [x] Vector Norms
- [x] Cosine Similarity
- [x] Linear Combination
- [x] Linear Independence
- [x] Basis and Dimension
- [x] Projection
- [x] Projection onto Subspaces
- [x] Gaussian Elimination
- [x] Determinant
- [x] Matrix Operations (transpose, multiply, identity)
- [x] Matrix Inverse
- [x] Special Matrices (symmetric, orthogonal, diagonal, singular, positive definite)
- [x] Eigenvalues and Eigenvectors
- [x] Spectral Decomposition
- [x] Singular Value Decomposition (SVD)
- [x] Orthonormal Basis and Gram-Schmidt
- [x] Linear Transformations
- [ ] Matrix Calculus (Jacobians, Hessians)

---

## THEORY TRACK

Deep understanding. Derive, don't memorize. Implement from scratch.

### T1: Linear Algebra (Weeks 1-3) — NEAR COMPLETE

> *Why*: Every ML algorithm is a matrix operation. You can't understand neural nets, PCA, or embeddings without this.

**Done:**
- [x] Vectors and Vector Spaces
- [x] Vector Operations
- [x] Vector Norms
- [x] Cosine Similarity
- [x] Linear Combination
- [x] Linear Independence
- [x] Basis and Dimension
- [x] Projection (single vector)
- [x] Projection onto Subspaces
- [x] Gaussian Elimination
- [x] Determinant

**Recently completed:**
- [x] Gram-Schmidt — #status/growing, session done (projection connection, worked examples)
- [x] Linear Transformations — #status/growing, session done (kernel, image, rank-nullity)
- [x] SVD — #status/seed, session done (recipe, worked example, low-rank approx)
- [x] Spectral Decomposition — #status/growing (knowledge check done)
- [x] Eigenvalues and Eigenvectors — #status/evergreen (8 total)

**Remaining:**
- [ ] Matrix Calculus (Jacobians, Hessians) — needs calculus track first
- [ ] **Code**: SVD for image compression

**Estimated remaining**: ~1 note (after calculus), 1 code file

### T2: Calculus (Weeks 3-4)

> *Why*: Optimization IS calculus. Gradient descent, backpropagation, loss functions — all calculus.

- [ ] Derivatives and Partial Derivatives
- [ ] Chain Rule (critical for backprop)
- [ ] Gradient and Directional Derivatives
- [ ] Optimization: Minima, Maxima, Saddle Points
- [ ] Multivariable Calculus for ML
- [ ] **Code**: Gradient descent from scratch

**Estimated**: ~5 notes, 1 code file

### T3: Probability and Statistics (Weeks 5-7)

> *Why*: ML is applied statistics. Bayesian thinking, distributions, hypothesis testing.

- [ ] Probability Fundamentals (Bayes' Theorem, conditional probability)
- [ ] Probability Distributions (Normal, Bernoulli, Poisson, Uniform)
- [ ] Expectation, Variance, Covariance
- [ ] Maximum Likelihood Estimation (MLE)
- [ ] Maximum A Posteriori (MAP)
- [ ] Hypothesis Testing and p-values
- [ ] Information Theory Basics (Entropy, KL Divergence, Cross-Entropy)
- [ ] **Code**: Distribution visualization and sampling
- [ ] **Code**: MLE from scratch

**Estimated**: ~8 notes, 2 code files

### T4: Supervised ML (Weeks 7-10)

> *Why*: The core of predictive modeling. Build from scratch before using libraries.

- [ ] Linear Regression (closed-form + gradient descent)
- [ ] Logistic Regression
- [ ] Decision Trees
- [ ] Support Vector Machines (SVM)
- [ ] K-Nearest Neighbors (KNN)
- [ ] Naive Bayes
- [ ] Bias-Variance Tradeoff
- [ ] Regularization (L1/L2, Ridge, Lasso, ElasticNet)
- [ ] **Code**: Linear regression from scratch
- [ ] **Code**: Logistic regression from scratch
- [ ] **Code**: Decision tree from scratch

**Estimated**: ~8 notes, 3 code files

### T5: Time Series Analysis and Forecasting (Weeks 10-12) — HIGH PRIORITY

> *Why*: Time-dependent data is everywhere — stock prices, sensor data, demand forecasting, user behavior. Most real-world production ML involves time series. This is a critical skill gap.

- [ ] Time Series Fundamentals (trend, seasonality, stationarity, autocorrelation)
- [ ] Decomposition (additive vs multiplicative, STL decomposition)
- [ ] Classical Methods (ARIMA, SARIMA, exponential smoothing)
- [ ] Feature Engineering for Time Series (lags, rolling stats, calendar features)
- [ ] Evaluation (walk-forward validation, MAPE, RMSE, time-aware splits)
- [ ] ML for Time Series (XGBoost on time features, Prophet)
- [ ] Deep Learning for Time Series (LSTM, Temporal Fusion Transformer, N-BEATS)
- [ ] Multivariate Time Series and Forecasting at Scale
- [ ] **Code**: ARIMA from scratch
- [ ] **Code**: LSTM forecaster in PyTorch
- [ ] **Code**: Feature engineering pipeline for time series

**Estimated**: ~8 notes, 3 code files

### T6: Unsupervised ML (Weeks 12-14)

> *Why*: Clustering, dimensionality reduction, anomaly detection.

- [ ] K-Means Clustering
- [ ] Hierarchical Clustering and DBSCAN
- [ ] Principal Component Analysis (PCA)
- [ ] t-SNE and UMAP
- [ ] Anomaly Detection
- [ ] **Code**: K-Means from scratch
- [ ] **Code**: PCA from scratch + visualization

**Estimated**: ~5 notes, 2 code files

### T7: Ensemble Methods (Weeks 14-15)

> *Why*: Random forests, XGBoost — dominate tabular data.

- [ ] Bagging, Bootstrap, Random Forests
- [ ] Boosting (AdaBoost, Gradient Boosting)
- [ ] XGBoost / LightGBM / CatBoost
- [ ] Stacking and Blending
- [ ] **Code**: Random forest from scratch

**Estimated**: ~4 notes, 1 code file

### T8: Deep Learning Fundamentals (Weeks 16-19)

> *Why*: Build neural networks from scratch before using frameworks.

- [ ] Perceptron and Multilayer Perceptron
- [ ] Activation Functions (ReLU, Sigmoid, Tanh, GELU)
- [ ] Forward and Backpropagation
- [ ] Loss Functions (MSE, Cross-Entropy, Focal Loss)
- [ ] Gradient Descent Variants and Optimizers (SGD, Adam)
- [ ] Batch Normalization, Dropout, Weight Init
- [ ] Vanishing/Exploding Gradients
- [ ] **Code**: Neural network from scratch (NumPy only)
- [ ] **Code**: Same network in PyTorch

**Estimated**: ~7 notes, 2 code files

### T9: CNNs and RNNs (Weeks 19-22)

> *Why*: Vision and sequences. Understanding these makes transformers click.

- [ ] Convolution Operation and Pooling
- [ ] CNN Architectures (LeNet → ResNet)
- [ ] Transfer Learning
- [ ] Vanilla RNN, LSTM, GRU
- [ ] Sequence-to-Sequence Models
- [ ] **Code**: CNN image classifier (PyTorch)
- [ ] **Code**: LSTM text generator (PyTorch)

**Estimated**: ~5 notes, 2 code files

### T10: Transformers and Attention (Weeks 22-25)

> *Why*: THE architecture behind modern AI. Everything leads here.

- [ ] Attention Mechanism (Scaled Dot-Product)
- [ ] Self-Attention and Multi-Head Attention
- [ ] Positional Encoding
- [ ] Transformer Architecture (Encoder-Decoder)
- [ ] BERT, GPT, and the Encoder/Decoder Split
- [ ] Vision Transformers (ViT)
- [ ] **Code**: Attention from scratch
- [ ] **Code**: Minimal transformer in PyTorch

**Estimated**: ~6 notes, 2 code files

### T11: LLM Internals (Weeks 25-27)

> *Why*: Understand what's inside GPT, Claude, LLaMA — not just how to call them.

- [ ] Language Modeling (autoregressive vs masked)
- [ ] Tokenization (BPE, WordPiece, SentencePiece)
- [ ] Scaling Laws
- [ ] Context Windows and KV-Cache
- [ ] RLHF and DPO (alignment)
- [ ] Fine-Tuning: Full vs LoRA/QLoRA
- [ ] **Code**: BPE tokenizer from scratch
- [ ] **Code**: LoRA fine-tuning with HuggingFace

**Estimated**: ~6 notes, 2 code files

---

## BUILDER TRACK

Learn by doing. Use real tools. Ship things. Runs in parallel with Theory.

### B1: Environment & First API Calls (Start: Week 1)

> *Start here on day 1.* You can call an API without understanding transformers.
> **Theory link**: None needed yet — just get your hands dirty.

- [ ] Python Development Setup (venv, pip, project structure)
- [x] LLM API Basics: Anthropic Claude API
- [x] LLM API Basics: OpenAI API
- [ ] API Key Management and .env Best Practices
- [ ] **MUST: [Anthropic Courses (Skilljar)](https://anthropic.skilljar.com/)** — official guided courses on Claude API, prompt engineering, and AI development. Complete before moving to B2.
- [ ] **Project**: Simple chatbot CLI that calls Claude API

**Estimated**: ~3 notes, 1 project

### Anthropic Ecosystem Notes Completed

- [x] Anthropic Claude API (`04-llms-and-agents/apis-and-services/`)
- [x] Claude Code — full feature docs (`04-llms-and-agents/tooling-ecosystem/`)
- [x] Claude Code Agent Teams (`04-llms-and-agents/tooling-ecosystem/`)
- [x] Model Context Protocol (`04-llms-and-agents/integration-patterns/`)
- [x] Claude Agent SDK (`04-llms-and-agents/agent-frameworks/`)
- [x] `code/llms/anthropic_api.py` — 8 demos + 9 exercises

### OpenAI Ecosystem Notes Completed

- [x] OpenAI API (`04-llms-and-agents/apis-and-services/`)
- [x] OpenAI Codex (`04-llms-and-agents/tooling-ecosystem/`)
- [x] OpenAI Agents SDK (`04-llms-and-agents/agent-frameworks/`)
- [x] `code/llms/openai_api.py` — 8 demos + 9 exercises

### B2: Prompt Engineering in Practice (Start: Week 2)

> Build reliable AI outputs through prompt design.
> **Theory link**: None needed yet — learn patterns by experimentation.

- [ ] Prompt Design Patterns (zero-shot, few-shot, chain-of-thought)
- [ ] Structured Output (JSON mode, function calling)
- [ ] System Prompts and Guardrails
- [ ] Prompt Testing and Iteration
- [ ] **Project**: Structured data extractor (PDF/text → JSON)

**Estimated**: ~4 notes, 1 project

### B3: LLM Providers Landscape (Start: Week 3)

> Know the playing field. Each provider has different strengths, pricing, and features.
> **Theory link**: None needed — this is practical market knowledge.

- [ ] Provider Comparison: Claude vs GPT vs Gemini vs DeepSeek vs Mistral vs Llama
- [ ] Key Features by Provider (tool use, vision, code gen, context window, structured output, streaming, batch)
- [ ] Pricing Models and Cost Optimization (tokens, caching, batching, model tiers)
- [ ] Open-Source vs Closed-Source Tradeoffs (control, cost, latency, privacy)
- [ ] Model Selection Framework (when to pick which model for which task)
- [ ] Multi-Provider Strategy (fallbacks, routing by task type, cost/quality balance)
- [ ] **Project**: Multi-provider CLI tool that routes prompts to the best model per task

**Estimated**: ~5 notes, 1 project

### B4: Embeddings & Vector Search (Start: Week 4-5)

> Your first real connection between theory and practice.
> **Theory link**: [[cosine-similarity]], [[vector-norms]], [[vectors-and-vector-spaces]] — NOW you see why vectors matter.

- [ ] Embedding Models (OpenAI, Cohere, open-source)
- [ ] What Embeddings Actually Represent (connecting to vector theory)
- [ ] Vector Databases: Chroma (local, simple)
- [ ] Vector Databases: Pinecone / Qdrant (cloud, production)
- [ ] Similarity Search in Practice
- [ ] **Project**: Semantic search over your own documents

**Estimated**: ~4 notes, 1 project

### B5: Build a RAG Pipeline (Start: Week 6-7)

> The most common production LLM pattern.
> **Theory link**: [[projection]] (finding closest match), cosine similarity, embeddings.

- [ ] RAG Architecture Overview
- [ ] Chunking Strategies (size, overlap, semantic)
- [ ] Retrieval Techniques (dense, sparse, hybrid)
- [ ] Reranking
- [ ] RAG Evaluation (faithfulness, relevance, recall)
- [ ] **Project**: RAG chatbot over a knowledge base (your vault!)

**Estimated**: ~5 notes, 1 project

### B6: Tool Use & Function Calling (Start: Week 8-9)

> Give LLMs the ability to take actions.
> **Theory link**: Connects to agent architectures later.

- [ ] Function Calling (OpenAI, Anthropic tool use)
- [ ] Designing Good Tool Schemas
- [ ] Error Handling and Retries
- [ ] **Project**: AI assistant that can search the web, read files, run code

**Estimated**: ~3 notes, 1 project

### B7: Agent Frameworks (Start: Week 10-12)

> Autonomous AI systems that reason, plan, and act.
> **Theory link**: T9 (attention/transformers) helps understand WHY agents work.

- [ ] Agent Patterns (ReAct, Plan-and-Execute)
- [ ] Memory Systems (short-term, long-term, episodic)
- [ ] LangChain / LangGraph Deep Dive
- [ ] Multi-Agent Systems
- [ ] Orchestration Tools (CrewAI, AutoGen, OpenAI Swarm)
- [ ] **Project**: Multi-agent system for a real task

**Estimated**: ~5 notes, 1 project

### B8: Evaluation & Observability (Start: Week 13-14)

> Measure and monitor your AI systems.
> **Theory link**: T5 evaluation metrics (precision, recall) apply here too.

- [ ] LLM Evaluation Frameworks (RAGAS, DeepEval)
- [ ] Observability Platforms (LangFuse, LangSmith)
- [ ] Cost Tracking and Optimization
- [ ] Logging, Tracing, and Debugging LLM Apps
- [ ] **Project**: Add evaluation + monitoring to your RAG app

**Estimated**: ~4 notes, 1 project

### B9: Production Patterns (Start: Week 15-17)

> Make your AI systems reliable, fast, and cost-efficient.
> **Theory link**: MLOps concepts from T10+.

- [ ] Multi-Model Routing and Fallbacks
- [ ] Caching Strategies for LLM Calls
- [ ] Rate Limiting and API Gateway Design
- [ ] Open-Source Model Serving (Ollama, vLLM, TGI)
- [ ] Containerization with Docker
- [ ] REST API Serving (FastAPI)
- [ ] **Project**: Production-grade AI API with fallbacks, caching, monitoring

**Estimated**: ~6 notes, 1 project

### B10: MLOps & Infrastructure (Start: Week 18-21)

> Taking models from notebook to production at scale.
> **Theory link**: Everything comes together.

- [ ] ML Pipeline Orchestration (Airflow, Prefect)
- [ ] Experiment Tracking (MLflow, W&B)
- [ ] Model Versioning (DVC, MLflow Registry)
- [ ] Data Drift Detection
- [ ] Cloud ML Services Overview (AWS, GCP, Azure)
- [ ] **Project**: End-to-end ML pipeline with tracking, versioning, deployment

**Estimated**: ~5 notes, 1 project

---

## CAPSTONE PROJECTS (Weeks 20+)

Combine both tracks into ambitious projects:

- [ ] **Full-Stack RAG Application**: Production RAG with evaluation, monitoring, multi-source retrieval, and a web UI
- [ ] **Custom Neural Network Library**: Mini PyTorch from scratch (tensors, autograd, layers)
- [ ] **AI Agent Platform**: Multi-agent system with memory, tools, evaluation, and observability
- [ ] **ML Pipeline Platform**: Full lifecycle — data ingestion, training, versioning, deployment, monitoring
- [ ] **Open-Source Contribution**: Contribute to a real AI/ML project (LangChain, HuggingFace, etc.)

---

## Parallel Schedule Overview

```
Week  | THEORY                    | BUILDER
------+---------------------------+---------------------------
1-2   | Linear Algebra (finish)   | B1: API setup + first calls
3     | Calculus                  | B2: Prompt engineering + B3: LLM Providers
4-5   | Calculus + Probability    | B4: Embeddings + vector DBs
6-7   | Probability               | B5: RAG pipeline
8-9   | Supervised ML             | B6: Tool use + function calling
10-12 | Unsupervised + Ensemble   | B7: Agent frameworks
13-14 | DL Fundamentals           | B8: Evaluation + observability
15-17 | CNNs + RNNs               | B9: Production patterns
18-20 | Transformers              | B10: MLOps + infrastructure
21-23 | LLM Internals             | Capstone projects
24+   | Advanced topics           | Capstone projects
```

**Rhythm**: Alternate between tracks during each week. Example day:
- Morning: Theory session (study, derive, implement from scratch)
- Afternoon: Builder session (use real tools, build real things)

Or alternate days: Mon/Wed/Fri = Theory, Tue/Thu = Builder.

---

## Summary

| Track | Topics | Notes | Code/Projects | Weeks |
|-------|--------|-------|---------------|-------|
| Theory (T1-T10) | Math → ML → DL → LLMs | ~60 | 17 code files | 1-25 |
| Builder (B1-B10) | APIs → Providers → RAG → Agents → Prod | ~44 | 10 projects | 1-21 |
| Capstone | Full-stack projects | ~5 | 5 projects | 20+ |
| **Total** | | **~104** | **31+** | **~25** |

---

## What to Do Right Now

**Theory (priority order)**:
1. **Start Calculus** — derivatives → chain rule → gradient descent. The bridge from math to ML optimization. Linear algebra is 95% done.
2. **Matrix Calculus** — Jacobians, Hessians. Do after calculus fundamentals are covered.

**Gaps to close:**
- Promote SVD from seed to growing (add code file, do exercises)
- Promote spectral-decomposition to evergreen (comprehensive, session done)
- Promote gram-schmidt and linear-transformations after review
- Complex eigenvalues (rotation matrices) — brief addition to eigenvalues note
- Create SVD code file with image compression demo

**Builder**: Continue B1 — complete Anthropic Skilljar courses (MUST). Then: API key management note, Python setup note, chatbot project. Then B3: Provider Comparison.
