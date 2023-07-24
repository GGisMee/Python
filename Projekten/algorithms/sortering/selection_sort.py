import numpy as np
from time import time
def sort(arr):
    
    changed = []
    for o in arr[:]:
        min_i = 0
        for i,el in enumerate(arr[1:]):
            if el<arr[min_i]:
                min_i = i+1
        changed.append(arr[min_i])
        del arr[min_i] 
    return changed
start = time()
sort(np.random.randint(1,3001, size=(1,3000))[0].tolist())
print(time()-start)