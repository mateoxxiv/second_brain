---
tags:
  - status/seed
  - probability
related:
  - "[[characteristics-of-data]]"
  - "[[data-types-and-levels-of-measurement]]"
  - "[[histogram]]"
  - "[[normal-distribution]]"
domain: probability
sources:
  - "Triola, Mario F. Estadística. 11ª edición. Pearson, 2013. Cap. 2, §2-2."
---

> **TL;DR** — A frequency distribution groups raw data into non-overlapping classes and counts how many values fall in each, turning a wall of numbers into the *shape* of the [[characteristics-of-data|distribution]] — the point is understanding, not the table itself.

---

## Intuition

Forty raw pulse readings tell you almost nothing at a glance. Bin them into ranges (60–69, 70–79, …) and count each bin, and the *shape* jumps out: most women's pulses cluster in the 60s–80s, tailing off sharply above 90. That's a **frequency distribution** — the bridge from unreadable raw data to the [[characteristics-of-data|five characteristics]], especially **Distribution** (shape). Software builds these instantly, so Triola's message is: don't obsess over the mechanics, understand *what the table tells you*.

## Mechanics

**Definition** — a table listing each **class** (category/range) with its **frequency** (how many original values fall in it). Worked example, women's pulses (n = 40):

| Pulse (class) | Frequency |
|---|---|
| 60–69 | 12 |
| 70–79 | 14 |
| 80–89 | 11 |
| 90–99 | 1 |
| 100–109 | 1 |
| 110–119 | 0 |
| 120–129 | 1 |

**The five components** (using this table):

| Term | Definition | Example |
|------|-----------|---------|
| **Lower class limits** | smallest values that can belong to each class | 60, 70, 80, 90, 100, 110, 120 |
| **Upper class limits** | largest values that can belong to each class | 69, 79, 89, 99, 109, 119, 129 |
| **Class boundaries** | the split points *between* classes, in the gaps | 59.5, 69.5, 79.5, …, 129.5 |
| **Class midpoints (marks)** | center of each class = (lower + upper limit) / 2 | 64.5, 74.5, 84.5, … |
| **Class width** | gap between two *consecutive lower limits* | 10 |

**⚠️ The classic trap** — class width is the distance between consecutive **lower limits** (70 − 60 = **10**), *not* upper minus lower of the same class (69 − 60 = 9). Boundaries fix the gap by sitting at the midpoint of it (59.5, 69.5, …).

**Construction procedure (6 steps):**
1. Choose the **number of classes**, between **5 and 20**.
2. **Class width** ≈ (max − min) / (number of classes), then **round up** to a convenient number.
3. Pick the **first lower limit** = the minimum value, or a convenient number just below it.
4. Add the width repeatedly to get the remaining lower limits.
5. Write lower limits in a column, then fill in the matching upper limits.
6. **Tally** each value into its class; sum tallies → frequencies.

Worked: max 124, min 60, 7 classes → (124 − 60)/7 = 9.14 → **round up to 10**; start at 60 → limits 60, 70, …, 120.

**Tips / exceptions Triola stresses:**
- Classes must **not overlap** — every value belongs to exactly one class.
- **Include all classes**, even those with **frequency 0** (note the 110–119 row).
- Use the **same width** for all classes where possible.
- Sometimes an **open-ended** class is unavoidable ("65 and over").

## In ML

**Frequency distributions are histograms in table form** — the same binning underlies `numpy.histogram` and every EDA histogram; the [[histogram]] is just this table drawn as bars, and choosing bin count/width is exactly steps 1–2.

**Binning = feature discretization** — converting a continuous feature into ranges (`pandas.cut`) is building a frequency distribution per feature; it powers decision-tree splits, WOE/credit scorecards, and coarse categorical encodings.

**Bin-count choice is a bias–variance knob** — too few classes hide structure (oversmoothing), too many make noise look like signal — the same tradeoff as histogram bandwidth and, later, model flexibility.

## Exercises

**Basic** — For classes 60–69, 70–79, 80–89: state the lower limits, upper limits, class width, and the midpoint of the second class.

**Intermediate** — Build a frequency distribution for the 40 *men's* pulses (min 56, max 96) using 6 classes: compute the width, list the class limits, then tally.

**Advanced** — Explain why class *boundaries* (59.5, 69.5, …) are needed at all when *limits* already define the classes. What ambiguity do boundaries resolve, and where does it matter (hint: a value exactly at a limit, or drawing a gap-free histogram)?
