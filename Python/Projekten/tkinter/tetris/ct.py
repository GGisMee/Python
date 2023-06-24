import numpy as np

empty_array = np.empty((0, 2))
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array3 = np.array([[9, 10], [11, 12]])

result = np.vstack((empty_array, array1))
result = np.vstack((result, array2))
result = np.vstack((result, array3))

print(result)
