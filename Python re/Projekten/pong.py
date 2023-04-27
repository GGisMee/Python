from tkinter import *; 
from time import *; 
from math import *; 
from random import *
import threading
import os
os.system('xset r off')
window = Tk()
window.geometry("800x800")
status = False
direction = None
class ballC:
    def __init__(self, speed):
        self.posy = 300
        # early config
        self.dirx = 100
        self.diry = 300
        self.direction = 120
        self.speed = speed
        self.obj = canvas.create_oval(0,0, 15, 15, fill="black")
        
def get_input():  
    def on_key_press(event):
        global direction
        if event.keysym == 'w':
            direction = "up"
        elif event.keysym == 's':
            direction = 'down'
        elif event.keysym == "space":
            direction = None
    window.bind('<KeyPress>', on_key_press)


def started(status):
    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    tic_per_second = 1/60
    speedai = 8
    speedplayer = 5
    try:
        speed = int(speedEnt.get())*10
    except ValueError:
        speed = 500
    speed  = speed*tic_per_second

    global ball, direction
    ball = ballC(speed)
    ball_iterations = 0
    no = 0
    noplayer =0
    minus_speed = False
    plus_speed = False
    canvas.move(ball.obj, ball.dirx, ball.diry)
    while status == True:
        window.update()
        def dir():
            # print(ball.direction)
            pass
        # status = False
        def runaichange(board ,no, ball_iterations, minus_speed, plus_speed):
            if len(list(canvas.find_overlapping(board_ai.x1, board_ai.y1, board_ai.x2, board_ai.y2))) > 1 and board_ai.y2 < 600 and board_ai.y1 > 5:
                print("r")
                if 0 < no:
                    return no, ball_iterations         

                if ball_iterations < 2:
                    no = 100

                ball.direction = abs((270-ball.direction)+90)
                dir()

                ball_iterations += 1
                return no, ball_iterations
            else:
                ball_iterations = 0
                no = 0
                return no, ball_iterations


        Vx = ball.speed*round(sin(radians(ball.direction)),2)
        Vy = ball.speed*round(cos(radians(ball.direction)),2)
        canvas.move(ball.obj, Vx, Vy)
        ball.posy += Vy

        # övre
        if len(list(canvas.find_overlapping(0,1, 600, 1))) >= 3:
            if not ball.direction >180:
                ball.direction = (180-ball.direction)
            else:
                ball.direction = (90+ball.direction)
            dir()
            
        # undre
        if len(list(canvas.find_overlapping(600,600, 0, 600))) > 3:   
            if ball.direction >270:
                ball.direction = ((270-ball.direction))
            else:
                ball.direction = (90+ball.direction)

            dir()

        # r and l 
        if (len(list(canvas.find_overlapping(600,600, 600, 0)))) > 3:
            if ball.direction >90:
                ball.direction+= 90
            else:
                ball.direction-=90
            dir()
        if(len(list(canvas.find_overlapping(3,0, 3, 600)))) > 3:
            ball.direction -= 180
            dir()
        
        # if ai touches ball...
        no, ball_iterations = runaichange(board_ai, no, ball_iterations, minus_speed, plus_speed)
        noplayer, ball_iterations = runaichange(board_ai, noplayer, ball_iterations, minus_speed, plus_speed)


        # movement ai
        if (board_ai.y2-board_ai.y1)/2+board_ai.y1 > ball.posy:
            if (board_ai.y1) > 10:
                board_ai.move(0, -speedai)
                minus_speed = True
                plus_speed = False

        if (board_ai.y2-board_ai.y1)/2+board_ai.y1 < ball.posy:
            if board_ai.y2 < 597:
                board_ai.move(0, speedai)
                plus_speed = True
                minus_speed = False
        
        if direction == "down":
            if board_player.y2 < 595:
                board_player.move(0, speedplayer)
            
        if direction == "up":
            if (board_player.y1) > 5:
                board_player.move(0, -speedplayer)



        ball.direction = abs(ball.direction)
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
        self.obj = canvas.create_rectangle(x1,y1, x2, y2, fill="black")
    def move(self, mx, my):
        self.x1 += mx
        self.x2 += mx
        self.y1 += my
        self.y2 += my
        canvas.move(self.obj, mx, my)


board_ai = board(0,0, 10, 50)
board_ai.move(10, 275)

board_player = board(0,0, 10,100)
board_player.move(580, 275)



canvas.pack()
window.mainloop()

