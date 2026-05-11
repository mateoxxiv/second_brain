"""
Inner product spaces: standard, weighted, and function inner products.
Demonstrates that geometry (length, angle, orthogonality) works in any
inner product space — not just R^n.
See also: euclidean_n_space.py, general_vector_spaces.py
"""

import numpy as np
from scipy import integrate


def standard_ip(u: np.ndarray, v: np.ndarray) -> float:
    """Standard dot product on R^n."""
    return float(np.dot(u, v))


def weighted_ip(u: np.ndarray, v: np.ndarray, w: np.ndarray) -> float:
    """Weighted inner product: <u,v>_w = sum(w_i * u_i * v_i), w_i > 0."""
    return float(np.dot(w * u, v))


def function_ip(f, g, a: float = 0, b: float = 1) -> float:
    """Function inner product: integral of f(x)*g(x) over [a, b]."""
    return float(integrate.quad(lambda x: f(x) * g(x), a, b)[0])


def induced_norm(u: np.ndarray, ip_fn) -> float:
    """Norm induced by any inner product: ||u|| = sqrt(<u,u>)."""
    return float(np.sqrt(ip_fn(u, u)))


# ---------------------------------------------------------------------------
# Basic: standard inner product — axiom verification
# ---------------------------------------------------------------------------
u = np.array([1., 2., 3.])
v = np.array([4., 5., 6.])
w_vec = np.array([0., 0., 0.])   # zero vector

print("=== Basic: standard inner product axioms ===")
print(f"<u,v> = {standard_ip(u, v)}")                              # 32.0
print(f"Symmetry:    <u,v> = <v,u>?  {np.isclose(standard_ip(u,v), standard_ip(v,u))}")  # True
print(f"Positivity:  <u,u> >= 0?     {standard_ip(u, u) >= 0}")                          # True
print(f"Zero only:   <0,0> = 0?      {np.isclose(standard_ip(w_vec, w_vec), 0)}")        # True
print(f"Induced norm ||u|| = {induced_norm(u, standard_ip):.4f}")  # sqrt(14) ≈ 3.742

# ---------------------------------------------------------------------------
# Intermediate: weighted inner product + orthogonality check
# ---------------------------------------------------------------------------
w = np.array([2., 3.])   # weights: feature 2 is 3× more important
a = np.array([1., 2.])
b = np.array([3., 1.])

ip_ab = weighted_ip(a, b, w)
norm_a = induced_norm(a, lambda u, v: weighted_ip(u, v, w))
norm_b = induced_norm(b, lambda u, v: weighted_ip(u, v, w))
cos_theta = ip_ab / (norm_a * norm_b)

print("\n=== Intermediate: weighted inner product ===")
print(f"<a,b>_w = 2·1·3 + 3·2·1 = {ip_ab}")          # 12.0
print(f"||a||_w = {norm_a:.4f}")                       # sqrt(2+12) = sqrt(14) ≈ 3.742
print(f"cos θ   = {cos_theta:.4f}")                    # angle in weighted geometry
print(f"Cauchy-Schwarz: {ip_ab:.4f} ≤ {norm_a * norm_b:.4f}?  {ip_ab <= norm_a * norm_b + 1e-9}")

# ---------------------------------------------------------------------------
# Advanced: function inner product — sin ⊥ cos on [0, 2π]
# ---------------------------------------------------------------------------
print("\n=== Advanced: function inner product ===")
ip_sin_cos = function_ip(np.sin, np.cos, 0, 2 * np.pi)
ip_sin_sin = function_ip(np.sin, np.sin, 0, 2 * np.pi)
ip_cos_cos = function_ip(np.cos, np.cos, 0, 2 * np.pi)

print(f"<sin, cos> = {ip_sin_cos:.6f}")    # ≈ 0.0  (orthogonal)
print(f"<sin, sin> = {ip_sin_sin:.4f}")    # π ≈ 3.1416
print(f"<cos, cos> = {ip_cos_cos:.4f}")    # π ≈ 3.1416
print(f"||sin|| = {np.sqrt(ip_sin_sin):.4f}")  # sqrt(π) ≈ 1.7725
print(f"sin ⊥ cos? {np.isclose(ip_sin_cos, 0, atol=1e-10)}")  # True


def exercises():
    """
    Exercise 1 (Basic):
        Weighted IP: <u,v> = 2u1v1 + 3u2v2. u=[1,2], v=[3,1].
        Verify all 4 axioms. Compute induced norm ||u||_w.
        Expected: <u,v>_w = 2·3 + 3·2 = 12, ||u||_w = sqrt(2+12) = sqrt(14) ≈ 3.742

    Exercise 2 (Intermediate):
        Show sin(x) ⊥ cos(x) on [0, 2π] under the function inner product.
        By hand: integral of sin(x)cos(x) = integral of sin(2x)/2 from 0 to 2π.
        Expected: [-cos(2x)/4] from 0 to 2π = 0.

    Exercise 3 (Advanced):
        Prove Cauchy-Schwarz for a general inner product space.
        Start: let h(t) = <u - t*v, u - t*v> >= 0 for all t.
        Expand using axioms 1-3: h(t) = <u,u> - 2t<u,v> + t^2<v,v>
        Minimize: t* = <u,v>/<v,v>
        Substitute back: h(t*) = <u,u> - <u,v>^2/<v,v> >= 0
        → <u,v>^2 <= <u,u>·<v,v> → |<u,v>| <= ||u||·||v||
    """
    pass
