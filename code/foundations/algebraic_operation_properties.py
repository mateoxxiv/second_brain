"""
Algebraic operation properties: commutativity, associativity, distributivity,
identity, and inverse for addition and multiplication.
Connects directly to the vector space axioms in general_vector_spaces.py.
"""

import numpy as np


a, b, c = 3.0, 5.0, 7.0

print("=== Basic: scalar arithmetic properties ===")
print(f"Commutativity +:    {a}+{b} = {b}+{a}?  {a+b == b+a}")
print(f"Commutativity ×:    {a}×{b} = {b}×{a}?  {a*b == b*a}")
print(f"Associativity +:    ({a}+{b})+{c} = {a}+({b}+{c})?  {(a+b)+c == a+(b+c)}")
print(f"Associativity ×:    ({a}×{b})×{c} = {a}×({b}×{c})?  {(a*b)*c == a*(b*c)}")
print(f"Distributivity:     {a}×({b}+{c}) = {a}×{b}+{a}×{c}?  {a*(b+c) == a*b+a*c}")
print(f"Identity +:         {a}+0 = {a}?  {a+0 == a}")
print(f"Identity ×:         {a}×1 = {a}?  {a*1 == a}")
print(f"Inverse +:          {a}+({-a}) = 0?  {a+(-a) == 0}")
print(f"Inverse ×:          {a}×(1/{a}) = 1?  {np.isclose(a*(1/a), 1)}")
print(f"Absorption:         {a}×0 = 0?  {a*0 == 0}")


# ---------------------------------------------------------------------------
# Intermediate: matrix multiplication breaks commutativity
# ---------------------------------------------------------------------------
A = np.array([[1., 2.], [3., 4.]])
B = np.array([[5., 6.], [7., 8.]])
C = np.array([[1., 0.], [0., 2.]])

print("\n=== Intermediate: matrix multiplication properties ===")
print(f"Commutativity AB=BA?   {np.allclose(A @ B, B @ A)}")    # False
print(f"Associativity A(BC)?   {np.allclose(A @ (B @ C), (A @ B) @ C)}")  # True
print(f"Distributivity A(B+C)? {np.allclose(A @ (B + C), A @ B + A @ C)}") # True
print(f"\nAB =\n{A @ B}")
print(f"BA =\n{B @ A}")


# ---------------------------------------------------------------------------
# Advanced: floating-point associativity breaks
# ---------------------------------------------------------------------------
print("\n=== Advanced: floating-point associativity failure ===")
x = 1e16
y = -1e16
z = 1.0

result_left  = (x + y) + z   # (1e16 - 1e16) + 1 = 0 + 1 = 1.0
result_right = x + (y + z)   # 1e16 + (-1e16 + 1) — rounding kills the 1

print(f"(x+y)+z = {result_left}")     # 1.0 — correct
print(f"x+(y+z) = {result_right}")    # 0.0 — wrong! associativity fails
print(f"Same result? {result_left == result_right}")


def exercises():
    """
    Exercise 1 (Basic):
        Expand (x+2)(x-3) using distributivity step by step.
        Step 1: x(x-3) + 2(x-3)
        Step 2: x²-3x + 2x-6
        Step 3: x²-x-6
        Verify at x=4: (6)(1)=6, 16-4-6=6 ✓

    Exercise 2 (Intermediate):
        For A=[[1,2],[0,1]], B=[[1,0],[1,1]]:
        Compute AB and BA. Show AB ≠ BA.
        Verify A(B+C) = AB+AC for a matrix C of your choice.

    Exercise 3 (Advanced):
        Prove additive inverse is unique using only commutativity and associativity.
        Assume u + v = 0 and u + w = 0.
        Then: v = v+0 = v+(u+w) = (v+u)+w = 0+w = w.
        Each step uses only one property — identify which.
    """
    pass
