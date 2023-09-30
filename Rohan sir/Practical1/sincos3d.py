import numpy as np
import matplotlib.pyplot as plt

#defining surface and axes

x  = np.linspace(0,6*np.pi,50)
y  = np.linspace(0,6*np.pi,50)
x,y= np.meshgrid(x,y)
z  =np.cos(x) + np.sin(y)

#syntax for thev3D plotting
ax = plt.axes(projection = '3d')

#syntax for the surface plotting
ax.plot_surface(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Surface plot of cos-sin')
plt.show()
