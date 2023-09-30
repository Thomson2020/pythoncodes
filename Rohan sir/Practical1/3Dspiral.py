import numpy as np
import matplotlib.pyplot as plt

#creating an empty canvas
fig = plt.figure()
ax = plt.axes(projection ='3d')

th=np.linspace(-15,15,300)

x=np.sin(th);y=np.cos(th);z=np.linspace(-2,2,300)

#syntax for the curve plotting
ax.plot3D(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D plot of spiral motion')
plt.show()
