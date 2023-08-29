#code for 2d ising model

import numpy as np
import matplotlib.pyplot as plt

cv_priv=np.zeros(48)
for z in range(100):
    N=128
    Nrun=(N**2)*10
    s_grid=np.random.choice([1],size=(N,N))
    s_grid0 = s_grid.copy()



    T_list= np.arange(0.1,5,0.1)
    #calculate the energy of the site (-ve)
    def rep(j):
        if j==N:
            return 0
        elif j==-1:
            return N-1
        else:
            return j

    def E_site(grid:list,i,j):
        del_e= 0.01*grid[i,j] + grid[i,j]*grid[i,rep(j+1)] + grid[i,j]*grid[i,rep(j-1)] + grid[i,j]*grid[rep(i+1),j] + grid[i,j]*grid[rep(i-1),j] 
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

    mag_list=[]
    en_list=[]
    print(T_list)
    for T in T_list:

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
        en=0
        for m in range(N):
            for n in range(N):
                en+= E_site(s_grid,m,n)
        en_list.append(en)
        
        print('running')
    print(en_list)

    cv_list=[]
    for i in range(len(en_list)-1):
        d_en= en_list[i+1]-en_list[i]
        cv_list.append(d_en/0.1) #as 0.1 is our energy spacing
    cv_list=np.array(cv_list)

    cv_priv+=cv_list
# # Create a new figure and axis
# fig, ax = plt.subplots(2,2)
# ax[0,1].imshow(s_grid0, cmap='binary', vmin=-1, vmax=1)
# ax[0,1].set_title('initial')

# # Plot the array as a bitmap image with black for -1 and white for +1
# ax[0,0].imshow(s_grid, cmap='binary', vmin=-1, vmax=1)
# ax[0,0].set_title('after')


# # Set the title and show the plot
# plt.show()

plt.plot(T_list[1:],cv_priv/100,label='Specific Heat')
plt.legend()
plt.xlabel('temp')
plt.ylabel('Energy/Specific heat')
plt.xticks(np.arange(0.1,5,0.2))
plt.grid(True,which='major', axis='both', linewidth=0.25, alpha=0.4)
plt.show()