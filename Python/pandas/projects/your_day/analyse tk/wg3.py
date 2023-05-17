from datetime import datetime
import numpy as np
def vec(func, arr):
    return (np.array(list(map(func, arr))))
arr = np.array([datetime(2023, 5, 1, 0, 0), datetime(2023, 5, 2, 0, 0), datetime(2023, 5, 3, 0, 0)])
print(vec(lambda el: print(el),arr))