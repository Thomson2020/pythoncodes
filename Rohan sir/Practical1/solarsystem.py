import numpy as np 
import matplotlib.pyplot as plt

th = np.linspace(0, 2*np.pi,2500)

#MERCURY
a1=0.387
e1=0.2056
c1=a1*e1
b1=np.sqrt(a1**2-c1**2)
X1=a1*np.cos(th)+c1
Y1=b1*np.sin(th)
plt.plot(X1,Y1,color='red')

#VENUS
a2=0.723
e2=0.0068
c2=a2*e2
b2=np.sqrt(a2**2-c2**2)
X2=a2*np.cos(th)+c2
Y2=b2*np.sin(th)
plt.plot(X2,Y2)

#EARTH
a3=1.000
e3=0.0167
c3=a3*e3
b3=np.sqrt(a3**3-c2**3)
X3=a3*np.cos(th)+c3
Y3=b3*np.sin(th)
plt.plot(X3,Y3)

#MARS
a4=1.524
e4=0.0167
c4=a4*e4
b4=np.sqrt(a4**2-c4**2)
X4=a4*np.cos(th)+c4
Y4=b4*np.sin(th)
plt.plot(X4,Y4)

#JUPTER
a5=5.203
e5=0.0484
c5=a5*e5
b5=np.sqrt(a5**2-c5**2)
X5=a5*np.cos(th)+c5
Y5=b5*np.sin(th)
plt.plot(X5,Y5)

#SATURN
a6=9.537;e6=0.0542
c6=a6*e6
b6=np.sqrt(a6**2-c6**2)
X6=a6*np.cos(th)+c2
Y6=b6*np.sin(th)
plt.plot(X6,Y6,color='black')

#URANUS
a7=19.191;e7=0.0472
c7=a7*e7
b7=np.sqrt(a7**2-c7**2)
X7=a7*np.cos(th)+c7
Y7=b7*np.sin(th)
plt.plot(X7,Y7)

#NEPTUNE
a8=30.069;e8=0.0086
c8=a8*e8
b8=np.sqrt(a8**2-c8**2)
x8=a8*np.cos(th)+c8
y8=b8*np.sin(th)
plt.plot(x8,y8)

#pluto

a9=30.069;e9=0.0086
c9=a9*e9
b9=np.sqrt(a9**2-c9**2)
x9=a9*np.cos(th)+c9
y9=b9*np.sin(th)
plt.plot(x9,y9)


#HALLEY'S COMET
a10=17.834;e10=0.9671
c10=a10*e10
b10=np.sqrt(a10**2-c10**2)
X10=a10*np.cos(th)+c10
Y10=b10*np.sin(th)
plt.plot(X10,Y10)

#Solar System 
plt.title('SOLAR SYSTEM')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()