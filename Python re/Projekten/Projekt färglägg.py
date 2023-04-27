import tkinter
from tkinter import Tk
fonster = tkinter.Tk()
print("Du ritar genom att hålla ner vänster musknapp och dra pekaren.")
print("Klicka på färgrutorna när du vill byta färg")
canvas = tkinter.Canvas(fonster, width=750, height=500, bg="white")
canvas.pack()
musX, musY = 0, 0  # kompakt sätt att skriva likasinnade variabler
color = "red"
farg = 1


def lagra_position(event):
    global musX, musY
    musX = event.x
    musY = event.y

def vid_klick(event):
    lagra_position(event)

def vid_drag(event):
    canvas.create_line(musX, musY, event.x, event.y, fill=color, width=3)
    lagra_position(event)

def colorchange(event):
    global farg
    global color
    farg = int(farg) + 1
    if farg == 1:
        color = "red"
    if farg == 2:
        color = "blue"
    if farg == 3:
        color = "black"
    if farg == 4:
        color = "white"
    if farg == 5:
        farg = 0
        colorchange(event)

canvas.bind("<Button-1>", vid_klick)
canvas.bind("<B1-Motion>", vid_drag)
canvas.bind("<Button-2>", colorchange)
fonster.mainloop()