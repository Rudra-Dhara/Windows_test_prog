import numpy as np
import matplotlib.pyplot as plt

# Define constants
L = 1
x = np.linspace(0, L, 1000)

# Choose n values
n_values = [2, 10, 200]

# Plotting wave functions
plt.figure(figsize=(8, 4))
for n in n_values:
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    plt.plot(x, psi_n, label=f'n = {n}')
plt.title('Wavefunctions')
plt.xlabel('Position (x)')
plt.ylabel('Wavefunction Amplitude')
plt.legend()
plt.grid()
plt.show()

# Plotting probability densities
plt.figure(figsize=(8, 4))
for n in n_values:
    psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    prob_density = np.abs(psi_n)**2
    plt.plot(x, prob_density, label=f'n = {n}')
plt.title('Probability Densities')
plt.xlabel('Position (x)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()
plt.show()
