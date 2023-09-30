import numpy as np
from scipy.special import eval_hermite
import matplotlib.pyplot as pt

x=np.arange(-5,5,0.01)
pt.xlim(-2,2)
pt.ylim(-30,30)

i=0
for i in range(0,5):
    pt.plot(x,eval_hermite(i,x),label=rf"$L_{i}$")

pt.title("Hermite Polynomials")
pt.legend(loc="best")
pt.xlabel("x")
pt.ylabel("$H_n{x}$")
pt.show()