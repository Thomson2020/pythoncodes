import matplotlib.pyplot as plt
import numpy as np

def func(x):
    y=(np.cos(x))**3
    return y

a=-3.14;b=3.14;n=50;i=0;sum=0
dx=(b-a)/n
x=[];y=[];Z=[]

while i<n:
    x1= a + i * dx
    x2= x1+dx
    trap=(x1+x2)/2
    x.append(trap)
    fn=func(trap)
    y.append(fn)

    sum += y[i]*dx
    Z.append(sum)
    i=i+1

print("integrated value is =", round(sum,5))
plt.figure()
plt.subplot(2,1,1)
plt.plot(x,y)
plt.title('graph of f(x)=x and $\int f(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2,1,2)
plt.plot(x,Z)
plt.xlabel('x')
plt.ylabel('$\int_{a}^{b} f(x) dx$')
plt.show()
