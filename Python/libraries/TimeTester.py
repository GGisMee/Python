from time import time
def timeit(func, times):
    start = time()
    for i in range(times):
        func()
    return time() - start 

