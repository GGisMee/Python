# 87__keyboard_events
from tkinter import *

def DoSomething(event):
    print("helloo")

def Quitfunc(event):
    window.quit()

def Varjekey(event):
    print("one of all keys was pressed in this case, "+event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Return>", DoSomething)
window.bind("<q>", Quitfunc)
window.bind("<Key>", Varjekey)
# bind är hur man bindar en keyboard input till en funktion
# <> används för att visa en keyboard input


label = Label(window, font=("Helvetica", 100))
label.pack()
window.mainloop()