"""
Cauchy-Schwarz inequality: verification and proof sketch in R^n and inner product spaces.
Shows |<u,v>| <= ||u|| * ||v|| and the equality condition (parallel vectors).
See: inner_product_spaces.py, euclidean_n_space.py
"""

import numpy as np
from scipy import integrate


def check_cauchy_schwarz(u: np.ndarray, v: np.ndarray) -> dict:
    """Verify CS for R^n vectors, return both sides and the angle."""
    lhs = abs(float(np.dot(u, v)))
    rhs = float(np.linalg.norm(u) * np.linalg.norm(v))
    cos_theta = np.clip(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)), -1, 1)
    return {"lhs": lhs, "rhs": rhs, "holds": lhs <= rhs + 1e-12,
            "angle_deg": float(np.degrees(np.arccos(cos_theta)))}


def function_cs(f, g, a: float, b: float) -> dict:
    """CS for functions: <f,g>^2 <= <f,f><g,g> on [a,b]."""
    ip = lambda p, q: integrate.quad(lambda x: p(x) * q(x), a, b)[0]
    lhs = ip(f, g) ** 2
    rhs = ip(f, f) * ip(g, g)
    return {"lhs": lhs, "rhs": rhs, "holds": lhs <= rhs + 1e-10}


# ---------------------------------------------------------------------------
# Basic: verify CS for two vectors; check equality when parallel
# ---------------------------------------------------------------------------
print("=== Basic: Cauchy-Schwarz in R^n ===")
u, v = np.array([1., 2., 2.]), np.array([2., 1., -2.])
res = check_cauchy_schwarz(u, v)
print(f"|<u,v>|      = {res['lhs']:.4f}")   # 0.0
print(f"||u||·||v||  = {res['rhs']:.4f}")   # 3 * 3 = 9
print(f"CS holds:      {res['holds']}")      # True
print(f"Angle:         {res['angle_deg']:.2f}°")

# Equality: parallel vectors u = 2v
u_par = np.array([2., 4., 4.])
v_par = np.array([1., 2., 2.])
res_eq = check_cauchy_schwarz(u_par, v_par)
print(f"\nParallel: |<u,v>| = {res_eq['lhs']:.4f}, ||u||·||v|| = {res_eq['rhs']:.4f}")
print(f"Equality holds: {np.isclose(res_eq['lhs'], res_eq['rhs'])}")  # True

# ---------------------------------------------------------------------------
# Intermediate: triangle inequality from Cauchy-Schwarz
# ---------------------------------------------------------------------------
print("\n=== Intermediate: triangle inequality ===")
a_vec = np.array([3., 4.])
b_vec = np.array([1., 2.])

lhs_tri = np.linalg.norm(a_vec + b_vec)
rhs_tri = np.linalg.norm(a_vec) + np.linalg.norm(b_vec)
print(f"||u+v||          = {lhs_tri:.4f}")   # sqrt(41) ≈ 6.403
print(f"||u|| + ||v||    = {rhs_tri:.4f}")   # 5 + sqrt(5) ≈ 7.236
print(f"Triangle holds:    {lhs_tri <= rhs_tri + 1e-12}")  # True

# ---------------------------------------------------------------------------
# Advanced: CS for functions — sin ⊥ cos, but sin and 1 are not
# ---------------------------------------------------------------------------
print("\n=== Advanced: CS for functions on [0, 2π] ===")
res_orth = function_cs(np.sin, np.cos, 0, 2 * np.pi)
print(f"sin, cos: <f,g>² = {res_orth['lhs']:.6f}, <f,f><g,g> = {res_orth['rhs']:.4f}")
print(f"CS holds: {res_orth['holds']}")  # True (equality at 0 since orthogonal)

f_const = lambda x: np.ones_like(x)
res_gen = function_cs(np.sin, f_const, 0, 2 * np.pi)
print(f"sin, 1:  <f,g>² = {res_gen['lhs']:.6f}, <f,f><g,g> = {res_gen['rhs']:.4f}")
print(f"CS holds: {res_gen['holds']}")   # True (strict inequality)


def exercises():
    """
    Exercise 1 (Basic):
        u=[1,2,2], v=[2,1,-2]. Compute |u·v| and ||u||·||v|| by hand.
        u·v = 2+2-4 = 0  →  |u·v| = 0
        ||u|| = sqrt(1+4+4) = 3,  ||v|| = sqrt(4+1+4) = 3  →  rhs = 9
        CS: 0 ≤ 9  ✓.  Angle = 90° (orthogonal).

    Exercise 2 (Intermediate):
        Prove the triangle inequality.
        ||u+v||² = <u+v,u+v> = <u,u> + 2<u,v> + <v,v>
                ≤ ||u||² + 2||u||·||v|| + ||v||²   (by CS on cross term)
                = (||u|| + ||v||)²
        Take square root: ||u+v|| ≤ ||u|| + ||v||.

    Exercise 3 (Advanced):
        Equality condition: CS holds with equality iff u = λv.
        In the proof, at* u + v = 0 where t* = -<u,v>/<u,u>.
        So v = -t* u = (<u,v>/<u,u>) u = λu  →  u and v are linearly dependent.
        Conversely, if v = λu, then <u,v> = λ<u,u>, so <u,v>² = λ²<u,u>² = <u,u><v,v>.
    """
    pass
