import numpy as np

def func(x):
    return x**3+2*x

def approximate(func, num_of_parts:int=None, interval:int=None, x0:int=0,x1:int=10):
    if interval == None and num_of_parts == None:
        print('Not num of parts nor interval was inputed')
        return 1
    if interval == None:
        interval = (x1-x0)/(num_of_parts)
    x_values = (np.arange(x0+interval/2, x1-interval/2, step=interval))
    y_values = func(x_values)
    areas = y_values*interval
    sum = np.sum(areas)
    return sum
