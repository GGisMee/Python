from tkinter import *
import numpy as np
import math



window = Tk()



class graph:
    def __init__(self, x_arr, y_arr, window, height=400, width=400, pad=25):
        fc = self.fc
        self.max_y = np.max(y_arr)
        self.max_x = np.max(x_arr)


        self.pad = pad
        self.height = height
        self.width = width

        self.canvas = Canvas(window, bg="#e0e0e0", width=(self.width+self.pad), height=(self.height+self.pad))
        self.canvas.pack()
        self.canvas.create_line(pad, height, pad, 0)
        self.canvas.create_line(pad, height, pad+width, height)
        
        #self.canvas.create_line(pad, height)
        # print(pad, height)
        self.x_arr = x_arr
        self.y_arr = y_arr

    def fc(self, xy):
        xy[0] = xy[0]/self.max_x*self.width+self.pad
        xy[1] = xy[1]/self.max_y*self.height+self.pad
        print(xy)
        exit()
        return xy

x_arr = np.arange(1,6)
y_arr = np.arange(1,6)**2
# print(x_arr, y_arr)
grph = graph(x_arr, y_arr, window)
window.mainloop()