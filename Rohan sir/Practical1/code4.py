import numpy as np
import matplotlib.pyplot as plt

e = 1;r= 0.2;l= 1.;t= 0;i= 0  #intial values
tt= []
ii= []
tf= 50.0 #final value of t
dt= 0.01 #step size


def f(t,i):
    y = e-i*r
    return y

while t<=tf:
    tt.append(t)
    ii.append(i)
    i+=dt* f(t, i)
    t=t+dt

tt = np.array((tt))
ii = np.array((ii))
exact = (e/r)*(1.0 - np.exp(-r/1**tt))

print ("Plotting of the solution with exact results")
#plt.subplot(1,1,1)
plt.title("Plotting of the solution with exact results")
plt.plot(tt,ii, 'k--',label="dt=%.4Ff"%(dt))
plt.plot(tt,exact, 'k',label="Exact Solution")
plt.xlabel('time')
plt.ylabel('current')
plt.grid()
plt.show()