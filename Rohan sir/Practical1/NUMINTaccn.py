import matplotlib.pyplot as plt
import numpy as np

# Define the acceleration values and time intervals
accelerations = [0, 5, 0, -5, 0]
time_intervals = np.arange(0, 26, 5)  # Time from 0 to 25 with 5 intervals each

# Initialize arrays to store speed and displacement values
speed = [0]  # Initial speed is 0
displacement = [0]  # Initial displacement is 0

# Numerical integration using Euler's method
for i in range(len(time_intervals) - 1):
    dt = time_intervals[i + 1] - time_intervals[i]
    new_speed = speed[-1] + accelerations[i] * dt
    new_displacement = displacement[-1] + speed[-1] * dt + 0.5 * accelerations[i] * dt**2
    speed.append(new_speed)
    displacement.append(new_displacement)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(time_intervals, speed, marker='o')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.title('Speed of the Particle vs Time')

plt.subplot(2, 1, 2)
plt.plot(time_intervals, displacement, marker='o', color='orange')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Displacement of the Particle vs Time')

plt.tight_layout()
plt.show()