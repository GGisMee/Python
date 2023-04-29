# 86__canvas
from tkinter import *
from tkinter import Grid

window = Tk()

def inp():
    entryVal = entry.get()+""
    
    canvasFunc(entryVal)

entry = Entry(window, )
entry.pack()
btn = Button(window, text="choose", command=inp)
btn.pack()

canvas = Canvas(window, height=500, width=500)
canvas.pack()

def canvasFunc(entryVal):
    if entryVal == "1":
        blueline = canvas.create_line(0,0, 500, 500, fill="blue", width=5) # från 0,0 till 500, 500
        redline = canvas.create_line(0,500, 500, 0, fill="red", width=5) # från 0,0 till 500, 500
        # this can be called later and be moved osv.
    elif entryVal == "2":
        canvas.create_rectangle(100, 100, 300, 300, fill="green")

    elif entryVal == "3":
        # månghörning, valbart antal hörn
        canvas.create_polygon(250, 0,  500, 500,  0, 500,  fill="yellow", outline="black", width=4)
    elif entryVal == "4":
        points = [250, 0, 500, 500, 0, 500]
        canvas.create_polygon(points,  fill="blue", outline="black", width=4)
    elif entryVal == "5":
        canvas.create_arc(0, 0,  500, 500, fill = "purple", style=PIESLICE, start=90)
        # val PIESLICE, CHORD, ARC
        # start = vilken riktning i gr

    elif entryVal == "6":
        canvas.create_arc(0,0,  500, 500, fill= "red", style=PIESLICE, extent=180, width=2)
        canvas.create_arc(0,0,  500, 500, fill= "white", style=PIESLICE, extent=180, start=180, width=2)
        canvas.create_arc(190, 190, 310,310, fill="white", width=2,)

window.mainloop()