import numpy as np

class particle:
    def __init__(self, x:bool,y:bool):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
    def move(self):
        self.x += self.vx
        self.y += self.vy
    

class partical_container:
    def __init__(self, num_par:int) -> None:
        """Creates lots of particles on an xy-plane with coordinates from 0-1
        
        Variables:
            num_par: int = nummer  n"""
        self.num_par = num_par
        self.par_list = []
        for i in range(num_par):
            self.par_list.append(particle)

    def apply(self):
        self.x_mat
        self.y_mat
        self.vx_mat