from tkinter import *; 
from time import *; 
from math import *; 
from random import *
import threading

window = Tk()
window.geometry("1000x1000")

screen = Canvas(window, width=900, height=900, bg="gray")
screen.place(relx=0.5, rely = 0.5, anchor=CENTER)
screen.create_rectangle(0,0,50, 50, fill="white", width=3, outline="black")
id = 0
class cordinate:
    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.obj = "obj"


class xyz_formater(cordinate):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        try:
            self.x  = sqrt((self.x**2)-(self.z**2))
        except ValueError:
            self.x = 0
        try:
            self.y  = sqrt((self.y**2)-(self.z**2))
        except ValueError:
            self.y = 0
        
        print(self.x, self.y, self.z, self.id)
        self.obj = screen.create_line(0, 0, self.x, self.y)

        screen.move(self.obj, 25, 25)
        xyz_formater_li.append(self)
xyz_formater_li = []
line_x = xyz_formater(10, 0, 2)
line_y = xyz_formater(0, 10, 0)



window.mainloop()