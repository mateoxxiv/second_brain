"""
Trigonometric identities: numerical verification and progressive exercises.
All identities derive from sin²x + cos²x = 1 and the angle addition formulas.
See also: algebraic_operation_properties.py, exponent_log_root_properties.py
"""

import numpy as np

x = np.linspace(0, 2 * np.pi, 1000)


# ---------------------------------------------------------------------------
# Core identities — verify numerically
# ---------------------------------------------------------------------------
print("=== Pythagorean ===")
assert np.allclose(np.sin(x)**2 + np.cos(x)**2, 1)
print("sin²x + cos²x = 1  ✓")

print("\n=== Power reduction ===")
assert np.allclose(np.sin(x)**2, (1 - np.cos(2*x)) / 2)
assert np.allclose(np.cos(x)**2, (1 + np.cos(2*x)) / 2)
print("sin²x = (1 - cos2x) / 2  ✓")
print("cos²x = (1 + cos2x) / 2  ✓")

print("\n=== Double angle ===")
assert np.allclose(np.sin(2*x), 2 * np.sin(x) * np.cos(x))
assert np.allclose(np.cos(2*x), np.cos(x)**2 - np.sin(x)**2)
assert np.allclose(np.cos(2*x), 1 - 2 * np.sin(x)**2)
assert np.allclose(np.cos(2*x), 2 * np.cos(x)**2 - 1)
print("sin 2x = 2 sin x cos x  ✓")
print("cos 2x = cos²x - sin²x = 1 - 2sin²x = 2cos²x - 1  ✓")

print("\n=== Angle addition ===")
a = np.pi / 3
b = np.pi / 6
assert np.isclose(np.sin(a + b), np.sin(a)*np.cos(b) + np.cos(a)*np.sin(b))
assert np.isclose(np.cos(a + b), np.cos(a)*np.cos(b) - np.sin(a)*np.sin(b))
print(f"sin({a:.2f}+{b:.2f}) = sin a cos b + cos a sin b  ✓")
print(f"cos({a:.2f}+{b:.2f}) = cos a cos b - sin a sin b  ✓")


# ---------------------------------------------------------------------------
# Exercise 1 (Basic): show {4sin²x, 4cos²x, 1} is dependent
# ---------------------------------------------------------------------------
print("\n=== Exercise 1: {4sin²x, 4cos²x, 1} dependent? ===")
# 4sin²x + 4cos²x = 4(sin²x + cos²x) = 4 = 4·1
# → c₁=1, c₂=1, c₃=-4  →  1·4sin²x + 1·4cos²x - 4·1 = 0
c1, c2, c3 = 1, 1, -4
result = c1 * 4*np.sin(x)**2 + c2 * 4*np.cos(x)**2 + c3 * np.ones_like(x)
assert np.allclose(result, 0)
print(f"1·(4sin²x) + 1·(4cos²x) + ({c3})·1 = 0 for all x  ✓  → dependent")


# ---------------------------------------------------------------------------
# Exercise 2 (Intermediate): {sin²x, cos²x} independent, {sin²x, cos²x, 1} dependent
# ---------------------------------------------------------------------------
print("\n=== Exercise 2: independence check ===")

# {sin²x, cos²x} — check: c1*sin²x + c2*cos²x = 0 for all x?
# x=0: c2 = 0; x=π/2: c1 = 0 → only trivial solution → independent
c1_check = np.sin(np.pi/2)**2  # = 1
c2_check = np.cos(0)**2        # = 1
print(f"sin²(π/2) = {c1_check}, cos²(0) = {c2_check}")
print("{sin²x, cos²x} → only trivial solution → independent ✓")

# {sin²x, cos²x, 1} — sin²x + cos²x - 1 = 0
result2 = np.sin(x)**2 + np.cos(x)**2 - np.ones_like(x)
assert np.allclose(result2, 0)
print("{sin²x, cos²x, 1} → c₁=1, c₂=1, c₃=-1 → dependent ✓")


# ---------------------------------------------------------------------------
# Exercise 3 (Advanced): {cos 2x, sin²x, cos²x} dependent
# ---------------------------------------------------------------------------
print("\n=== Exercise 3: {cos2x, sin²x, cos²x} ===")
# cos 2x = cos²x - sin²x
# → 1·cos2x + 1·sin²x - 1·cos²x = (cos²x-sin²x) + sin²x - cos²x = 0
result3 = np.cos(2*x) + np.sin(x)**2 - np.cos(x)**2
assert np.allclose(result3, 0)
print("cos2x + sin²x - cos²x = 0 for all x  ✓  → dependent")


def exercises():
    """
    Exercise 1 (Basic):
        Show {4sin²x, 4cos²x, 1} is dependent.
        Find c₁, c₂, c₃ such that c₁·4sin²x + c₂·4cos²x + c₃·1 = 0.
        Expected: c₁=1, c₂=1, c₃=-4 (or any scalar multiple).

    Exercise 2 (Intermediate):
        Show {sin²x, cos²x} is independent but {sin²x, cos²x, 1} is dependent.
        Hint: for independence, plug in x=0 and x=π/2 to force each c to zero.

    Exercise 3 (Advanced):
        Show {1, sin x, cos x, sin 2x, cos 2x} is linearly independent in V.
        Strategy: assume c₁ + c₂sinx + c₃cosx + c₄sin2x + c₅cos2x = 0 for all x,
        then differentiate repeatedly and evaluate at x=0 to extract each coefficient.
    """
    pass
