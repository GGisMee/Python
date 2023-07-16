import numpy as np
iterations = 20
triangle_list = [[1], [1,1]]

for i in range(iterations):
    current = triangle_list[-1]
    next = []
    for i, el in enumerate(current[:-1]):
        next.append(current[i]+current[i+1])
    next.insert(0, 1)
    next.append(1)
    triangle_list.append(next)
for i in triangle_list:
    print(i)