import matplotlib.pyplot as plt
import numpy as np

#defining the potential
def v_pot(r):
    x=0.7*r

    v=-0.5041*np.exp(-x)/x - 79.530227*np.exp(-4*x)/x + 312.4307*np.exp(-7*x)/x
    return v

x1=np.linspace(0.6,10,1000)

v_min= np.min(v_pot(x1))

x=np.array([])


#shooting ---------------------------------------------------------------------------------

y_min= 1000 #arbitrary large garbage value

e_min= v_min
e_max=-0.00
tol=0.01
#loop
count=0
y_min0=0
y_min=100000 #arbitary large garbage value

e1=-0.30
e2=-0.28
while True:
   
    e=(e1 + e2)/2 

    def f(x,t):
        return (v_pot(t)-e)*x
    
    # Initial conditions kept const for the rest of the problem
    ti = 10
    tf = 0.001
    x0 = 0.01
    v0 = -np.sqrt(abs(e))*x0 #arbitarary value just effect the normalization

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
    x, y, z = runge_kutta(f,1000)

    #finding the minimum energy and error
    if y[-1]>0:
        e1=e
    elif y[-1]<0:
        e2=e
    if abs(y[-1])<=0.001:
        print('Bound state energy = ',e)
        break



print('The minimum value of the potential is = ',v_min)
plt.plot(x1,v_pot(x1),label = 'Potential')
plt.plot(x,np.ones_like(x)*e,ls=':',label='BS Energy')
plt.plot(x,y+np.ones_like(x)*e,label= 'wave function')
plt.title("Potential vs distance plot")
plt.xlabel('distance (r)')
plt.ylabel('Reduced potential/ Wave function')
plt.legend()
plt.show()


