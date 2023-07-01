import tkinter as tk
import numpy as np
window = tk.Tk()
class shape():
    def __init__(self, boxes, color) -> None:
        self.boxes = boxes
        self.color = color


class show_box:
    def __init__(self, Frame, bl:int=20, color="light gray"): # bl for boxlength
        self.canvas = tk.Canvas(Frame)
        self.canvas.pack()

        # fixa shapen [[1,2,3,4], [5,6,7,8]...]
        self.box_arr = (np.arange(1,17).reshape(4,4))
        for i in range(4):
            for i2 in range(4):
                self.canvas.create_rectangle(i2*bl, i*bl, i2*bl+bl, i*bl+bl, fill="light gray")

    def change_shape(self, shape):
        boxes = (shape.boxes)
        shape_color = shape.color
        for i in range(2):
            while np.any(boxes[:,i]==-1):
                boxes[:,i]+=1
        ordered_boxes = []
        ordered_boxes = self.box_arr[boxes[:, 1], boxes[:, 0]]
        for i in ordered_boxes:
            self.canvas.itemconfig(i, fill=shape_color)

shape1 = shape(np.array([[-1,0], [0,0], [1,0], [2,0]]), "#00ffff")
shape2 = shape(np.array([[-1,-1], [-1,0], [0,0], [1,0]]), "#0000ff")
shape3 = shape(np.array([[-1,0], [0,0], [1,0], [1,-1]]), "#ff7f00")
box = show_box(window)
box.add_shape(shape1)
box.add_shape(shape2)


window.mainloop()
        