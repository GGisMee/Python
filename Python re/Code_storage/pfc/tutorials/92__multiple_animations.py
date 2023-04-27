# 92__multiple_animations

# 91__animations
from tkinter import *
import time

window = Tk()
WIDTH = 500
HEIGHT = 500
window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

class Ball:
    def __init__(self, name, wh, color, xVelocity, yVelocity):
        self.color = color
        self.wh = wh
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.name = name
        self.name = canvas.create_oval(0,0, self.wh, self.wh, fill=self.color)
    def oncorner(self):
        self.coordinates = canvas.coords(self.name)
        if self.coordinates[0] >= WIDTH-self.wh or not self.coordinates[0] >= 0: # x axeln
            self.xVelocity = -self.xVelocity
        if self.coordinates[1] >= HEIGHT-self.wh or not self.coordinates[1] >= 0: # x axeln
            self.yVelocity = -self.yVelocity
        canvas.move(self.name, self.xVelocity, self.yVelocity)

grayball = Ball("grayball", 20, "gray", 3,2)
blueball = Ball("blueball", 50, "blue", 2,3)
redball = Ball("redball", 10, "red", 5,6)
purpleball = Ball("purpleball", 70, "purple", 2, 1)

while True:
    
    
    grayball.oncorner()
    blueball.oncorner()
    redball.oncorner()
    purpleball.oncorner()
    
    window.update()
    time.sleep(0.01)

window.mainloop()  
