import matplotlib.pyplot as plt
import numpy as np

# Data for the bar charts
data1 = np.array([10, 15, 20, 25])
data2 = np.array([5, 10, 15, 20])
data3 = np.array([8, 12, 16, 20])
x = np.arange(len(data1))
width = 0.25

# Set up the figure and subplot
fig, ax = plt.subplots(figsize=(6, 4))

# Create the grouped bar chart
ax.bar(x - width, data1, width, label='Bar Chart 1')
ax.bar(x, data2, width, label='Bar Chart 2')
ax.bar(x + width, data3, width, label='Bar Chart 3')

# Add axis labels and a title
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Grouped Bar Chart')

# Add a legend
ax.legend()

# Show the figure
plt.show()


