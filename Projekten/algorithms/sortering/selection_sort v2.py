import numpy as np
from time import time
def sort(arr):
    excluding_i = 0
    for o in arr[:]:
        min_i = excluding_i
        for i,el in enumerate(arr[excluding_i+1:]):
            if el<arr[min_i]:
                min_i = i+excluding_i+1
        arr.insert(excluding_i,arr[min_i])
        del arr[min_i+1]
        excluding_i+=1
    return arr
start = time()
sort(np.random.randint(1,3001, size=(1,3000))[0].tolist())
print(time()-start)