import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
m = 1
v1 = 10.0
a = 0.1
hbar = 1

# Functions
def wave(x, v, m):
    return np.sqrt((m * v) / (hbar ** 2)) * np.exp(-((m * v) / (hbar ** 2)) * np.abs(x))

def prob(x, v, m):
    return wave(x, v, m) ** 2

def gaussian(x, si, mu):
    return (1 / (si * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * si ** 2))

# Plotting
x = np.linspace(-15, 15, 10000)
v_values = [v1 / 3, v1 / 2, v1, v1 * 2, v1 * 3]

# Plotting the wave-function
plt.figure(figsize=(8, 6))
for v in v_values:
    plt.plot(x, wave(x, v, m), label=f'Wave-Function of the Particle with $V_0$ = {round(v, 2)}')
plt.xlabel('x', fontsize='12')
plt.ylabel('Wavefunction of the particle ($\Psi(x)$)', fontsize='12')
plt.axvline(x=a, color='black', linestyle='-.', label='Region of Observation')
plt.axvline(x=-a, color='black', linestyle='-.')
plt.xlim(-a - 1, a + 1)
plt.ylim(bottom=-1)
plt.grid(True, linewidth='0.3')
plt.axhline(color='black', linewidth='0.5')
plt.axvline(color='black', linewidth='0.5')
plt.title('Wave-Function of a particle as a function of position (x)', fontsize='12')
plt.legend(loc='upper right', fontsize='7')

# Plotting the Probability density graph
plt.figure(figsize=(8, 6))
for v in v_values:
    plt.plot(x, prob(x, v, m), '-', label=f'Particle with $V_0$ ={round(v, 2)}\nProb of finding the particle b/w { - a } & { a } is P : {round(quad(prob, -a, a, args=(v, m))[0] * 100, 3)}%')
plt.axvline(x=a, color='black', linestyle='-.', label='Region of Observation')
plt.axvline(x=-a, color='black', linestyle='-.')
plt.ylim(bottom=-2)
plt.xlim(-a - 1, a + 1)
plt.xlabel('x', fontsize='12')
plt.grid(True, linewidth='0.3')
plt.axhline(color='black', linewidth='0.5')
plt.axvline(color='black', linewidth='0.5')
plt.ylabel('Probability distribution function ($|\Psi(x)|^2$)', fontsize='12')
plt.legend(loc='upper right', fontsize='6')

# The Change in Probability as the a changes
t = np.linspace(0, 5, 1000)
plt.figure(figsize=(8, 6))
for v in v_values:
    y = [quad(prob, -ti, ti, args=(m, v))[0] for ti in t]
    plt.plot(t, y, label=f'particle under dirac potential: {round(v, 2)}')
plt.xlabel('Region of Observation (a)', fontsize='7')
plt.ylabel('Probability of finding particle under the potential as a function of a', fontsize='7')
plt.grid(True, linewidth='0.3')
plt.axhline(color='black', linewidth='0.5')
plt.axvline(color='black', linewidth='0.5')
plt.title('Probability of a particle to be bounded as a function of a')
plt.legend(loc='upper right', fontsize='7')

# Gaussian Plot
plt.figure(figsize=(8, 6))
n = 0.2
while n <= 1:
    plt.plot(x, gaussian(x, n, 0), '-.', label=f'$\mu=0$, $\sigma^2$={round(n, 3)}')
    n += 0.2
plt.ylabel('Gaussian function ($\Phi_{\mu,\sigma^2}(x)$)', fontsize='12')
plt.xlabel('x', fontsize='12')
plt.legend(fontsize='7')
plt.xlim(-7, 7)
plt.grid(True, linewidth='0.3')
plt.axhline(color='black', linewidth='0.7')
plt.axvline(color='black', linewidth='0.7')
plt.title('Gaussian Function')

plt.tight_layout()
plt.show()
