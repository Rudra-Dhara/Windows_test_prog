import numpy as np

# Define the kernel
kernel = np.array([0, 1, 2, 3])

# Define your square grid (example values)
square_grid = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]])

# Determine the dimensions of the grid
rows, cols = square_grid.shape

# Create an empty result array with the same shape as the grid
result = np.zeros((rows, cols))

# Perform the convolution-like operation
for i in range(rows):
    for j in range(cols):
        for k in range(len(kernel)):
            if j - k >= 0:
                result[i, j] += square_grid[i, j - k] * kernel[k]

# Display the result
print("Result of convolution-like operation:")
print(result)
