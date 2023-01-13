import tkinter
from tkinter import Tk
fonster = tkinter.Tk()

knapp = tkinter.Button(fonster, text="tryck inte på knappen.", width=40)
knapp.pack(padx=10, pady=10)  # pad x = width, pady = length downwards
antalklick = 0


def onclick(event):
    global antalklick
    antalklick = antalklick + 1
    if antalklick == 1:
        knapp.configure(text="allvarligt? Tryck. Inte. Här.")
    elif antalklick == 2:
        knapp.configure(text="En gång till så rycker knappen")
    else:
        knapp.pack_forget()


knapp.bind("<ButtonRelease-1>", onclick)
fonster.mainloop()
