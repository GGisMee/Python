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
        #print('run')
        distanses = []
        for child in children:
            if child == self:
                distanses.append([2, child])
                continue
            distanses.append([self.getDistans(child), child])
        chosen = np.argmin(np.array(distanses)[:,0])
        for i, child in enumerate(children): 
            if child == distanses[chosen][1]:
                children[i].got_ball = True
                break
def get_random():
    random_1 = random()
    random_2 = random()
    if random_1 != random_2:
        return random_1, random_2
    return get_random()
results = []
iterations = 1000
for i in range(iterations):
    children = []
    for i in range(3):
        random1, random2 = get_random()
        child = Child(random1, random2, i)
        children.append(child)
    for child in children:
        child.throw()
    results.append(np.all([child.got_ball for child in children]))
print(np.sum(results))


