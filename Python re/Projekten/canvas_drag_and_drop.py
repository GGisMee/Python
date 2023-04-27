# 88__mouse_events
from tkinter import *
from tkinter import Canvas


x, y = 0, 0
onoff = None

window = Tk()
window.geometry("400x400")

def lfunc(event):
    global onoff
    print("You clicked left at "+str(event.x)+ " "+ str(event.y))

    if x1 <= int(event.x) <= x2 and y1 <= int(event.y)<= y2:
        onoff = True
        print("on")

    

def b1r(event):
    global onoff

    print("release")
    onoff = False
    print("off")

def motion(event):

    global x, y, onoff, x1, x2, y1, y2
    xlabel.config(text=int(event.x)-x)
    ylabel.config(text=int(event.y)-y)
    if onoff:
        canvas.move(rec, int(event.x)-x, int(event.y)-y)

        x1 += int(event.x)-x
        x2 += int(event.x)-x
        y1 += int(event.y)-y
        y2 += int(event.y)-y

    x = int(event.x)
    y = int(event.y)

def info(event):
    print(x, y, onoff)
    print(x1, x2, y1, y2)
        

window.bind("<ButtonRelease-1>", b1r)
window.bind("<Button-1>", lfunc)
window.bind("<Motion>", motion) # var man på nytt öppnar bilden
window.bind("<i>", info) # var man på nytt öppnar bilden


frame = Frame(window, width=100, height=20)
frame.place(x=180, y=0)

xlabel = Label(frame, font=("Arial", 20))
xlabel.grid(row=0, column=0)
ylabel = Label(frame, font=("Arial", 20))
ylabel.grid(row=0, column=1)

canvas = Canvas(window, height=300, width=300, bg="red")
canvas.place(y=100, x=50)
x1, x2 = 0, 40
y1, y2 = 0, 40
rec = canvas.create_rectangle(x1, y1, x2, y2, fill="green")


window.mainloop()