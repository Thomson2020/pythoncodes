import math
import matplotlib.pyplot as plt

a=1
xplot=[];yaxis=[];probability_density =[]

for n in range(1, 5):
    x = -a
    x_values = []
    y_values = []
    density_values = []

    while x<= a:
        if n%2==0:
            y=(math.sin((n*math.pi*x)/(2*a)))/math.sqrt(a)
        else:
            y=(math.cos((n*math.pi*x)/(2*a)))/math.sqrt(a)

        x_values.append(x)
        y_values.append(y)
        density=y**2
        density_values.append(density)
        x += 0.0001

    xplot.append(x_values)
    yaxis.append(y_values)
    probability_density.append(density_values)

# Plot the eigenfunctions and their probability densities for n = 1 to 4
plt.figure(figsize=(10,9))

for i in range(4):
    plt.subplot(4,2,2*i+1)
    plt.plot(xplot[i], yaxis[i],color='black')
    plt.title(f'n ={i+1} (Eigenfunction)')
    plt.xlabel('Position (x)')
    plt.ylabel('$\psi(x)$')
    plt.grid()

    plt.subplot(4,2,2*i+2)
    plt.plot(xplot[i], probability_density[i], color='cyan')
    plt.title(f'n={i+1} (Probability Density)')
    plt.xlabel('Position (x)')
    plt.ylabel('Probability Density')
    plt.grid()

plt.tight_layout()
plt.show()
