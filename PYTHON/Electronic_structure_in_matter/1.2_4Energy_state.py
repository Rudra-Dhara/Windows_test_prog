import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1
N = 5000
dx = L / N
x = np.linspace(0, L, N)

# Potential energy (inside the box, V = 0)
V = np.zeros(N)

def schrodinger_psi(psi, x, E):
    phi = psi[1]
    dphi_dx = -2 * (E - V[int(x)]) * psi[0]
    return np.array([phi, dphi_dx])

# Energy search range
E_min = 1
E_max = 100
num_energies = 1000
energies = np.linspace(E_min, E_max, num_energies)

# Find eigenvalues, eigenfunctions, node counts, and minimum error energies
eigenvalues = []
eigenfunctions = []
node_counts = []
min_error_energies = []

for E in energies:
    psi_initial = np.array([0.0, 1.0])  # Initial conditions: psi(0) = 0, psi'(0) = 1
    psi_solution = np.zeros((N, 2))
    psi_solution[0] = psi_initial
    for i in range(1, N):
        psi_solution[i] = psi_solution[i - 1] + dx * schrodinger_psi(psi_solution[i - 1], x[i - 1], E)
    
    # Count nodes by finding sign changes in wavefunction
    nodes = np.where(np.diff(np.sign(psi_solution[:, 0])))[0]
    node_count = len(nodes)
    
    if node_count not in node_counts:
        node_counts.append(node_count)
        min_error_energies.append(E)
        eigenfunctions.append(psi_solution[:, 0])
    
    # If the node count already exists, check if the current energy has a lower error
    else:
        index = node_counts.index(node_count)
        psi_error = np.sum(np.square(psi_solution[:, 0] - eigenfunctions[index]))
        min_error = np.sum(np.square(psi_solution[:, 0] - eigenfunctions[index]))
        if psi_error < min_error:
            min_error_energies[index] = E
            eigenfunctions[index] = psi_solution[:, 0]

#defining true function
def psi_true(n,x):
    return np.sqrt(2)*np.sin(n*np.pi*x)

# Plot the eigenfunctions with minimum error energies
plt.figure(figsize=(10, 6))
for i, energy in enumerate(min_error_energies):
    if node_counts[i] == 1:
        continue
    norm2 = np.sum((np.array(eigenfunctions[i])**2))*dx  #integrating the factor
    norm = np.sqrt(norm2)
    plt.plot(x, np.array(eigenfunctions[i])/norm, label=f'E = {energy:.2f}, Nodes = {node_counts[i]-2}')
    plt.plot(x,psi_true(i-1,x), ls = ":",label=f'True wf {i-1} state')
    print(node_counts[i]-1,'th energy',energy,"where the original value is",(node_counts[i]-1)**2*np.pi**2/2)

plt.xlabel('Position')
plt.ylabel('Wavefunction')
plt.title('Wavefunctions for Particle in a 1D Box with Minimum Error Energies')
plt.legend()
plt.show()
