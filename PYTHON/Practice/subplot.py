import matplotlib.pyplot as plt
import numpy as np

# create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# create a figure with 3 subplots arranged in a 1x3 grid
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# plot the data on each subplot and set x-labels
ax1.plot(x, y1)
ax1.set_title('sin(x)')
ax1.set_xlabel('x')
ax2.plot(x, y2)
ax2.set_title('cos(x)')
ax2.set_xlabel('x')
ax3.plot(x, y3)
ax3.set_title('tan(x)')

# add x-labels to ax3
ax3.text(0, -0.15, 'x label 1', ha='left', transform=ax3.transAxes)
ax3.text(1, -0.15, 'x label 2', ha='right', transform=ax3.transAxes)

# add a main title to the figure
fig.suptitle('Trigonometric Functions')

# adjust spacing between subplots and x-labels
fig.subplots_adjust(left=0.2, wspace=0, bottom=0.3)

# show the plot
plt.show()
