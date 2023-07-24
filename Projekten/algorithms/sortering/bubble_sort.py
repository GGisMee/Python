import numpy as np
import time
def sort(arr):
    swapp_done = False
    i = 0
    while True:
        i+=1
        swapp_done = False
        for i, el in enumerate(arr[:-1]):
                if arr[i]>arr[i+1]:
                    swapp_done = True
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        #print(arr)
        if not swapp_done:
             return arr,i
        swapp_done = False
start = time.time()
print(sort(np.random.randint(1,3001, size=(1,3000))[0]))
print(time.time()-start)