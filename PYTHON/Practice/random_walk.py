import numpy as np
import matplotlib.pyplot as plt
# program for random walk pdf

# the functon take the number of steps N and give the o/p of distance travelled
# here we consider the length of each step is = 1
def rand_walker(N):
    dist=0
    for i in range(N):
        a=np.random.random()
        
        if a>=0.5:
            dist+=1
        else:
            dist-=1
    return dist

#random walker in a periodic boundary condition
def rand_wk_perdk_bc(N,length=50):
    dist=0
    for i in range(N):
        a=np.random.random()
        
        if a>=0.5:
            if dist + 1 > length:
                dist = -1*length
            else:
                dist+=1
        else:
            if dist - 1 < -1*length:
                dist = length
            else:
                dist-=1
    return dist

N_list = [10,100,1000,10000]
N_run = 1000  #number of simulation

for N in N_list:
    d_arr= np.array([])
    for i in range(N_run):
        d_arr = np.append(d_arr,rand_wk_perdk_bc(N))
    plt.hist(d_arr,bins=50)
    plt.show()
        
    


