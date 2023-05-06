#finding the solution the bound state energy using rk4 method
import numpy as np
import matplotlib.pyplot as plt

a=1.45
def v_pot(x):
    v_op=[]
    for i in range(len(x)):
        if x[i]<a:
            v_op.append(-2.891)
        else:
            v_op.append(0)
    v_op[0]=1
    return v_op

e_arr = np.linspace(-0.74,-0.78,100)

y_min= 1000 #arbitrary large garbage value

e_min=-0.74
e_max=-0.78
while abs(y_min)>=0.001:
    #defining potential
    a=1.45
    def v(x):
        if x<a:
            return -2.891
        else:
            return 0
        

    # function of x at RHS
    #setting energy
    e=(e_min+e_max)/2

    def f(x,t):
        return (v(t)-e)*x
    # Initial conditions kept const for the rest of the problem
    ti = 0
    tf = 10
    x0 = 0.00
    v0 = 1 #arbitarary value just effect the normalization

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

    #finding the minimum energy and error
    
    if y[-1]<0:
        e_min = e
    elif y[-1]>0:
        e_max = e
    y_min=y[-1]

print(f'The energy value of the box potential = {e}')
plt.plot(x,np.ones_like(x)*e,ls=":",label='BS energy')
plt.plot(x,y+np.ones_like(x)*e,label='wave fn')
plt.plot(x,v_pot(x),label='Potential')
plt.xlabel('distance')
plt.legend()
plt.show()