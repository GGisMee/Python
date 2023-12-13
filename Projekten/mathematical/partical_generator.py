import numpy as np
import tkinter as tk
import random

#* Parameters
# gravitational
max_gravity = 2
towards_max = 100
degree = 0.7


window = tk.Tk()
window.geometry('400x400')
Canvas = tk.Canvas()
Canvas.pack(fill=tk.BOTH, expand=True)

class particle:
    def __init__(self, coords:list):
        self.coords = coords
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        size = 5/2
        self.look = Canvas.create_oval(self.coords[0]-size,self.coords[1]-size,self.coords[0]+size,self.coords[1]+size, fill="blue")
    def move(self):
        self.x += self.vx
        self.y += self.vy

class partical_container:
    def __init__(self, num_par:int) -> None:
        """Creates lots of particles on an xy-plane with coordinates from 0-1
        
        Variables:
            num_par: int = nummer n"""
        self.num_par = num_par
        self.par_list = []
        for i in range(num_par):
            self.par_list.append(particle([random.random()*400, random.random()*400]))

    def find_gravity(self):
        self.coord_list = np.array([particle.coords for particle in self.par_list])
        for i,coord in enumerate(self.coord_list):
            coord_n_list = np.sqrt(np.square(self.coord_list[:,0])+np.square(self.coord_list[:,1]))
        

c1 = partical_container(10)
c1.find_gravity()




window.mainloop()