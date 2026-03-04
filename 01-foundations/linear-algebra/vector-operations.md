**Related**: [[vectors-and-vector-spaces]], [[vector-norms]], [[cosine-similarity]], [[projection]], [[basis-and-dimension]], [[linear-independence]], [[linear-combination]]
**Tags**: #status/seed

## Core Idea

Vectors are useless unless you can do things with them. Three operations form the
backbone of all linear algebra — and therefore all of ML:

| Operation | Question it answers | One-sentence summary |
|-----------|-------------------|---------------------|
| **Addition** | What happens when two effects combine? | Merge two vectors into one by adding matching components |
| **Scalar multiplication** | What happens when I amplify or shrink an effect? | Stretch, shrink, or flip a vector by a constant |
| **Dot product** | How much do two vectors agree? | A single number that measures alignment between two vectors |

Every ML algorithm — gradient descent, attention, PCA, neural network layers —
is built from combinations of these three. Master them mechanically (how to
compute) and geometrically (what they mean), and you can read any ML equation.

## Details

### Addition: "What happens when two effects combine?"

**Analogy**: You're in a boat. The current pushes you East at 3 km/h. You row
North at 4 km/h. Your actual movement is the **sum** of these two forces —
a diagonal path Northeast.

$$\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}$$

Component-wise: each dimension combines independently. Both vectors must live
in the same space (you can't add a 3D vector to a 4D vector — it's meaningless).

**Geometric meaning**: Place $\mathbf{v}$ at the tip of $\mathbf{u}$. The
result points from the origin to where you end up. Equivalently, it's the
diagonal of the parallelogram formed by both vectors.

```
         u + v
          *
         /|
        / |
    u  /  | v
      /   |
     /    |
    *-----*
  origin   (v placed at origin)

Parallelogram rule:
       *---------*  u + v
      /         /
   v /         / v
    /         /
   *---------*
     u
```

**ML use**: Residual connections in transformers are vector addition:
$\mathbf{y} = f(\mathbf{x}) + \mathbf{x}$. The network's output is the
"modification" $f(\mathbf{x})$ added to the original signal. Gradient
accumulation across mini-batches is also addition — each batch produces a
gradient vector and they're summed.

### Worked Example: Addition

$$\mathbf{u} = \begin{bmatrix} 3 \\ -1 \\ 4 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} 1 \\ 5 \\ -2 \end{bmatrix}$$

$$\mathbf{u} + \mathbf{v} = \begin{bmatrix} 3+1 \\ -1+5 \\ 4+(-2) \end{bmatrix} = \begin{bmatrix} 4 \\ 4 \\ 2 \end{bmatrix}$$

Each dimension is independent — what happens in dimension 1 doesn't affect
dimension 2.

### Scalar Multiplication: "What happens when I amplify or shrink?"

**Analogy**: A recipe calls for a sauce. Scalar multiplication is doubling the
recipe (multiply every ingredient by 2) or halving it (multiply by 0.5). The
proportions stay the same — the direction doesn't change — only the amount
changes.

$$c \cdot \mathbf{v} = \begin{bmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{bmatrix}$$

**Geometric meaning**:

```
c = 2:    stretches (longer, same direction)
          *--------->--------->
          origin              2v

c = 0.5:  shrinks (shorter, same direction)
          *---->
          origin  0.5v

c = -1:   flips direction (same length, opposite way)
          <---------*--------->
            -v     origin     v

c = 0:    collapses to zero (the vector disappears)
          *
          origin = 0v
```

- $|c| > 1$: stretches the vector
- $|c| < 1$: shrinks it
- $c < 0$: reverses direction
- $c = 0$: kills it entirely

**ML use**: The gradient descent update $\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla L$
multiplies the gradient by learning rate $\alpha$. Too large? You overshoot.
Too small? You crawl. The scalar $\alpha$ controls how aggressively you step.

### Worked Example: Scalar Multiplication

$$\mathbf{v} = \begin{bmatrix} 2 \\ -3 \\ 1 \end{bmatrix}, \quad c = -2$$

$$c \cdot \mathbf{v} = -2 \begin{bmatrix} 2 \\ -3 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ 6 \\ -2 \end{bmatrix}$$

The result is twice as long and points in the opposite direction. Every
component flipped sign and doubled.

### Linear Combination

Addition and scalar multiplication combine into the most important operation in
ML: the **[[linear-combination]]**. Scale some vectors, add them up — that's it.
Every neuron, every gradient update, every regression prediction is a linear
combination. See the dedicated note for worked examples, span, and ML applications.

### Dot Product: "How much do two vectors agree?"

The dot product takes two vectors and returns a **single number** that measures
their alignment — how much they "point in the same direction."

**Analogy**: Think of a solar panel and sunlight. The power generated depends on
how aligned the panel is with the sun. Directly facing the sun (same direction)
= maximum power. Panel at 90° to the sun = zero power. Facing away = negative
(if that were possible). The dot product measures this "alignment."

$$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i = u_1v_1 + u_2v_2 + \cdots + u_nv_n$$

**The geometric identity** (derivation below):

$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$

This formula says the dot product captures three things at once:
1. How long $\mathbf{u}$ is ($\|\mathbf{u}\|$)
2. How long $\mathbf{v}$ is ($\|\mathbf{v}\|$)
3. The angle between them ($\cos\theta$)

### Derivation: Why does the dot product equal $\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$?

Start from the **law of cosines**. For a triangle with sides $a, b, c$ and
angle $\theta$ opposite to side $c$:

$$c^2 = a^2 + b^2 - 2ab\cos\theta$$

Now build a triangle from vectors. Let $a = \|\mathbf{u}\|$, $b = \|\mathbf{v}\|$,
and the third side is $c = \|\mathbf{u} - \mathbf{v}\|$ (the vector from tip
of $\mathbf{v}$ to tip of $\mathbf{u}$):

```
         u
        *
       / \
      /   \  u - v
     / θ   \
    *-------*
   origin    v
```

Substituting:

$$\|\mathbf{u} - \mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

Now expand the left side using the definition of norm:

$$\|\mathbf{u} - \mathbf{v}\|^2 = \sum_i (u_i - v_i)^2 = \sum_i u_i^2 - 2\sum_i u_iv_i + \sum_i v_i^2 = \|\mathbf{u}\|^2 - 2(\mathbf{u} \cdot \mathbf{v}) + \|\mathbf{v}\|^2$$

Set both expressions equal:

$$\|\mathbf{u}\|^2 - 2(\mathbf{u} \cdot \mathbf{v}) + \|\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

Cancel $\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$ from both sides:

$$-2(\mathbf{u} \cdot \mathbf{v}) = -2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

$$\boxed{\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta} \quad \blacksquare$$

### Key Dot Product Properties

| Property | Geometric meaning | Why it matters |
|----------|------------------|----------------|
| $\mathbf{u} \cdot \mathbf{v} > 0$ | Angle < 90° — same-ish direction | Vectors "agree" |
| $\mathbf{u} \cdot \mathbf{v} = 0$ | Angle = 90° — **orthogonal** | Vectors carry zero mutual information. Orthogonality is the foundation of [[projection]] and [[cosine-similarity]] |
| $\mathbf{u} \cdot \mathbf{v} < 0$ | Angle > 90° — opposite-ish direction | Vectors "disagree" |
| $\mathbf{u} \cdot \mathbf{u} = \|\mathbf{u}\|^2$ | Dot with yourself = squared length | This is how [[vector-norms|L2 norm]] is defined |

**Orthogonality ($\mathbf{u} \cdot \mathbf{v} = 0$)** is especially important.
It means two vectors share NO information — they're completely independent
directions. In ML:
- Orthogonal features = no redundancy = efficient representation
- PCA produces orthogonal components
- The residual in [[projection]] is always orthogonal to the target

### Worked Example: Dot Product

$$\mathbf{u} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}, \quad \mathbf{v} = \begin{bmatrix} -1 \\ 4 \end{bmatrix}$$

**Algebraic**:
$$\mathbf{u} \cdot \mathbf{v} = (2)(-1) + (3)(4) = -2 + 12 = 10$$

**Geometric verification**:
- $\|\mathbf{u}\| = \sqrt{4+9} = \sqrt{13}$
- $\|\mathbf{v}\| = \sqrt{1+16} = \sqrt{17}$
- $\cos\theta = \frac{10}{\sqrt{13}\sqrt{17}} = \frac{10}{\sqrt{221}} \approx 0.673$
- $\theta \approx 47.7°$ — acute angle, the vectors "agree"

Both methods give the same answer — that's what the derivation guarantees.

### What the Dot Product Does NOT Tell You

The dot product mixes magnitude and direction together. A large dot product
could mean:
- Two vectors are well-aligned (small angle), OR
- Both vectors are very long, OR
- Both

If you want ONLY the directional information (ignoring magnitude), divide out
the norms → that's [[cosine-similarity]].

If you want the "shadow" of one vector onto another → that's [[projection]].

## Code Example

```python
import numpy as np

u = np.array([2.0, 3.0])
v = np.array([-1.0, 4.0])

# --- Addition ---
w = u + v  # [1.0, 7.0]

# --- Scalar multiplication ---
scaled = -2 * u  # [-4.0, -6.0]

# --- Linear combination ---
e1, e2 = np.array([1, 0]), np.array([0, 1])
point = 3 * e1 + 1 * e2  # [3, 1] — coordinates ARE the coefficients

# --- Dot product (algebraic) ---
dot = sum(u_i * v_i for u_i, v_i in zip(u, v))  # 10.0

# --- Dot product (geometric verification) ---
norm_u = np.sqrt(np.dot(u, u))  # sqrt(13)
norm_v = np.sqrt(np.dot(v, v))  # sqrt(17)
cos_theta = dot / (norm_u * norm_v)  # 0.673
theta_degrees = np.degrees(np.arccos(cos_theta))  # 47.7°

# --- Orthogonality check ---
a = np.array([1.0, 0.0])
b = np.array([0.0, 5.0])
print(np.dot(a, b))  # 0.0 — orthogonal
```

> For runnable implementation, see: [[code/foundations/vectors_and_spaces.py]]

## Connections

- These operations live inside [[vectors-and-vector-spaces]] — closure guarantees they always produce valid vectors
- The dot product defines [[vector-norms|L2 norm]]: $\|\mathbf{v}\|_2 = \sqrt{\mathbf{v} \cdot \mathbf{v}}$
- The dot product is the foundation of [[cosine-similarity]] — normalize by norms to isolate the angle
- The dot product directly enables [[projection]] — finding the "shadow" of one vector onto another
- Linear combinations connect to [[basis-and-dimension]] — coordinates are coefficients in a basis
- Linear combinations lead to [[linear-independence]] — can one vector be "reached" from others?
- Matrix multiplication is organized dot products → [[Matrix Operations and Properties]]
- In neural networks, each neuron computes $\mathbf{w} \cdot \mathbf{x} + b$ — a dot product + bias

## Sources

- [3Blue1Brown — Vectors, what even are they?](https://www.youtube.com/watch?v=fNk_zzaMoSs)
- [3Blue1Brown — Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0)
- [MIT 18.06 — Strang, Lecture 1: Geometry of Linear Equations](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Mathematics for Machine Learning — Chapter 2.2](https://mml-book.github.io/book/mml-book.pdf)
