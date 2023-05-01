from sgl import *
import matplotlib.pyplot as plt
from itertools import combinations 
import random

coords = list(shape.format_from_middle(points=5))
print(coords)

index_save = 4

last_coord = coords[0]
new_coords = []
exp_save = 1
for i in range(10):
    for i in range(exp_save):
        a = index_save
        while a == index_save:
            a = random.randint(0, len(coords)-1)
        last_coord = Line.specific_point_between_points(coords[a], last_coord, 0.5)
        new_coords.append(last_coord)
        index_save = a


    coords2 = np.vstack((new_coords, coords))
    coords2 = coords2.reshape((-1,2))
    coords2 = np.hsplit(coords2, 2)
    plt.figure(figsize=(5,5), dpi=150)
    plt.scatter(coords2[0], coords2[1], s=1)
    # plt.scatter(coords2[0][-1], coords2[1][-1], s=3)
    # plt.scatter(coords2[0][-2], coords2[1][-2], s=2)

    plt.xticks(np.linspace(-1, 1, 10))
    plt.yticks(np.linspace(-1, 1, 10))
    plt.show()
    exp_save*=4
    