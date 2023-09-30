import numpy as np
import matplotlib.pyplot as plt

# Defining the original vector
vector=np.array([3, 4])

# Defining the rotation angle in radians (75, -150, 90 degress(converted into radians))
rotate_angle1=np.deg2rad(75)
rotate_angle2=np.deg2rad(-150)
rotate_angle3=np.deg2rad(90)

# Creating 2x2 rotation matrix
rotate_matrix1=np.array([[np.cos(rotate_angle1), -np.sin(rotate_angle1)],
                          [np.sin(rotate_angle1), np.cos(rotate_angle1)]])

rotate_matrix2=np.array([[np.cos(rotate_angle2), -np.sin(rotate_angle2)],
                          [np.sin(rotate_angle2), np.cos(rotate_angle2)]])

rotate_matrix3=np.array([[np.cos(rotate_angle3), -np.sin(rotate_angle3)],
                          [np.sin(rotate_angle3), np.cos(rotate_angle3)]])

# Rotate the vector by multiplying with the rotation matrix
rotated_vector1=np.dot(rotate_matrix1, vector)
rotated_vector2=np.dot(rotate_matrix2, vector)
rotated_vector3=np.dot(rotate_matrix3, vector)

# Reflect the rotated vector across y=-x line by swapping x and y coordinates
reflected_vector1=np.array([-rotated_vector1[1], -rotated_vector1[0]])
reflected_vector2=np.array([-rotated_vector2[1], -rotated_vector2[0]])
reflected_vector3=np.array([-rotated_vector3[1], -rotated_vector3[0]])

# Create a plot
plt.figure(figsize=(10, 8))

#Plotting the original vector
plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='black', label='Original Vector')

#Plotting rotated vector
plt.quiver(0, 0, rotated_vector1[0], rotated_vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Rotated +75 degrees')
plt.quiver(0, 0, rotated_vector2[0], rotated_vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Rotated -150 degrees')
plt.quiver(0, 0, rotated_vector3[0], rotated_vector3[1], angles='xy', scale_units='xy', scale=1, color='b', label='Rotated +90 degrees')

#Plotting the reflected vector
plt.quiver(0, 0, reflected_vector1[0], reflected_vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Reflected')
plt.quiver(0, 0, reflected_vector2[0], reflected_vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Reflected')
plt.quiver(0, 0, reflected_vector3[0], reflected_vector3[1], angles='xy', scale_units='xy', scale=1, color='b', label='Reflected')

#Limiting axes
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Add gridlines
plt.grid()

#Adding labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='lower left')

# Show the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Vector Operations')
#plt.gca().set_aspect('equal', adjustable='box')
plt.show()
