#code for 2d ising model

import numpy as np
import matplotlib.pyplot as plt

N=100
Nrun=10*N**2
s_grid=np.random.choice([1,-1],size=(N,N))
s_grid0 = s_grid.copy()
# Create a new figure and axis
fig, ax = plt.subplots(1,2)
ax[1].imshow(s_grid0, cmap='binary', vmin=-1, vmax=1)
ax[1].set_title('initial')


T=1
#calculate the energy of the site (-ve)
def rep(j):
    if j==N:
        return 0
    elif j==-1:
        return N-1
    else:
        return j

def E_site(grid:list,i,j):
    del_e= grid[i,j]*grid[i,rep(j+1)] + grid[i,j]*grid[i,rep(j-1)] + grid[i,j]*grid[rep(i+1),j] + grid[i,j]*grid[rep(i-1),j] 
    return -del_e

def s_flip(grid, i,j):
    print(E_site(grid,i,j))
    if E_site(grid,i,j)>0:
        grid[i,j]=-1*grid[i,j]  # allowing the flip
        return grid
    else:
        rn=np.random.random()
        if (rn <= 2*np.exp(2*E_site(grid,i,j)*100)):
            grid[i,j]=-1*grid[i,j]  # allowing the flip
            return grid
        else:
            return grid

for k in range(Nrun):
    #random lattice site
    i=np.random.randint(0,N)
    j=np.random.randint(0,N)

    if E_site(s_grid,i,j)>0:
        s_grid[i,j]=-1*s_grid[i,j]  # allowing the  flip
    else:
        rn=np.random.random()
        if (rn <= np.exp(2*E_site(s_grid,i,j)/T)):
            s_grid[i,j]=-1*s_grid[i,j]  # allowing the flip






# Plot the array as a bitmap image with black for -1 and white for +1
ax[0].imshow(s_grid, cmap='binary', vmin=-1, vmax=1)
ax[0].set_title('after')
ax[1].imshow(s_grid0, cmap='binary', vmin=-1, vmax=1)
ax[1].set_title('before')

# Set the title and show the plot
plt.show()