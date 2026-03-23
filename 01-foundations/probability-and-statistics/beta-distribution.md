**Related**: [[probability-distributions]], [[bernoulli-distribution]], [[binomial-distribution]], [[dirichlet-distribution]]
**Tags**: #status/growing

## Core Idea

The Beta distribution models **uncertainty about a probability**. While Bernoulli
models a binary outcome with a known $p$, Beta models what $p$ itself might be.
It lives on $[0, 1]$, making it natural for probabilities and proportions. Its
two parameters $\alpha$ and $\beta$ act as counts of observed successes and
failures, and it is the **conjugate prior** for the Bernoulli and Binomial
likelihoods — updating beliefs after observing data stays in closed form.

## Details

### Parameters

- $\alpha$ — shape parameter, interpreted as pseudo-successes (must be > 0)
- $\beta$ — shape parameter, interpreted as pseudo-failures (must be > 0)
- $x$ — the outcome: a probability value in $[0, 1]$

### PDF

$$f(x; \alpha, \beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}, \quad x \in [0,1]$$

where $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ is the
Beta function — a normalizing constant ensuring the PDF integrates to 1.

The shape $x^{\alpha-1}(1-x)^{\beta-1}$ mirrors the Binomial likelihood — this is
why conjugacy works.

### Expectation and Variance

$$E[X] = \frac{\alpha}{\alpha + \beta} \qquad \text{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$$

Mean = observed success rate. Variance shrinks as $\alpha + \beta$ grows —
more total observations, tighter estimate of $p$.

### Special Cases

```
alpha=1, beta=1   ->  Uniform(0,1)  — no prior knowledge
alpha = beta      ->  symmetric, peaks at 0.5
alpha >> beta     ->  peaks near 1 (strong evidence of success)
alpha << beta     ->  peaks near 0 (strong evidence of failure)
```

### Conjugate Prior for Bernoulli/Binomial

Start with prior $\text{Beta}(\alpha, \beta)$. Observe $h$ heads and $t$ tails:

$$\text{Prior: } \text{Beta}(\alpha, \beta) \quad \xrightarrow{\text{observe } h, t} \quad \text{Posterior: } \text{Beta}(\alpha + h,\; \beta + t)$$

Just add the counts. The posterior is still Beta — no integration required.
This closed-form update is the **conjugate prior** property.

### Bayesian A/B Testing

Two webpage versions observed over 200 visits each:

```
Version A: 40 conversions  ->  Beta(40, 160)
Version B: 50 conversions  ->  Beta(50, 150)
```

Sample from both distributions, compute P(B > A) by counting samples where
B's draw exceeds A's draw. No p-values, no normality assumption.

## Code Example

```python
import numpy as np

def beta_pdf(x: np.ndarray, alpha: float, beta: float) -> np.ndarray:
    """Beta PDF from scratch using log-space for numerical stability."""
    from math import lgamma
    log_norm = lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta)
    log_pdf = log_norm + (alpha - 1) * np.log(x) + (beta - 1) * np.log(1 - x)
    return np.exp(log_pdf)

# Prior: complete ignorance
x = np.linspace(0.01, 0.99, 1000)
uniform_prior = beta_pdf(x, alpha=1, beta=1)
print(f"Uniform prior (Beta(1,1)) is flat: {np.allclose(uniform_prior, 1.0)}")

# Update: observe 5 heads, 2 tails
alpha_prior, beta_prior = 1, 1
h, t = 5, 2
alpha_post = alpha_prior + h   # 6
beta_post  = beta_prior + t    # 3
print(f"Posterior mean: {alpha_post / (alpha_post + beta_post):.4f}")  # ~0.667

# Verify E[X] and Var(X)
samples = np.random.beta(alpha_post, beta_post, size=100000)
expected_mean = alpha_post / (alpha_post + beta_post)
expected_var  = (alpha_post * beta_post) / ((alpha_post + beta_post)**2 * (alpha_post + beta_post + 1))
print(f"E[X]   = {samples.mean():.4f}  (expected {expected_mean:.4f})")
print(f"Var(X) = {samples.var():.6f}  (expected {expected_var:.6f})")

# Bayesian A/B test
def ab_test(conversions_a, visits_a, conversions_b, visits_b, n_samples=100000):
    """P(B is better than A) via Beta posterior sampling."""
    alpha_a = 1 + conversions_a
    beta_a  = 1 + (visits_a - conversions_a)
    alpha_b = 1 + conversions_b
    beta_b  = 1 + (visits_b - conversions_b)

    samples_a = np.random.beta(alpha_a, beta_a, n_samples)
    samples_b = np.random.beta(alpha_b, beta_b, n_samples)
    prob_b_wins = np.mean(samples_b > samples_a)
    print(f"P(B better than A) = {prob_b_wins:.4f}")
    return prob_b_wins

ab_test(conversions_a=40, visits_a=200, conversions_b=50, visits_b=200)
```

> For runnable implementation with exercises, see: [[code/foundations/beta_distribution.py]]

## Connections

- [[bernoulli-distribution]] — Beta is the conjugate prior for Bernoulli
- [[binomial-distribution]] — Beta is the conjugate prior for Binomial
- [[dirichlet-distribution]] — Dirichlet generalizes Beta to k categories
- [[probability-distributions]] — overview of all distributions
- Forward link: Bayesian inference — Beta-Binomial conjugacy is the simplest example
- Forward link: Thompson sampling — Beta posteriors used in bandit algorithms

## Sources

- [Mathematics for Machine Learning — Chapter 6.6](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Bayesian Methods for Hackers — Chapter 1](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)
- [Count Bayesie — Beta distribution](https://www.countbayesie.com/blog/2015/4/25/bayesian-ab-testing)
