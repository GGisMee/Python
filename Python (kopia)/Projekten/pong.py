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
        self.posy = 300
        # early config
        self.dirx = 100
        self.diry = 300
        self.direction = 10
        self.speed = speed
        self.obj = canvas.create_oval(0,0, 15, 15, fill="black")
        

def started(status):
    tic_per_second = 1/60
    try:
        speed = int(speedEnt.get())*10
    except ValueError:
        speed = 500
    speed  = speed*tic_per_second

    global ball
    ball = ballC(speed)
    iterations = 0
    no = 0
    canvas.move(ball.obj, ball.dirx, ball.diry)
    while status == True:
        # status = False
        def runaichange(no, iterations):
            if len(list(canvas.find_overlapping(board_ai_info.x1, board_ai_info.y1, board_ai_info.x2, board_ai_info.y2))) > 1:
                if 0 < no:
                    return no, iterations
                    
                
                if iterations < 2:
                    no = 100
            
                ball.direction += 180
                iterations += 1
                return no, iterations
            else:
                iterations = 0
                no = 0
                return no, iterations
                


        Vx = ball.speed*round(sin(radians(ball.direction)),2)
        Vy = ball.speed*round(cos(radians(ball.direction)),2)
        canvas.move(ball.obj, Vx, Vy)
        ball.posy += Vy

        if len(list(canvas.find_overlapping(0,3, 600, 3))) > 3 or len(list(canvas.find_overlapping(600,600, 0, 600))) > 3:
            ball.direction = 180-ball.direction
        if (len(list(canvas.find_overlapping(600,600, 600, 0))))  > 3 or (len(list(canvas.find_overlapping(3,0, 3, 600))))  > 3:
            ball.direction += 180
        no, iterations = runaichange(no, iterations)
        if (board_ai_info.y2-board_ai_info.y1)/2+board_ai_info.y1 > ball.posy:
            board_ai_info.move(0, -2)
        if (board_ai_info.y2-board_ai_info.y1)/2+board_ai_info.y1 < ball.posy:
            board_ai_info.move(0, 2)


        window.update()
        sleep(tic_per_second)

def startfunc():
    global status
    status = True
    started(status)


startbtn = Button(window, text="start", command=startfunc, width=7, font=("Arial",25 ))
startbtn.pack()

inp_frame = Frame(window)
inp_frame.pack()

speedlabel = Label(inp_frame, text="speed/sek", width=7)
speedlabel.grid(row=0, column=0)
speedEnt = Entry(inp_frame, width=7)
speedEnt.grid(row=1, column=0)


canvas = Canvas(window, width=600, height=600, bg="#f0f0f0")


border_upper = canvas.create_line(0,3, 600, 3, width=1, fill="black")
border_down = canvas.create_line(600,600, 0, 600, width=1, fill="black")

border_left = canvas.create_line(3,0, 3, 600, width=1, fill="yellow")
border_right = canvas.create_line(600,600, 600, 0, width=1, fill="yellow")

class board:
    def __init__(self, x1, y1, x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.obj = canvas.create_rectangle(0,0, 10, 50, fill="black")
    def move(self, mx, my):
        self.x1 += mx
        self.x2 += mx
        self.y1 += my
        self.y2 += my
        canvas.move(self.obj, mx, my)


board_ai_info = board(0,0, 10, 50)
board_ai_info.move(10, 275)



canvas.pack()
window.mainloop()

