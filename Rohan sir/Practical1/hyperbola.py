import numpy as np
import matplotlib.pyplot as plt

#creating a parameter theta array
x = np.linspace(-10,10,30)

a=np.sqrt(2+x**2/4)
b=-np.sqrt(2+x**2/4)

#plotting the hyperbola
plt.plot(x,a, color = 'red')
plt.scatter(x,a, color = 'black')
plt.plot(x,b, color = 'red')
plt.scatter(x,b, color = 'black')
plt.axis('equal')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('hyperbola')
plt.grid()
plt.show()