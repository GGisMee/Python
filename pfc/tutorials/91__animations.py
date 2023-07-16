# 91__animations
from tkinter import *
import time

window = Tk()
WIDTH = 477
HEIGHT = 500
window.geometry(f"{WIDTH}x{HEIGHT}")
xVelocity = 3
yVelocity = 2  

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bgimg = PhotoImage(file="/Users/gustavgamstedt/Desktop/Hemma_folder/programmering/Python (kopia)/Code_storage/pfc/till_library/space.png")
background = canvas.create_image(0,0, image=bgimg, anchor=NW)


photoimage = PhotoImage(file="/Users/gustavgamstedt/Desktop/Hemma_folder/programmering/Python (kopia)/Code_storage/pfc/till_library/ufo.png")
ufo = canvas.create_image(0,0, image=photoimage, anchor=NW)

image_width = photoimage.width()
image_height = photoimage.height()


while True:
    coordinates = canvas.coords(ufo)
    print(coordinates)
    
    

    if coordinates[0] >= WIDTH-image_width or not coordinates[0] >= 0: # x axeln
        xVelocity = -xVelocity
    if coordinates[1] >= HEIGHT-image_height or not coordinates[1] >= 0: # x axeln
        yVelocity = -yVelocity
    canvas.move(ufo, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()  
