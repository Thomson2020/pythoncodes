#initial cond are pi/4 and t=0, (-pi/4), t=0

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
L1,L2 = 1,1  # Length of the second pendulum (m)
m1,m2 = 1,1 # Mass of the second pendulum bob (kg)

def deriv(y, t, L1, L2, m1, m2):
    """Return the first derivatives of y = theta1, z1, theta2, z2."""
    theta1, z1, theta2, z2 = y

    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)

    theta1dot = z1
    z1dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2)-(m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    theta2dot = z2
    z2dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) + m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    return theta1dot, z1dot, theta2dot, z2dot

def calc_E(y):
    """Return the total energy of the system."""

    th1, th1d, th2, th2d = y.T
    V = -(m1+m2)*L1*g*np.cos(th1) - m2*L2*g*np.cos(th2)
    T = 0.5*m1*(L1*th1d)**2 + 0.5*m2*((L1*th1d)**2 + (L2*th2d)**2 +2*L1*L2*th1d*th2d*np.cos(th1-th2))
    return T + V

# Maximum time, time point spacings and the time grid (all in s).
tmax, dt = 30, 0.01
t = np.arange(0, tmax+dt, dt)
# Initial conditions: theta1, dtheta1/dt, theta2, dtheta2/dt.
y0 = np.array([np.pi/4, 0, -np.pi/4, 0])

# Do the numerical integration of the equations of motion
y = odeint(deriv, y0, t, args=(L1, L2, m1, m2))

# Unpack z and theta as a function of time
theta1, theta2 = y[:,0], y[:,2]

# Convert to Cartesian coordinates
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# Plot the double pendulum motion
plt.plot(t,theta1,'m')
plt.title('$\\theta_{1}$ vs time: when $\\theta_{1}$ is = $\\pi$/4 at t=0',weight = 'bold')
plt.xlabel('time',weight = 'bold')
plt.ylabel('$\\theta_{1}$',weight = 'bold')
plt.show()

plt.plot(t,theta2,'m')
plt.title('$\\theta_{2}$ vs time: when $\\theta_{2}$ is = -$\\pi$/4 at t=0',weight = 'bold')
plt.xlabel('time',weight = 'bold')
plt.ylabel('$\\theta_{2}$',weight = 'bold')
plt.show()

plt.plot(x1,y1,'m')
plt.title('Plot of position of 1st bob at $\\theta_{1}$ = $\\pi$/4',weight = 'bold')
plt.xlabel('$x_{1}$',weight = 'bold')
plt.ylabel('$y_{1}$',weight = 'bold')
plt.show()

plt.plot(x2,y2,'m')
plt.title('Plot of position of 2nd bob at $\\theta_{2}$ = -$\\pi$/4',weight = 'bold')
plt.xlabel('$x_{2}$',weight = 'bold')
plt.ylabel('$x_{2}$',weight = 'bold')
plt.show()