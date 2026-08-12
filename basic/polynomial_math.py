import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

# 1. Define the x-axis grid over the interval [-1, 1]
x = np.linspace(-1, 1, 1000)

# 2. Configure the plot layout
plt.figure(figsize=(8, 5))

# 3. Compute and plot polynomials for orders n = 0 through 4
for n in range(5):
    y = eval_legendre(n, x)
    plt.plot(x, y, label=f'$P_{n}(x)$', linewidth=2)

# 4. Add mathematical notation and chart styling
plt.title("Legendre Polynomials ($P_n(x)$)", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("$P_n(x)$", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # X-axis baseline
plt.axvline(0, color='black', linewidth=0.5, linestyle='--') # Y-axis baseline
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc="lower right")

# 5. Display the result
plt.show()
