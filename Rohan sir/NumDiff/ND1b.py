import numpy as np
import matplotlib.pyplot as plt
def f(x):
	y=(np.sin(x))**2/np.cos(x)
	return y
x=np.linspace(0,np.pi, 50)
a=0;b=np.pi;n= 50 #minimum range,maximum range,step size
h= (b-a)/n
i=0
derv=[]
while i<n-2:
	dervj=(-f(x[i+2])+4*f(x[i+1])-(3*f(x[i])))/(2*h)
	derv.append(dervj)
	i=i+1

print('differentiated value=',derv[-1])
#plt.plot(x[0:48],derv)
#plt.title('Result $\sin^2(x)\div(\cos(x))$')
#plt.xlabel('x')
#plt.ylabel('derv')
#plt.show()
