**Related**: [[probability-distributions]], [[probability-fundamentals]], [[gradient-descent]], [[optimization]]
**Tags**: #status/growing

## Core Idea

The Normal (Gaussian) distribution is the most important distribution in statistics
and ML. It emerges naturally via the **Central Limit Theorem**: the sum of many
independent random variables converges to Normal, regardless of their individual
shapes. This is why noise, measurement error, and natural variation are all
approximately Gaussian. Its two parameters fully describe it: $\mu$ (center) and
$\sigma^2$ (spread).

## Details

### Building the Formula

We want a symmetric, bell-shaped function that decays away from a center $\mu$
and integrates to 1. The natural starting point is $e^{-x^2}$ — positive, symmetric,
decays fast. Adding parameters for center and spread:

$$e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

The Gaussian integral gives $\int_{-\infty}^{\infty} e^{-x^2/2}\,dx = \sqrt{2\pi}$,
so the normalizing constant is $\frac{1}{\sigma\sqrt{2\pi}}$:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Written $X \sim \mathcal{N}(\mu, \sigma^2)$.

### Expectation and Variance

$$E[X] = \mu \qquad \text{Var}(X) = \sigma^2$$

$E[X] = \mu$ follows from symmetry — the distribution is symmetric around $\mu$,
so the weighted average must be $\mu$.

$\text{Var}(X) = \sigma^2$ is by construction — the parameter $\sigma^2$ was chosen
precisely so the variance integral equals $\sigma^2$.

### Standard Normal and Standardization

$Z \sim \mathcal{N}(0, 1)$ — zero mean, unit variance. Any Normal converts via:

$$Z = \frac{X - \mu}{\sigma}$$

Used everywhere: feature scaling, batch normalization, z-scores.

### 68-95-99.7 Rule

Area under the bell curve within $k$ standard deviations of the mean:

```
mu +- 1*sigma  ->  68.27%  of data
mu +- 2*sigma  ->  95.45%  of data
mu +- 3*sigma  ->  99.73%  of data
```

A data point beyond $3\sigma$ is unusual (0.3% chance). Basis of outlier detection.

### Central Limit Theorem

Let $X_1, \ldots, X_n$ be i.i.d. with mean $\mu$ and variance $\sigma^2$. Then:

$$\bar{X}_n \xrightarrow{d} \mathcal{N}\!\left(\mu,\, \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty$$

The variance shrinks as $1/n$ — more samples, tighter estimate. This justifies
using Normal approximations almost everywhere in statistics.

### Why MSE Assumes Gaussian Noise

Assume regression noise is Gaussian: $y = \mathbf{w}^T\mathbf{x} + \epsilon$,
$\epsilon \sim \mathcal{N}(0, \sigma^2)$. The log-likelihood over $n$ points:

$$\log P(\mathbf{y} | \mathbf{X}, \mathbf{w}) = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - \mathbf{w}^T\mathbf{x}_i)^2$$

Maximizing over $\mathbf{w}$ is equivalent to minimizing $\sum(y_i - \hat{y}_i)^2$ — **MSE**.
MSE is the MLE estimator under Gaussian noise. Wrong noise assumption → wrong loss.

### ML Connections Summary

| Use case | How Normal appears |
|---|---|
| Weight initialization | $w \sim \mathcal{N}(0, \sigma^2)$ — Xavier/He init |
| MSE loss | MLE under Gaussian noise assumption |
| Batch normalization | Forces activations toward $\mathcal{N}(0,1)$ |
| VAEs | Encoder outputs $\mu$ and $\sigma$ of a Normal |
| Diffusion models | Forward process adds Gaussian noise step by step |

## Code Example

```python
import numpy as np

def normal_pdf(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    """Normal probability density function from scratch."""
    coeff = 1.0 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coeff * np.exp(exponent)

# Verify: integrates to 1
x = np.linspace(-10, 10, 10000)
dx = x[1] - x[0]
area = np.sum(normal_pdf(x, mu=0, sigma=1)) * dx
print(f"Area under curve: {area:.6f}")  # ~1.0

# 68-95-99.7 rule verification
samples = np.random.normal(0, 1, 100000)
for k in [1, 2, 3]:
    within = np.mean(np.abs(samples) <= k)
    print(f"Within {k} sigma: {within:.4f}")

# Standardization
data = np.array([170, 175, 160, 180, 165, 172])
z_scores = (data - data.mean()) / data.std()
print(f"Z-scores: {z_scores.round(2)}")

# CLT demonstration
original = np.random.exponential(scale=2, size=(10000, 50))
sample_means = original.mean(axis=1)
print(f"CLT: mean={sample_means.mean():.3f}, std={sample_means.std():.3f}")
```

> For runnable implementation with exercises, see: [[code/foundations/normal_distribution.py]]

## Connections

- [[probability-distributions]] — overview of all distributions
- [[probability-fundamentals]] — probability rules this is built on
- [[optimization]] — MSE minimization is MLE under Gaussian noise
- [[gradient-descent]] — training under MSE assumes Gaussian noise
- Forward link: MLE — deriving MSE from log-likelihood
- Forward link: linear regression — uses Normal noise assumption
- Forward link: batch normalization — forces activations toward N(0,1)
- Forward link: VAEs — latent space is Gaussian

## Sources

- [3Blue1Brown — But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo)
- [Mathematics for Machine Learning — Chapter 6.5](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Khan Academy — Normal distributions](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data)
