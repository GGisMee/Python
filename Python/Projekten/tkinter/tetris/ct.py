import numpy as np

arr1 = np.array([[4, 5],
                 [5, 5],
                 [6, 5],
                 [7, 5]])

arr2 = np.array([[4, 19],
                 [5, 19],
                 [6, 19],
                 [7, 19],
                 [4, 18],
                 [5, 18],
                 [6, 18],
                 [7, 18]])

exists_in_arr2 = np.any(np.all(arr1[:, None] == arr2, axis=2))
# print(np.all(arr1[:, None] == arr2, axis=2))


if exists_in_arr2: # ... is where a condition that checks if examplewise the whole coordinate [4,5] from arr1 is in arr2, then [5,5] and so on
    print("At least one coordinate in arr1 exists in arr2.")
else:
    print("No coordinates in arr1 exist in arr2.")
