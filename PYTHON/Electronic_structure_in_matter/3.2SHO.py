#2nd part of problem 2 part c
import matplotlib.pyplot as plt
import numpy as np

#defining the potential
def v_pot(r):
    x=r

    v = 0.5*x**2
    return v

x=np.array([])

e_list= np.linspace(0,7,1000)
for e in e_list:
   
    

    def f(x,t):
        return (v_pot(t)-e)*x
    
    # Initial conditions kept const for the rest of the problem
    ti = -3
    tf = 3
    x0 = 0.01
    v0 = -x0*np.exp(-ti**2/2) #slope
    x1=np.linspace(ti,tf,100)

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
    x, y, z = runge_kutta(f,1000) # x is x values y is the wave function z is the derivative of the wf

    if abs(y[-1])<abs(x0)+0.003 and abs(y[-1])>abs(x0)-0.003:
        print(y[-1])
        plt.plot(x1,v_pot(x1),label = 'Potential')
        plt.plot(x,np.ones_like(x)*e,ls=':',label=f'BS Energy{e}')
        plt.plot(x,5*y+np.ones_like(x)*e,label= f'wave function{e}')
        plt.plot(x,25*y**2+np.ones_like(x)*e,label= f'pdf{e}')
plt.title("Potential vs distance plot")
plt.xlabel('distance (x)')
plt.ylabel('Reduced potential/ Wave function')
plt.legend()
plt.show()


