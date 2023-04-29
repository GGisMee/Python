import tkinter
from tkinter import Tk
fonster = tkinter.Tk()

def printName(event):
    print("Mitt namn är Gustav")
# v1
# button_1 = tkinter.Button(fonster, text="Print name")
# button_1.bind("<Button-1>", printName)

# v2
# button_1 = tkinter.Button(fonster, text="Print name", command=printName) # ha inga () vid printNamn

# button_1.pack()  # pack är som display för button

# fonster.mainloop()