"""
Exponent, logarithm, and root properties.
All rules derived from: exponentiation is repeated multiplication.
See also: algebraic_operation_properties.py
"""

import numpy as np


a, b, m, n = 4.0, 9.0, 3.0, 2.0

print("=== Basic: exponent rules ===")
print(f"Product rule:       a^m · a^n = a^(m+n)?  {np.isclose(a**m * a**n, a**(m+n))}")
print(f"Quotient rule:      a^m / a^n = a^(m-n)?  {np.isclose(a**m / a**n, a**(m-n))}")
print(f"Power of power:     (a^m)^n   = a^(mn)?   {np.isclose((a**m)**n, a**(m*n))}")
print(f"Power of product:   (ab)^n    = a^n·b^n?  {np.isclose((a*b)**n, a**n * b**n)}")
print(f"Zero exponent:      a^0       = 1?         {np.isclose(a**0, 1)}")
print(f"Negative exponent:  a^(-n)    = 1/a^n?    {np.isclose(a**(-n), 1/a**n)}")
print(f"Fractional exp:     a^(1/2)   = sqrt(a)?  {np.isclose(a**0.5, np.sqrt(a))}")

print("\n=== Basic: logarithm rules ===")
print(f"Log product:    log(ab)  = log(a)+log(b)?  {np.isclose(np.log(a*b), np.log(a)+np.log(b))}")
print(f"Log quotient:   log(a/b) = log(a)-log(b)?  {np.isclose(np.log(a/b), np.log(a)-np.log(b))}")
print(f"Log power:      log(a^n) = n·log(a)?       {np.isclose(np.log(a**n), n*np.log(a))}")
print(f"Log identity:   log_a(a) = 1?              {np.isclose(np.log(a)/np.log(a), 1)}")
print(f"Log zero:       log_a(1) = 0?              {np.isclose(np.log(1), 0)}")
print(f"Change of base: log_9(4) via ln?           {np.isclose(np.log(a)/np.log(b), np.log(a)/np.log(b))}")

print("\n=== Basic: root rules ===")
print(f"Root product:   sqrt(ab)   = sqrt(a)·sqrt(b)?  {np.isclose(np.sqrt(a*b), np.sqrt(a)*np.sqrt(b))}")
print(f"Root quotient:  sqrt(a/b)  = sqrt(a)/sqrt(b)?  {np.isclose(np.sqrt(a/b), np.sqrt(a)/np.sqrt(b))}")
print(f"Root of power:  a^(m/n)?                       {np.isclose(a**(m/n), (a**m)**(1/n))}")


# ---------------------------------------------------------------------------
# Intermediate: log-sum-exp trick for numerical stability
# ---------------------------------------------------------------------------
def log_sum_exp_naive(x):
    return np.log(np.sum(np.exp(x)))

def log_sum_exp_stable(x):
    c = np.max(x)
    return c + np.log(np.sum(np.exp(x - c)))

x_small = np.array([1.0, 2.0, 3.0])
x_large = np.array([1000.0, 1001.0, 1002.0])

print("\n=== Intermediate: log-sum-exp stability ===")
print(f"Small values — naive:  {log_sum_exp_naive(x_small):.6f}")
print(f"Small values — stable: {log_sum_exp_stable(x_small):.6f}")
print(f"Large values — naive:  {log_sum_exp_naive(x_large)}")    # inf (overflow)
print(f"Large values — stable: {log_sum_exp_stable(x_large):.6f}")  # 1002 + log(e^0+e^-1+e^-2)


# ---------------------------------------------------------------------------
# Advanced: change of base derivation verified numerically
# ---------------------------------------------------------------------------
print("\n=== Advanced: change of base ===")
# log_b(x) = ln(x) / ln(b)
x_val = 16.0
base  = 2.0
log_b_x = np.log(x_val) / np.log(base)   # change of base
direct  = np.log2(x_val)                  # numpy built-in
print(f"log_2(16) via change-of-base: {log_b_x}")  # 4.0
print(f"log_2(16) direct:             {direct}")    # 4.0
print(f"Match? {np.isclose(log_b_x, direct)}")


def exercises():
    """
    Exercise 1 (Basic):
        Simplify by hand: (a) 2^3 · 2^4, (b) (3^2)^3, (c) log2(32), (d) log(1000)-log(10)
        Expected: (a) 2^7=128, (b) 3^6=729, (c) 5, (d) log(100)=2

    Exercise 2 (Intermediate):
        Implement log_sum_exp_stable for a batch of vectors (2D array, row-wise).
        Expected: shape (n_rows,) where each entry is log(sum(exp(row))).

    Exercise 3 (Advanced):
        Derive change of base from scratch.
        Let y = log_b(x). Then b^y = x.
        Apply ln: ln(b^y) = ln(x) → y·ln(b) = ln(x) → y = ln(x)/ln(b). ✓
        Implement: given any base b and value x, compute log_b(x) using only np.log.
        Verify for b=10, x=1000: expected 3.0.
    """
    pass
