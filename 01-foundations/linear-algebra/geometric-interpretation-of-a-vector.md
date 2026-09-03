---
tags:
  - status/seed
  - linear-algebra
related:
  - "[[vectors-and-vector-spaces]]"
  - "[[vector-operations]]"
  - "[[vector-norms]]"
  - "[[euclidean-n-space]]"
  - "[[angles-and-orthogonality]]"
  - "[[cosine-similarity]]"
  - "[[platzi-algebra-lineal]]"
domain: linear-algebra
sources:
  - "Platzi — Álgebra Lineal, Clase 2 (intuition companion: qué es un vector y cómo graficarlo)."
  - "3Blue1Brown, Essence of Linear Algebra, Ch. 1 (vectors, what even are they?)."
---

> **TL;DR** — The *same* ordered list of numbers is two geometric objects at once: a **point** (a fixed location) and an **arrow** (a displacement from the origin with direction and length) — and you switch between the two readings depending on what you want to see.

---

## Intuition

Start below a vector: a **scalar** is a single number — one magnitude, like 25°C or $10. But most real things need several numbers at once, and their *order* carries meaning. That ordered list is a **vector**: $(3,2)$ is not $(2,3)$ — the first slot and second slot mean different things (3 items at \$2 vs. 2 items at \$3). Each entry is a **component**, and its position is fixed.

Where [[vectors-and-vector-spaces]] says "forget arrows" to focus on vectors *as data*, this note does the opposite: it recovers the **geometry** that makes the operations visual. The one list $(3,2)$ reads two ways:

- **As a point** — the location you reach by going 3 along $x$ and 2 along $y$. A fixed spot. Handy when plotting *many* vectors at once (a cloud of dots, not a tangle of arrows).
- **As an arrow** — the trip *from the origin* $(0,0)$ to that point. An arrow has exactly two properties: **direction** (where it points) and **[[vector-norms|magnitude]]** (how long it is). This is the default in linear algebra because it turns [[vector-operations|addition and scaling]] into visible *movements* — sliding, stretching, flipping.

## Mechanics

The count of components is the **dimension** — it names the space the vector lives in ([[euclidean-n-space|$\mathbb{R}^n$]], the reals to the $n$):

| Vector | Space | Picture |
|--------|-------|---------|
| $(x,y)$ | $\mathbb{R}^2$ | a plane |
| $(x,y,z)$ | $\mathbb{R}^3$ | 3D space we live in |
| $(x_1,\dots,x_n)$ | $\mathbb{R}^n$ | $n$ axes (no longer drawable, same rules) |

**To graph** any vector: place component 1 on the $x$-axis, component 2 on $y$ (component 3 on $z$ in $\mathbb{R}^3$), mark the point, draw an arrow from the origin to it. Signs steer the arrow — a negative component points down/left:

```
U = (-1, 3)  → up-left   (x negative)
V = ( 4, 1)  → right, shallow rise
W = ( 2,-1)  → down-right (y negative)
```

In $\mathbb{R}^3$, $V=(3,4,5)$: 3 along $x$, 4 along $y$, 5 up $z$ — the tip of the arrow from the origin. Reading signs and lengths at a glance is a trainable skill, and it's the foundation the operation notes build on.

## In ML

**Embeddings are arrows in $\mathbb{R}^n$.** A word or image embedding is a point in a high-dimensional space; "similar meaning" becomes "small angle between arrows," which is exactly [[cosine-similarity]] and [[angles-and-orthogonality]]. The geometric reading is what makes that intuition possible — you can't picture $\mathbb{R}^{1536}$, but the *rules* are identical to $\mathbb{R}^2$.

**Real quantities are vectors.** A drone's state $(\text{lon},\text{lat},\text{alt})$, a character's per-frame movement $(\Delta x,\Delta y)$, or a velocity "80 km/h northeast" are all arrows — magnitude *and* direction — not lone scalars. Modeling them as vectors is what lets one equation move the whole object.

## Exercises

**Basic** — Plot $\mathbf{a}=(-2,-3)$ as an arrow from the origin. Which quadrant does it point into, and how do you know from the signs alone?

**Intermediate** — Give a real quantity that needs a 3-component vector in $\mathbb{R}^3$, name what each component is, and explain why a single scalar loses information. Then say why $(1,2,3)\neq(3,2,1)$ for your example.

**Advanced** — The "point" and "arrow" readings coincide only because the arrow starts at the origin. If an arrow may start *anywhere* (a free vector / displacement), argue why $(3,2)$ then describes infinitely many arrows but still one displacement — and connect this to why vector addition is "tip-to-tail."
