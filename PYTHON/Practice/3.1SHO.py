#finding the solution the bound state energy using rk4 method
#first part of the problem c

import numpy as np
import matplotlib.pyplot as plt

#Potential for harmonic oscillator
def v_pot(x):
    return 0.5*x**2

for e in [0.6,0.7,0.8]:
    #defining potential
    def v(x):
        return 0.5*x**2


    def f(x,y):
        return (v(y)-e)*x
    # Initial conditions kept const for the rest of the problem
    yi = -5
    yf = 5
    x0 = np.exp(-yi**2/2)
    v0 = -yi*np.exp(-yi**2/2) #arbitarary value just effect the normalization

    # Define the fourth-order Runge-Kutta method
    # N is the number of time division
    def runge_kutta(f,N):
        dy = (yf - yi) / N
        y = np.linspace(yi, yf, N)
        x = np.ones(N)
        v = np.zeros(N)
        #initial conditions
        x[0] = x0 
        v[0] = v0
        for i in range(1, N):
            #the coefficients of rk 4 method
            # change in position is a linear function of v so the coeff are written accordingly
            # change in velocity depends on the positions
            k1x = dy * v[i-1]  
            k1v = dy * f(x[i-1],y[i-1])
            k2x = dy * (v[i-1] + 0.5 * k1v)
            k2v = dy * f(x[i-1] + 0.5 * k1x,y[i-1])
            k3x = dy * (v[i-1] + 0.5 * k2v)
            k3v = dy * f(x[i-1] + 0.5 * k2x,y[i-1])
            k4x = dy * (v[i-1] + k3v)
            k4v = dy * f(x[i-1] + k3x,y[i-1])

            x[i] = x[i-1] + (1/6) * (k1x + 2 * k2x + 2 * k3x + k4x) # change of position    
            #change of velocity depending on the position (k(n) are function of position)
            v[i] = v[i-1] + (1/6) * (k1v + 2 * k2v + 2 * k3v + k4v) 
        return y, x, v


    # Define the number of mesh points
    x, y, z = runge_kutta(f,1000)


    print(f'The energy value of the box potential = {e}')
    plt.plot(x,np.ones_like(x)*e,ls=":",label='BS energy')
    plt.plot(x,(y+np.ones_like(x)*e),label=f'wave fn {e}')
    plt.plot(x,v_pot(x),label='Potential')
    plt.xlabel('distance')
    plt.legend()
plt.show()