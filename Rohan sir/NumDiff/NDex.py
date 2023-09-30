import numpy as np
import matplotlib.pyplot as plt
def f(x):
	y = x**2
	return y

x = np.linspace(0 , 50, 500)
a = 0;b = 50;n = 500 #maximum range, minimum range,step size
h= (b-a)/n
i=0
derv=[ ]
while i<n-2:
	dervj = (-f(x[i+2])+4*f(x[i+1])-(3*f(x[i])))/(2*h)
	derv.append(dervj)
	i = i+1

print('differentiated value=',derv[-1])
plt.plot(x[0:498],derv)
plt.title('Result for y$^2$')
plt.xlabel('x')
plt.ylabel('derv')
plt.show()