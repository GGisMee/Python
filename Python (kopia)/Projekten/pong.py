from tkinter import *; 
from time import *; 
from math import *; 
from random import *
import threading

window = Tk()
window.geometry("800x800")
status = False
class ballC:
    def __init__(self, speed):
        # early config
        self.dirx = 100
        self.diry = 300
        self.direction = 179
        self.speed = speed
        

def started(status):

    try:
        speed = int(speedEnt.get())
    except ValueError:
        speed = 1

    global ballinfo
    ballinfo = ballC(speed)


    canvas.move(ball, ballinfo.dirx, ballinfo.diry)
    while status == True:
        
        Vx = round(sin(radians(ballinfo.direction)),2)
        print(Vx, ballinfo.speed, ballinfo.direction)

        window.update()
        
        sleep(1)
def startfunc():
    global status
    status = True
    started(status)


startbtn = Button(window, text="start", command=startfunc, width=7, font=("Arial",25 ))
startbtn.pack()
speedlabel = Label(window, text="px/tick", width=5)
speedlabel.pack()
speedEnt = Entry(window, width=5)
speedEnt.pack()

canvas = Canvas(window, width=600, height=600, bg="#f0f0f0")

ball = canvas.create_oval(0,0, 15, 15, fill="black")
ballinfo = "ballinfo"

canvas.pack()
window.mainloop()

