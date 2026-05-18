"""
Subspaces: verifying the two-condition test and exploring key examples.
A subspace is a subset of a vector space closed under addition and scalar multiplication.
See also: general_vector_spaces.py, algebraic_operation_properties.py
"""

import numpy as np


def check_conditions(candidate_fn, test_vectors, scalars=(-2.0, 0.5, 0.0, -1.0)):
    """
    Verify the two subspace conditions on a set defined by candidate_fn.
    candidate_fn(v) → True if v belongs to the set.
    Returns (condition_a, condition_b, zero_in_set).
    """
    # Condition (a): closed under addition
    cond_a = all(
        candidate_fn(u + v)
        for u in test_vectors
        for v in test_vectors
    )
    # Condition (b): closed under scalar multiplication
    cond_b = all(
        candidate_fn(k * u)
        for u in test_vectors
        for k in scalars
    )
    zero = candidate_fn(np.zeros_like(test_vectors[0]))
    return cond_a, cond_b, zero


# ---------------------------------------------------------------------------
# Basic: plane through origin — x + y + z = 0
# ---------------------------------------------------------------------------
def on_plane(v):
    return np.isclose(v[0] + v[1] + v[2], 0)

plane_vectors = [
    np.array([1., -1., 0.]),
    np.array([0., 1., -1.]),
    np.array([2., -3., 1.]),
]

a, b, z = check_conditions(on_plane, plane_vectors)
print("=== Basic: plane x+y+z=0 ===")
print(f"Condition (a) closed under addition:           {a}")  # True
print(f"Condition (b) closed under scalar mult:        {b}")  # True
print(f"Zero vector in set:                            {z}")  # True
print(f"→ IS a subspace ✓" if (a and b) else "→ NOT a subspace ✗")


# ---------------------------------------------------------------------------
# Intermediate: function space f(1)=0 vs f(1)=1
# ---------------------------------------------------------------------------
print("\n=== Intermediate: function spaces ===")

# Represent functions as (slope, intercept) pairs: f(x) = m*x + c
# f(1) = m + c — must be 0

def f_at_1_zero(params):
    m, c = params
    return np.isclose(m + c, 0)

def f_at_1_one(params):
    m, c = params
    return np.isclose(m + c, 1)

# Operations: (m1,c1) + (m2,c2) = (m1+m2, c1+c2), k*(m,c) = (km, kc)
def add_fn(p, q): return np.array([p[0]+q[0], p[1]+q[1]])
def scale_fn(k, p): return np.array([k*p[0], k*p[1]])

# Functions in f(1)=0: e.g., f(x)=x-1, g(x)=2x-2
fns_zero = [np.array([1., -1.]), np.array([2., -2.]), np.array([-1., 1.])]

# Manually check conditions for f(1)=0
sum_check = all(f_at_1_zero(add_fn(p, q)) for p in fns_zero for q in fns_zero)
scale_check = all(f_at_1_zero(scale_fn(k, p)) for p in fns_zero for k in [-2, 0, 0.5, -1])
print(f"f(1)=0: closed under addition?         {sum_check}")   # True
print(f"f(1)=0: closed under scalar mult?      {scale_check}") # True
print(f"f(1)=0: IS a subspace ✓")

# Functions in f(1)=1: e.g., f(x)=x, g(x)=2x-1
fns_one = [np.array([1., 0.]), np.array([2., -1.]), np.array([0., 1.])]
sum_check_one = all(f_at_1_one(add_fn(p, q)) for p in fns_one for q in fns_one)
scale_check_one = all(f_at_1_one(scale_fn(k, p)) for p in fns_one for k in [-2, 0, 0.5])
print(f"\nf(1)=1: closed under addition?         {sum_check_one}")   # False — (1+1=2≠1)
print(f"f(1)=1: closed under scalar mult?      {scale_check_one}") # False — k=0 gives 0≠1
print(f"f(1)=1: NOT a subspace ✗ (fixed value ≠ 0 always fails)")


# ---------------------------------------------------------------------------
# Advanced: intersection of two subspaces is a subspace
# ---------------------------------------------------------------------------
print("\n=== Advanced: intersection of subspaces ===")

# W1: plane x+y+z=0, W2: plane x-y=0 (i.e. x=y)
def in_W1(v): return np.isclose(v[0]+v[1]+v[2], 0)
def in_W2(v): return np.isclose(v[0]-v[1], 0)
def in_intersection(v): return in_W1(v) and in_W2(v)

# Vectors in W1 ∩ W2: x=y, x+y+z=0 → 2x+z=0 → z=-2x. So (t,t,-2t)
intersect_vectors = [np.array([t, t, -2*t]) for t in [1., -1., 2., 0.5]]

a, b, z = check_conditions(in_intersection, intersect_vectors)
print(f"W1 ∩ W2 closed under addition?         {a}")  # True
print(f"W1 ∩ W2 closed under scalar mult?      {b}")  # True
print(f"Zero in W1 ∩ W2?                       {z}")  # True
print(f"W1 ∩ W2 IS a subspace ✓")

# Union is NOT always a subspace
print("\nUnion W1 ∪ W2 counterexample in R²:")
u = np.array([1., 0.])  # in W1: x-axis (y=0)
v = np.array([0., 1.])  # in W2: y-axis (x=0)
print(f"u={u} in x-axis (W1), v={v} in y-axis (W2)")
print(f"u+v={u+v} — on x-axis? {np.isclose(u[1]+v[1], 0)} — on y-axis? {np.isclose(u[0]+v[0], 0)}")
print(f"u+v not in W1 ∪ W2 → union is NOT a subspace ✗")


def exercises():
    """
    Exercise 1 (Basic):
        Is {(x,y,z) : 2x - y + 3z = 0} a subspace of R³?
        Apply the two-condition test symbolically, then verify with vectors
        u=(1,2,0) and v=(0,3,1). Expected: yes, it's a subspace.

    Exercise 2 (Intermediate):
        Is the set of all polynomials p(x) of degree ≤ 2 with p(0) = 0 a subspace of P₂?
        Hint: p(0)=0 means the constant term is 0, so p(x)=ax+bx².
        Verify both conditions. Expected: yes, it's a subspace.

    Exercise 3 (Advanced):
        Prove the union of two subspaces W1 ∪ W2 is a subspace
        if and only if W1 ⊆ W2 or W2 ⊆ W1.
        Hint: if neither contains the other, find u ∈ W1\W2 and v ∈ W2\W1
        and show u+v can't be in either.
    """
    pass
