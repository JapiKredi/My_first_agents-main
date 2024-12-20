# filename: sine_plot.py

import os
import numpy as np
import matplotlib.pyplot as plt

# Generate array of angles from 0 to 2pi
x = np.linspace(0, 2*np.pi, 100)

# Generate sine values
y = np.sin(x)

# Create a new figure and a subplot
fig, ax = plt.subplots()

# Plot sine function with dark green color
ax.plot(x, y, color='darkgreen')

# Set the title and labels
ax.set_title('Sine Wave')
ax.set_xlabel('Angle [rad]')
ax.set_ylabel('sin(x)')

# Check whether specified directory exists or not
if not os.path.exists('coding'):
    os.makedirs('coding')

# Save the figure to the desired directory and in PNG format
plt.savefig('coding/sine_in_green.png')

# Close the figure
plt.close(fig)