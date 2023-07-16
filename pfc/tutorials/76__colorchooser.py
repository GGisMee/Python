# 76__colorchooser
from tkinter import *
from tkinter import colorchooser # submodul
colors = []
def btn():
    color = colorchooser.askcolor()
    color = color[1]
    colors.append(color)
    window.config(bg=color)

window = Tk()
window.geometry("400x400")

btn = Button(window, command=btn, text="colorchoser")
btn.pack()



window.mainloop()