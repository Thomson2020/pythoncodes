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
    s = math.sqrt((math.factorial(n - l - 1)) / (2 * n * (math.factorial(n + l))**3))
    u = (2 * r) / (n * a0)
    R = (t**1.5) * s * (u**l) * np.exp(-u) * spe.assoc_laguerre(u, n - l - 1, 2 * l + 1)
    return R

for n in range(1, 5):
    fig, axs = plt.subplots(n, 1, sharex=True, figsize=(6, 6))
    if n == 1:
        axs = [axs]
    for l in range(n):
        Radial = np.zeros((h))
        for i in range(h):
            Radial[i] = R(x[i], n, l)
        axs[l].plot(x, Radial, label='n = {}, l = {}'.format(n, l))
        axs[l].set_ylabel('R(r)')
        axs[l].legend()
    axs[-1].set_xlabel('r')
plt.show()
