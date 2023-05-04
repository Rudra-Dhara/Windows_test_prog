import numpy as np
import matplotlib.pyplot as plt

#part a -----------------------------------------------------------------------
#initial parameters
ab_e = np.arange(0,2.89,0.01)
v0_til = 2.891*np.ones_like(ab_e)
a=1.45

#defining the transindental equation
def tran_eq(e,v_til):
    return np.sqrt(v_til - e)/(np.tan(np.sqrt(v_til - e)*a)) + np.sqrt(e) 

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

def df_tran(e,v_til):
    return -0.5/( np.sqrt(v_til - e)*(np.tan(np.sqrt(v_til - e)*a)) )  + a*0.5/(  (np.cos(a*np.sqrt(v_til - e)))**2 *np.sqrt(v_til - e) ) + 1/np.sqrt(e)


soln= -1*NR_rt(tran_eq,df_tran,1,0.001,2.891)
print('The value of reduced energy where the eqn is satisfied is = ',soln)

#finding the lowest value of v_til

v_var=np.linspace(1.4,1.2,1000)
dif = v_var[0]-v_var[1]
for v in v_var:
    e_t=np.linspace(0.01,v-0.01,1000)
    tran_list=tran_eq(e_t,v*np.ones_like(v_var))
    min_val = np.min(tran_list)
    
    if min_val>=0:
        print(f'\n\nThe value where minimum value of the transindental equation is just above 0 (i.e. {min_val}).\nwhere the value of the reduced potential is {-v}')
        print(f'So, the previous minimum value where the solution exist = {-v-dif}')
        break