from tkinter import *
import time
import random

window = Tk()
WIDTH = 500
HEIGHT = 500
window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
 
class cat:
    def __init__(self, obj,dirx, diry):
        # early config
        self.obj = obj
        self.x = HEIGHT
        self.y = random.randint(0, 500)
        self.dirx = dirx
        self.diry = diry
        self.catpic = f"cat folder/cat{random.randint(1,4)}.png"

        photo_image = PhotoImage(file=self.catpic)

        # creation
        self.obj = canvas.create_image(0,0, image=photo_image, anchor=NW)
    def move(self):
        self.x += self.dirx
        self.y += self.diry
        canvas.move(self.obj, self.dirx, self.diry)
        self.dirx -= 1
        self.diry -= 0.1

cat_index = 0
listofcat = []

listofcat.append("cat"+str(cat_index))
thiscat = "cat"+str(cat_index)
thiscat = cat(thiscat,0,0)
print(thiscat.obj)

window.mainloop()  
