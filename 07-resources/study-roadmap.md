# Study Roadmap

**Created**: 2026-02-24
**Last updated**: 2026-02-24
**Goal**: Become an expert AI architect and engineer — design, implement, and orchestrate intelligent systems end-to-end.

---

## Progress Overview

| Area | Notes | Code | Status |
|------|-------|------|--------|
| 01-foundations | 0 | 0 | Not started |
| 02-machine-learning | 0 | 0 | Not started |
| 03-deep-learning | 0 | 0 | Not started |
| 04-llms-and-agents | 0 | 0 | Not started |
| 05-mlops | 0 | 0 | Not started |
| 06-projects | 0 | 0 | Not started |

---

## Phase 1: Foundations (Weeks 1-6)

The bedrock everything else builds on. You have intermediate knowledge here, so this is deep review, not learning from zero. Move fast but fill gaps.

### 1.1 Linear Algebra (Week 1-2)
> *Why*: Every ML algorithm is a matrix operation. You can't understand neural nets, PCA, or embeddings without this.

- [ ] Vectors and Vector Spaces
- [ ] Matrix Operations and Properties
- [ ] Eigenvalues and Eigenvectors
- [ ] Singular Value Decomposition (SVD)
- [ ] Matrix Calculus (Jacobians, Hessians)
- [ ] Linear Transformations
- [ ] **Code**: Matrix operations from scratch with NumPy
- [ ] **Code**: SVD for image compression

**Estimated**: ~6 notes, 2 code files

### 1.2 Calculus (Week 2-3)
> *Why*: Optimization IS calculus. Gradient descent, backpropagation, loss functions — all calculus.

- [ ] Derivatives and Partial Derivatives
- [ ] Chain Rule (critical for backprop)
- [ ] Gradient and Directional Derivatives
- [ ] Optimization: Minima, Maxima, Saddle Points
- [ ] Multivariable Calculus for ML
- [ ] **Code**: Gradient descent from scratch

**Estimated**: ~5 notes, 1 code file

### 1.3 Probability and Statistics (Week 3-5)
> *Why*: ML is applied statistics. Bayesian thinking, distributions, hypothesis testing — you'll use this daily.

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

### 1.4 Algorithms and Data Structures (Week 5-6)
> *Why*: Efficient data handling, complexity analysis, and graph algorithms matter for ML pipelines and agent systems.

- [ ] Big-O Notation and Complexity Analysis
- [ ] Hash Tables and Their Role in ML
- [ ] Trees and Graphs (for decision trees, GNNs, knowledge graphs)
- [ ] Dynamic Programming (for sequence models, Viterbi)
- [ ] Search Algorithms (for beam search in NLP)
- [ ] **Code**: Implement a basic search algorithm

**Estimated**: ~5 notes, 1 code file

### 1.5 Databases (Week 6)
> *Why*: Data storage, retrieval, and vector search are core to RAG and production ML systems.

- [ ] Relational Databases and SQL Fundamentals
- [ ] NoSQL Concepts (document, key-value, graph)
- [ ] Vector Databases (Pinecone, Chroma, Weaviate)
- [ ] Data Modeling for ML Pipelines
- [ ] **Code**: Vector similarity search from scratch

**Estimated**: ~4 notes, 1 code file

### Phase 1 Total: ~28 notes, 7 code files

---

## Phase 2: Machine Learning (Weeks 7-14)

Classical ML from theory to implementation. Build everything from scratch, then use scikit-learn.

### 2.1 Supervised Learning (Week 7-10)
> *Why*: The core of predictive modeling. Master this and you can solve 80% of business ML problems.

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
- [ ] **Code**: Full supervised pipeline with scikit-learn

**Estimated**: ~8 notes, 4 code files

### 2.2 Unsupervised Learning (Week 10-11)
> *Why*: Clustering, dimensionality reduction, and anomaly detection — critical for data exploration and feature creation.

- [ ] K-Means Clustering
- [ ] Hierarchical Clustering
- [ ] DBSCAN
- [ ] Principal Component Analysis (PCA)
- [ ] t-SNE and UMAP
- [ ] Anomaly Detection
- [ ] **Code**: K-Means from scratch
- [ ] **Code**: PCA from scratch + visualization

**Estimated**: ~6 notes, 2 code files

### 2.3 Ensemble Methods (Week 12)
> *Why*: Random forests, gradient boosting, XGBoost — these dominate tabular data competitions and production systems.

- [ ] Bagging and Bootstrap
- [ ] Random Forests
- [ ] Boosting (AdaBoost, Gradient Boosting)
- [ ] XGBoost / LightGBM / CatBoost
- [ ] Stacking and Blending
- [ ] **Code**: Random forest from scratch
- [ ] **Code**: XGBoost pipeline on real dataset

**Estimated**: ~5 notes, 2 code files

### 2.4 Feature Engineering (Week 13)
> *Why*: "Garbage in, garbage out." Feature engineering is often the difference between a mediocre and great model.

- [ ] Feature Scaling (normalization, standardization)
- [ ] Encoding Categorical Variables
- [ ] Feature Selection Methods
- [ ] Handling Missing Data
- [ ] Feature Extraction and Creation
- [ ] **Code**: End-to-end feature engineering pipeline

**Estimated**: ~5 notes, 1 code file

### 2.5 Evaluation (Week 14)
> *Why*: If you can't measure it, you can't improve it. Know which metric matters for which problem.

- [ ] Classification Metrics (accuracy, precision, recall, F1, AUC-ROC)
- [ ] Regression Metrics (MSE, RMSE, MAE, R-squared)
- [ ] Cross-Validation Strategies
- [ ] Confusion Matrix Deep Dive
- [ ] Overfitting and Underfitting Detection
- [ ] **Code**: Custom evaluation framework

**Estimated**: ~5 notes, 1 code file

### Phase 2 Total: ~29 notes, 10 code files

---

## Phase 3: Deep Learning (Weeks 15-24)

Build neural networks from scratch, then transition to PyTorch.

### 3.1 Fundamentals (Week 15-17)
> *Why*: You need to truly understand what happens inside a neural network before using frameworks.

- [ ] Perceptron and Multilayer Perceptron
- [ ] Activation Functions (ReLU, Sigmoid, Tanh, GELU, Swish)
- [ ] Forward Propagation
- [ ] Backpropagation and Computational Graphs
- [ ] Loss Functions (MSE, Cross-Entropy, Focal Loss)
- [ ] Universal Approximation Theorem
- [ ] **Code**: Neural network from scratch (NumPy only)
- [ ] **Code**: Same network in PyTorch

**Estimated**: ~6 notes, 2 code files

### 3.2 Training Techniques (Week 17-19)
> *Why*: The difference between a model that converges and one that doesn't.

- [ ] Gradient Descent Variants (SGD, Mini-batch, Momentum)
- [ ] Adaptive Optimizers (Adam, AdaGrad, RMSprop)
- [ ] Learning Rate Scheduling
- [ ] Batch Normalization
- [ ] Dropout and Regularization
- [ ] Weight Initialization Strategies
- [ ] Vanishing/Exploding Gradients
- [ ] **Code**: Optimizer comparison on same dataset

**Estimated**: ~7 notes, 1 code file

### 3.3 CNNs (Week 19-20)
> *Why*: Foundation of computer vision. Convolutions are also used in time series and NLP.

- [ ] Convolution Operation
- [ ] Pooling Layers
- [ ] CNN Architectures (LeNet, AlexNet, VGG, ResNet)
- [ ] Transfer Learning with Pretrained CNNs
- [ ] **Code**: CNN image classifier in PyTorch

**Estimated**: ~4 notes, 1 code file

### 3.4 RNNs (Week 21-22)
> *Why*: Sequential data processing — time series, text. Understanding RNNs makes transformers click.

- [ ] Vanilla RNN and its limitations
- [ ] LSTM (Long Short-Term Memory)
- [ ] GRU (Gated Recurrent Unit)
- [ ] Sequence-to-Sequence Models
- [ ] **Code**: LSTM text generator in PyTorch

**Estimated**: ~4 notes, 1 code file

### 3.5 Transformers (Week 22-24)
> *Why*: THE architecture behind modern AI. Everything leads here.

- [ ] Attention Mechanism (Scaled Dot-Product)
- [ ] Self-Attention and Multi-Head Attention
- [ ] Positional Encoding
- [ ] Transformer Architecture (Encoder-Decoder)
- [ ] BERT, GPT, and the Encoder/Decoder Split
- [ ] Vision Transformers (ViT)
- [ ] **Code**: Attention mechanism from scratch
- [ ] **Code**: Minimal transformer in PyTorch

**Estimated**: ~6 notes, 2 code files

### Phase 3 Total: ~27 notes, 7 code files

---

## Phase 4: LLMs, Agents & AI Tools (Weeks 25-34)

From understanding LLMs to building production agent systems.

### 4.1 LLM Architectures (Week 25-26)
> *Why*: Understand what's inside GPT, Claude, LLaMA, Mistral — not just how to call them.

- [ ] Language Modeling (autoregressive vs masked)
- [ ] Tokenization (BPE, WordPiece, SentencePiece)
- [ ] Scaling Laws
- [ ] Key LLM Families (GPT, LLaMA, Mistral, Claude architecture insights)
- [ ] Context Windows and KV-Cache
- [ ] **Code**: BPE tokenizer from scratch

**Estimated**: ~5 notes, 1 code file

### 4.2 Fine-Tuning (Week 27-28)
> *Why*: Adapt pre-trained models to your specific domain and tasks.

- [ ] Transfer Learning for NLP
- [ ] Full Fine-Tuning vs Parameter-Efficient (LoRA, QLoRA)
- [ ] RLHF and DPO (alignment techniques)
- [ ] Dataset Preparation for Fine-Tuning
- [ ] Evaluation of Fine-Tuned Models
- [ ] **Code**: LoRA fine-tuning with HuggingFace

**Estimated**: ~5 notes, 1 code file

### 4.3 RAG (Week 29-30)
> *Why*: The most common production pattern for LLM applications today.

- [ ] RAG Architecture Overview
- [ ] Embedding Models and Vector Search
- [ ] Chunking Strategies
- [ ] Retrieval Techniques (dense, sparse, hybrid)
- [ ] Reranking
- [ ] RAG Evaluation (faithfulness, relevance, recall)
- [ ] **Code**: RAG pipeline from scratch
- [ ] **Code**: Advanced RAG with reranking

**Estimated**: ~6 notes, 2 code files

### 4.4 Prompt Engineering (Week 30-31)
> *Why*: The interface between humans and LLMs. Critical for building reliable AI systems.

- [ ] Prompt Design Principles
- [ ] Few-Shot and Chain-of-Thought
- [ ] Structured Output (JSON mode, function calling)
- [ ] System Prompts and Guardrails
- [ ] Prompt Testing and Evaluation
- [ ] **Code**: Prompt evaluation framework

**Estimated**: ~5 notes, 1 code file

### 4.5 Agent Frameworks (Week 31-32)
> *Why*: Autonomous AI systems that reason, plan, and use tools — the frontier.

- [ ] Agent Architecture Patterns (ReAct, Plan-and-Execute)
- [ ] Tool Use and Function Calling
- [ ] Memory Systems (short-term, long-term, episodic)
- [ ] Multi-Agent Systems
- [ ] LangChain / LangGraph Deep Dive
- [ ] **Code**: Custom agent with tool use
- [ ] **Code**: Multi-agent system

**Estimated**: ~5 notes, 2 code files

### 4.6 APIs and Services (Week 33)
> *Why*: An architect must know how to evaluate, integrate, and switch between providers.

- [ ] OpenAI API (models, endpoints, best practices)
- [ ] Anthropic API (Claude, Messages API, tool use)
- [ ] Open-Source Model Serving (vLLM, Ollama, TGI)
- [ ] Model Selection and Cost-Performance Tradeoffs
- [ ] **Code**: Multi-provider abstraction layer

**Estimated**: ~4 notes, 1 code file

### 4.7 Tooling Ecosystem (Week 33-34)
> *Why*: Know the landscape of tools available before building everything from scratch.

- [ ] Vector Databases Comparison (Pinecone, Chroma, Weaviate, Qdrant)
- [ ] Evaluation Frameworks (RAGAS, DeepEval, LangSmith)
- [ ] Observability (LangFuse, Weights & Biases, Phoenix)
- [ ] Orchestration Tools (CrewAI, AutoGen, OpenAI Swarm)
- [ ] **Code**: Tool integration examples

**Estimated**: ~4 notes, 1 code file

### 4.8 Integration Patterns (Week 34)
> *Why*: Production AI systems need reliability, cost control, and graceful degradation.

- [ ] Multi-Model Routing and Fallbacks
- [ ] Cost Optimization Strategies
- [ ] Rate Limiting and Caching
- [ ] API Gateway Design for AI Services
- [ ] **Code**: Resilient multi-model client

**Estimated**: ~4 notes, 1 code file

### Phase 4 Total: ~38 notes, 10 code files

---

## Phase 5: MLOps (Weeks 35-40)

Taking models from notebook to production.

### 5.1 Deployment (Week 35-36)
- [ ] Model Serialization (pickle, ONNX, TorchScript)
- [ ] REST API Serving (FastAPI, Flask)
- [ ] Containerization with Docker
- [ ] Serverless Deployment
- [ ] **Code**: FastAPI model serving endpoint

**Estimated**: ~4 notes, 1 code file

### 5.2 Monitoring (Week 37-38)
- [ ] Data Drift Detection
- [ ] Model Performance Monitoring
- [ ] Logging and Alerting
- [ ] A/B Testing for Models
- [ ] **Code**: Drift detection pipeline

**Estimated**: ~4 notes, 1 code file

### 5.3 CI/CD for ML (Week 39)
- [ ] ML Pipeline Orchestration (Airflow, Prefect)
- [ ] Experiment Tracking (MLflow, W&B)
- [ ] Model Versioning (DVC, MLflow Model Registry)
- [ ] Automated Testing for ML
- [ ] **Code**: MLflow experiment tracking setup

**Estimated**: ~4 notes, 1 code file

### 5.4 Infrastructure (Week 40)
- [ ] Cloud ML Services (AWS SageMaker, GCP Vertex, Azure ML)
- [ ] GPU/TPU Management
- [ ] Distributed Training Basics
- [ ] Cost Management for ML Workloads

**Estimated**: ~4 notes, 0 code files

### Phase 5 Total: ~16 notes, 3 code files

---

## Phase 6: Capstone Projects (Weeks 41+)

Apply everything. Each project should combine multiple phases.

### Project Ideas
- [ ] **ML Pipeline**: End-to-end classification system with feature engineering, model selection, evaluation, and deployment
- [ ] **Custom Neural Network Library**: Build a mini PyTorch from scratch (tensors, autograd, layers)
- [ ] **RAG Application**: Production-quality RAG system with evaluation, monitoring, and multi-source retrieval
- [ ] **Multi-Agent System**: Autonomous agents that collaborate to solve complex tasks
- [ ] **MLOps Platform**: Full ML lifecycle — training, versioning, deployment, monitoring

---

## Summary

| Phase | Topics | Notes | Code | Weeks |
|-------|--------|-------|------|-------|
| 1. Foundations | Math, CS, Databases | ~28 | 7 | 1-6 |
| 2. Machine Learning | Supervised, Unsupervised, Ensembles | ~29 | 10 | 7-14 |
| 3. Deep Learning | NNs, CNNs, RNNs, Transformers | ~27 | 7 | 15-24 |
| 4. LLMs & Agents | LLMs, RAG, Agents, APIs, Tools | ~38 | 10 | 25-34 |
| 5. MLOps | Deploy, Monitor, CI/CD, Infra | ~16 | 3 | 35-40 |
| 6. Projects | Capstone implementations | ~5 | 5+ | 41+ |
| **Total** | | **~143** | **42+** | **~40+** |

---

## Next Session

**Recommended start**: `/session linear algebra` — the foundation for everything that follows.
