import tkinter as tk
import numpy as np
from sgl import newcoord
import time
from random import randint
import threading

window = tk.Tk()
box_geometry: int = 30
window.geometry(f"{10*box_geometry}x{20*box_geometry}")

canvas = tk.Canvas(window, width=10*box_geometry, height=20*box_geometry)
canvas.pack()
# 10 i bas, 20 i höjd
        

class shape:
    local_boxes: list
    
    def __init__(self, position, color):
        self.color = color
        self.position = position # denna är positionen och visar var på mappen den finns
        self.boxes = np.array(self.local_boxes)+position
        self.create(self.boxes)

    def delete(self, boxes):
        for i, el in enumerate(boxes):
            #el = np.vectorize(lambda el1: int(el1))(el)
            positions_on_grid = (box_arr[el[1]][el[0]])
            #print(positions_on_grid, type(positions_on_grid))
            canvas.itemconfig(positions_on_grid, fill="light gray")
            #canvas.update_idletasks()

    def create(self, boxes):
        for i, el in enumerate(boxes):
            #el = np.vectorize(lambda el1: int(el1))(el)
            positions_on_grid = (box_arr[el[1]][el[0]])
            #print(positions_on_grid, type(positions_on_grid))
            canvas.itemconfig(positions_on_grid, fill=self.color)
        #canvas.update_idletasks()     
           # fixa så den tar in på den positionen från arrayen och ändrar färgen

    def evaluate(self, boxes): # testar om den är utanför några gränser
        if (np.any(boxes[:,1]<0)): # [:,1]
            print("outside of higher border")
            return 1
        if (np.any(boxes[:,0]>=10) or np.any(boxes[:,0]<0)):
            print("outside of right or left border")
            return 1
        if np.any(boxes[:,1]>=20):
            print("outside of lower border")
            return 1
        if np.any(np.all(old_shapes == self.boxes[:, None], axis=-1)):
            print("inside of another box")
            return 1

        return 0

    def rotate(self):

        if str(self) == "O":
            print("O, so no rotation")
            return

        save_local_boxes = self.local_boxes[:]
        save_boxes = self.boxes[:]
        for i, el in enumerate(self.local_boxes):
            if el!= [0,0]:
                self.local_boxes[i] = newcoord.rotate_from_origo(el, 90)
            else: 
                self.local_boxes[i] = [0,0]
        self.local_boxes = np.round(self.local_boxes).tolist()

        self.boxes = (np.array(self.local_boxes)+self.position).astype(int)
        #print(self.boxes)
        
        
        if self.evaluate(self.boxes):
            self.boxes = save_boxes 
            self.local_boxes = save_local_boxes
            print("unable")
            print(self.boxes)
            print(self.local_boxes)
            return
        self.delete(save_boxes)
        self.create(self.boxes)
    #@decorator
    def move_down(self):
        save_boxes = self.boxes[:]
        self.position[-1] += 1
        
        self.boxes = (np.array(self.local_boxes)+self.position).astype(int)
        if self.evaluate(self.boxes):
            self.position[-1]-=1
            self.boxes = save_boxes
            new_shape()
            return 1
        self.delete(save_boxes)
        self.create(self.boxes)

    def move_right(self):
        save_boxes = self.boxes[:]
        self.position[0] += 1
        
        self.boxes = (np.array(self.local_boxes)+self.position).astype(int)
        if self.evaluate(self.boxes):
            self.position[0]-=1
            self.boxes = save_boxes
            return
        self.delete(save_boxes)
        self.create(self.boxes)

    def move_left(self):
        save_boxes = self.boxes[:]
        self.position[0] -= 1
        
        self.boxes = (np.array(self.local_boxes)+self.position).astype(int)
        if self.evaluate(self.boxes):
            self.position[0]+=1
            self.boxes = save_boxes
            return
        self.delete(save_boxes)
        self.create(self.boxes)
    def auto_move_down(self):
        self.delete
        print(self.boxes)
        while not self.evaluate(self.boxes):
            self.move_down()
# själva blocken
class I_block(shape):
    local_boxes = [[-1,0], [0,0], [1,0], [2,0]]
    color = "aqua"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "I"


class J_block(shape):
    local_boxes = [[-1,-1], [-1,0], [0,0], [1,0]]
    color = "blue"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "J"

class L_block(shape):
    local_boxes = [[-1,0], [0,0], [1,0], [1,-1]]
    color = "orange"
    def __init__(self, position):
        shape.__init__(self,position, self.color)
    def __repr__(self):
        return "L"


class O_block(shape):
    local_boxes = [[0,0], [1,0], [0,1], [1,1]]
    color = "yellow"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "O"
    
class S_block(shape):
    local_boxes = [[-1,0], [0,0], [0,-1], [1,-1]]
    color = "lime"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "S"
    
class T_block(shape):
    local_boxes = [[-1,0], [0,0], [0,-1], [1,0]]
    color = "#A020F0"
    def __init__(self, position):
        shape.__init__(self,  position, self.color)
    def __repr__(self):
        return "T"

class Z_block(shape):
    local_boxes = [[-1,-1], [0,-1], [0,0], [1,0]]
    color = "red"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "Z"


box_arr = np.resize(np.arange(0, 10*20), (20,10))+1 # ska användas för att genom xy positioner i index få ut boxen att ändra
# ger en xy grid med 0,0 till 10, 20 till höger nedåt
for i in range(20):
    for i2 in range(10):
        box_id = canvas.create_rectangle(i2*box_geometry, i*box_geometry, i2*box_geometry+box_geometry, i*box_geometry+box_geometry, fill="light gray", outline="green")



run_v: bool = True
all_shapes = ["I_block", "J_block", "L_block", "O_block", "S_block", "T_block", "Z_block"]
upcoming_shapes = np.vectorize(lambda el: all_shapes[el])(np.random.randint(6, size=3))
old_shapes = []
shape_c = None


def new_shape():
    global upcoming_shapes, shape_c, old_shapes
    if shape_c != None:
        old_shapes.append(shape_c.boxes.astype(int))

        
    
    current_shape = eval(upcoming_shapes[0])
    #current_shape = eval(all_shapes[0]) #* remove after dev:ing
    upcoming_shapes = np.delete(upcoming_shapes, 0)
    upcoming_shapes = np.append(upcoming_shapes, all_shapes[randint(0,6)])

    x = (np.array(current_shape.local_boxes)[:,0]) 
    y = (np.array(current_shape.local_boxes)[:,1])
    #print(current_shape.local_boxes)
    width = (np.amax(x)-np.amin(x)+1)
    y_offset = np.abs(np.amin(y)) # om 0,0 kordinaten är högst upp blir den 0 annars 1 om på andra lagret
    x_offset = np.abs(np.amin(x)) # samma fast för x axeln
    # print(x_offset, y_offset)
    # print(width)
    # print(current_shape)
    random_position = (randint(0, 9-width))
    #random_position = 4 #* remove after dev:ing
    position = [random_position+x_offset, y_offset]
    #print(position)
    shape_c = current_shape(position)
    
def check_rows():
    pass # old_shapes

def right_packer(event):
    shape_c.move_right()
def left_packer(event):
    shape_c.move_left()
def up_packer(event):
    shape_c.rotate()
def down_packer(event):
    shape_c.move_down()
def space_packer(event):
    shape_c.auto_move_down()
    time.sleep(1)
def get_input():
    window.bind("<Right>", right_packer)   
    window.bind("<Left>", left_packer)      
    window.bind("<Up>", up_packer)
    window.bind("<Down>", down_packer)
    window.bind("<space>", space_packer)


def fall_func():
    while True:
        time.sleep(2)
        shape_c.move_down()
    

def run():
    new_shape()
    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    fall_thread = threading.Thread(target=fall_func)
    fall_thread.start()


    
    


run()
window.mainloop()