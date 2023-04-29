import matplotlib.pyplot as plt
import numpy as np

labels = ["A", "B", "C"]
values = [1,4,2]

Bars = plt.bar(labels, values)

Bars[0].set_hatch("/")
Bars[1].set_hatch("O")
Bars[2].set_hatch("*")


plt.show()
