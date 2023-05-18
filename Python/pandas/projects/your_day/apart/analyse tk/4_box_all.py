import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

window = Tk()
window.title("Matplotlib in Tkinter")

df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')
n_df = (np.array(df)[:,2:])
print(n_df)

# Set up the figure and subplots
fig, axs = plt.subplots(figsize=(8, 6), dpi=40)

# Create the boxplot
axs.boxplot(n_df, labels=['Food', 'Sleep', 'School', 'Mood'])

# Add some padding to the plot
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
window.mainloop()