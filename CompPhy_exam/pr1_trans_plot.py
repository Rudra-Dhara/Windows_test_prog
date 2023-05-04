import numpy as np
import matplotlib.pyplot as plt

#part a -----------------------------------------------------------------------
#initial parameters
ab_e = np.arange(0,2.891,0.01)
v0_til = 2.891*np.ones_like(ab_e)
a=1.45

#defining the transindental equation
def tran_eq(e,v_til):
    return np.sqrt(v_til - e)/(np.tan(np.sqrt(v_til - e)*a)) + e

#plots
plt.plot(ab_e,tran_eq(ab_e,v0_til),label='Transidental equation plot')
plt.ylabel('Value')
plt.xlabel('$-E/20.75436}$')
plt.grid()
plt.title('Plot of transidental equation with reduced Energy')
plt.show()

#part b: NR-solution ------------------------------------
# this is function for root finding
#F is the function and f is it's derivative x_tol is the degree of accuracy and x_start is the starting point of the integral
def NR_rt(F,f,x_start,x_tol,*args):
    while abs(F(x_start,*args))>x_tol:
        x_start =x_start - F(x_start,*args)/f(x_start,*args)
    
    return x_start