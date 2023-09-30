import matplotlib.pyplot as plt
import numpy as np
def function(Q, r):
    V=-Q/r
    return V
Q=4;Q1 =2*Q;x_st=1;x_en=5;n = 100;i = 0
x = np.linspace(x_st, x_en, n)
x1=np.linspace(x_en, x_st, n)
h =(x_en- x_st)/n
y1=[]
while i < len(x) - 2:
    t=(4*function(Q, x[i+1])-function(Q, x[i+2])-3*function(Q, x[i])) / (2*h)
    t1=(4*function(Q1, x1[i+1])-function(Q1, x1[i+2])-3*function (Q1, x1[i])) / (2*h)
    y1.append(abs(t1-t))
    i+=1

min_electric_field = min(y1)
min_electric_field_x = x[y1.index(min_electric_field)]

print("The minimum value of the electric field is:", min_electric_field)
print('The Electric field is minimum at x =', round(min_electric_field_x, 4))
plt.plot(x[0:n -2 ], y1,'--', color='black')
plt.xlabel('Distance between two point charges', fontsize=10)
plt.ylabel('Magnitude of the electric field', fontsize=10)
plt.scatter(min_electric_field_x, min_electric_field, color='red')
plt.title('Analyzing the Electric Field between two points along the x-axis', fontsize=10 )
plt.legend(fontsize=20)
plt.show()
