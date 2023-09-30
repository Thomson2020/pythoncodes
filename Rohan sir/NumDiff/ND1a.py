import numpy as np
import matplotlib.pyplot as plt

def f(x):
	y = np.sqrt(x)*np.exp(-x)
	return y

x = np.linspace(0.2,2, 500)
a = 0.2;b = 2;n = 500		#minimum range,maximum range,step size
h = (b-a)/n
i  = 0
derv=[ ]
while i<n-2:
	dervj = (-f(x[i+2])+4*f(x[i+1])-(3*f(x[i])))/(2*h)
	derv.append(dervj)
	i = i+1
print('differentiated value=',derv[-1])
#plt.plot(x[0:3],derv)
#plt.title('Result $\\sqrt{x}*e^{-x}$')
#plt.xlabel('x')
#lt.ylabel('derv')
#plt.show()
