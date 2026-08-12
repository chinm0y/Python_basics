import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import legval


# 1. Define the x-axis grid over the interval [-1, 1]
x = np.linspace(-1, 1, 1000)

# 2. Configure the plot layout
plt.figure(figsize=(8, 5))

# 3. Compute and plot polynomials for orders n = 0 through 4
for n in range(7):
    # Create a coefficient array where only index 'n' is 1 (all lower orders are 0)
    coeffs = [2] * n + [1]
    
    # Evaluate the Legendre polynomial using NumPy
    y = legval(x, coeffs)
    
    plt.plot(x, y, label=f'$P_{n}(x)$', linewidth=2)


plt.title("Legendre Polynomials (Using NumPy legval) by chinmoy", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("$P_n(x)$", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc="lower right")
plt.show()
