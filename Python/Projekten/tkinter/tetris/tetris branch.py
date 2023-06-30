import tkinter as tk
import numpy as np
from sgl import newcoord
import time
from random import randint
import threading

#todo
#! bug fritt
# fixa senare en outline till blocken
# en outline längst ned där blocket kommer hamna eller en grå väg ned
# en titel screen med rekord
# se på sidan kommande block, kanske en hold funktion
# paus knapp kanske
# att den avslutas när man kommer högst upp
# hastighetssystem

window = tk.Tk()
box_geometry: int = 20 # ger ut storleken av varje box

window.geometry(f"{10*box_geometry}x{20*box_geometry}")
#window_size = 10
block_area = tk.Canvas(window, width=10*box_geometry, height=10*2*box_geometry)
block_area.pack()
# 10 i bas, 20 i höjd


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


class shape:
    local_boxes: list   
    def __init__(self, position, color): 
        self.color = color
        self.position = position # denna är positionen och visar var på mappen den finns
        self.boxes = np.array(self.local_boxes)+position
        self.create(self.boxes)
        self.s_local_boxes = self.local_boxes[:] # lokal variant för just detta blocket av local boxes
        self.last_boxes_td: np.ndarray

    def down_display(self): #! kan förenklas med bara de raderna och sedan lägg på blocket istället för att ta bort block positionen
        print("\n\n")
        #window.update() # remove after deving
        boxes_to_display = np.array(box_arr[:])
        min = np.min(self.boxes[:,0])
        max = np.max(self.boxes[:,0])+1
        boxes_to_display = (boxes_to_display[:, min:max])
        # raderar över och själva self.boxes
        for i in np.unique(self.boxes[:,0]):
            max_y_value = (np.max(self.boxes[np.where(self.boxes[:,0]==i)][:,1]))
            positional_value_boxes = box_arr[max_y_value][i] # ordnar så den blir av samma typ som boxes_to_display
            positional_values = box_arr[np.where(box_arr[:,i]<=positional_value_boxes),i][0] # tar fram värderna över boxen eller boxen själv
            for obj in positional_values:
                boxes_to_display = np.where(boxes_to_display == obj, None, boxes_to_display)


        # för old_shapes och under
        if not np.array_equal(old_shapes, np.array([0,0])):
            pass
            window.update()
            arr = old_shapes[:, 0]
            l_old_shapes = old_shapes[(arr > min-1) & (arr < max)]
            


            for i,el in enumerate(np.unique(self.boxes[:,0])):
                max_y_value = (np.max(self.boxes[np.where(self.boxes[:,0]==el)][:,1]))
                #print(max_y_value)
                positional_value_boxes = box_arr[max_y_value][el] # ordnar så den blir av samma typ som boxes_to_display
                positional_values = box_arr[box_arr[:,el]<=positional_value_boxes,el][0] # tar fram värderna över boxen
                
                
                # old_shapes deleteing above
                l_os_for_row = l_old_shapes[l_old_shapes[:,0]==el] # narrowed down for only this row
                l_os_for_row = l_os_for_row[:, 0] + l_os_for_row[:, 1] * 10   # fix to boxes_to_display format
                l_os_for_row = np.delete(l_os_for_row, [np.where(l_os_for_row<positional_value_boxes)])
                
                # below deletion
                try:
                    old_min_y_val = (np.min(l_os_for_row))

                    boxes_td_in_column = (boxes_to_display[:, i][boxes_to_display[:, i] != None])
                    b_to_del = (boxes_td_in_column[boxes_td_in_column>=old_min_y_val])
                    for obj in b_to_del:
                        boxes_to_display = np.where(boxes_to_display == obj, None, boxes_to_display)
                except ValueError:
                    pass

        # deletion
        for i in self.last_boxes_td: #! fixa problemet med att old_shapes försvinner, annars typ klart :D
               block_area.itemconfig(i, fill="#262626", outline = "#4f4f4f")
        
        
        # creation
        boxes_to_display = np.reshape(boxes_to_display, (1, -1))
        boxes_to_display = boxes_to_display[boxes_to_display!=None]
        for i in boxes_to_display:
            block_area.itemconfig(i, fill="#262626", outline = "#4f4f4f") 
        self.last_boxes_td = boxes_to_display

                


                


            

    def delete(self, boxes):
        for i, el in enumerate(boxes):
            #el = np.vectorize(lambda el1: int(el1))(el)
            positions_on_grid = (box_arr[el[1]][el[0]])
            try:
                block_area.itemconfig(positions_on_grid, fill="#262626", outline = "#4f4f4f")
            except RuntimeError:
                exit()

    def create(self, boxes):
        for i, el in enumerate(boxes):
            #el = np.vectorize(lambda el1: int(el1))(el)
            positions_on_grid = box_arr[int(el[1])][int(el[0])]
            block_area.itemconfig(positions_on_grid, fill=self.color, outline=lighten(self.color))


    def evaluate(self, boxes): # testar om den är utanför några gränser
        v = 0
        for i, el in enumerate(old_shapes): #! säger att den befinner sig på [4,18] när den egentligne är på [0,18]
            for i2, el2 in enumerate(boxes):
                if np.array_equal(el, el2):
                    v = 1
                    break

        if (np.any(boxes[:,1]<0)): # [:,1]
            print("outside of higher border")
            return 1
        elif (np.any(boxes[:,0]>=10) or np.any(boxes[:,0]<0)):
            print("outside of right or left border")
            return 1
        elif np.any(boxes[:,1]>=20):
            print("outside of lower border")
            return 1
        elif v:
            #print("\n",el, boxes, "\n", old_shapes) # >12
            #print("inside of another box")
            return 2
        return 0


    def rotate(self):
        if str(self) == "O":
            print("O, so no rotation")
            return

        save_local_boxes = self.s_local_boxes[:]
        save_boxes = self.boxes[:]
        for i, el in enumerate(self.s_local_boxes):
            if el!= [0,0]:
                self.s_local_boxes[i] = newcoord.rotate_from_origo(el, 90)
            else: 
                self.s_local_boxes[i] = [0,0]
        self.s_local_boxes = np.round(self.s_local_boxes).tolist()

        self.boxes = (np.array(self.s_local_boxes)+self.position).astype(int)

        evaluation = self.evaluate(self.boxes)
        if evaluation:
            if evaluation == 2:
                for i in shape_c.boxes:
                    i[1]-=1
            self.boxes = save_boxes 
            self.s_local_boxes = save_local_boxes
            print("unable")
            return
        self.delete(save_boxes)
        self.down_display()
        self.create(self.boxes)
    
    
    def move_down(self, from_auto=False):
        save_boxes = self.boxes[:]
        self.position[-1] += 1
        
        self.boxes = (np.array(self.s_local_boxes)+self.position).astype(int)
        if self.evaluate(self.boxes):
            self.position[-1]-=1
            self.boxes = save_boxes
            shape_c = self
            new_shape()
            return 2
        self.delete(save_boxes)
        self.create(self.boxes) #! också error när den åker nedåt DX
        #! kan prob fixas genom att köra någon extra down_display och deletea allt först, alternativt bara skilla down_display
        if not from_auto: #! för att se till att den inte behöver animera varje steg lade jag till denna, orsakar dock error att det blir mörkt på blocksen och ändå tar tid
            
            self.down_display()
            


    def move_right(self):
        save_boxes = self.boxes[:]
        self.position[0] += 1
        
        self.boxes = (np.array(self.s_local_boxes)+self.position).astype(int)
        if self.evaluate(self.boxes):
            self.position[0]-=1
            self.boxes = save_boxes
            return
        self.delete(save_boxes)
        self.create(self.boxes)

        self.down_display()


    def move_left(self):
        save_boxes = self.boxes[:]
        self.position[0] -= 1
        
        self.boxes = (np.array(self.s_local_boxes)+self.position).astype(int)
        if self.evaluate(self.boxes):
            self.position[0]+=1
            self.boxes = save_boxes
            return
        self.delete(save_boxes)
        self.create(self.boxes)

        self.down_display()



    def auto_move_down(self):
        print(self)
        #self.delete()
        while not self.evaluate(self.boxes): #* verkar som om shape_c och boxen inte är bundna av någon anledning, leta i roten
            #time.sleep(0.005) #* fix after deving
            if self.move_down(1) == 2:
                return
            window.update_idletasks()
# själva blocken
class I_block(shape):
    local_boxes = [[-1,0], [0,0], [1,0], [2,0]]
    color = "#00ffff"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "I"

class J_block(shape):
    local_boxes = [[-1,-1], [-1,0], [0,0], [1,0]]
    color = "#0000ff"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "J"

class L_block(shape):
    local_boxes = [[-1,0], [0,0], [1,0], [1,-1]]
    color = "#ff7f00"
    def __init__(self, position):
        shape.__init__(self,position, self.color)
    def __repr__(self):
        return "L"

class O_block(shape):
    local_boxes = [[0,0], [1,0], [0,1], [1,1]]
    color = "#ffff00"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "O"
    
class S_block(shape):
    local_boxes = [[-1,0], [0,0], [0,-1], [1,-1]]
    color = "#00ff00"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "S"
    
class T_block(shape):
    local_boxes = [[-1,0], [0,0], [0,-1], [1,0]]
    color = "#800080"
    def __init__(self, position):
        shape.__init__(self,  position, self.color)
    def __repr__(self):
        return "T"

class Z_block(shape):
    local_boxes = [[-1,-1], [0,-1], [0,0], [1,0]]
    color = "#ff0000"
    def __init__(self, position):
        shape.__init__(self, position, self.color)
    def __repr__(self):
        return "Z"


box_arr = np.resize(np.arange(0, 10*20), (20,10))+1 # ska användas för att genom xy positioner i index få ut boxen att ändra
# ger en xy grid med 0,0 till 10, 20 till höger nedåt
for i in range(20):
    for i2 in range(10): # gör upp gridden av x och y block
        box_id = block_area.create_rectangle(i2*box_geometry, i*box_geometry, i2*box_geometry+box_geometry, i*box_geometry+box_geometry, fill="#262626", outline="#4f4f4f")


run_v: bool = True
all_shapes = ["I_block", "J_block", "L_block", "O_block", "S_block", "T_block", "Z_block"]
upcoming_shapes = np.vectorize(lambda el: all_shapes[el])(np.random.randint(6, size=3))
old_shapes = np.zeros(2)
shape_c = None

def get_color_f(values):
    arr = []
    #print(len(values))
    for i,el in enumerate(values):
        positions_on_grid = (box_arr[el[1]][el[0]])
        color = block_area.itemcget(positions_on_grid, "fill")
        arr.append(color)
    return np.array(arr)   

def delete_f(boxes):
    for i, el in enumerate(boxes):
            #el = np.vectorize(lambda el1: int(el1))(el)
            positions_on_grid = (box_arr[el[1]][el[0]])
            block_area.itemconfig(positions_on_grid, fill="#262626", outline = "#4f4f4f")
def create_f(boxes, color_arr):
    for i, el in enumerate(boxes):
        positions_on_grid = box_arr[int(el[1])][int(el[0])]
        block_area.itemconfig(positions_on_grid, fill=color_arr[i], outline = lighten(color_arr[i]))
        block_area.itemconfig(positions_on_grid, outline = lighten(color_arr[i]))

def check_rows(): #! ett error är när denna dubbelaktiveras eftersom flera rader raderas
    global old_shapes
    #window.update()
    if np.any(old_shapes != np.zeros(2)):
        indexes = (np.unique(old_shapes[:,1])) # tar fram alla rader med block för att testa om det finns rad på de
        for i in indexes:
            if np.array_equal(np.sort((old_shapes[np.where(old_shapes[:,1] == i)[0]])[:,0]), np.arange(10)): # testar om det är en full rad
                #window.update()
                save_old_shapes = old_shapes[:]
                #print("row")
                #print(values)
                #print(old_shapes,"\n",values, "\n\n\n")
                indexes2 = np.where(old_shapes[:,1]==i)[0]
                old_shapes = np.delete(old_shapes, indexes2, axis=0)
                #print(old_shapes)
                color_arr = get_color_f(old_shapes)
                delete_f(save_old_shapes)
                print(f"len: {i}")

                #print(old_shapes, "\n\n")
                rows = old_shapes[:, 1]<i
                old_shapes[rows, 1]+=1
                #old_shapes[:,1]+=1 # den kan helt enkelt inte flytta ned utan man måste hitta alla över den nivån och flytta ned dem
                create_f(old_shapes, color_arr)
                



test = True
def new_shape():
    global upcoming_shapes, shape_c, old_shapes, test
    if shape_c != None:

        save_last_boxes_td = shape_c.last_boxes_td
        

        print(shape_c.boxes)
        if np.any(shape_c.boxes[:,1]==0): #* attempt to fix
            return # old shapes empty bc of all used
        old_shapes = np.vstack((old_shapes, shape_c.boxes)).astype(int)
        if test:
            old_shapes = old_shapes[1:]
            test = False
    else:
        save_last_boxes_td = np.array([[0,0]])

    

    
    current_shape = eval(upcoming_shapes[0])
    current_shape = eval(all_shapes[0]) #* remove after dev:ing
    upcoming_shapes = np.delete(upcoming_shapes, 0)
    upcoming_shapes = np.append(upcoming_shapes, all_shapes[randint(0,6)])

    x = (np.array(current_shape.local_boxes)[:,0]) 
    y = (np.array(current_shape.local_boxes)[:,1])

    width = (np.amax(x)-np.amin(x)+1)
    y_offset = np.abs(np.amin(y)) # om 0,0 kordinaten är högst upp blir den 0 annars 1 om på andra lagret
    x_offset = np.abs(np.amin(x)) # samma fast för x axeln

    random_position = (randint(0, 10-width))
    random_position = 1 #* remove after dev:ing
    position = [random_position+x_offset, y_offset]

    shape_c = current_shape(position)
    shape_c.last_boxes_td = save_last_boxes_td
    shape_c.down_display()

    check_rows() 

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
    time.sleep(0.5)
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
    global old_shape
    new_shape()
    # shape_c.auto_move_down()

    # shape_c.move_down()
    # shape_c.move_down()
    # shape_c.move_left()


    shape_c.auto_move_down()

    shape_c.auto_move_down()
    shape_c.move_down()
    shape_c.rotate()
    shape_c.move_left()
    shape_c.auto_move_down()
    shape_c.move_down()
    shape_c.rotate()
    shape_c.move_left()
    shape_c.auto_move_down()
    
    shape_c.move_down()
    shape_c.rotate()
    shape_c.move_left()
    shape_c.auto_move_down()
    shape_c.auto_move_down()
    shape_c.auto_move_down()
    shape_c.move_down()

    for i in range(4):
        shape_c.move_right()
    for i in range(6):
        shape_c.move_down()

    shape_c.move_left()
    shape_c.move_left()
    shape_c.down_display()

    

    # input_thread = threading.Thread(target=get_input)
    # input_thread.start()
    # fall_thread = threading.Thread(target=fall_func)
    # fall_thread.start()


    """
    shape_c.auto_move_down()
    window.update()
    shape_c.move_down()
    shape_c.move_right()
    shape_c.move_left()
    shape_c.rotate()
    """

    

    
    


run()
window.mainloop()