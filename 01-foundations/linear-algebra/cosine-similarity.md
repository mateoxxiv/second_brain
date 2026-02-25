**Related**: [[vector-operations]], [[vector-norms]], [[Attention Mechanism]]
**Tags**: #status/seed

## Core Idea

Cosine similarity measures the angle between two vectors, ignoring their magnitude. It answers: "are these vectors pointing in the same direction?" This makes it the default similarity metric for embeddings, attention scores, and information retrieval — because in these contexts, direction (meaning) matters more than magnitude (scale).

## Details

### Definition

$$\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \cos\theta$$

| Value | Meaning |
|-------|---------|
| 1 | Identical direction (parallel) |
| 0 | Perpendicular (orthogonal, no relationship) |
| -1 | Opposite direction (anti-parallel) |

### Derivation from Dot Product

From the [[vector-operations|dot product identity]]:

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$

Solving for $\cos\theta$:

$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

This is just the dot product of the **unit vectors** $\hat{\mathbf{u}}$ and $\hat{\mathbf{v}}$:

$$\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \hat{\mathbf{u}} \cdot \hat{\mathbf{v}} \quad \text{where } \hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}$$

### Why Not Just Euclidean Distance?

Euclidean distance $\|\mathbf{u} - \mathbf{v}\|_2$ is affected by magnitude. Consider:

$$\mathbf{a} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 100 \\ 200 \end{bmatrix}, \quad \mathbf{c} = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$$

- $\mathbf{a}$ and $\mathbf{b}$ point in the **same direction** (both represent the same "concept")
- $\mathbf{a}$ and $\mathbf{c}$ point in **different directions**

But Euclidean distance says $\mathbf{a}$ is closer to $\mathbf{c}$:
- $\|\mathbf{a} - \mathbf{b}\|_2 = \sqrt{99^2 + 198^2} \approx 221$
- $\|\mathbf{a} - \mathbf{c}\|_2 = \sqrt{0 + 16} = 4$

Cosine similarity gets it right:
- $\text{cos\_sim}(\mathbf{a}, \mathbf{b}) = 1.0$ (identical direction)
- $\text{cos\_sim}(\mathbf{a}, \mathbf{c}) = -0.6$ (different direction)

### Worked Example

$$\mathbf{u} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$

Step by step:
1. $\mathbf{u} \cdot \mathbf{v} = (3)(1) + (4)(2) = 3 + 8 = 11$
2. $\|\mathbf{u}\| = \sqrt{9 + 16} = 5$
3. $\|\mathbf{v}\| = \sqrt{1 + 4} = \sqrt{5} \approx 2.236$
4. $\text{cos\_sim} = \frac{11}{5 \cdot \sqrt{5}} = \frac{11}{11.18} \approx 0.984$

High similarity — these vectors point in nearly the same direction ($\theta \approx 10.3°$).

### Cosine Distance

Often used as a distance metric (for clustering, KNN):

$$\text{cos\_dist}(\mathbf{u}, \mathbf{v}) = 1 - \text{cos\_sim}(\mathbf{u}, \mathbf{v})$$

Range: 0 (identical) to 2 (opposite).

### Where It Appears in ML

| Application | How cosine similarity is used |
|-------------|-------------------------------|
| **RAG / vector search** | Find documents whose embeddings are closest in direction to the query embedding |
| **Attention mechanism** | Scaled dot-product attention is cosine similarity (after normalization): $\text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)$ |
| **Word embeddings** | word2vec, GloVe: "king - man + woman ≈ queen" works because of directional similarity |
| **Recommendation** | User and item vectors: high cosine = good recommendation |
| **Contrastive learning** | SimCLR, CLIP: maximize cosine similarity between augmented pairs |

## Code Example

```python
import numpy as np

def cosine_similarity(u, v):
    dot = np.dot(u, v)
    norm_u, norm_v = np.linalg.norm(u), np.linalg.norm(v)
    if norm_u == 0 or norm_v == 0:
        return 0.0
    return dot / (norm_u * norm_v)

# Simulated embeddings
king = np.array([0.8, 0.6, 0.1])
queen = np.array([0.75, 0.65, 0.1])
apple = np.array([0.1, 0.05, 0.9])

print(cosine_similarity(king, queen))  # 0.998 — semantically close
print(cosine_similarity(king, apple))  # 0.416 — semantically distant
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- Derived from the [[vector-operations|dot product]] and [[vector-norms|L2 norm]]
- Foundation of [[Attention Mechanism]] — scaled dot-product attention is cosine similarity at scale
- Used in [[RAG]] for retrieval: embed query → find nearest neighbors by cosine
- [[projection]] is related: projecting $\mathbf{u}$ onto $\mathbf{v}$ uses the same $\cos\theta$
- Cosine distance enables clustering in embedding space → [[K-Means Clustering]]

## Sources

- [Understanding Cosine Similarity and its applications](https://towardsdatascience.com/understanding-cosine-similarity-and-its-application-fd42f585296a)
- [Mathematics for Machine Learning — Chapter 3.2](https://mml-book.github.io/book/mml-book.pdf)
- [The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)
