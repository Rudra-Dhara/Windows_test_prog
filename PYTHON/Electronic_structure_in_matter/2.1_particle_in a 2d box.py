import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Parameters
L = 1
N = 100
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
E_max = 25
num_energies = 100
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

# Plot the eigenfunctions with minimum error energies
plt.figure(figsize=(10, 6))
eigen_fun_x=[]
for i, energy in enumerate(min_error_energies):
    if node_counts[i] == 1:
        continue
    eigen_fun_x.append(eigenfunctions[i])

eigen_fun_x1 = np.array(eigen_fun_x[0])
x, y = np.meshgrid(x,x)
z=[]
for i in range(len(eigen_fun_x1)):
    z_row=[]
    for j in range(len(eigen_fun_x1)):
        z_row.append(eigen_fun_x1[i]*eigen_fun_x1[j])
    z.append(z_row) 
#z= eigen_fun_x1.reshape(100,100)*eigen_fun_x1.reshape(100,100) 


# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(x, y, z, c=z, cmap='viridis')  # You can customize the colormap ('cmap') as you like

# Add labels to the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()










