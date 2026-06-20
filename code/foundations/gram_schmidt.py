"""
Gram-Schmidt orthogonalization: converts any linearly independent set to an
orthonormal basis by iteratively projecting out components and normalizing.
Theorem 21 (Anton §4.9): every nonzero finite-dimensional inner product space
has an orthonormal basis.
See: orthonormal_bases.py, angles_and_orthogonality.py
"""

import numpy as np
from scipy import integrate


def gram_schmidt(basis: list[np.ndarray], ip=None) -> list[np.ndarray]:
    """
    Modified Gram-Schmidt: subtracts projections from the running vector
    (numerically more stable than classical GS which uses the original u each time).
    Returns a list of orthonormal vectors spanning the same subspace as `basis`.
    """
    if ip is None:
        ip = lambda u, v: float(np.dot(u, v))
    ortho = []
    for u in basis:
        v = u.copy().astype(float)
        for q in ortho:
            v = v - ip(v, q) * q   # subtract projection onto each prior vector
        ortho.append(v / np.sqrt(ip(v, v)))
    return ortho


def verify_orthonormal(vecs: list[np.ndarray], ip=None, tol: float = 1e-10) -> bool:
    if ip is None:
        ip = lambda u, v: float(np.dot(u, v))
    for i, u in enumerate(vecs):
        if abs(ip(u, u) - 1.0) > tol:
            return False
        for j, v in enumerate(vecs):
            if i != j and abs(ip(u, v)) > tol:
                return False
    return True


# ---------------------------------------------------------------------------
# Basic: Anton Example 58 — GS on R^3
# ---------------------------------------------------------------------------
print("=== Basic: Anton Example 58 — GS on R^3 ===")

basis_r3 = [
    np.array([1., 1., 1.]),
    np.array([0., 1., 1.]),
    np.array([0., 0., 1.]),
]

Q_vecs = gram_schmidt(basis_r3)
for i, v in enumerate(Q_vecs, 1):
    print(f"v{i} = {np.round(v, 6)}")

# Expected:
# v1 = (1/√3, 1/√3, 1/√3)    ≈ (0.577, 0.577, 0.577)
# v2 = (-2/√6, 1/√6, 1/√6)   ≈ (-0.816, 0.408, 0.408)
# v3 = (0, -1/√2, 1/√2)       ≈ (0, -0.707, 0.707)

Q = np.column_stack(Q_vecs)
print(f"Is orthonormal: {verify_orthonormal(Q_vecs)}")   # True
print(f"Q^T Q =\n{np.round(Q.T @ Q, 10)}")              # identity

# ---------------------------------------------------------------------------
# Intermediate: verify the key invariant — GS preserves span at each step
# ---------------------------------------------------------------------------
print("\n=== Intermediate: span preservation ===")

u1, u2, u3 = basis_r3
v1, v2, v3 = Q_vecs

# span{u1} == span{v1}: v1 is a scalar multiple of u1
c = np.dot(v1, u1) / np.dot(u1, u1)
print(f"v1 = {c:.6f} * u1: {np.allclose(v1, c * u1)}")   # True

# span{u1,u2} == span{v1,v2}: u2 lives in span{v1,v2}
u2_in_new = np.dot(u2, v1) * v1 + np.dot(u2, v2) * v2
print(f"u2 in span{{v1,v2}}: {np.allclose(u2, u2_in_new)}")  # True

# span{u1,u2,u3} == span{v1,v2,v3}: u3 lives in span{v1,v2,v3}
u3_in_new = np.dot(u3, v1)*v1 + np.dot(u3, v2)*v2 + np.dot(u3, v3)*v3
print(f"u3 in span{{v1,v2,v3}}: {np.allclose(u3, u3_in_new)}")  # True

# ---------------------------------------------------------------------------
# Advanced: GS in polynomial space P2 with ip = integral over [-1,1]
# ---------------------------------------------------------------------------
print("\n=== Advanced: GS on {1, x, x^2} in P2 ===")

ip_poly = lambda f, g: integrate.quad(lambda x: f(x) * g(x), -1, 1)[0]

p0 = lambda x: 1.0 + 0 * x    # constant 1
p1 = lambda x: x
p2 = lambda x: x**2

def gram_schmidt_fn(funcs, ip):
    """GS for functions: returns list of orthonormal functions."""
    ortho = []
    for f in funcs:
        coeffs_and_basis = list(zip([ip(f, q) for q in ortho], ortho))
        def residual(x, f=f, cab=coeffs_and_basis):
            return f(x) - sum(c * q(x) for c, q in cab)
        norm = np.sqrt(ip(residual, residual))
        q_new = (lambda r, n: (lambda x: r(x) / n))(residual, norm)
        ortho.append(q_new)
    return ortho

q0, q1, q2 = gram_schmidt_fn([p0, p1, p2], ip_poly)

print(f"<q0,q1> = {ip_poly(q0,q1):.8f}")   # 0.0 — orthogonal
print(f"<q0,q2> = {ip_poly(q0,q2):.8f}")   # 0.0 — orthogonal
print(f"<q1,q2> = {ip_poly(q1,q2):.8f}")   # 0.0 — orthogonal
print(f"||q0||  = {np.sqrt(ip_poly(q0,q0)):.6f}")  # 1.0
print(f"||q1||  = {np.sqrt(ip_poly(q1,q1)):.6f}")  # 1.0
print(f"||q2||  = {np.sqrt(ip_poly(q2,q2)):.6f}")  # 1.0
# These are the first three normalized Legendre polynomials


def exercises():
    """
    Exercise 1 (Basic):
        u1=(1,0,1), u2=(1,1,0) in R^3.
        Step 1: v1 = (1,0,1)/sqrt(2)
        Step 2: <u2,v1> = 1/sqrt(2)
                v_raw = (1,1,0) - (1/sqrt(2)) * (1/sqrt(2), 0, 1/sqrt(2))
                      = (1,1,0) - (1/2, 0, 1/2) = (1/2, 1, -1/2)
                norm  = sqrt(1/4 + 1 + 1/4) = sqrt(6)/2
                v2    = (1/sqrt(6), 2/sqrt(6), -1/sqrt(6))
        Result: 2D ONB spanning the plane through u1 and u2.

    Exercise 2 (Intermediate):
        q0: ||1||^2 = int_{-1}^1 1 dx = 2, so q0 = 1/sqrt(2)
        q1: <x, q0> = (1/sqrt(2)) * int_{-1}^1 x dx = 0 (odd integrand)
            raw = x, ||x||^2 = int x^2 dx = 2/3 → q1 = sqrt(3/2) * x
        q0 and q1 orthogonal: <q0,q1> = int 1/sqrt(2) * sqrt(3/2)*x dx = 0 ✓

    Exercise 3 (Advanced):
        Base case k=1: v1 = u1/||u1||, so span{v1} = span{u1} ✓
        Inductive step: assume span{v1,...,v_{k-1}} = span{u1,...,u_{k-1}}.
        Numerator of v_k = u_k - proj_{W_{k-1}} u_k ∈ span{u1,...,u_k}.
        Also u_k = v_k*norm + proj_{W_{k-1}} u_k ∈ span{v1,...,v_k}.
        So span{v1,...,v_k} = span{u1,...,u_k}. QED.
    """
    pass
