"""
Induced norm and distance in inner product spaces.
Shows that ||u|| = sqrt(<u,u>) and d(u,v) = ||u-v|| satisfy all 8 geometric
properties (L1-L4, D1-D4) for any inner product — standard, weighted, or function.
See: inner_product_spaces.py, cauchy_schwarz.py
"""

import numpy as np
from scipy import integrate


def induced_norm(u: np.ndarray, ip) -> float:
    return float(np.sqrt(ip(u, u)))


def induced_dist(u: np.ndarray, v: np.ndarray, ip) -> float:
    diff = u - v
    return float(np.sqrt(ip(diff, diff)))


def standard_ip(u, v):
    return float(np.dot(u, v))


def weighted_ip(u, v, W):
    return float(u @ W @ v)


# ---------------------------------------------------------------------------
# Basic: standard inner product norm and distance
# ---------------------------------------------------------------------------
print("=== Basic: standard induced norm and distance ===")
u = np.array([3., 4.])
v = np.array([1., 1.])

norm_u = induced_norm(u, standard_ip)
dist_uv = induced_dist(u, v, standard_ip)

print(f"||u|| = {norm_u:.4f}")                # 5.0
print(f"d(u,v) = {dist_uv:.4f}")              # sqrt(8) ≈ 2.828
print(f"L1 (non-neg): {norm_u >= 0}")         # True
print(f"L2 (zero iff 0): {induced_norm(np.zeros(2), standard_ip) == 0}")  # True
print(f"D3 (symmetric): {np.isclose(dist_uv, induced_dist(v, u, standard_ip))}")  # True

# ---------------------------------------------------------------------------
# Intermediate: weighted inner product — different geometry
# ---------------------------------------------------------------------------
print("\n=== Intermediate: weighted induced norm (W = diag(2, 1)) ===")
W = np.diag([2., 1.])
ip_W = lambda a, b: weighted_ip(a, b, W)

norm_u_W = induced_norm(u, ip_W)
norm_v_W = induced_norm(v, ip_W)
norm_sum_W = induced_norm(u + v, ip_W)

print(f"||u||_W = {norm_u_W:.4f}")             # sqrt(2*9 + 16) = sqrt(34) ≈ 5.831
print(f"||v||_W = {norm_v_W:.4f}")             # sqrt(2+1) = sqrt(3) ≈ 1.732
print(f"||u+v||_W = {norm_sum_W:.4f}")         # triangle inequality LHS
print(f"||u||_W + ||v||_W = {norm_u_W + norm_v_W:.4f}")  # RHS
print(f"L4 (triangle): {norm_sum_W <= norm_u_W + norm_v_W + 1e-12}")  # True

# ---------------------------------------------------------------------------
# Advanced: function space norm on [-1, 1]
# ---------------------------------------------------------------------------
print("\n=== Advanced: induced norm in function space ===")
ip_fn = lambda f, g: integrate.quad(lambda x: f(x) * g(x), -1, 1)[0]

p = lambda x: x          # polynomial p(x) = x
q = lambda x: x ** 2     # polynomial q(x) = x^2

norm_p = np.sqrt(ip_fn(p, p))   # sqrt(2/3) ≈ 0.8165
norm_q = np.sqrt(ip_fn(q, q))   # sqrt(2/5) ≈ 0.6325
pq_sum = lambda x: p(x) + q(x)
norm_sum_fn = np.sqrt(ip_fn(pq_sum, pq_sum))

print(f"||p|| = {norm_p:.4f}")               # sqrt(2/3) ≈ 0.8165
print(f"||q|| = {norm_q:.4f}")               # sqrt(2/5) ≈ 0.6325
print(f"||p+q|| = {norm_sum_fn:.4f}")        # triangle inequality LHS
print(f"||p||+||q|| = {norm_p + norm_q:.4f}")  # RHS
print(f"L4 holds: {norm_sum_fn <= norm_p + norm_q + 1e-12}")  # True


def exercises():
    """
    Exercise 1 (Basic):
        Weighted IP <u,v> = 2u1v1 + u2v2. u=[3,4], v=[1,1].
        ||u||_W = sqrt(2*9 + 16) = sqrt(34) ≈ 5.831
        d(u,v) = ||u-v||_W = ||[2,3]||_W = sqrt(2*4 + 9) = sqrt(17) ≈ 4.123

    Exercise 2 (Intermediate):
        Prove L3: ||ku||^2 = <ku,ku> = k^2<u,u> = k^2||u||^2
        Take sqrt: ||ku|| = |k| * ||u||. Uses homogeneity axiom twice.

    Exercise 3 (Advanced):
        W = [[2,1],[1,2]] (positive definite).
        Show all L1-L4 and D1-D4 hold. Key: W pos. def. → <u,u>_W > 0 for u≠0,
        so L2 holds. L4 follows from Cauchy-Schwarz for this IP.
    """
    pass
