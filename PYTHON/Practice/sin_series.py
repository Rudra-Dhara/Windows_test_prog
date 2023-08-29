import matplotlib.pyplot as plt
import numpy as np

N_list=[100,1000]

for N in N_list:
    u_2_list=[]
    for i in range(N+1):
        sum=0
        for n in range(1,N):
            sum+=(1/N)*(np.sin(n*np.pi*i/N))**2/(np.sin(n*np.pi/(2*N)))**2
        u_2_list.append(sum)
    plt.plot(u_2_list,label='For N = {}'.format(N))

plt.legend()
plt.show()
