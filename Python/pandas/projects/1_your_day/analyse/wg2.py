import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1, 100)
data3 = np.random.normal(4, 1, 100)
data4 = np.random.normal(6, 1, 100)

# Create a list of data to plot
data = [data1, data2, data3, data4]

# Set up the figure and subplots
fig, axs = plt.subplots(figsize=(8, 6))

# Create the boxplot
axs.boxplot(data, labels=['Box 1', 'Box 2', 'Box 3', 'Box 4'])

# Add some padding to the plot
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Show the plot
plt.show()
