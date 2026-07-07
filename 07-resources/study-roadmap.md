# Study Roadmap

**Created**: 2026-02-24
**Last updated**: 2026-07-07 (linear algebra track nearly complete — 11 new notes on subspaces/orthogonality/kernel-range/rank-nullity; added trigonometric-identities to calculus; 3 new Claude Code tooling notes; surfaced new 08-applied-domains/people-analytics side track; flagged unresolved matrix-transpose inbox drafts)
**Goal**: Become an expert AI architect and engineer — design, implement, and orchestrate intelligent systems end-to-end.

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
```

---

## Progress Overview

| Area | Notes | Status |
|------|-------|--------|
| 01-foundations/linear-algebra | 43 | Near-complete — subspaces, orthogonality, kernel/range, rank-nullity added. Only matrix calculus, pseudoinverse, matrix norms remain |
| 01-foundations/calculus | 9 | Core complete — trigonometric identities added |
| 01-foundations/probability | 10 | Distributions done — MLE, entropy, multivariate Normal next |
| 01-foundations/algorithms | 0 | Not started |
| 01-foundations/databases | 0 | Not started |
| 02-machine-learning | 0 | Not started |
| 03-deep-learning | 0 | Not started |
| 04-llms-and-agents | 11 | Anthropic + OpenAI ecosystems + Claude Code tooling (hooks, cron, chrome) covered |
| 05-mlops/cloud | 0 | Not started |
| 08-applied-domains/people-analytics | 6 | **Side track, outside core path** — HR/people analytics fundamentals |

**Total notes**: 81 | **8 evergreen** | **25 growing** | **48 seed**

**Vault hygiene gap**: `00-inbox/proposals/` has three unresolved template drafts for `matrix-transpose` (frontmatter/card/layered variants) — a real gap, since matrix transpose has no permanent note in `linear-algebra/` yet despite being referenced by other notes. Pick one format and promote it, or discard the drafts.

---

## THEORY TRACK

### T1: Linear Algebra — NEAR-COMPLETE (43/~46 notes)

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

**Remaining:**
- [ ] Matrix Transpose — surprising gap: no permanent note exists, only 3 unresolved template drafts sitting in `00-inbox/proposals/`. Resolve before anything else in this track.
- [ ] Matrix Calculus (Jacobians, Hessians, dL/dW) — needs calculus track first, CRITICAL for backprop
- [ ] Pseudoinverse (Moore-Penrose) — via SVD, for least-squares
- [ ] Matrix Norms and Condition Number — numerical stability

**Estimated remaining**: ~4 notes — this track is essentially done. Once matrix calculus lands, move fully into T4 (Supervised ML).

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
- [x] Claude Code Hooks ← new
- [x] Claude Code Cron Jobs ← new
- [x] Claude Code + Chrome ← new
- [x] Model Context Protocol
- [x] Claude Agent SDK
- [x] OpenAI Codex
- [x] OpenAI Agents SDK

---

### B2: Prompt Engineering — NOT STARTED

- [ ] Prompt Design Patterns (zero-shot, few-shot, chain-of-thought)
- [ ] Structured Output (JSON mode, function calling)
- [ ] System Prompts and Guardrails
- [ ] **Project**: Structured data extractor

---

### B3: LLM Providers Landscape — NOT STARTED

- [ ] Provider Comparison (Claude vs GPT vs Gemini vs Mistral vs LLaMA)
- [ ] Pricing and Cost Optimization
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

### B6: Cloud Infrastructure for AI & Data — NOT STARTED ← NEW

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

#### Microsoft Azure / Fabric
- [ ] Microsoft Fabric overview — unified analytics: Data Engineering, Data Science, Data Warehouse, Real-Time Analytics
- [ ] Fabric Lakehouses and OneLake — Delta Lake-based unified storage
- [ ] Fabric Pipelines and Dataflows — ETL/ELT with drag-and-drop + PySpark
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
- [ ] Medallion architecture — Bronze / Silver / Gold layers, data quality tiers

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

### B10–B12: Tool Use, Agents, Evaluation, MLOps — NOT STARTED

---

## SIDE TRACK (outside core AI architect path)

### S1: Applied Domains — People Analytics (6 notes, all seed)

> Not part of the theory or builder tracks above — this is domain knowledge (HR/people analytics), likely tied to a specific course (Platzi) or work context rather than the AI-architect goal. Tracked here so it doesn't get lost, but it shouldn't compete with T1–T10 for study time unless there's a specific reason (e.g., a work project applying ML to HR data).

- [x] People Analytics (overview)
- [x] People Analytics — Employee Lifecycle
- [x] People Analytics — Project Framework
- [x] HR Data Types
- [x] HR Data Ethics
- [x] Data-Driven Culture

**Open question**: is this a side interest to keep growing, or should it eventually connect back to T4/T5 (e.g., attrition prediction as a supervised learning project)? Worth clarifying so the roadmap can link it in rather than treating it as orphaned.

---

## Parallel Schedule

```
Weeks 1-3   | Linear Algebra (✓ done)      | B1: APIs (✓ done)
Weeks 4-5   | Calculus (✓ done)             | B2: Prompt engineering
Weeks 6-8   | Probability (in progress)     | B3: Providers landscape
Weeks 9-10  | MLE + Information Theory      | B4: Embeddings + vector DBs
Weeks 11-13 | Supervised ML                 | B5: RAG pipeline
Weeks 14-15 | Unsupervised + Ensemble       | B6: Cloud infra (AWS + Fabric)
Weeks 16-18 | Deep Learning Fundamentals    | B7-DE: SQL + Spark + dbt
Weeks 19-20 | CNNs + RNNs                   | B7-DE: Kafka + streaming
Weeks 21-22 | Transformers                  | B7-DE: Delta Lake + warehousing
Weeks 23-24 | LLM Internals                 | B8-C++: Fundamentals + memory
Weeks 25-27 | Fine-tuning + RLHF            | B8-C++: Performance + CUDA
Weeks 28+   | Capstone projects             | B8-C++: ONNX + TensorRT + custom ops
```

---

## What to Do Right Now

**Immediate priorities (theory):**

1. Resolve the `matrix-transpose` inbox drafts (`00-inbox/proposals/`) — pick one of the 3 template variants and promote it to `01-foundations/linear-algebra/matrix-transpose.md`. Quick win, closes the last real gap in linear algebra.
2. `/note maximum-likelihood-estimation` — derives ALL loss functions from probability. Single most important missing concept.
3. `/note cross-entropy-and-kl-divergence` — information theory, connects to classification losses and VAEs.
4. `/note matrix-calculus` — Jacobians, Hessians, dL/dW. Required before any deep learning. Linear algebra is otherwise done, so this is the last theory gate before starting T4 (Supervised ML).
5. `/session linear-regression` — first ML model, bridges foundations → ML.

**Immediate priorities (builder):**

1. Complete Anthropic Skilljar courses
2. `/note prompt-design-patterns` — zero-shot, few-shot, CoT
3. Start B4: embeddings project using this vault

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
- 48 of 81 vault notes are still `status/seed` — worth a `/review` pass on the linear-algebra seed notes (25 of them) before starting T4, since several (subspaces, kernel-and-range, rank-nullity-theorem) are load-bearing for everything downstream
