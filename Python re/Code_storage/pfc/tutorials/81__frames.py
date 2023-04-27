# 81__frames
from tkinter import *
window = Tk()

# frames = div
frame = Frame(
    bg="pink",
    bd=5,
    relief=SUNKEN
)
frame.place(y = 10, x = 10)

Button(frame, text="W", font=("Consolas", 20), width=3,).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 20), width=3,).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 20), width=3,).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 20), width=3,).pack(side=LEFT)



window.mainloop()