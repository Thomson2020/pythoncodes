import numpy as np
import scipy.special as sp
import matplotlib.pyplot as pt

x=np.arange(-50,50,0.01)
pt.xlim(-20,20)

i=0
for i in range(0,5):
    pt.plot(x,sp.jv(i,x),label=rf"$b_{i}$")

pt.title("Bessel Polynomial $b_n$")
pt.legend(loc="best")
pt.xlabel("x")
pt.ylabel("B(x)")
pt.show()