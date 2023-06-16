#import matplotlib.pyplot as plt
#import math
#from simplegraphlib import newcoord
# Create a figure and axes
import datetime
import numpy as np
arr = np.array([datetime.datetime(2023, 6, 15, 0, 0),
       datetime.datetime(2023, 6, 15, 1, 0),
       datetime.datetime(2023, 6, 15, 2, 0),
       datetime.datetime(2023, 6, 15, 3, 0),
       datetime.datetime(2023, 6, 15, 4, 0),
       datetime.datetime(2023, 6, 15, 5, 0),
       datetime.datetime(2023, 6, 15, 6, 0),
       datetime.datetime(2023, 6, 15, 7, 0),
       datetime.datetime(2023, 6, 15, 8, 0),
       datetime.datetime(2023, 6, 15, 9, 0),
       datetime.datetime(2023, 6, 15, 10, 0),
       datetime.datetime(2023, 6, 15, 11, 0),
       datetime.datetime(2023, 6, 15, 12, 0),
       datetime.datetime(2023, 6, 15, 13, 0),
       datetime.datetime(2023, 6, 15, 14, 0),
       datetime.datetime(2023, 6, 15, 15, 0),
       datetime.datetime(2023, 6, 15, 16, 0),
       datetime.datetime(2023, 6, 15, 17, 0),
       datetime.datetime(2023, 6, 15, 18, 0),
       datetime.datetime(2023, 6, 15, 19, 0),
       datetime.datetime(2023, 6, 15, 20, 0),
       datetime.datetime(2023, 6, 15, 21, 0),
       datetime.datetime(2023, 6, 15, 22, 0),
       datetime.datetime(2023, 6, 15, 23, 0)], dtype=object)
ind_arr = np.array([
       [ 0.,  0.],
       [ 1.,  1.],
       [ 2.,  2.],
       [ 3.,  3.],
       [ 4.,  4.],
       [ 5.,  5.],
       [ 6.,  6.],
       [ 7.,  7.],
       [ 8.,  8.],
       [ 9.,  9.],
       [10., 10.],
       [11., 11.],
       [12., 12.],
       [13., 13.],
       [14., 14.],
       [15., 15.],
       [16., 16.],
       [17., 17.],
       [18., 18.],
       [19., 19.],
       [20., 20.],
       [21., 21.],
       [22., 22.]])

print(len(ind_arr))
exit()
for i, el in enumerate(ind_arr):
    print(arr[int(el[0]):int(el[1]+1)])