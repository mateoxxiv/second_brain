**Related**: [[vector-operations]], [[vector-norms]], [[projection]], [[linear-independence]], [[Attention Mechanism]]
**Tags**: #status/evergreen

## Core Idea

The [[vector-operations|dot product]] mixes two things together: how long
vectors are and what direction they point. Sometimes you only care about
direction — "are these two things similar in kind, regardless of scale?"
Cosine similarity strips away magnitude and isolates the angle. It answers:
**"are these vectors pointing the same way?"**

**Analogy**: A whisper and a shout of the word "hello" have very different
volumes (magnitude), but they carry the same meaning (direction). Cosine
similarity hears the meaning, not the volume. This is why it's the default
metric for comparing embeddings, documents, and anything where scale is noise.

## Details

### Definition

$$\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \cos\theta$$

| Value | Angle | Meaning |
|-------|-------|---------|
| 1 | 0° | Identical direction (parallel) |
| 0 | 90° | Perpendicular — no relationship at all |
| -1 | 180° | Opposite direction (anti-parallel) |

```
cos_sim = 1          cos_sim = 0          cos_sim = -1
(same direction)     (perpendicular)      (opposite)

   u →                u →                 u →
   v →                  ↑ v               ← v
```

### Derivation from Dot Product

From the [[vector-operations|dot product geometric identity]]:

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$

Solve for $\cos\theta$ (divide both sides by the norms):

$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

This is the same as computing the dot product of the **unit vectors**
$\hat{\mathbf{u}}$ and $\hat{\mathbf{v}}$:

$$\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \hat{\mathbf{u}} \cdot \hat{\mathbf{v}} \quad \text{where } \hat{\mathbf{u}} = \frac{\mathbf{u}}{\|\mathbf{u}\|}$$

**Why does this work?** Unit vectors have length 1, so the dot product formula
becomes $1 \cdot 1 \cdot \cos\theta = \cos\theta$. By normalizing, you've
removed magnitude from the equation entirely. Only the angle survives. $\blacksquare$

### Why Not Just Euclidean Distance?

Euclidean distance $\|\mathbf{u} - \mathbf{v}\|_2$ is affected by magnitude.
This causes problems when magnitude is noise:

$$\mathbf{a} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 100 \\ 200 \end{bmatrix}, \quad \mathbf{c} = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$$

$\mathbf{a}$ and $\mathbf{b}$ point in the **same direction** (b = 100 × a).
$\mathbf{a}$ and $\mathbf{c}$ point in **different directions**.

But Euclidean distance is fooled by scale:
- $\|\mathbf{a} - \mathbf{b}\|_2 = \sqrt{99^2 + 198^2} \approx 221$ (says they're far apart!)
- $\|\mathbf{a} - \mathbf{c}\|_2 = \sqrt{0 + 16} = 4$ (says they're close!)

Cosine similarity sees through the magnitude:
- $\text{cos\_sim}(\mathbf{a}, \mathbf{b}) = 1.0$ (identical direction — correct!)
- $\text{cos\_sim}(\mathbf{a}, \mathbf{c}) = -0.6$ (different direction — correct!)

### When SHOULD You Use Euclidean Instead?

Cosine similarity isn't always better. Use Euclidean distance when **magnitude
carries meaning**:

| Use cosine similarity when... | Use Euclidean distance when... |
|------------------------------|-------------------------------|
| Comparing text embeddings (document length varies) | Measuring physical distances (meters matter) |
| Comparing user preference vectors (some users rate more) | K-means clustering on raw features (scale = signal) |
| Information retrieval / RAG (query length varies) | Pixel intensity comparison (brightness matters) |
| Word vectors (frequency artifacts inflate magnitude) | Anomaly detection based on deviation from center |

**Rule of thumb**: If doubling every component of a vector should mean "same
thing," use cosine. If doubling should mean "different thing," use Euclidean.

### Worked Example

$$\mathbf{u} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$

Step by step:
1. $\mathbf{u} \cdot \mathbf{v} = (3)(1) + (4)(2) = 3 + 8 = 11$
2. $\|\mathbf{u}\| = \sqrt{9 + 16} = 5$
3. $\|\mathbf{v}\| = \sqrt{1 + 4} = \sqrt{5} \approx 2.236$
4. $\text{cos\_sim} = \frac{11}{5 \cdot \sqrt{5}} = \frac{11}{11.18} \approx 0.984$

High similarity — these vectors point in nearly the same direction
($\theta \approx 10.3°$).

Now scale $\mathbf{v}$ up: $\mathbf{v}' = \begin{bmatrix} 100 \\ 200 \end{bmatrix}$

- $\text{cos\_sim}(\mathbf{u}, \mathbf{v}') = \frac{300 + 800}{5 \cdot \sqrt{50000}} = \frac{1100}{1118.0} \approx 0.984$

Same cosine similarity — the scaling didn't change the angle. That's the point.

### Cosine Distance

To use cosine similarity as a **distance** metric (where 0 = identical), flip it:

$$\text{cos\_dist}(\mathbf{u}, \mathbf{v}) = 1 - \text{cos\_sim}(\mathbf{u}, \mathbf{v})$$

| cos_sim | cos_dist | Meaning |
|---------|----------|---------|
| 1 | 0 | Identical direction |
| 0 | 1 | Perpendicular |
| -1 | 2 | Opposite |

**Why $1 - \text{cos\_sim}$ and not $\arccos$?** Both work. $\arccos$ gives
the actual angle in radians, which is a true metric (satisfies triangle
inequality). $1 - \text{cos\_sim}$ is cheaper to compute and sufficient for
ranking — if you only need "which is more similar," the ordering is the same.
Most vector databases use $1 - \text{cos\_sim}$ for speed.

### Connection to Orthogonality and Independence

When $\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = 0$, the vectors are
**orthogonal** — they share zero directional overlap. This connects to
[[linear-independence]]: orthogonal vectors are always independent (each
points in a direction the others can't reach).

In embedding spaces, orthogonality means the two concepts are unrelated.
"King" and "quantum physics" should have cosine similarity near 0 — they
occupy independent dimensions of meaning.

### Where It Appears in ML

| Application | How cosine similarity is used |
|-------------|-------------------------------|
| **RAG / vector search** | Find documents whose embeddings are closest in direction to the query embedding |
| **Attention mechanism** | Scaled dot-product attention: $\text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)$. The $QK^T$ computes dot products between queries and keys. The $\sqrt{d}$ scaling prevents dot products from growing too large with high dimensions (not normalization — numerical stability) |
| **Word embeddings** | word2vec, GloVe: "king - man + woman ≈ queen" works because of directional similarity |
| **Recommendation** | User and item vectors: high cosine = good recommendation |
| **Contrastive learning** | SimCLR, CLIP: maximize cosine similarity between augmented pairs, minimize it between unrelated pairs |

## Code Example

```python
import numpy as np

def cosine_similarity(u, v):
    """Cosine similarity = dot product of unit vectors."""
    dot = np.dot(u, v)
    norm_u, norm_v = np.linalg.norm(u), np.linalg.norm(v)
    if norm_u == 0 or norm_v == 0:
        return 0.0  # zero vector has no direction
    return dot / (norm_u * norm_v)

# Magnitude doesn't matter — direction does
a = np.array([1.0, 2.0])
b = np.array([100.0, 200.0])  # same direction, 100x larger
c = np.array([1.0, -2.0])     # different direction
print(cosine_similarity(a, b))  # 1.0  — same direction
print(cosine_similarity(a, c))  # -0.6 — different direction

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
- [[projection|Scalar projection]] = cosine similarity × target norm. Cosine similarity is what remains after removing magnitude
- Orthogonality (cos_sim = 0) connects to [[linear-independence]] — orthogonal vectors are always independent
- Foundation of [[Attention Mechanism]] — scaled dot-product attention measures query-key alignment
- Used in [[RAG]] for retrieval: embed query → find nearest neighbors by cosine
- Cosine distance enables clustering in embedding space → [[K-Means Clustering]]

## Sources

- [Understanding Cosine Similarity and its applications](https://towardsdatascience.com/understanding-cosine-similarity-and-its-application-fd42f585296a)
- [Mathematics for Machine Learning — Chapter 3.2](https://mml-book.github.io/book/mml-book.pdf)
- [The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)
- [3Blue1Brown — Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0)
