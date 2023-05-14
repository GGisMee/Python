import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Create a Matplotlib figure
figure = Figure(figsize=(6, 4), dpi=100)
subplot = figure.add_subplot(111)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
subplot.plot(x, y)

# Create a FigureCanvasTkAgg widget to embed the figure in the Tkinter window
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()
