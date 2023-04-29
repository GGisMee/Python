import numpy as np
import matplotlib.pyplot as plt
import time
iterations = 1
list = np.array([1])

def ploting():
    coord = np.array([0,0])
    listofcoord = np.array([0,0])
    for i in range(len(list)):
        match list[i]:
            case 1:
                coord = [coord[0]+1, coord[1]]
            case 2:
                coord = [coord[0], coord[1]+1]
            case 3:
                coord = [coord[0]-1, coord[1]]
            case 4:
                coord = [coord[0], coord[1]-1]
        listofcoord = np.vstack((listofcoord, coord))
    x,y = np.hsplit(listofcoord,2)
    plt.plot(x,y)
    plt.show()




def order():
    global list
    list = np.append(list,np.flip(list+1))
    for i in range(len(list)):
        if list[i] == 5:
            list[i] = 1


for i1 in range(14):
    for i in range(i1):
        order()
    ploting()


