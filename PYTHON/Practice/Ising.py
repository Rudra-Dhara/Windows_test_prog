#code for 2d ising model

import numpy as np
import matplotlib.pyplot as plt

N=40
s_grid=np.random.choice([1,-1],size=(N,N))
s_grid0 = s_grid

def del_E(grid:list,i):


# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the array as a bitmap image with black for -1 and white for +1
ax.imshow(s_grid, cmap='binary', vmin=-1, vmax=1)

# Set the title and show the plot
ax.set_title('Random 2x2 Array')
plt.show()