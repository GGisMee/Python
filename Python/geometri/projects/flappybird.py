from tkinter import *
from tkinter import Grid
import numpy as np
import time

window = Tk()
width = 700
height = width/1.5

canvas = Canvas(window, height=height, width=width, bg="lightgray")
canvas.pack()

class bird():
    def place(x,y, self, where):
        for i in self.bodyparts:
            if i[1][1] == "oval":
                obj = canvas.create_oval(i[0][0]+x, i[0][1]+y, i[0][2]+x, i[0][3]+y, fill=i[1][0])
            if i[1][1] == "line":
                obj = canvas.create_line(i[0][0]+x, i[0][1]+y, i[0][2]+x, i[0][3]+y, fill=i[1][0])
            if where == "self":
                self.objlist.append(obj)
        print(self.objlist)    
    def __init__(self,x,y):
        self.objlist = []
        self.body = [[0,0,30,30], ["yellow", "oval"]]
        self.head = [[7.5,18, 34.5,-10.5], ["yellow", "oval"]]
        self.beak = [[24,6, 42,4.5], ["orange", "oval"]]
        self.eye = [[22.5,-4.5, 27,0], ["blue", "oval"]]
        self.leg1 = [[22.5,22.5,24,33], ["black", "line"]]
        self.leg2 = [[9,22.5,6,34.5], ["black", "line"]]
        self.bodyparts = [self.body, self.head, self.beak, self.eye, self.leg1, self.leg2]
        
        self.x = x
        self.y = y
        
        bird.place(x=self.x,y=self.y, self=self, where="self")
    def gravity(self):
        self.x -= 2
        self.y -= 2
        bird.place(x=self.x,y=self.y, self=self, where="gravity")

birdvar = bird(100,100)
window.update()

time.sleep(4)
while True:
    birdvar.gravity()
    time.sleep(5)
    window.update()


window.mainloop()