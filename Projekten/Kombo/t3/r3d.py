from tkinter import *
import numpy as np
import math
window = Tk()
height = 400
width = 400
canvas = Canvas(window, bg = "#e3e3e3", width=width, height=height)
canvas.pack()


class vec():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        

class triangle():
    def __init__(self, p):
        self.p1 = p[0]
        self.p2 = p[1]
        self.p3 = p[2]

cube = np.array([
    # syd
    [0,0,0],[0,1,0],[1,1,0],
    [0,0,0],[1,1,0],[1,0,0],

    # öst
    [1,0,0],[1,1,0],[1,1,1],
    [1,0,0],[1,1,1],[1,0,1],
    
    # norr
    [1,0,1],[1,1,1],[0,1,1],
    [1,0,1],[0,1,1],[0,0,1],

    # väst
    [0,0,1], [0,1,1], [0,1,0],
    [0,0,1], [0,1,0], [0,0,0],

    # toppen
    [0,1,0],[0,1,1],[1,1,1],
    [0,1,0],[1,1,1],[1,1,0],

    # botten
    [1,0,1], [0,0,1], [0,0,0],
    [1,0,1], [0,0,0], [1,0,0]

])

def Multiply_Matrix_Vector(v, m):
    # v = vector, m = matrix
    x = v.x*m.m[0][0]+v.y*m.m[1][0]+v.z*m.m[2][0]+m.m[3][0]
    y = v.x*m.m[0][1]+v.y*m.m[1][1]+v.z*m.m[2][1]+m.m[3][1]
    z = v.x*m.m[0][2]+v.y*m.m[1][2]+v.z*m.m[2][2]+m.m[3][2]
    vec(x,y,z)
    w = v.x*m.m[0][3]+v.y*m.m[1][3]+v.z*m.m[2][3]+m.m[3][3]
    if w != 0:
        v_new = vec(np.array(x,y,z)/w)
        return v_new
    
    

class matrix_4x4():
    def __init__(self):
        self.m = (np.zeros((4,4)))

mat_proj = matrix_4x4()

fNear = 0.1
fFar = 1000.
fFov = 90.
fAspectRatio = height/width
fFovRad = 1/math.tan(fFov*0.5/189*math.pi)

mat_proj.m[0][0] = fAspectRatio*fFovRad
mat_proj.m[1][1] = fFovRad
mat_proj.m[2][2] = fFar/(fFar-fNear)
mat_proj.m[3][2] = (-fFar*fNear)/(fFar-fNear)
mat_proj.m[2][3] = 1
mat_proj.m[3][3] = 0
# cube



window.mainloop()

