# sg2 = simplegeometrylib.py 
from sgl import *
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

class triangle:
    def __init__(self, xy1, xy2, xy3):
        self.xy1 = xy1
        self.xy2 = xy2
        self.xy3 = xy3
        print(xy1, xy2, xy3)

frst_triangle = triangle([0,0], [1,0], [0.5, sqrt(0.75)])