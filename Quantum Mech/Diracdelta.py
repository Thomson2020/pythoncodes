import numpy as np
import matplotlib.pyplot as plt

# Values of sigma (standard deviation) for which you want to plot the Gaussian distribution
sigmas = [0.5, 1.0, 1.5, 2.0]

x = np.arange(-5, 5, 0.01)

# Create a plot for each sigma
for sigma in sigmas:
    variance = sigma ** 2
    gf = np.exp(-np.square(x) / (2 * variance)) / (np.sqrt(2 * np.pi * variance))
    plt.plot(x, gf, label=f'Sigma = {sigma}')

plt.ylabel('Gaussian distribution')
plt.legend()
plt.show()
