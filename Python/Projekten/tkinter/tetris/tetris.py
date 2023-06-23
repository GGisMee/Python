import tkinter as tk
import numpy as np
from sgl import newcoord


window = tk.Tk()
box_geometry: int = 30
window.geometry("400x400")

canvas = tk.Canvas(window, width=10*box_geometry, height=20*box_geometry)
canvas.pack()
# 10 i bas, 20 i höjd
        

class shape:
    def __init__(self, boxes, position, color):
        self.color = color
        self.position = position # denna är som andra box position och visar var på mappen den finns
        self.boxes = boxes # är alla boxar i en shape
    def rotate(self):
        print(self.boxes)
        print()
        for i, el in enumerate(self.boxes):
            print(self.boxes[i])
            if el!= [0,0]:
                self.boxes[i] = newcoord.rotate_from_origo(el, -90)
            else: 
                self.boxes[i] = [0,0]
            self.boxes = np.round(self.boxes)
            print(self.boxes[i])

# själva blocken
class I_block(shape):
    def __init__(self, position, color):
        shape.__init__(self, [[-1,0], [0,0], [1,0], [2,0]], position, color)
        print(newcoord.from_deg_xy_len(90, [1,1], 2))
    def __repr__(self):
        return "I"


class J_block(shape):
    def __init__(self, position, color):
        shape.__init__(self, [[-1,1], [-1,0], [0,0], [1,0]], position, color)
    def __repr__(self):
        return "J"

class L_block(shape):
    def __init__(self, position, color):
        shape.__init__(self, [[-1,0], [0,0], [1,0], [1,1]], position, color)
    def __repr__(self):
        return "L"


class O_block(shape):
    def __init__(self, position, color):
        shape.__init__(self, [[0,0], [1,0], [0,-1], [1,-1]], position, color)
    def __repr__(self):
        return "O"


#! fixa en kvadrant konverterare i sgl för att enkelt kunna rotera
#! fixa error med kvadrant konverterare
#print(newcoord.rotate_from_origo([1,0], -90))
j = I_block(position=[5,2], color="yellow")   
j.rotate()
exit()
box_arr = np.resize(np.arange(0, 10*20), (20,10))+1 # ska användas för att genom xy positioner i index få ut boxen att ändra
# ger en xy grid med 0,0 till 10, 20 till höger nedåt
for i in range(20):
    for i2 in range(10):
        box_id = canvas.create_rectangle(i2*box_geometry, i*box_geometry, i2*box_geometry+box_geometry, i*box_geometry+box_geometry, fill="light gray", outline="green")

    
    

window.mainloop()