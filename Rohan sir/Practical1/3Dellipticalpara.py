import numpy as np
import matplotlib.pyplot as plt

#grid creation 
x=np.linspace(-8,8,100)
y=np.linspace(-3,3,100)
X,Y=np.meshgrid(x,y)

a=8;b=3

Z=(X/a)**2+(Y/b)**2

#plotting the surface
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
surf=ax.plot_surface(X,Y,Z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Elliptical Paraboloid')
plt.show()