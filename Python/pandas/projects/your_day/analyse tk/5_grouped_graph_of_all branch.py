import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# input = int(input("Write the groupation: "))
input = 3
df = pd.read_csv("Python/pandas/projects/your_day/mydata_ext.csv", index_col='ID')
Date = np.vectorize(lambda element:datetime.strptime(element, '%Y-%m-%d'))(np.array(df.sort_index()["Date"]))
day_date = np.vectorize(lambda element: element.day)(Date)
# print(day_date)
print()

start_day = Date[0]
print(Date)
ind_arr = np.array([0,0])
for i,element in enumerate(Date):
    if (element-start_day).days > input-1:
        # print(np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i-1])[0])))
        # print(ind_arr)
        ind_arr = np.vstack((ind_arr, np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i-1])[0]))))
        # print("new startvar", element)
        start_day = element
ind_arr = ind_arr[1:]
print(ind_arr)
print()
list_of_formated_dates = np.array(np.zeros(input))
for el in ind_arr:
    list = Date[el[0]:el[1]+1]
    list = np.pad(list, (0,(input-(len(Date[el[0]:el[1]])+1))), mode="constant")
    # print(list, "ddd")
    list_of_formated_dates = np.vstack((list_of_formated_dates, list))
list_of_formated_dates = list_of_formated_dates[1:]
print(list_of_formated_dates)