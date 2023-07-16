from tkinter import *; 
from time import *; 
from math import *; 
from random import *
import threading

geometry = 400
size_sub = 10
startVar = False
apple_sub = 3
direction = "rigth"
speed_sub = 0.5
on = 0
def start():
    continuation("runscr")
    

win_start_geo = 600
# print("write row/column below")
# inp = round(float(input()))
# print(inp)



b = 0
def betweening(row, column):
    global b
    b+=1
    name = f"b{b}"
    name = Frame(inp_frame, height=20, width=1.5, bg="gray")
    name.grid(row=row, column=column)

    
# window and placements
def config():
    global apple_sub, geometry, size_sub, speed_sub
    if "" != entry_px.get():
        if int(entry_px.get()) >= 10:
            print("too large")
            print(f"{int(entry_px.get())} >= 7")
            return
        geometry = int(entry_px.get())*100
    if "" != entry_apple.get():
        if apple_sub == 0:
            print("too small")
            apple_sub = 3
            return
        apple_sub = int(entry_apple.get())

    if "" != entry_size.get():
        size_sub = int(entry_size.get())

    if "" != entry_speed.get():
        if speed_sub == 0 or speed_sub > 10:
            print("too large or too small")
            speed_sub = 1
            return
        speed_sub = float(entry_speed.get())
    
    continuation("false")

window = Tk()

window.geometry(str(win_start_geo)+"x"+str(win_start_geo))

launch_frame = Frame(window)
launch_frame.pack()

inp_frame = Frame(window)
inp_frame.pack()
label_px = Label(inp_frame, text="px", font=("Arial", 25))
label_px.grid(row=0, column=0)
betweening(0, 1)
label_apples = Label(inp_frame, text="apples", font=("Arial", 25))
label_apples.grid(row=0, column=2)
betweening(0, 3)
label_size = Label(inp_frame, text="size", font=("Arial", 25))
label_size.grid(row=0, column=4)
betweening(0, 5)
label_speed = Label(inp_frame, text="speed", font=("Arial", 25))
label_speed.grid(row=0, column=6)


entry_px = Entry(inp_frame, width=4)
entry_px.grid(row=1, column=0)
betweening(1, 1)
entry_apple = Entry(inp_frame, width=7)
entry_apple.grid(row=1, column=2)
betweening(1, 3)
entry_size = Entry(inp_frame, width=4)
entry_size.grid(row=1, column=4)
betweening(1, 5)
entry_speed = Entry(inp_frame, width=6)
entry_speed.grid(row=1, column=6)

submit_btn = Button(inp_frame, command=config, text="Play", width=10)
submit_btn.grid(row=2, columnspan=8, column=0)

def continuation(runscr):
    global geometry, apple_sub, size_sub, direction
    if runscr == runscr: 
        print("runscr")   
        global startVar, on
        if on != 0:
            startVar = True
        else:
            on+=1

    canvas = Canvas(window, width=geometry, height=geometry, bg="#afafaf")
    canvas.place(anchor=CENTER, x=win_start_geo/2, y = win_start_geo/2)

    # pixel_generator
    def roundfunc(i, bool):
            i = int(i)
            if round(i/2)-i/2 != 0:
                return bool
            else:
                return not bool


    size = geometry/size_sub
    bggrid = []

    class color:
        def __init__(self, color):
            self.color = color

    for y in range(size_sub):
        loclist = []
        bggrid.append(loclist)

        for x in range(size_sub):
            loclist.append([str(y)+"_"+str(x), "bgrec"])
            bggrid[y][x][1] = canvas.create_rectangle(0,0, size, size, fill="#afafaf", outline="black", width=2)
            bggrid[y][x][0] = color("#afafaf")

            posy = y*size
            posx = x*size
            canvas.move(bggrid[y][x][1], posx, posy)

            if roundfunc(size_sub, False): # false för om det är 0
                    if roundfunc(y, False):
                        if roundfunc(bggrid[y][x][1], True): # true för om det inte är 0
                            canvas.itemconfig(bggrid[y][x][1], fill="#fafafa")
                            bggrid[y][x][0] = color("#fafafa")

                    elif roundfunc(y, True):
                        if roundfunc(bggrid[y][x][1], False): # true för om det inte är 0
                            canvas.itemconfig(bggrid[y][x][1], fill="#fafafa")
                            bggrid[y][x][0] = color("#fafafa")
            if roundfunc(size_sub, True) and roundfunc(bggrid[y][x][1], True):
                # true för om det inte är 0
                canvas.itemconfig(bggrid[y][x][1], fill="#fafafa")
                bggrid[y][x][0] = color("#fafafa")



    class snake_part:
        def __init__(self, posx, posy, ID):
             self.posx = posx
             self.posy = posy
             self.ID = ID

        def for_start(self, x):
            self.posx = x
            self.posy = floor((size_sub)/2)


    class apple_part: 
        def __init__(self, posx, posy):
            self.posx = posx
            self.posy = posy
# run scr   

    # functions
    def reps(times):
        for i in range(times):
            spawn(listofsnake)
    def spawn(listofsnake):
        shownlist = []
        for i in listofsnake:
            posx_a = randint(0, size_sub-1)
            posy_a = randint(0, size_sub-1)
            shownlist.append([i.posx, i.posy])
        if [posx_a, posy_a] in shownlist:
            spawn(listofsnake)
            return
        print()
        print()
        print([posx_a, posy_a])
        print(shownlist)
        temp_list = [posx_a, posy_a]
        apples_list.append(temp_list)
        canvas.itemconfig(bggrid[posy_a][posx_a][1], fill="#9c1414")
    def snake_pos():
        for  i in listofsnake:
            if i == head:
                canvas.itemconfig(bggrid[i.posy][i.posx][1], fill="red")
            else:
                canvas.itemconfig(bggrid[i.posy][i.posx][1], fill="green")  
    def get_input():
        def rightfunc(event):
            global direction, this_dir
            if direction != "left":
                direction = "right"
                
            upd()
        def leftfunc(event):
            global direction, this_dir
            if direction != "right":
                direction = "left"
            upd()      
        def upfunc(event):
            global direction, this_dir
            if direction != "down":
                direction = "up"
            upd()
        def downfunc(event):
            global direction, this_dir
            if direction != "up":
                direction = "down"
            upd()
        def upd():
            pass
        window.bind("<Right>", rightfunc)   
        window.bind("<Left>", leftfunc)   
        window.bind("<Up>", upfunc)   
        window.bind("<Down>", downfunc)
    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    # early config
    listofsnake = []
    head = snake_part(None, None, 0)
    head.for_start(3)
    listofsnake.append(head)
    pID = 0
    for i in range(2):
        pID+=1
        listofsnake.append("p"+str(pID))
    listofsnake[1] = snake_part(2, 5, 1)
    listofsnake[1].for_start(2)
    listofsnake[2] = snake_part(1, 5, 2)
    listofsnake[2].for_start(1)
    snake_pos()
    direction = "right"
    apples = 3
    apple_eaten = False
    if startVar == True:
        apples_list = []
        reps(apple_sub)
    # game tick
    while startVar == True:
        def end():
            print("end")
            return False
        window.update()
        submit_btn.config(state=DISABLED)
        if [head.posx,head.posy] in apples_list:
            spawn(listofsnake)
            del apples_list[apples_list.index([head.posx, head.posy])]
            apple_eaten = True
        temp_previous_headpos = [head.posx, head.posy]
        if direction == "right":
            head.posx+=1
        elif direction == "left":
            head.posx-=1 
        elif direction == "up":
            head.posy-=1 
        elif direction == "down":
            head.posy+=1
        try:
            canvas.itemconfig(bggrid[head.posy][head.posx][1], fill="red")
        except IndexError:
            pass 
        
        pID+=1
        listofsnake.insert(1,"p"+str(pID))
        listofsnake[1] = snake_part(temp_previous_headpos[0], temp_previous_headpos[1], pID)
        canvas.itemconfig(bggrid[listofsnake[1].posy][listofsnake[1].posx][1], fill="green")
        bc = listofsnake[-1] # bakom kordinat
        if apple_eaten == False:   
            canvas.itemconfig(bggrid[listofsnake[-1].posy][listofsnake[-1].posx][1], fill=bggrid[listofsnake[-1].posy][listofsnake[-1].posx][0].color)
            del listofsnake[-1]
        else:
            apple_eaten = False
        window.update()
        x1 = head.posx == size_sub
        y1 = head.posy == size_sub
        x2 = head.posx == -1
        y2 = head.posy == -1
        if x1 or y1 or x2 or y2:
            startVar = False
            on = 0
            submit_btn.config(state=NORMAL)
        for i in listofsnake:
            if i != head and head.posx == i.posx and head.posy == i.posy:
                startVar = False
                on = 0
                submit_btn.config(state=NORMAL)
        sleep(speed_sub)
window.mainloop()