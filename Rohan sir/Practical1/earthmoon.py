import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create a figure and axis
fig, ax = plt.subplots()

# Define Earth's properties
earth_radius = 6371  # Earth's radius in kilometers
earth_color = 'blue'

# Define Moon's properties
moon_radius = 1737  # Moon's radius in kilometers
moon_distance = 384400  # Moon's distance from Earth in kilometers
moon_color = 'gray'

# Plot Earth as a circle
earth_circle = Circle((0, 0, 0), earth_radius, color=earth_color, label='Earth')
ax.add_patch(earth_circle)

# Plot Moon's orbit
moon_orbit = plt.Circle((0, 0, 0), moon_distance, color='black', fill=False, linestyle='dotted')
ax.add_artist(moon_orbit)

# Plot Moon as a circle
moon_circle = Circle((moon_distance, 0), moon_radius, color=moon_color, label='Moon')
ax.add_patch(moon_circle)

# Set aspect ratio to be equal, so the circle appears as a circle
ax.set_aspect('equal', adjustable='datalim')

# Set plot limits based on Moon's distance
ax.set_xlim(-moon_distance * 1.5, moon_distance * 1.5)
ax.set_ylim(-moon_distance * 1.5, moon_distance * 1.5)

# Add a legend
ax.legend()

# Add labels
plt.xlabel('Distance (km)')
plt.ylabel('Distance (km)')
plt.title('Earth and Moon')

plt.grid()
plt.show()