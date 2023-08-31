import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0
N = 1000
dx = L / N
x = np.linspace(0, L, N)

# Potential energy (inside the box, V = 0)
V = np.zeros(N)

def schrodinger_psi(psi, x, E):
    phi = psi[1]
    dphi_dx = -2 * (E - V[int(x)]) * psi[0]
    return np.array([phi, dphi_dx])

# Energy search range
E_min = 0.1
E_max = 20.0
num_energies = 10
energies = np.linspace(E_min, E_max, num_energies)

# Find eigenvalues and eigenfunctions using shooting method
eigenvalues = []
eigenfunctions = []

for E in energies:
    psi_initial = np.array([0.0, 1.0])  # Initial conditions: psi(0) = 0, psi'(0) = 1
    psi_solution = np.zeros((N, 2))
    psi_solution[0] = psi_initial
    for i in range(1, N):
        psi_solution[i] = psi_solution[i - 1] + dx * schrodinger_psi(psi_solution[i - 1], x[i - 1], E)
    eigenvalues.append(E)
    eigenfunctions.append(psi_solution[:, 0])

# Plot the eigenfunctions
plt.figure(figsize=(10, 6))
for i in range(num_energies):
    plt.plot(x, eigenfunctions[i], label=f'E = {eigenvalues[i]:.2f}')
plt.xlabel('Position')
plt.ylabel('Wavefunction')
plt.title('Wavefunctions for Particle in a 1D Box')
plt.legend()
plt.show()
