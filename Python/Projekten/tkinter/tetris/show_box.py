import tkinter as tk
import numpy as np
window = tk.Tk()
class shape():
    def __init__(self, boxes, color) -> None:
        self.boxes = boxes
        self.color = color

def lighten(hex):
    hex = hex[1:]
    rgb: list = []
    for i in [0,2,4]:
        decimal = int(hex[i:i+2],16)
        rgb.append(decimal)
    rgb = np.array(rgb)-60

    rgb = np.where(rgb<0, 0, rgb) # lighten value
    r,g,b = np.where(rgb>255, 255, rgb)
    #print(r,g,b)
    new_hex =  "#{:02x}{:02x}{:02x}".format(r, g, b)
    return new_hex


class show_box:
    def __init__(self, Frame, bl:int=20, color="light gray"): # bl for boxlength
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(pady=10)
        self.color = color
        
        self.box_arr = (np.arange(1,9).reshape(2,4))
        self.boxes = np.array([0,0])
        for i in range(2):
            for i2 in range(4):
                self.canvas.create_rectangle(i2*bl, i*bl, i2*bl+bl, i*bl+bl, outline="")

    def change_shape(self, shape):
        boxes = (shape.boxes)
        shape_color = shape.color
        for i in range(2):
            while np.any(boxes[:,i]==-1):
                boxes[:,i]+=1
        ordered_boxes = []
        ordered_boxes = self.box_arr[boxes[:, 1], boxes[:, 0]]
        if not np.array_equal(self.boxes, np.array([0,0])):
            for i in self.boxes:
                self.canvas.itemconfig(i, fill=self.color, outline="")
        
        for i in ordered_boxes:
            self.canvas.itemconfig(i, fill=shape_color, outline=lighten(shape_color))
        self.boxes = ordered_boxes
        

shape1 = shape(np.array([[-1,0], [0,0], [1,0], [2,0]]), "#00ffff")
shape2 = shape(np.array([[-1,-1], [-1,0], [0,0], [1,0]]), "#0000ff")
shape3 = shape(np.array([[-1,0], [0,0], [1,0], [1,-1]]), "#ff7f00")
box = show_box(window)
#box.change_shape(shape1)
#box.change_shape(shape2)
box.change_shape(shape3)


window.mainloop()
        