from tkinter import *
import time
import random
from PIL import Image, ImageTk

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

window = Tk()
WIDTH = 1000
HEIGHT = 1000
window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
 
class cat:
    def __init__(self, obj,dirx, diry):
        global catpic
        # early config
        self.obj = obj
        self.x = random.randint(0, HEIGHT-100)
        self.y = WIDTH-(WIDTH/10)# random.randint(0+200, WIDTH-200)
        self.dirx = dirx
        self.diry = diry
        self.cat_nr = random.randint(1,5)
        self.og_catpic = Image.open(f"cat{self.cat_nr}.png")

        self.edited_catpic=self.og_catpic.resize((int(WIDTH/10), int(HEIGHT/10)))

        self.photo_image = ImageTk.PhotoImage(self.og_catpic)
        self.obj = canvas.create_image(self.x, self.y, image=self.photo_image)
        window.update_idletasks()
        # creation
        

    def move(self):
        self.x += self.dirx
        self.y += self.diry
        canvas.move(self.obj, self.dirx, self.diry)
        self.dirx -= 1
        self.diry -= 0.1

 
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
    


while True:
    
    
    time.sleep(2)
window.mainloop()  
