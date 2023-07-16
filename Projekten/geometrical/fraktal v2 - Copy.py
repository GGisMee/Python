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

def triangle_1_2(i):
    c1 = [i.m1_2[0]+i.len_3_1[0], i.m1_2[1]+i.len_3_1[1]]
    c2 = [i.m1_2[0]-i.len_2_3[0], i.m1_2[1]-i.len_2_3[1]]
    c3 = i.m1_2
    obj = triangle(c1, c2,  c3, color = "purple")
    triangles.append(obj)


def triangle_2_3(i):
    c1 = i.m2_3
    c2 = [i.m2_3[0]+i.len_1_2[0], i.m2_3[1]+i.len_1_2[1]]
    c3 = [i.m2_3[0]-i.len_3_1[0], i.m2_3[1]-i.len_3_1[1]]
    obj = triangle(c1, c2,  c3, color = "purple")
    triangles.append(obj)


def triangle_3_1(i):
    c1 = [i.m3_1[0]-i.len_1_2[0], i.m3_1[1]-i.len_1_2[1]]
    c2 = i.m3_1
    c3 = [i.m3_1[0]+i.len_2_3[0], i.m3_1[1]+i.len_2_3[1]]
    obj = triangle(c1, c2,  c3, color = "purple")
    triangles.append(obj)


def new_triangles():
    global triangles
    for i in range(len(triangles)):
        if triangles[i].new == True:
            triangles[i].new = False
            for n in range(3):
                match n:
                    case 0:
                        triangle_3_1(triangles[i])
                        
                        
                    case 1:
                        triangle_2_3(triangles[i])
                        
                        
                    case 2:
                        triangle_1_2(triangles[i])
                         
                        
                
            

triangles = []
t1 = triangle([100, 400], [400, 400], [250, 100], color="blue")
t2 = triangle([175, 250], [325, 250], [250, 400], color="green")
triangles.append(t2)
for i in range(6):
    new_triangles()

window.mainloop()