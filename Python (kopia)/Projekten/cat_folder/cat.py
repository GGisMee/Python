from tkinter import *
import time
import random
from PIL import Image, ImageTk
import threading

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

window = Tk()
WIDTH = 1000
HEIGHT = 1000
window.geometry(f"{WIDTH}x{HEIGHT}")

label = Label(text="0,0")
label.pack()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
 
class cat:
    def __init__(self, obj,dirx, diry):
        global catpic
        # early config
        self.obj = obj
        self.x1 = random.randint(0, WIDTH-100)
        self.y1 = HEIGHT-(HEIGHT/4)# random.randint(0+200, WIDTH-200)
        self.x2 = 0
        self.y2 = 0
        self.dirx = dirx
        self.diry = diry
        self.cat_nr = random.randint(1,5)
        self.og_catpic = Image.open(f"cat{self.cat_nr}.png")
        self.width = int(WIDTH/5)
        self.height = int(HEIGHT/5)
        self.edited_catpic=self.og_catpic.resize((self.width, self.height))

        self.photo_image = ImageTk.PhotoImage(self.edited_catpic)
        self.obj = canvas.create_image(self.x1, self.y1, image=self.photo_image, anchor=NW)
        window.update_idletasks()
        # creation

    def hold_check(self, event, movement_x, movement_y): # <>

        self.x2 = self.x1+self.width
        self.y2 = self.y1+self.height
        if self.x1 < event.x < self.x2 and self.y1 < event.y < self.y2:
            print(self.x1, self.y1, self.x2, self.y2)
            print(event.x, event.y)
            self.movefunc(movement_x, movement_y)

    def movefunc(self, movement_x, movement_y):
        canvas.move(self.obj, movement_x, movement_y)
        self.x1 += movement_x
        self.x2 += movement_x
        self.y1 += movement_y
        self.y2 += movement_y
        print(movement_x, movement_y, left_button_on)
        if left_button_on:
            window.after(20, self.movefunc, movement_x, movement_y)
                
        # canvas.move(self.obj, self.dirx, self.diry)
        # self.dirx -= 1
        # self.diry -= 0.1

 
def newcat():
    global cat_index, listofcat
    thiscat = cat("cat"+str(cat_index),0,0)
    listofcat.append(thiscat)
    cat_index += 1
    print(thiscat.cat_nr)

cat_index = 0
listofcat = []

for i in range(3):
    newcat()

x,y = -1, -1
left_button_on = False
def get_input():
    def spacefunc(event):
        print("spacefunc")
        newcat()

    def motion(event):
        global x,y, movement_x, movement_y
        if x == -1: 
            x = int(event.x)
            y = int(event.y)
            return (x,y)
        else:
            movement_x = int(event.x)-x
            movement_y = int(event.y)-y
            x = int(event.x)
            y = int(event.y)
    def l_release_func(event):
        global left_button_on
        left_button_on = False

    def lfunc(event):
        global left_button_on
        label.config(text=f"{event.x}, {event.y}")
        global left_button_on
        left_button_on = True
        for cat in listofcat:
            cat.hold_check(event, movement_x, movement_y)
    def clear(event):
        canvas.delete("all")
        listofcat.clear()
        

    window.bind("<space>", spacefunc)   
    window.bind("<Motion>", motion) # var man på nytt öppnar bilden
    window.bind("<Button-1>", lfunc)
    window.bind("<ButtonRelease-1>", l_release_func)
    window.bind("c", clear)



  
get_input()
window.mainloop()
while True:
    for cat in listofcat:
        cat.move()
    
    time.sleep(0.1)
    


