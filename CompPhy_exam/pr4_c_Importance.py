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


# number of sampling 
N = 10000000 #max number supported by my ram

# Generate random samples from the importance sampling distributions for r1 and r2
r1_samp = np.random.rand(N)
r2_samp = np.random.rand(N)

# transformation to exp distribution
A = 1 / (1 - np.exp(-r_max)) # Calculate the value of A to normalize p(x)

r1_imp = -np.log(np.ones_like(r1_samp) - r1_samp/A)
r2_imp = -np.log(np.ones_like(r2_samp) - r2_samp/A)


# random samples within the integration limits for th
th_samp = np.random.uniform(th_min, th_max, N)

# Compute the function values at the sample points
f_samp = f(r1_imp, r2_imp, th_samp)

# Intigration simulation
I_samp = (th_max - th_min)*(f_samp) / (g_r(r1_imp,r2_imp,A))   #first and last terms are normalization factor

# Compute the integral by taking the mean 
intg = np.mean(I_samp)

# Scale the result by the volume of the integration region

# Print the result
print("The Monte Carlo integral approximation with importance sampling is:", intg*8*np.pi**2)

