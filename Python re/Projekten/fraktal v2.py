from tkinter import *
from tkinter import Grid
import numpy as np
import time

window = Tk()
geometry = 1400

canvas = Canvas(window, height=geometry, width=geometry, bg="lightgray")
canvas.pack()
id = 0

class triangle:
    def __init__(self, c1, c2, c3, color):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.color = color
        self.new = True

        self.obj = canvas.create_polygon(c1[0], c1[1], c2[0], c2[1], c3[0], c3[1], width=0.5, outline=color, fill="lightgray")


        self.m1_2 = [0.5*(self.c1[0]+self.c2[0]), 0.5*(self.c1[1]+self.c2[1])]
        self.m2_3 = [0.5*(self.c2[0]+self.c3[0]), 0.5*(self.c2[1]+self.c3[1])]
        self.m3_1 = [0.5*(self.c3[0]+self.c1[0]), 0.5*(self.c3[1]+self.c1[1])]


        self.len_1_2 = [0.5*(self.c2[0]-self.c1[0]), 0.5*(self.c2[1]-self.c1[1])]
        self.len_2_3 = [0.5*(self.c3[0]-self.c2[0]), 0.5*(self.c3[1]-self.c2[1])]
        self.len_3_1 = [0.5*(self.c1[0]-self.c3[0]), 0.5*(self.c1[1]-self.c3[1])]

        # att göra, hitta medelpunkt och även skillnad för att sedan lätt kunna hitta de andra punkterna
        # använd skillnad ((x2-x1)/2 och medel (x1+x2)/2)

def triangle_1_2(i, hex):
    c1 = [i.m1_2[0]+i.len_3_1[0], i.m1_2[1]+i.len_3_1[1]]
    c2 = [i.m1_2[0]-i.len_2_3[0], i.m1_2[1]-i.len_2_3[1]]
    c3 = i.m1_2
    obj = triangle(c1, c2,  c3, color = hex)
    triangles.append(obj)


def triangle_2_3(i, hex):
    c1 = i.m2_3
    c2 = [i.m2_3[0]+i.len_1_2[0], i.m2_3[1]+i.len_1_2[1]]
    c3 = [i.m2_3[0]-i.len_3_1[0], i.m2_3[1]-i.len_3_1[1]]
    obj = triangle(c1, c2,  c3, color = hex)
    triangles.append(obj)


def triangle_3_1(i, hex):
    c1 = [i.m3_1[0]-i.len_1_2[0], i.m3_1[1]-i.len_1_2[1]]
    c2 = i.m3_1
    c3 = [i.m3_1[0]+i.len_2_3[0], i.m3_1[1]+i.len_2_3[1]]
    obj = triangle(c1, c2,  c3, color = hex)
    triangles.append(obj)


def new_triangles(hex):
    global triangles

    for i in range(len(triangles)):
        if triangles[i].new == True:
            triangles[i].new = False
            for n in range(3):
                match n:
                    case 0:
                        triangle_3_1(triangles[i], hex)

                        
                    case 1:
                        triangle_2_3(triangles[i], hex)

                        
                    case 2:
                        triangle_1_2(triangles[i], hex)
  
                        
                
def first_triangle():
    global t2
    c1 = [0.5*(t1.c1[0]+t1.c3[0]), 0.5*(t1.c1[1]+t1.c3[1])]
    c2 = [0.5*(t1.c2[0]+t1.c3[0]), 0.5*(t1.c2[1]+t1.c3[1])]
    c3 = [0.5*(t1.c2[0]+t1.c1[0]), 0.5*(t1.c2[1]+t1.c1[1])]
    t2 = triangle(c1, c2, c3, color="green")


triangles = []
t1 = triangle([100, 1300], [1300, 1300], [700, 100], color="blue")
first_triangle()
triangles.append(t2)

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
r = 10
g = 10
b = 10    

for i in range(10):
    r += 5
    b += 10
    g += 20
    hex = (rgbtohex(r, g, b))
    print(hex)
    new_triangles(hex)
    window.update()
    time.sleep(4)
window.mainloop()