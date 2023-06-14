import numpy as np
import matplotlib.pyplot as plt

# Example data
x_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
label_view1 = 1  # Spacing for first layer of xticks
label_view2 = 2  # Spacing for second layer of xticks

# Plotting
fig, ax = plt.subplots()
ax.plot(x_arr)

# Set the first layer of xticks
ax.set_xticks(range(len(x_arr))[::label_view1])

# Create a secondary x-axis with the second layer of xticks below the primary x-axis
ax2 = ax.secondary_xaxis('bottom')
ax2.set_xticks(range(len(x_arr))[::label_view2])

# Display the plot
plt.show()
