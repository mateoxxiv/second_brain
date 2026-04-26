---
tags:
  - status/evergreen
  - linear-algebra
related:
  - "[[vector-operations]]"
  - "[[vector-norms]]"
  - "[[projection]]"
  - "[[linear-independence]]"
domain: linear-algebra
sources:
  - "https://mml-book.github.io/book/mml-book.pdf"
  - "https://www.youtube.com/watch?v=LyGKycYT2v0"
---

> **TL;DR** — Cosine similarity isolates the angle between two vectors by dividing out their magnitudes. It answers "are these vectors pointing the same way?" regardless of how long they are.

---

## Intuition

The dot product mixes two things: magnitude and direction. A large dot product could mean well-aligned vectors, or just very long vectors, or both.

Cosine similarity normalizes out the magnitude — it's just the dot product of unit vectors. **A whisper and a shout of "hello" have very different volumes but the same meaning.** Cosine similarity hears the meaning, not the volume. This is why it's the default metric for comparing embeddings.

## Mechanics

$$\text{cos\_sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|} = \cos\theta$$

| Value | Angle | Meaning |
|---|---|---|
| $1$ | $0°$ | Identical direction |
| $0$ | $90°$ | No relationship (orthogonal) |
| $-1$ | $180°$ | Opposite direction |

**Distance vs similarity** — cosine *distance* = $1 - \text{cos\_sim}$. Range $[0, 2]$. Use when you need a proper metric.

When vectors are already unit-normalized, $\text{cos\_sim} = \mathbf{u}\cdot\mathbf{v}$ — so dot product IS cosine similarity on unit vectors. This is how attention works.

```python
import numpy as np

def cosine_similarity(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

a = np.array([1.0, 0.0])
b = np.array([1.0, 1.0])
c = np.array([0.0, 1.0])

print(cosine_similarity(a, b))   # 0.707 — 45° apart
print(cosine_similarity(a, c))   # 0.0   — orthogonal
print(cosine_similarity(a, -a))  # -1.0  — opposite
```

> Runnable: [[code/foundations/vectors_and_spaces.py]]

## In ML

**Embedding similarity** — word2vec, BERT, and all embedding models use cosine similarity to compare semantic closeness. "king" and "queen" have high cosine similarity; "king" and "bicycle" do not.

**Attention mechanism** — the scaled dot-product attention computes $\frac{QK^T}{\sqrt{d_k}}$. When $Q$ and $K$ are unit-normalized, this is cosine similarity scaled by $\sqrt{d_k}$.

**Recommendation systems** — user and item embeddings are compared by cosine similarity. If your embedding for "jazz music" and a user's preference vector point in the same direction, the user gets a jazz recommendation.

## Exercises

**Basic** — Compute cosine similarity between $[1,2,3]$ and $[2,4,6]$. What does the result tell you about their relationship?

**Intermediate** — Two word embeddings have dot product $0.8$. Their norms are $1.2$ and $0.5$ respectively. Compute cosine similarity and interpret.

**Advanced** — Why is cosine similarity scale-invariant but NOT shift-invariant? Give an example showing that adding a constant to all components destroys the semantic meaning that cosine similarity was measuring.
