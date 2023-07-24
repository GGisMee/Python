from time import time
import numpy as np

def sort(arr):
    for i in range(1, len(arr)):
        while arr[i-1]>arr[i] and i!=0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i-=1
    return arr
start = time()

print(sort(np.random.randint(1,3001, size=(1,3000))[0].tolist()))

print(time()-start)
