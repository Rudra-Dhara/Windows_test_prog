import numpy as np
import matplotlib.pyplot as plt
# Define the function to integrate
def f(r1, r2, th):
    return (r1**2 * r2**2 * np.sin(th) * np.exp(-2*(r1 + r2))) / (np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(th)))

def p(x, A):
    return A * np.exp(-x)
# Define the integration limits
r_min = 0
r_max = 10
th_min = 0
th_max = np.pi

# Define the importance sampling distributions for r1 and r2
def g_r(r1,r2,A):
    return A**2 * np.exp(-r1-r2)


# Set the number of samples to use for the Monte Carlo integration
N = 10000000

# Generate random samples from the importance sampling distributions for r1 and r2
r1_samples = np.random.rand(N)
r2_samples = np.random.rand(N)

# Transform the samples to the integration limits using the inverse CDF method
A = 1 / (1 - np.exp(-10)) # Calculate the value of A to normalize p(x)

r1_imp = -np.log(np.ones_like(r1_samples) - r1_samples/A)
r2_imp = -np.log(np.ones_like(r2_samples) - r2_samples/A)


# Generate random samples within the integration limits for th
th_samples = np.random.uniform(th_min, th_max, N)

# Compute the function values at the sample points
f_samples = f(r1_imp, r2_imp, th_samples)

# Compute the weights for each sample using the importance sampling distributions
weights = (f_samples) / (g_r(r1_imp,r2_imp,A))

# Compute the integral approximation using the Monte Carlo method and importance sampling
integral = np.mean(weights)

# Scale the result by the volume of the integration region
integral *= (th_max - th_min)

# Print the result
print("The Monte Carlo integral approximation with importance sampling is:", integral*8*np.pi**2)
