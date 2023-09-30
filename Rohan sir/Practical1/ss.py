import numpy as np
import matplotlib.pyplot as plt

# Define parameters for each celestial body (semi-major axis, eccentricity, color, name)
celestial_bodies = [
    {"a": 0.387,  "e": 0.2056, "color": "red",    "name": "Mercury"},
    {"a": 0.723,  "e": 0.0068, "color": "orange", "name": "Venus"},
    {"a": 1.000,  "e": 0.0167, "color": "blue",   "name": "Earth"},
    {"a": 1.524,  "e": 0.0934, "color": "red",    "name": "Mars"},
    {"a": 5.203,  "e": 0.0484, "color": "orange", "name": "Jupiter"},
    {"a": 9.537,  "e": 0.0542, "color": "black",  "name": "Saturn"},
    {"a": 19.191, "e": 0.0472, "color": "cyan",   "name": "Uranus"},
    {"a": 30.069, "e": 0.0086, "color": "blue",   "name": "Neptune"},
    {"a": 17.834, "e": 0.9671, "color": "gray",   "name": "Halley's Comet"},]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the orbits for each celestial body
for body in celestial_bodies:
    a = body["a"]
    e = body["e"]
    color = body["color"]
    name = body["name"]

    theta = np.linspace(0,2*np.pi,1000)

    c=a*e
    b=np.sqrt(a**2-c**2)
    X = a * np.cos(theta)+c
    Y = b * np.sin(theta)
    ax.plot(X, Y, label=name, color=color)

# Set aspect ratio to equal
#ax.set_aspect('equal')

# Set labels and legend
plt.title('Solar System Orbits')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#plt.legend()

# Show the plot
plt.show()
