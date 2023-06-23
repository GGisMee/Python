import tkinter as tk
import numpy as np

arr = np.array([[1,2], [3,4], [5,6]])+[1,2]
print(arr)

exit()
window = tk.Tk()

canvas = tk.Canvas(window)
canvas.pack()
canvas.create_rectangle(0,0, 100, 100, fill="lime")


window.mainloop()