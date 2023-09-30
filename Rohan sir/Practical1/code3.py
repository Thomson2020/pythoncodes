import numpy as np
import matplotlib.pyplot as plt

def fxy(xf,yf):
    y = 6*(yf**2)*xf
    return y

a =1;b = 3;h = 0.5;i =0
n = (b-a)/h # width of each interval
x =[]
y =[]
intg =[] #initial value y(8) = 1
x.append(0)
y.append(1/25)

while i<n:
    x.append(a + h*(i+1))
    y.append(y[i]+h*fxy(x[i],y[i]))
    i+=1

print ('value of y(x) is', y[i], "at x =",x[i])
plt.plot(x,y)
plt.title("Solution of DE dy/dx = 6y**2x")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()