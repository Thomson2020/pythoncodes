import numpy as np
import matplotlib.pyplot as plt

#creating a parameter theta array
x = np.linspace(-0.25,0.25,60)

#initializing the constants for the given equation to be plot
a=2

y=4*a*x**2      #eqn for parabola

#plotting the parabola
plt.plot(x,y, color = 'red')
plt.scatter(x,y, color = 'black')
plt.axis('equal')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('parabola')
plt.grid()
plt.show()