import numpy as np

# Create a NumPy array
boxes = np.array([[1,2], [3,4], [5,6], [7,8], [6,19]])

old_shapes = np.array([[1,19], [2,19], [3,19], [4,19], [5,19],[6,16], [6,17], [6,18], [6,19]])

for i in old_shapes:
    for i2 in boxes:
        if np.array_equal(i, i2):
            print("equal", i, i2)



array([[ 7, 19],
       [ 8, 19],
       [ 9, 19],
       [ 2, 19],
       [ 3, 19],
       [ 4, 19],
       [ 5, 19],
       [ 8, 16],
       [ 8, 17],
       [ 9, 16],
       [ 9, 17]])