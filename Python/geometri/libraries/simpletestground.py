import numpy as np
from simplegraphlib import *
import matplotlib.pyplot as plt

coords = shape.format_from_middle(xy=[0,0], points=3, length=1, sidelen=False, show=True)
coords = np.array([coords])
coords = coords.reshape((-1,2))
coords = np.hsplit(coords, 2)
plt.figure(figsize=(5,5), dpi=150)
plt.scatter(coords[0], coords[1])

plt.xticks(np.linspace(-1, 1, 10))
plt.yticks(np.linspace(-1, 1, 10))


plt.show()

