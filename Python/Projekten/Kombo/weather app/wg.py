import matplotlib.pyplot as plt
import numpy as np

# Generate example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
fig, ax1 = plt.subplots()

# Plot the first dataset with the original x-axis
ax1.plot(x, y1, color='blue')
ax1.set_xlabel('X-axis')

# Create a secondary y-axis which will behave as a third x-axis
ax2 = ax1.twinx()

# Hide the secondary y-axis ticks and labels
ax2.set_yticks([])
ax2.set_yticklabels([])

# Set the limits and label for the secondary x-axis
ax2.set_xlim(ax1.get_xlim())
ax2.set_xlabel('Third X-axis')

# Show the plot
plt.show()
