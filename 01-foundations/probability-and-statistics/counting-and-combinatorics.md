---
tags:
  - status/seed
  - probability
related:
  - "[[sample-space-and-events]]"
  - "[[three-methods-of-assigning-probability]]"
  - "[[binomial-distribution]]"
  - "[[probability-fundamentals]]"
  - "[[triola-estadistica]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. §4-7 (Ejemplos 1–7)."
---

> **TL;DR** — Counting rules give the **total number of possible outcomes** without listing them; the whole toolkit is picked by two questions — *does order matter?* (permutation vs. combination) and *are items repeated?*

---

## Intuition

The [[three-methods-of-assigning-probability|classical method]] needs the size of the [[sample-space-and-events|sample space]] — but writing out all outcomes is hopeless (a 9-digit number has a *billion* possibilities). Counting rules compute that total directly.

Everything builds on one idea: the **fundamental counting rule** — if a first choice has m options and a second has n, together they have m·n. Chain it and you get factorials (arranging n things), permutations (order matters), and combinations (order doesn't). The single most important fork: **is ABC different from CBA?** If yes → *permutation*; if they're the same → *combination*.

## Mechanics

| Rule | Formula | Use when |
|------|---------|----------|
| **Fundamental counting** | $m \cdot n \cdot \dots$ | a sequence of independent choices |
| **Factorial** | $n!$ | arrange *all* $n$ distinct items in order |
| **Permutations** (distinct) | $_nP_r = \dfrac{n!}{(n-r)!}$ | pick & **order** $r$ of $n$ (order matters) |
| **Permutations** (identical items) | $\dfrac{n!}{n_1!\,n_2!\cdots n_k!}$ | arrange all $n$ when some are alike |
| **Combinations** | $_nC_r = \dfrac{n!}{(n-r)!\,r!}$ | pick $r$ of $n$, **order ignored** |

Notation: $n! = n(n-1)\cdots 1$, and by definition $0! = 1$.

**The key link:** a combination undercounts a permutation by exactly the $r!$ ways to reorder the chosen items: $_nP_r = r!\cdot {}_nC_r$. That extra $r!$ in the denominator of $_nC_r$ is "dividing out the order."

**Worked (Triola):**
- *Exacta* — pick horses for 1st & 2nd of 20, order matters: $_{20}P_2 = 20!/18! = 380$.
- *Lottery* — pick 6 of 53, order irrelevant: $_{53}C_6 = 53!/(47!\,6!) = 22{,}957{,}480$, so P(jackpot) = 1/22,957,480.

```python
from math import comb, perm, factorial
print(perm(20, 2))   # 380   (order matters)
print(comb(53, 6))   # 22957480 (order ignored)
```

## In ML

**The binomial coefficient is nCr.** $\binom{n}{k}$ — the number of ways to get $k$ successes in $n$ trials — is exactly a combination, and it's the front factor of the [[binomial-distribution|binomial]] PMF. Triola even flags §4-7's two-category permutation formula $\frac{n!}{(n-x)!x!}$ as the §5-3 binomial setup.

**Combinatorial explosion motivates smart search.** $n!$ growth is *why* brute force fails: 20 delivery stops = 20! ≈ 2.4×10¹⁸ routes (the traveling-salesman problem). Feature-subset selection, hyperparameter grids, and decision-tree splits all face this blow-up, forcing greedy/heuristic/approximate methods instead of enumeration.

**Combinations underlie sampling and evaluation.** Choosing $k$ features from $p$, forming cross-validation folds, or bagging subsets are all "count/choose without order" problems; permutation *importance* and permutation *tests*, conversely, rely on reordering (order matters) to build a null distribution.

## Exercises

**Basic** — A PIN is 4 digits (0–9), repeats allowed. How many PINs exist? Which rule, and why isn't it a permutation?

**Intermediate** — From 10 books, how many ways to (a) arrange 3 on a shelf, (b) choose 3 to give away? Explain why (a) is $6\times$ larger than (b).

**Advanced** — Show that $_nC_r = {}_nC_{n-r}$ both algebraically and by a "choosing = leaving behind" argument. Then explain why $\binom{n}{k}$ counts the paths with exactly $k$ successes in the binomial PMF.
