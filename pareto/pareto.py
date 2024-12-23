import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ["PYTHONWARNINGS"] = "ignore"
os.environ["TK_SILENCE_DEPRECATION"] = "1"

matplotlib.use('TkAgg')
alpha = 0.7

# Create a figure and subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 12))  # 3 rows, 1 column of subplots

# Plot 0-100 Pareto distribution
x = np.arange(1, 100)  # Start from 1 to avoid division by zero
y = alpha * x / x**(alpha + 1)
axs[0].plot(x, y)
axs[0].grid()
axs[0].set_title("0-100 Pareto distribution")

# Plot 0-20 Pareto distribution
x = np.arange(1, 20)  # Start from 1 to avoid division by zero
y = alpha * x / x**(alpha + 1)
axs[1].plot(x, y)
axs[1].grid()
axs[1].set_title("0-20 Pareto distribution")

# Plot 20-100 Pareto distribution
x = np.arange(20, 100)  # Start from 1 to avoid division by zero
y = alpha * x / x**(alpha + 1)
axs[2].plot(x, y)
axs[2].grid()
axs[2].set_title("20-100 Pareto distribution")

# Adjust layout
plt.tight_layout()

# Show all plots in one figure
plt.show()
