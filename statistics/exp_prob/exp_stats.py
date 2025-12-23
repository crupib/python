import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# ---- hard reset matplotlib state (important in PyCharm) ----
plt.close("all")

# ================== Normal distribution section ==================
mean = 0
std_dev = 1

samples = np.random.normal(mean, std_dev, 10000)

within_1_std = np.sum(np.abs(samples - mean) < std_dev)
within_2_std = np.sum(np.abs(samples - mean) < 2 * std_dev)
within_3_std = np.sum(np.abs(samples - mean) < 3 * std_dev)

N = len(samples)
print(f"Percent within 1 standard deviation: {within_1_std / N * 100:.2f}%")
print(f"Percent within 2 standard deviation: {within_2_std / N * 100:.2f}%")
print(f"Percent within 3 standard deviation: {within_3_std / N * 100:.2f}%")

# ================== Binomial PMF section ==================
print("***** Binomial Section *****************")

n = 20
k = np.arange(0, n + 1)
p_values = [0.20, 0.50, 0.75, 0.90]

# ---- 4 graphs: manual PMF (math.comb) ----
for p in p_values:
    pmf_manual = np.array([
        math.comb(n, j) * (p ** j) * ((1 - p) ** (n - j))
        for j in k
    ])

    plt.figure()
    markerline, stemlines, baseline = plt.stem(k, pmf_manual)
    baseline.set_visible(False)
    plt.title(f"Manual Binomial PMF (n={n}, p={p})")
    plt.xlabel("k")
    plt.ylabel("P(X=k)")
    plt.ylim(0.0, 1.0)
    plt.grid(True)

# ---- 4 graphs: SciPy PMF (binom.pmf) ----
for p in p_values:
    pmf_scipy = binom.pmf(k, n, p)

    plt.figure()
    markerline, stemlines, baseline = plt.stem(k, pmf_scipy)
    baseline.set_visible(False)
    plt.title(f"SciPy Binomial PMF (n={n}, p={p})")
    plt.xlabel("k")
    plt.ylabel("P(X=k)")
    plt.ylim(0.0, 1.0)
    plt.grid(True)

# ================== Discrete Uniform Distribution ==================
print("***** Discrete Uniform Distribution *****************")

a, b = 1, 6
x = np.arange(a, b + 1)
prob = np.ones_like(x, dtype=float) / (b - a + 1)

plt.figure()
plt.bar(x, prob, width=0.6)
plt.title("Discrete Uniform Distribution (a=1, b=6)")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.xticks(x)
plt.ylim(0.0, 1.0)
plt.grid(axis="y")

# ================== Show and cleanup ==================
plt.show()
plt.close("all")
