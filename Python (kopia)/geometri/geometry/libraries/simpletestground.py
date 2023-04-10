from tkinter import *
from simplegeometrylib import *

window = Tk()
geometry = 200
canvas = Canvas(window, width=geometry, height=geometry, bg="white")
canvas.pack()

line1 = canvas.create_line(10,10,200,200, fill="blue", width=2) 
mid = Line.length_of_points([10,10], [200,200], show=True)


window.mainloop()