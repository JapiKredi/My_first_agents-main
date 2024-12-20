# Filename: sine_plot.py

import numpy as np
import matplotlib.pyplot as plt

# Generate data for the sine wave
x = np.linspace(0, 10, 1000)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the sine wave
ax.plot(x, y, color='darkgreen')

# Display the plot
plt.show()