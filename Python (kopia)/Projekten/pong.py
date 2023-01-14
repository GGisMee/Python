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
        self.posx = 100
        self.posy = 300
        self.direction = 0
        self.speed = speed
        

def started(status):

    try:
        speed = int(speedEnt.get())
    except ValueError:
        speed = 1

    global ballinfo
    ballinfo = ballC(speed)


    canvas.move(ball, ballinfo.posx, ballinfo.posy)
    while status == True:
        

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
ballinfo = "1"

canvas.pack()
window.mainloop()

