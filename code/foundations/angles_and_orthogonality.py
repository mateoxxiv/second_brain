"""
Angles and orthogonality in inner product spaces.
Demonstrates: angle formula cos θ = <u,v>/(||u||||v||), orthogonality (<u,v>=0),
and the generalized Pythagorean theorem in R^n and function spaces.
See: inner_product_spaces.py, cauchy_schwarz.py
"""

import numpy as np
from scipy import integrate


def angle_deg(u: np.ndarray, v: np.ndarray, ip) -> float:
    """Angle between u and v in degrees under inner product ip."""
    cos_t = ip(u, v) / (np.sqrt(ip(u, u)) * np.sqrt(ip(v, v)))
    cos_t = np.clip(cos_t, -1.0, 1.0)
    return float(np.degrees(np.arccos(cos_t)))


def is_orthogonal(u, v, ip, tol: float = 1e-10) -> bool:
    return abs(ip(u, v)) < tol


standard_ip = lambda u, v: float(np.dot(u, v))

# ---------------------------------------------------------------------------
# Basic: angle in R^4 (Example 50, Anton Ch. 6)
# ---------------------------------------------------------------------------
print("=== Basic: angle in R^4 ===")
u = np.array([4., 3., 1., -2.])
v = np.array([-2., 1., 2., 3.])

ip_uv   = standard_ip(u, v)       # 4*(-2)+3*1+1*2+(-2)*3 = -8+3+2-6 = -9
norm_u  = np.sqrt(standard_ip(u, u))  # sqrt(30)
norm_v  = np.sqrt(standard_ip(v, v))  # sqrt(18)

print(f"<u,v> = {ip_uv}")                     # -9
print(f"||u|| = {norm_u:.4f}")                # sqrt(30) ≈ 5.477
print(f"||v|| = {norm_v:.4f}")                # sqrt(18) ≈ 4.243
print(f"cos θ = {ip_uv/(norm_u*norm_v):.4f}") # -9/(sqrt(30)*sqrt(18)) ≈ -0.387
print(f"θ     = {angle_deg(u, v, standard_ip):.2f}°")  # ≈ 112.8°

# ---------------------------------------------------------------------------
# Intermediate: orthogonality in polynomial space P2 (Example 52, Anton)
# ---------------------------------------------------------------------------
print("\n=== Intermediate: orthogonality in function space [-1,1] ===")
ip_fn = lambda f, g: integrate.quad(lambda x: f(x) * g(x), -1, 1)[0]

p = lambda x: x       # p(x) = x
q = lambda x: x**2    # q(x) = x^2

ip_pq = ip_fn(p, q)
norm_p = np.sqrt(ip_fn(p, p))   # sqrt(int x^2 on [-1,1]) = sqrt(2/3)
norm_q = np.sqrt(ip_fn(q, q))   # sqrt(int x^4 on [-1,1]) = sqrt(2/5)

print(f"<p, q> = {ip_pq:.6f}")               # 0.0 → orthogonal
print(f"||p||  = {norm_p:.4f}")              # sqrt(2/3) ≈ 0.8165
print(f"||q||  = {norm_q:.4f}")              # sqrt(2/5) ≈ 0.6325
print(f"orthogonal: {is_orthogonal(p, q, ip_fn)}")  # True

# ---------------------------------------------------------------------------
# Advanced: generalized Pythagorean theorem — verify and use
# ---------------------------------------------------------------------------
print("\n=== Advanced: generalized Pythagorean theorem ===")

# In R^n: u perp v → ||u+v||^2 = ||u||^2 + ||v||^2
a = np.array([1., 0., 0.])
b = np.array([0., 1., 0.])   # a and b are orthogonal

lhs = standard_ip(a + b, a + b)
rhs = standard_ip(a, a) + standard_ip(b, b)
print(f"||a+b||^2 = {lhs:.4f}")              # 2.0
print(f"||a||^2 + ||b||^2 = {rhs:.4f}")      # 2.0
print(f"Pythagorean: {np.isclose(lhs, rhs)}") # True

# In function space: p⊥q, so ||p+q||^2 = ||p||^2 + ||q||^2
pq_sum = lambda x: p(x) + q(x)
lhs_fn = ip_fn(pq_sum, pq_sum)
rhs_fn = ip_fn(p, p) + ip_fn(q, q)
print(f"\n||p+q||^2      = {lhs_fn:.4f}")     # 2/3 + 2/5 = 16/15 ≈ 1.067
print(f"||p||^2+||q||^2 = {rhs_fn:.4f}")     # same
print(f"Pythagorean fn:  {np.isclose(lhs_fn, rhs_fn)}")  # True


def exercises():
    """
    Exercise 1 (Basic):
        u=[4,3,1,-2], v=[-2,1,2,3] in R^4.
        <u,v> = -8+3+2-6 = -9
        ||u|| = sqrt(16+9+1+4) = sqrt(30), ||v|| = sqrt(4+1+4+9) = sqrt(18)
        cos θ = -9/(sqrt(30)*sqrt(18)) = -9/sqrt(540) = -3/sqrt(60) = -3/(2sqrt(15))
        θ = arccos(-3/(2sqrt(15))) ≈ 112.8°

    Exercise 2 (Intermediate):
        <p,q> = int_{-1}^{1} x * x^2 dx = int_{-1}^{1} x^3 dx = [x^4/4]_{-1}^{1} = 1/4 - 1/4 = 0
        ||p|| = sqrt(int_{-1}^1 x^2 dx) = sqrt([x^3/3]_{-1}^1) = sqrt(2/3)
        ||q|| = sqrt(int_{-1}^1 x^4 dx) = sqrt([x^5/5]_{-1}^1) = sqrt(2/5)

    Exercise 3 (Advanced):
        Converse of Pythagorean: assume ||u+v||^2 = ||u||^2 + ||v||^2.
        Expand: ||u||^2 + 2<u,v> + ||v||^2 = ||u||^2 + ||v||^2
        → 2<u,v> = 0 → <u,v> = 0. Done.
    """
    pass
