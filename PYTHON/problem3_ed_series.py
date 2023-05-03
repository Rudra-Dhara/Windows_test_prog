import numpy as np

N=np.arange(1,15,2)

sum=0
for n in N:
    for m in range(1,n+1,2):
        sum+=(16/(np.pi**2*n*m*np.cosh(np.pi*np.sqrt(n**2 + m**2)/2)))*(np.sin(n*np.pi*0.5)*np.sin(m*np.pi*0.5)) * np.cosh(0)
    print(f'The numerical factor for the sum up to {n} is = {sum}')