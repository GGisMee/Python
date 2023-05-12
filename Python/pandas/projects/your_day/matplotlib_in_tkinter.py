import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Create a new Tkinter window
Window = tk.Tk()

# Create a new Matplotlib figure
fig = Figure(figsize=(5, 4), dpi=200)
ax = fig.add_subplot(211)
ax.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])

# Create a Tkinter canvas for the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=Window)
canvas.draw()
canvas.get_tk_widget().pack()

# Start the Tkinter event loop
tk.mainloop()
