import numpy as np
import matplotlib.pyplot as plt

# Generate data for the plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.plot(x, y1, label='Plot 1')
plt.plot(x, y2, label='Plot 2')

# Fill the area between the two plots with gray color
plt.fill_between(x, y1, y2, where=(y1 > y2), facecolor='#dedede', alpha=0.5)

plt.arrow(x=4, y=18, dx=2, dy=5, width=.08)  # denna i mitten

# Add labels, title, and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Two Plots with Gray Area Between')
plt.legend()

# Display the plot
plt.show()
