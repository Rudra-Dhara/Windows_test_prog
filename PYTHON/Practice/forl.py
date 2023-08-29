import numpy as np

def f(x, y, z):
    return np.sin(x) + np.cos(y) + np.exp(-z**2)

def mc_integrate(f, limits, N):
    volume = np.prod([limit[1] - limit[0] for limit in limits])
    samples = np.random.uniform(*limits, size=(N, len(limits)))
    values = f(*samples.T)
    integral = volume * np.mean(values)
    return integral

limits = [(0, np.pi), (-np.pi, np.pi), (0, 10)]
N = 10000000

integral = mc_integrate(f, limits, N)
print(f"Using {N} samples, the integral is {integral}")
