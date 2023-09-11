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

#printing the minimum value energy    
print('The ground state energy = ',2*min_error_energies[1])
print('The first exited state energy = ',min_error_energies[1] + min_error_energies[2])

eigen_fun_x1 = np.array(eigen_fun_x[0])
eigen_fun_x2 = np.array(eigen_fun_x[1])
x, y = np.meshgrid(x,x)
z1=[]
for i in range(len(eigen_fun_x1)):
    z_row=[]
    for j in range(len(eigen_fun_x1)):
        z_row.append(eigen_fun_x1[i]*eigen_fun_x1[j])
    z1.append(z_row) 
#z= eigen_fun_x1.reshape(100,100)*eigen_fun_x1.reshape(100,100) 


# Create a 3D figure for amplitude
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(x, y, z1, c=z1, cmap='viridis')  # You can customize the colormap ('cmap') as you like

# Add labels to the axesaa
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Wave Function')

# Show the plot
plt.show()

# Create a 3D figure for PDF
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(x, y, np.square(z1),c=z1, cmap='viridis')  # You can customize the colormap ('cmap') as you like

# Add labels to the axesaa
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability density')

# Show the plot
plt.show()

z2=[]
for i in range(len(eigen_fun_x1)):
    z_row=[]
    for j in range(len(eigen_fun_x1)):
        z_row.append(eigen_fun_x1[i]*eigen_fun_x2[j])
    z2.append(z_row) 
#z= eigen_fun_x1.reshape(100,100)*eigen_fun_x1.reshape(100,100) 


# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(x, y, z2, c=z2)  # You can customize the colormap ('cmap') as you like

# Add labels to the axesaa
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('wave function')

# Show the plot
plt.show()

# Create a 3D figure for PDF
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(x, y, np.square(z2),c=z2, cmap='viridis')  # You can customize the colormap ('cmap') as you like

# Add labels to the axesaa
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability density')

plt.show()




