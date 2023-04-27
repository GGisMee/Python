from tkinter import *
from tkinter import Grid
import numpy as np

window = Tk()


canvas = Canvas(window, height=500, width=500, bg="lightgray")
canvas.pack()
id = 0

class line:
    def __init__(self,x1,y1,x2,y2, color):
        self.x1, self.y1, self.x2, self.y2 = x1,y1,x2,y2
        self.obj = canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=color, width=2)
        
    def middlepoint(self):
        self.x1 = (self.x1+self.x2)/2
        self.y1 = (self.y1+self.y2)/2
        self.y2, self.x2 = 0,0

lines = np.array([[line(100, 400, 400, 400, "red"),line(250, 100, 100,400, "red"), line(250, 100, 400,400, "red")]])
# lines = np.vstack([lines, [[line(100, 400, 400, 400),line(250, 100, 100,400), line(250, 100, 400,400)]]])

def new_lines(color):
    global lines
    State = True
    for i1 in lines:
        for i2 in i1:
            i2.middlepoint()
    temp_list = np.array([])
    for i in lines:
        print(i)
        new_line_1 = line(i[0].x1, i[0].y1, i[1].x1, i[1].y1, color)
        new_line_2 = line(i[0].x1, i[0].y1, i[2].x1, i[2].y1, color)
        new_line_3 = line(i[1].x1, i[1].y1, i[2].x1, i[2].y1, color)

        if State == True:
            temp_list = np.append(temp_list, [new_line_1, new_line_2, new_line_3])
            State = False
        else:
            temp_list = np.vstack((temp_list, [new_line_1, new_line_2, new_line_3]))

    lines = np.vstack([lines, temp_list])


# följd
new_lines("blue")
new_lines("green")


for i in lines[2]:
    print(i.obj)


window.mainloop()