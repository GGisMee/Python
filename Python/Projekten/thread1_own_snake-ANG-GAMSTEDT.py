from tkinter import *; 
from time import *; 
from math import *; 
from random import *
import threading
startVar = False
on = 0
def start():
    global startVar, on
    if on != 0:
        startVar = True
    else:
        on+=1
    runscr()

win_start_geo = 800
# print("write row/column below")
# inp = round(float(input()))
# print(inp)

inp = 10
geometry = 800*0.5

if geometry > win_start_geo:
    print("too large")
    exit()

window = Tk()

window.geometry(str(win_start_geo)+"x"+str(win_start_geo))

startbtn = Button(window, text="Start", font=("Arial", 20), command=start)
startbtn.pack()

canvas = Canvas(window, width=geometry, height=geometry, bg="#afafaf")
canvas.place(anchor=CENTER, x=win_start_geo/2, y = win_start_geo/2)

# pixel_generator
def roundfunc(i, bool):
        i = int(i)
        if round(i/2)-i/2 != 0:
            return bool
        else:
            return not bool
    

size = geometry/inp
bggrid = []

for y in range(inp):
    loclist = []
    bggrid.append(loclist)

    for x in range(inp):
        loclist.append([str(y)+"_"+str(x), "bgrec"])
        bggrid[y][x][1] = canvas.create_rectangle(0,0, size, size, fill="#afafaf", outline="black", width=2)
        
        posy = y*size
        posx = x*size
        canvas.move(bggrid[y][x][1], posx, posy)

        if roundfunc(inp, False): # false för om det är 0
                if roundfunc(y, False):
                    if roundfunc(bggrid[y][x][1], True): # true för om det inte är 0
                        canvas.itemconfig(bggrid[y][x][1], fill="#fafafa")
                
                elif roundfunc(y, True):
                    if roundfunc(bggrid[y][x][1], False): # true för om det inte är 0
                        canvas.itemconfig(bggrid[y][x][1], fill="#fafafa")
        if roundfunc(inp, True) and roundfunc(bggrid[y][x][1], True):
            # true för om det inte är 0
            canvas.itemconfig(bggrid[y][x][1], fill="#fafafa")

            

class snake_part:
    def __init__(self, posx, posy, ID):
         self.posx = posx
         self.posy = posy
         self.ID = ID
         
    def for_head(self):
        self.posx = 3
        self.posy = floor((inp)/2)

class apple_part: 
    def __init__(self, posx, posy):
         self.posx = posx
         self.posy = posy
# run scr   
def runscr():
    
    global direction
    # functions
    def spawn(apples):
        apples+= 1
        posx_a = randint(0, inp-1)
        posy_a = randint(0, inp-1)
        temp_list = [posx_a, posy_a]
        apples_list.append(temp_list)
        canvas.itemconfig(bggrid[posy_a][posx_a][1], fill="#9c1414")
        return apples

    def snake_pos():
        for  i in listofsnake:
            if i == head:
                canvas.itemconfig(bggrid[i.posy][i.posx][1], fill="red")
            else:
                canvas.itemconfig(bggrid[i.posy][i.posx][1], fill="green")  
    def get_input():
        def rightfunc(event):
            global direction
            direction = "right"
            upd()
            

        def leftfunc(event):
            global direction
            direction = "left"
            upd()      
            

        def upfunc(event):
            global direction
            direction = "up"
            upd()

        def downfunc(event):
            global direction
            direction = "down"
            upd()

        def upd():
            print(direction)
        window.bind("<Right>", rightfunc)   
        window.bind("<Left>", leftfunc)   
        window.bind("<Up>", upfunc)   
        window.bind("<Down>", downfunc)

    input_thread = threading.Thread(target=get_input)
    input_thread.start()

    # early config
    snake_len=3
    listofsnake = []
    head = snake_part(None, None, 0)
    head.for_head()
    listofsnake.append(head)
    pID = 0
    for i in range(2):
        pID+=1
        listofsnake.append("p"+str(pID))
    listofsnake[1] = snake_part(2, 5, 1)
    listofsnake[2] = snake_part(1, 5, 2)
    snake_pos()

    direction = "right"

    apples = 0
    apples_list = []

    # game tick
    while startVar == True:
        window.update()
        startbtn.config(state=DISABLED)
            
        
        if apples < 3:
            apples = spawn(apples)
            print("upd "+str(apples))
            
        if [head.posy, head.posx] in apples_list:
            apples-=1
            snake_len+=1
        temp_previous_headpos = [head.posx, head.posy]
        if direction == "right":
            head.posx+=1
        elif direction == "left":
            head.posx-=1 
        elif direction == "up":
            head.posy-=1 
        elif direction == "down":
            head.posy+=1 
        canvas.itemconfig(bggrid[head.posy][head.posx][1], fill="red")


        
        pID+=1
        listofsnake.insert(1,"p"+str(pID))
        listofsnake[1] = snake_part(temp_previous_headpos[0], temp_previous_headpos[1], pID)
        canvas.itemconfig(bggrid[listofsnake[1].posy][listofsnake[1].posx][1], fill="green")
        canvas.itemconfig(bggrid[listofsnake[-1].posy][listofsnake[-1].posx][1], fill="white")
        del listofsnake[-1]

        print(listofsnake[-1])
        print(listofsnake)
        sleep(1)
    
    
    


    
    


window.mainloop()