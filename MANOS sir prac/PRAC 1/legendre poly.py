import numpy as np
from scipy.special import eval_legendre
import matplotlib.pyplot as pt

x=np.arange(-50,50,0.01)
pt.xlim(-2,2)
pt.ylim(-3,3)

i=0
for i in range(0,5):
    pt.plot(x,eval_legendre(i,x),label=rf"$L_{i}$")

pt.title("Legendre Polynomials")
pt.legend(loc="best")
pt.xlabel("x")
pt.ylabel("$L_n{x}$")
pt.show()