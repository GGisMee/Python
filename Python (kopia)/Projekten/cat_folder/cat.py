from tkinter import *
import time
import random
from PIL import Image, ImageTk

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
        self.x = HEIGHT
        self.y = random.randint(0+200, WIDTH-200)
        self.dirx = dirx
        self.diry = diry
        self.cat_nr = random.randint(1,3)
        self.og_catpic = Image.open("/Users/gustavgamstedt/Desktop/Hemma_folder/programmering/Python (kopia)/Projekten/cat_folder/cat1.png")
        self.edited_catpic=self.og_catpic.resize((100, 100))

        self.photo_image = ImageTk.PhotoImage(file=self.edited_catpic)
        self.obj = canvas.create_image(self.y, HEIGHT-100, image=self.photo_image)
        window.update_idletasks()
        # creation
        

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

window.mainloop()  
