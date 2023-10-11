import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spe
import math

# Bohr radius
a0 = 0.529
# Number of points
h = 100
# Defining the 'r' interval
x = np.linspace(0.5, 10, h)

# Defining a function for the radial part
def R(r, n, l):
    t = (2 / (n * a0))
    s = math.sqrt((spe.factorial(n - l - 1)) / (2 * n * (spe.factorial(n + l))**3))
    u = (2 * r) / (n * a0)
    R = (t**1.5) * s * (u**l) * np.exp(-u) * spe.assoc_laguerre(u, n - l - 1, 2 * l + 1)
    return R

for n in range(1, 5):
    for l in range(n):
        fig, ax = plt.subplots(figsize=(6, 6))
        Radial = np.zeros((h))
        for i in range(h):
            Radial[i] = (x[i]**2) * R(x[i], n, l)**2
        ax.plot(x, Radial, label='n = {}, l = {}'.format(n, l))
        ax.set_ylabel('$r^2 * R^2(r)$')
        ax.set_xlabel('r')
        ax.legend()
        plt.show()
