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

# del 1 graf över alla värden (kan välja om specifikt senaste 30 eller så)
Food = np.array(df["Food"])
Sleep = np.array(df["Sleep"])
School = np.array(df["School"])
Mood = np.array(df["Mood"])
x = np.arange(0, len(df))
plt.title("Your day")
plt.xlabel("Day")
plt.ylabel("Grade")

fig, axs = plt.subplots(figsize=(8, 6), dpi=50)


axs.plot(x,Food, "ro-",  label="Food", linewidth=3)
axs.plot(x,Sleep, "go-",  label="Sleep", linewidth=3)
axs.plot(x,School, "bo-",  label="School", linewidth=3)
axs.plot(x,Mood, "yo-",  label="Mood", linewidth=3)
axs.legend()


canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
window.mainloop()