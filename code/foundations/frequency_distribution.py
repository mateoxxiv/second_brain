"""
Frequency distribution builder — Triola Estadistica, Cap. 2, seccion 2-2.

Constructs a frequency distribution from raw data following Triola's 6-step
procedure, and exposes the five standard components (class limits, boundaries,
midpoints, width). Demonstrated on the women's pulse data from Table 2-1.

Companion to the note: 01-foundations/probability-and-statistics/frequency-distribution.md

Run:
    python frequency_distribution.py
Depends on: numpy (stdlib math would also do; numpy used for clarity).
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# Women's pulse readings (beats per minute), Triola Table 2-1, n = 40.
WOMEN_PULSES: list[int] = [
    76, 72, 88, 60, 72, 68, 80, 64, 68, 68, 80, 76, 68, 72, 96, 72, 68, 72, 64, 80,
    64, 80, 76, 76, 76, 80, 104, 88, 60, 76, 72, 72, 88, 80, 60, 72, 88, 88, 124, 64,
]


@dataclass
class FrequencyDistribution:
    """A frequency distribution and its five Triola components."""

    lower_limits: list[int]
    upper_limits: list[int]
    frequencies: list[int]
    width: int

    @property
    def boundaries(self) -> list[float]:
        """Class boundaries: midpoints of the gaps between limits."""
        bounds = [self.lower_limits[0] - 0.5]
        bounds += [u + 0.5 for u in self.upper_limits]
        return bounds

    @property
    def midpoints(self) -> list[float]:
        """Class midpoints (marks) = (lower + upper) / 2."""
        return [(lo + up) / 2 for lo, up in zip(self.lower_limits, self.upper_limits)]

    def total(self) -> int:
        return sum(self.frequencies)

    def show(self) -> None:
        print(f"{'Class':>12} {'Mid':>7} {'Freq':>5}")
        for lo, up, mid, f in zip(
            self.lower_limits, self.upper_limits, self.midpoints, self.frequencies
        ):
            print(f"{lo:>5}-{up:<6} {mid:>7} {f:>5}")
        print(f"{'width =':>12} {self.width}   total = {self.total()}")


def build_frequency_distribution(
    data: list[int], n_classes: int, first_lower: int | None = None
) -> FrequencyDistribution:
    """Follow Triola's 6-step procedure to build a frequency distribution.

    Step 1: choose n_classes (caller supplies, should be 5-20).
    Step 2: width = ceil((max - min) / n_classes)   -- round UP.
    Step 3: first lower limit = min (or a convenient value just below).
    Step 4: successive lower limits by adding the width.
    Step 5: upper limits = next lower limit - 1.
    Step 6: tally each value into exactly one class.
    """
    if not 5 <= n_classes <= 20:
        # Triola's guideline; a warning, not a hard error.
        print(f"[warn] n_classes={n_classes} is outside the recommended 5-20 range.")

    lo_val, hi_val = min(data), max(data)
    width = math.ceil((hi_val - lo_val) / n_classes)          # step 2: round up
    start = lo_val if first_lower is None else first_lower     # step 3

    lower_limits = [start + i * width for i in range(n_classes)]   # step 4
    upper_limits = [lo + width - 1 for lo in lower_limits]         # step 5

    frequencies = [0] * n_classes                                  # step 6
    for x in data:
        idx = (x - start) // width
        if 0 <= idx < n_classes:
            frequencies[idx] += 1
        else:
            raise ValueError(f"value {x} falls outside the class range")

    return FrequencyDistribution(lower_limits, upper_limits, frequencies, width)


def exercises() -> None:
    """Progressive checks with expected outputs."""
    print("\n=== BASIC: reproduce Triola Table 2-2 (women, 7 classes) ===")
    fd = build_frequency_distribution(WOMEN_PULSES, n_classes=7)
    fd.show()
    # Expected frequencies: [12, 14, 11, 1, 1, 0, 1], width 10, total 40
    assert fd.frequencies == [12, 14, 11, 1, 1, 0, 1], fd.frequencies
    assert fd.width == 10 and fd.total() == 40
    assert fd.boundaries[0] == 59.5 and fd.boundaries[-1] == 129.5
    assert fd.midpoints[0] == 64.5
    print("basic OK")

    print("\n=== INTERMEDIATE: men's pulses, 6 classes ===")
    men = [
        68, 64, 88, 72, 64, 72, 60, 88, 76, 60, 96, 72, 56, 64, 60, 64, 84, 76, 84, 88,
        72, 56, 68, 64, 60, 68, 60, 60, 56, 84, 72, 84, 88, 56, 64, 56, 56, 60, 64, 72,
    ]
    fd_men = build_frequency_distribution(men, n_classes=6)
    fd_men.show()
    assert fd_men.total() == 40
    print("intermediate OK")

    print("\n=== ADVANCED: width trap — consecutive lower limits, not upper-lower ===")
    # width is 10 (70-60), NOT 9 (69-60).
    assert fd.lower_limits[1] - fd.lower_limits[0] == fd.width == 10
    assert fd.upper_limits[0] - fd.lower_limits[0] == 9  # the tempting wrong answer
    print("advanced OK — width is 10, not 9")


if __name__ == "__main__":
    exercises()
