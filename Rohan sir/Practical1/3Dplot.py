import numpy as np
import matplotlib.pyplot as plt

#creating an empty canvas
fig = plt.figure()
ax = plt.axes(projection ='3d')

x=[0,1,2,3,4,5,6]
y=[0,1,4,9,16,25,36]
z=[0,1,4,9,16,25,36]

#syntax for the curve plotting
ax.plot3D(x,y,z)
ax.scatter(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D plot for a curve passing through the given points')
plt.show()
