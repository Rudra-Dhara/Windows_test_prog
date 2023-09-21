import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

# Parameters
num_points = 200  # Number of grid points for angular coordinate
theta_max = 2 * np.pi  # Maximum angular coordinate (360 degrees)
moment_of_inertia = 1.0  # Adjust as needed
hbar = 1.0  # Reduced Planck's constant (you can adjust as needed)

# Discretize angular coordinate
theta = np.linspace(0, theta_max, num_points)
dtheta = theta[1] - theta[0]  # Angular step size

# Construct the Hamiltonian matrix
# H = -hbar^2 / (2 * I) * d^2/dtheta^2
H = (-hbar**2 / (2 * moment_of_inertia)) * (np.diag(-2 * np.ones(num_points)) +
                                             np.diag(np.ones(num_points - 1), 1) +
                                             np.diag(np.ones(num_points - 1), -1)) / (dtheta**2)

# Solve the eigenvalue problem for Hamiltonian
eigenvalues, eigenvectors = eigh(H)


# Plot the first few eigenvectors (wave functions)
plt.figure()
for i in range(5):
    plt.plot(theta, eigenvectors[:, i], label=f'wave function E{i}')
    plt.plot(theta, eigenvectors[:, i]**2, label=f'Probability density E{i}')
    print(f'level {i} energy is ',eigenvalues[i])
plt.title('Real part of the wave function and probability density')
plt.xlabel('Angular coordinate (theta)')
plt.ylabel('Wavefunction amplitude/PDF')
plt.legend()
plt.show()

