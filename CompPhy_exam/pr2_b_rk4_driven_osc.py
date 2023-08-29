import numpy as np
import matplotlib.pyplot as plt

# Initial conditions kept const for the rest of the problem
ti = 0
tf = 150 * np.pi
x0 = 0.2
v0 = 0

# function of x at RHS
def f(x,v,nu,t,a):
    w = 2/3
    return -nu*v - np.sin(x) + a*np.cos(w*t)

# Define the fourth-order Runge-Kutta method
# N is the number of time division
def runge_kutta(f,N,nu,a):
    dt = (tf - ti) / N
    t = np.linspace(ti, tf, N)
    x = np.zeros(N)
    v = np.zeros(N)
    #initial conditions
    x[0] = x0 
    v[0] = v0
    for i in range(1, N):
        #the coefficients of rk 4 method
        # change in position is a linear function of v so the coeff are written accordingly
        # change in velocity depends on the positions
        k1x = dt * v[i-1]  
        k1v = dt * f(x[i-1],v[i-1],nu,t[i-1],a)
        k2x = dt * (v[i-1] + 0.5 * k1v)
        k2v = dt * f(x[i-1] + 0.5 * k1x,v[i-1],nu,t[i-1],a)
        k3x = dt * (v[i-1] + 0.5 * k2v)
        k3v = dt * f(x[i-1] + 0.5 * k2x,v[i-1],nu,t[i-1],a)
        k4x = dt * (v[i-1] + k3v)
        k4v = dt * f(x[i-1] + k3x,v[i-1],nu,t[i-1],a)

        x[i] = x[i-1] + (1/6) * (k1x + 2 * k2x + 2 * k3x + k4x) # change of position    
        #change of velocity depending on the position (k(n) are function of position)
        v[i] = v[i-1] + (1/6) * (k1v + 2 * k2v + 2 * k3v + k4v) 
    return t, x, v



# Loop over different values of N
nu_list=[0.5,0.5]


#plotting for N = 100
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Run the Runge-Kutta method for two different damping coefficients
N_list=[1000,10000,100000,10**6]
for N in N_list:
    t1, x1, v1 = runge_kutta(f, N, nu_list[0],0.5)
    t5, x5, v5 = runge_kutta(f, N, nu_list[1],1.2)

    # Plot the results
    ax[0].plot(t1, x1, label="A = 0.5, N = {}".format(N))
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Theta")
    ax[0].set_title("Damped driven Pendulum (A = 0.5)")
    ax[0].legend()

    ax[1].plot(t5, x5, label="A = 1.2, N = {}".format(N))
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Theta")
    ax[1].set_title("Damped driven Pendulum (A = 1.2)")
    ax[1].legend()

plt.tight_layout()
plt.show()
