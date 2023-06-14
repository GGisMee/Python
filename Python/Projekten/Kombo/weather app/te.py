import matplotlib.pyplot as plt
import math
from simplegraphlib import newcoord
# Create a figure and axes
fig, ax = plt.subplots()

value: int = 1
x, y = newcoord.from_deg_xy_len(90, [0,0], 2/3*value, show=True)
# Create a custom arrowhead shape


# Create arrows with the same shape
#arrow1 = plt.arrow(0, 0, x, y, **arrow_shape)
#arrow2 = plt.arrow(1, 1, -1, -1, **arrow_shape)
#arrow3 = plt.arrow(2, 2, 0, 0, **arrow_shape)
arrow4 = plt.arrow(0, 0, x, y, head_length = 1/3*value, width=0.1)
plt.scatter([0,math.sqrt(0.5)], [0,math.sqrt(0.5)], color="red")
plt.show()
