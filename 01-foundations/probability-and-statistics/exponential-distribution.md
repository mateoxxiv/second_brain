**Related**: [[probability-distributions]], [[poisson-distribution]], [[probability-fundamentals]]
**Tags**: #status/growing

## Core Idea

The Exponential distribution models the **time between events** in a Poisson
process. If events arrive at rate $\lambda$ (Poisson), the waiting time until
the next event is Exponential($\lambda$). Its defining property is the
**memoryless property**: how long you've already waited gives no information
about how much longer you'll wait. This makes it the foundation of queuing theory.

## Details

### Parameters

- $\lambda$ — rate of events (same $\lambda$ as the corresponding Poisson process)
- $x$ — waiting time (continuous, $x \geq 0$)

### Building the PDF

If events arrive at rate $\lambda$, the probability of **no event by time $t$**
(survival function) decays exponentially:

$$P(X > t) = e^{-\lambda t}$$

The PDF is the negative derivative of the survival function:

$$\boxed{f(x) = \lambda e^{-\lambda x}, \quad x \geq 0}$$

Verify: $\int_0^{\infty} \lambda e^{-\lambda x}\,dx = 1$ ✓

### Expectation and Variance

$$E[X] = \frac{1}{\lambda} \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$

Higher rate → shorter average wait. If $\lambda = 3$ events/hour, average wait = 20 minutes.

### The Memoryless Property

$$P(X > s + t \mid X > s) = P(X > t)$$

Having already waited $s$ units gives zero information about future waiting time.
Among continuous distributions, **only the Exponential is memoryless**.

This is why queuing systems built on Exponential inter-arrival times have clean
closed-form solutions — the math doesn't need to track history.

### Poisson–Exponential Duality

| Question | Distribution | Parameter |
|---|---|---|
| How many events in interval $[0, t]$? | Poisson($\lambda t$) | rate $\lambda$ |
| How long until the next event? | Exponential($\lambda$) | same $\lambda$ |

Same process, two views: count vs. time.

### ML and Systems Connections

| Use case | How Exponential appears |
|---|---|
| Queuing (M/M/1) | Inter-arrival and service times ~ Exponential |
| Reliability | Time to component failure (constant hazard rate) |
| Survival analysis | Simplest model for time-to-event data |
| Simulations | Generating synthetic event streams |

## Code Example

```python
import numpy as np

def exponential_pdf(x: np.ndarray, lam: float) -> np.ndarray:
    """Exponential PDF from scratch.
    x: waiting times (must be >= 0)
    lam: rate parameter (events per unit time)
    """
    return lam * np.exp(-lam * x)

def exponential_survival(t: float, lam: float) -> float:
    """P(X > t) — probability of waiting longer than t."""
    return np.exp(-lam * t)

lam = 3.0  # 3 events per hour
x = np.linspace(0, 3, 1000)

# Verify: integrates to 1
dx = x[1] - x[0]
area = np.sum(exponential_pdf(x, lam)) * dx
print(f"Area under PDF: {area:.6f}")  # ~1.0

# E[X] and Var(X)
samples = np.random.exponential(scale=1/lam, size=100000)
print(f"E[X]   = {samples.mean():.4f}  (expected {1/lam:.4f})")
print(f"Var(X) = {samples.var():.4f}  (expected {1/lam**2:.4f})")

# Memoryless property verification
# P(X > 0.5 + 0.3 | X > 0.5) should equal P(X > 0.3)
p_gt_03 = exponential_survival(0.3, lam)
p_gt_08 = exponential_survival(0.8, lam)
p_gt_05 = exponential_survival(0.5, lam)
conditional = p_gt_08 / p_gt_05
print(f"P(X > 0.3)             = {p_gt_03:.6f}")
print(f"P(X > 0.8 | X > 0.5)  = {conditional:.6f}")
print(f"Equal (memoryless): {abs(p_gt_03 - conditional) < 1e-9}")  # True

# Queuing simulation: M/M/1 queue
def simulate_queue(lam_arrive: float, lam_serve: float, n_customers: int):
    """Simulate M/M/1 queue with Exponential inter-arrivals and service times."""
    inter_arrivals = np.random.exponential(1/lam_arrive, n_customers)
    service_times  = np.random.exponential(1/lam_serve,  n_customers)
    arrival_times  = np.cumsum(inter_arrivals)

    wait_times = np.zeros(n_customers)
    finish_time = 0.0
    for i in range(n_customers):
        start = max(arrival_times[i], finish_time)
        wait_times[i] = start - arrival_times[i]
        finish_time = start + service_times[i]

    return wait_times

waits = simulate_queue(lam_arrive=2, lam_serve=3, n_customers=10000)
print(f"Average wait in queue: {waits.mean():.4f} time units")
```

> For runnable implementation with exercises, see: [[code/foundations/exponential_distribution.py]]

## Connections

- [[poisson-distribution]] — Poisson counts events; Exponential times them
- [[probability-distributions]] — overview of all distributions
- Forward link: survival analysis — Exponential is the baseline hazard model
- Forward link: queuing theory — M/M/1 queue built on Exponential assumptions
- Forward link: Gamma distribution — sum of k Exponentials follows Gamma

## Sources

- [Mathematics for Machine Learning — Chapter 6.2](https://mml-book.github.io/book/mml-book.pdf)
- [Statistics for Machine Learning — Pratap Dangeti](https://www.packtpub.com/) — Chapter 2
- [Wikipedia — Exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution)
- [Brilliant — Queuing Theory](https://brilliant.org/wiki/queuing-theory/)
