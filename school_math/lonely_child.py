import numpy as np
from random import random
from math import sqrt

class Child:
    def __init__(self, x,y, identifier) -> None:
        self.x = x
        self.y = y
        self.identifier = identifier
        self.got_ball = False
    
    def getDistans(self, child):
        return sqrt((self.x+child.x)**2+(self.y+child.y)**2)

    def throw(self):
        print('run')
        distanses = []
        for child in children:
            if child == self:
                print(child)
                continue
            distanses.append([self.getDistans(child), child])
        chosen = np.argmin(np.array(distanses)[:,0])
        print(children[chosen])
        print()

children = []

for i in range(2):
    child = Child(random(), random(), i)
    children.append(child)
for child in children:
    child.throw()
for child in children:
    if not (child.got_ball):
        print('False')
        exit()
    else:
        print('True')
        exit()

