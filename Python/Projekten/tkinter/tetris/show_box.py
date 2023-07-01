import tkinter as tk
import numpy as np
window = tk.Tk()
class show_box:
    def __init__(self, Frame, bl:int=20, color="light gray"): # bl for boxlength
        self.canvas = tk.Canvas(Frame)
        self.canvas.pack()
        self.color = color
        # fixa shapen [[1,2,3,4], [5,6,7,8]...]
        for i in range(4):
            for i2 in range(4):
                print(self.canvas.create_rectangle(i*bl, i2*bl, i*bl+bl, i2*bl+bl, fill="light gray"))

    def add_shape(self, shape_arr, color):
        pass
box = show_box(window)
window.mainloop()
        