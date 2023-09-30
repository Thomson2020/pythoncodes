import matplotlib.pyplot as plt
import numpy as np

def function(x):
    y=(np.cos(x))**3
    return y

a=-3.14;b=3.14;n=20;i=0;sum=0
dx=(b-a)/n
x=[];f=[];intg=[]

while i<n:
#getting midpoint
    midpt=a+(i+1/2)*dx
    x.append(midpt)
    fn=function(midpt)
    f.append(fn)
    sum=sum+ f[i]*dx
    intg.append(sum)
    i=i+1

print('integrated value=', round(sum,3))
#plotting
plt.figure()
plt.subplot(2,1,1)
plt.plot(x,f)
plt.title('graph of f(x)=x and $\int_{a}^{b} f(x) dx$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(x,intg)
plt.xlabel('x')
plt.ylabel('$\int_{a}^{b} f(x) dx$')
plt.show()