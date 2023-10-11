import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from mpl_toolkits.mplot3d import Axes3D

a0 = 0.529
i = complex(0, 1)

def R(theta, phi, m, l):
    z = np.cos(theta)
    L = special.lpmv(abs(m), l, z)
    k = (((2 * l + 1) * special.factorial(1 - abs(m))) / ((4 * np.pi) * special.factorial(1 + abs(m)))) ** (1/2)
    if m < 0:
        R = k * L * ((np.cos(m * phi)) + (i * np.sin(m * phi)))
        R = R.imag
        return R
    else:
        R = ((-1) ** m) * k * L * ((np.cos(m * phi)) + (i * np.sin(m * phi)))
        R = R.real
        return R

# Define the values of theta and phi with more points
theta = np.linspace(0, np.pi, 300)
phi = np.linspace(0, 2 * np.pi, 600)
theta, phi = np.meshgrid(theta, phi)
l = int(input("Enter the value of l:\n"))
m = int(input("Enter the value of m:\n"))
# Calculate spherical harmonics
Y = R(theta, phi, m, l)

x = np.sin(theta) * np.cos(phi) * (abs(Y))
y = np.sin(theta) * np.sin(phi) * (abs(Y))
z = np.cos(theta) * (abs(Y))

# Create a larger figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with a colormap and color bar
ax.plot_surface(x, y, z, rstride=2,cstride=2,cmap='viridis',
                edgecolor='none')
ax_lim = 20
ax.plot([-ax_lim, ax_lim], [0, 0], [0, 0], c='0.5', lw=1, zorder=10)
ax.plot([0, 0], [-ax_lim, ax_lim], [0, 0], c='0.5', lw=1, zorder=10)
ax.plot([0, 0], [0, 0], [-ax_lim, ax_lim], c='0.5', lw=1, zorder=10)

# Remove the axis labels and customize the viewing angle for perspective
ax.axis('off')
ax.view_init(elev=30, azim=30)

# Add a title
ax.set_title(f'Spherical Harmonics: l={l}, m={m}', fontsize=16)

# Increase tick label font size
ax.tick_params(axis='both', which='major', labelsize=12)

# Set the plot limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.axis('on')
ax.view_init(40, 60)
plt.show()
