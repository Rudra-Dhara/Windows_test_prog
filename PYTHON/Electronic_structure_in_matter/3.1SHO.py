import numpy as np
import matplotlib.pyplot as plt

# Define the harmonic oscillator equation
def harmonic_oscillator(y, t):
    omega = 1.0  # Frequency of the oscillator
    dydt = np.zeros_like(y)
    dydt[0] = y[1]
    dydt[1] = -omega**2 * y[0]
    return dydt

# Implement the RK4 method
def runge_kutta_4(func, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0

    for i in range(0, n - 1):
        h = t[i + 1] - t[i]
        k1 = h * func(y[i], t[i])
        k2 = h * func(y[i] + k1 / 2, t[i] + h / 2)
        k3 = h * func(y[i] + k2 / 2, t[i] + h / 2)
        k4 = h * func(y[i] + k3, t[i] + h)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return y

# Set initial conditions and time span
y0 = np.array([0.0, 1.0])  # Initial position and velocity as a NumPy array
t = np.linspace(0, 10, 100)  # Time span

# Use the shooting method to find the correct boundary condition
def shooting_method(target_position):
    def boundary_condition(y):
        return y[-1, 0] - target_position

    guess = 1.0  # Initial guess for the boundary condition
    tol = 0.1  # Tolerance for the shooting method
    while True:
        y = runge_kutta_4(harmonic_oscillator, np.array([0.0, guess]), t)
        if abs(boundary_condition(y)) < tol:
            break
        guess -= boundary_condition(y) / (y[-1, 1] - guess)
    
    return y

# Solve the harmonic oscillator problem with the correct boundary condition
target_position = 2.0  # Adjust this as needed
y_solution = shooting_method(target_position)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(t, y_solution[:, 0], label=f'Solution for target position {target_position}')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.grid()
plt.show()
