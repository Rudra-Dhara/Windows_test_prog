import numpy as np
import matplotlib.pyplot as plt


#defining potential
a=1.45
def v(x):
    if x<a:
        return -2.891
    else:
        return 0
    

# function of x at RHS
#setting energy
e=-0.7
def f(x,t,e):
    return (v(t)-e)*x
# Initial conditions kept const for the rest of the problem
k = 1
m = 1
ti = 0
tf = 4
x0 = 0
v0 = np.sqrt(-v(0)-e)

# Define the fourth-order Runge-Kutta method
# N is the number of time division
def runge_kutta(f,N):
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
        k1v = dt * f(x[i-1],t[i-1])
        k2x = dt * (v[i-1] + 0.5 * k1v)
        k2v = dt * f(x[i-1] + 0.5 * k1x,t[i-1])
        k3x = dt * (v[i-1] + 0.5 * k2v)
        k3v = dt * f(x[i-1] + 0.5 * k2x,t[i-1])
        k4x = dt * (v[i-1] + k3v)
        k4v = dt * f(x[i-1] + k3x,t[i-1])

        x[i] = x[i-1] + (1/6) * (k1x + 2 * k2x + 2 * k3x + k4x) # change of position    
        #change of velocity depending on the position (k(n) are function of position)
        v[i] = v[i-1] + (1/6) * (k1v + 2 * k2v + 2 * k3v + k4v) 
    return t, x, v


# Define the number of mesh points
x, y, z = runge_kutta(f,10000)



# Plot the results
plt.plot(x,y)
plt.xlabel('Time (t)')
plt.ylabel(' $\Delta E$ (E_analytic - E_computed)')
plt.legend()
plt.title('$\Delta E$ vs Time plot')
plt.show()