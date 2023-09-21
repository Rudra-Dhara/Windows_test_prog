#2nd part of problem 2 part c
import matplotlib.pyplot as plt
import numpy as np

#defining the potential
l=2 #angular momentum
def v_pot(r):
    v=-1/r + l*(l+1)/(2*r**2)
    return v

x1=np.linspace(2,20,1000)

v_min= np.min(v_pot(x1))

x=np.array([])


e_max= -0.01
e_min = -0.1
for e in np.linspace(e_min,e_max,100):
   

    def f(x,t):
        return 2*(v_pot(t)-e)*x
    
    # Initial conditions kept const for the rest of the problem
    ti = 22
    tf = 0.5
    x0 = np.exp(-np.sqrt(abs(e))*ti)
    v0 = -x0*np.sqrt(abs(e)) #arbitarary value just effect the normalization

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

    


    if abs(y[-1])<0.003:
        print(y[-1])
        print('Bound state energy',e)
        plt.plot(x1,v_pot(x1),label = 'Potential')
        plt.plot(x,np.ones_like(x)*e,ls=':',label='BS Energy')
        plt.plot(x,y+np.ones_like(x)*e,label= f'wave function{e}')
        plt.title(f"Potential vs distance plot for energy ")
        plt.xlabel('distance (r)')
        plt.ylabel('Reduced potential/ Wave function')
        plt.legend()
plt.show()