"""
Probability Distributions - Sampling, Diagnostics, and MLE -> Loss Connection

Demonstrates:
- Sampling from key distributions using only NumPy
- Distribution diagnostics (mean/variance checks, overdispersion)
- The MLE derivation: how distributional assumptions produce loss functions
- Inverse transform sampling from scratch
"""

import numpy as np


# ──────────────────────────────────────────────
# SAMPLING
# ──────────────────────────────────────────────

def sample_bernoulli(p: float, n: int) -> np.ndarray:
    """Sample n Bernoulli(p) outcomes using Uniform threshold."""
    return (np.random.uniform(0, 1, n) < p).astype(int)


def sample_exponential(lam: float, n: int) -> np.ndarray:
    """Sample Exponential(lambda) via inverse transform: F_inv(u) = -ln(1-u)/lambda."""
    u = np.random.uniform(0, 1, n)
    return -np.log(1 - u) / lam


def sample_normal_box_muller(mu: float, sigma: float, n: int) -> np.ndarray:
    """Sample Normal(mu, sigma^2) using Box-Muller transform (no np.random.normal)."""
    u1 = np.random.uniform(0, 1, n)
    u2 = np.random.uniform(0, 1, n)
    z = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    return mu + sigma * z


# ──────────────────────────────────────────────
# DIAGNOSTICS
# ──────────────────────────────────────────────

def overdispersion_check(data: np.ndarray) -> dict:
    """
    Check if count data follows Poisson (mean ~= variance).
    Dispersion ratio ~1 -> Poisson, >>1 -> overdispersed (use Negative Binomial).
    """
    mean = data.mean()
    var = data.var()
    ratio = var / mean
    if 0.8 < ratio < 1.2:
        verdict = "Poisson-like"
    elif ratio > 1.2:
        verdict = "overdispersed (Negative Binomial)"
    else:
        verdict = "underdispersed (Binomial)"
    return {"mean": float(mean), "variance": float(var), "dispersion_ratio": float(ratio), "verdict": verdict}


def memoryless_check(lam: float, t: float, s: float, n: int = 100_000) -> dict:
    """
    Verify P(X > t+s | X > t) == P(X > s) for Exponential.
    Memoryless: past waiting time does not affect future probability.
    """
    samples = sample_exponential(lam, n)
    p_greater_s = float(np.mean(samples > s))
    p_given_past = float(np.mean(samples[samples > t] > (t + s)))
    return {
        "P(X > s)": round(p_greater_s, 4),
        "P(X > t+s | X > t)": round(p_given_past, 4),
        "memoryless": abs(p_greater_s - p_given_past) < 0.01,
    }


# ──────────────────────────────────────────────
# MLE -> LOSS FUNCTION DERIVATION
# ──────────────────────────────────────────────

def mse_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    MSE = MLE under Gaussian noise assumption.
    Maximizing log-likelihood of N(y | f(x), sigma^2) = minimizing sum of squared errors.
    """
    return float(np.mean((y_true - y_pred) ** 2))


def binary_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    BCE = negative log-likelihood of Bernoulli distribution.
    For each sample: -[y*log(p) + (1-y)*log(1-p)]
    y_pred must be in (0, 1) -- clipped for numerical stability.
    """
    p = np.clip(y_pred, 1e-10, 1 - 1e-10)
    return float(-np.mean(y_true * np.log(p) + (1 - y_true) * np.log(1 - p)))


def categorical_cross_entropy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    CCE = negative log-likelihood of Categorical/Multinomial distribution.
    y_true: one-hot encoded (n_samples, n_classes)
    y_pred: softmax probabilities (n_samples, n_classes)
    """
    p = np.clip(y_pred, 1e-10, 1.0)
    return float(-np.mean(np.sum(y_true * np.log(p), axis=1)))


def demonstrate_mle_connection():
    """Show that MSE and BCE are both MLE -- just under different distributions."""
    np.random.seed(42)
    n = 1000

    # Gaussian case: true signal + Gaussian noise -> MSE is the optimal loss
    x = np.linspace(0, 1, n)
    y_true = 2 * x + 1 + np.random.normal(0, 0.3, n)
    y_pred = 2 * x + 1
    print(f"MSE (Gaussian noise, perfect model): {mse_loss(y_true, y_pred):.4f}")
    print(f"  Expected ~= sigma^2 = 0.09")

    # Bernoulli case: true probabilities -> BCE is the correct loss
    p_true = np.array([0.8, 0.3, 0.6, 0.1, 0.9])
    y_obs = (np.random.uniform(0, 1, 5) < p_true).astype(float)
    p_pred = p_true
    print(f"\nBCE (Bernoulli, perfect model): {binary_cross_entropy(y_obs, p_pred):.4f}")
    print(f"  Lower = better; perfect model minimizes expected BCE")

    print("\n--- MLE -> Loss connection ---")
    print("Gaussian likelihood    ->  minimize MSE")
    print("Bernoulli likelihood   ->  minimize Binary Cross-Entropy")
    print("Categorical likelihood ->  minimize Categorical Cross-Entropy")
    print("Loss functions are NOT arbitrary -- they ARE negative log-likelihoods.")


# ──────────────────────────────────────────────
# EXERCISES
# ──────────────────────────────────────────────

def exercises():
    """
    Progressive exercises on probability distributions.

    BASIC
    -----
    1. Sample 10,000 values from Exponential(lambda=0.5) using inverse transform sampling
       (no np.random.exponential). Verify mean ~= 2.0 and variance ~= 4.0.

    2. Use overdispersion_check() on these two datasets:
         a = np.random.poisson(5, 1000)
         b = np.random.negative_binomial(2, 0.3, 1000)
       What does the dispersion ratio tell you about which model to use?

    INTERMEDIATE
    ------------
    3. Implement mle_fit_gaussian(data) that returns MLE estimates of mu and sigma
       from scratch (numpy only). Hint: MLE gives mu=mean, sigma=std.
       Verify on np.random.normal(3, 2, 10000).

    4. Given binary labels y = [1, 1, 0, 1, 0] and predictions p = [0.9, 0.8, 0.2, 0.7, 0.3],
       compute BCE by hand. Then verify with binary_cross_entropy().

    5. Implement beta_posterior(alpha_prior, beta_prior, successes, failures).
       Run A/B test:
         A: 30 conversions, 120 visits
         B: 40 conversions, 120 visits
       Compute P(B > A) by sampling 100,000 draws from each posterior.

    ADVANCED
    --------
    6. Prove the MLE -> MSE derivation in code:
       - Generate y = 3x + Gaussian noise (sigma=1)
       - Write log-likelihood function L(mu, sigma | data) for Gaussian
       - Show that maximizing L is equivalent to minimizing sum of squared residuals
       - Verify: parameters that minimize MSE also maximize log-likelihood

    7. Implement a Dirichlet-Multinomial conjugate update from scratch:
       - Start with uniform prior Dirichlet([1,1,1])
       - Observe word counts: [cat: 15, dog: 5, fish: 30]
       - Compute posterior, sample 10,000 probability vectors
       - Show posterior mean matches observed frequencies
    """
    print("See docstring for exercises. Run each one manually.")


if __name__ == "__main__":
    np.random.seed(42)

    print("=== Sampling Verification ===")
    exp_samples = sample_exponential(lam=2.0, n=100_000)
    print(f"Exponential(2): mean={exp_samples.mean():.3f} (expected 0.5), var={exp_samples.var():.3f} (expected 0.25)")

    norm_samples = sample_normal_box_muller(mu=5, sigma=2, n=100_000)
    print(f"Normal(5,4):    mean={norm_samples.mean():.3f}, var={norm_samples.var():.3f}")

    print("\n=== Overdispersion Check ===")
    poisson_data = np.random.poisson(5, 1000)
    print(f"Poisson data:   {overdispersion_check(poisson_data)}")

    print("\n=== Memoryless Property ===")
    print(memoryless_check(lam=1.0, t=2.0, s=1.0))

    print("\n=== MLE -> Loss Connection ===")
    demonstrate_mle_connection()
