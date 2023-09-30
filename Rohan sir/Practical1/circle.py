import numpy as np
import matplotlib.pyplot as plt

#creating a parameter theta array
th = np.linspace(0,2*np.pi,75)

#initializing the constants for the given equation to be plot
a=3;b=3
#co-ordinates for the center of the Circle
xcord = 0;ycord = 0

#creating parametric equation of x and y arrays from theta
x = xcord + a*np.cos(th)
y = ycord + b*np.sin(th)

#plotting the Circle
plt.plot(x,y, color = 'red')
plt.scatter(x,y, color = 'black')
plt.axis('equal')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Circle')
plt.grid()
plt.show()