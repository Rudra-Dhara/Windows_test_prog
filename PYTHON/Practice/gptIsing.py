import numpy as np
import matplotlib.pyplot as plt

# Define the size of the lattice
L = 20

# Define the initial state of the spins (random +1 or -1)
spins = np.random.choice([-1, 1], size=(L, L))

# Define the parameters of the model
J = 1  # coupling constant
T = 10  # temperature

# Define the number of Monte Carlo steps (MCS) to run
num_steps = 1000

# Define a function to calculate the energy change of flipping a spin
def delta_E(spins, i, j, J):
    neighbor_sum = spins[(i-1)%L,j] + spins[(i+1)%L,j] + \
                   spins[i,(j-1)%L] + spins[i,(j+1)%L]
    return 2*J*spins[i,j]*neighbor_sum

# Define a function to run the Metropolis algorithm for one step
def metropolis_step(spins, T, J):
    # Choose a random spin
    i, j = np.random.randint(0, L), np.random.randint(0, L)
    # Calculate the energy change if we flip the spin
    dE = delta_E(spins, i, j, J)
    # Accept or reject the flip based on the Metropolis criterion
    if dE <= 0 or np.exp(-dE/T) > np.random.random():
        spins[i,j] *= -1

# Run the simulation for the specified number of steps
energies = []
for step in range(num_steps):
    # Run one step of the Metropolis algorithm
    metropolis_step(spins, T, J)
    # Calculate and store the energy of the current state
    energy = -J*np.sum(spins*(np.roll(spins, -1, axis=0) + np.roll(spins, -1, axis=1)))
    energies.append(energy)

# Plot the energy vs. time
plt.plot(energies)
plt.xlabel('Time (MCS)')
plt.ylabel('Energy')
plt.title(f'Ising model simulation (L={L}, T={T}, J={J})')
plt.show()
