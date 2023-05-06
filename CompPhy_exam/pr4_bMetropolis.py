import numpy as np

# Define the function to integrate
def f(r1,r2,th):
    fn= (r1**2 * r2**2 * np.sin(th) * np.exp( -2*(r1 + r2) ) )/( np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(th)))
    return fn

# Define the integration limits
r1_min = 0
r1_max = 10
r2_min = 0
r2_max = 10
th_min = 0
th_max = np.pi

def mc_3d_intg(N):
    num_samples = N

    # Generate random samples within the integration limits
    r1_samples = np.random.uniform(r1_min, r1_max, num_samples)
    r2_samples = np.random.uniform(r2_min, r2_max, num_samples)
    th_samples = np.random.uniform(th_min, th_max, num_samples)

    # Compute the function values at the sample points
    f_samples = f(r1_samples, r2_samples, th_samples)

    # Compute the integral approximation using the Monte Carlo method
    integral = 8*np.pi**2 * ((r1_max - r1_min) * (r2_max - r2_min) * (th_max - th_min) * np.mean(f_samples))

    return integral

n=10000000
intg_prev= mc_3d_intg(n//10)

intg = mc_3d_intg(n)

print(f'With n = {n} random point meshgrid we get our integral = {intg}\n the differnce in integral value between n = {n//10} and n = {n} is = {abs(intg - intg_prev)}')

