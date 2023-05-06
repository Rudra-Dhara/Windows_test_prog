import numpy as np

# the function to integrate
def f(r1,r2,th):
    fn= (r1**2 * r2**2 * np.sin(th) * np.exp( -2*(r1 + r2) ) )/( np.sqrt(r1**2 + r2**2 - 2*r1*r2*np.cos(th)))
    return fn

# the integration limits
r1_min = 0
r1_max = 10
r2_min = 0
r2_max = 10
th_min = 0
th_max = np.pi

def mc_3d_intg(N):
    num_samp = N

    # Generate random samples
    r1_samp = np.random.uniform(r1_min, r1_max, num_samp)
    r2_samp = np.random.uniform(r2_min, r2_max, num_samp)
    th_samp = np.random.uniform(th_min, th_max, num_samp)

    # simulated sample
    f_samp = f(r1_samp, r2_samp, th_samp)

    # Compute the integral
    int = 8*np.pi**2 * ((r1_max - r1_min) * (r2_max - r2_min) * (th_max - th_min) * np.mean(f_samp))

    return int

n=10000000

intg = mc_3d_intg(n)

print(f'With n = {n} random point meshgrid we get our integral = {intg}')

