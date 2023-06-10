import os
import pandas as pd
import numpy as np
import sys
from datetime import datetime
inp = 4
df = pd.read_csv("Python/Projekten/Kombo/weather app/mydata.csv")
date = np.array(df["time"])

date = np.vectorize(lambda element:datetime.strptime(element, "%Y-%m-%dT%H:%M"))(date)
date = date[::2]
# print((date[24]-date[0]).total_seconds() // 3600)
pos_date = date[0]
ind_arr = np.zeros(2)
for i, element in enumerate(date):
    if ((element-pos_date).total_seconds()//3600) >= inp:
        i_obj = (np.where(date==pos_date)[0][0], i-1)
        pos_date = element
    elif i == len(date)-1:
        i_obj = (np.where(date==pos_date)[0][0], i)
    else:
        continue
    ind_arr = np.vstack((ind_arr, i_obj))
ind_arr = ind_arr[1:]

date_arr = np.arange(0, inp)
#print(ind_arr)
for el in ind_arr:
    part_dates = date[np.vectorize(lambda el: int(el))(np.arange(el[0], el[1]+1))]
    length = inp - len(part_dates)
    padded_dates = np.pad(part_dates, (0, length), mode='constant')
    date_arr = np.vstack((date_arr, padded_dates))
date_arr = date_arr[1:]
print(date_arr)