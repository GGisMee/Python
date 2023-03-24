from tkinter import *
from tkinter import Grid
import numpy as np

window = Tk()


canvas = Canvas(window, height=500, width=500, bg="lightgray")
canvas.pack()
id = 0

class triangle:
    def __init__(self, c1, c2, c3, color):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.color = color

        self.obj = canvas.create_polygon(c1[0], c1[1], c2[0], c2[1], c3[0], c3[1], width=4, outline=color, fill="lightgray")
    def mittpoints(self):
        self.c1_2 = 
        self.c2_3 = 
        self.c3_1 = 
        # att göra, hitta medelpunkt och även skillnad för att sedan lätt kunna hitta de andra punkterna
        # använd skillnad ((x2-x1)/2 och medel (x1+x2)/2)


t1 = triangle([100, 400], [400, 400], [250, 100], color="blue")
t2 = triangle([175, 250], [325, 250], [250, 400], color="green")

t2.smalltriangle()
triangle(t2.c1s, t2.c2s, t2.c3s, color = "yellow")

window.mainloop()