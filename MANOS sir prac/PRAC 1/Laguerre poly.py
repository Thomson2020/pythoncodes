import numpy as np
from scipy.special import eval_laguerre
import matplotlib.pyplot as pt

x=np.arange(-5,5,0.01)
pt.xlim(-1,5)
pt.ylim(-3,5)

i=0
for i in range(0,5):
    pt.plot(x,eval_laguerre(i,x),label=rf"$L_{i}$")

pt.title("Laguerre Polynomials")
pt.legend(loc="best")
pt.xlabel("x")
pt.ylabel("$L_n{x}$")
pt.show()