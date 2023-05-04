import pandas as pd
import os
import numpy as np

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

Date = np.array(df.iloc[:, 0])
Date2 = [[]]
for i in range(len(Date)):
    Date[i] = np.fromstring(Date[i][1:-1], dtype=int, sep=",")
Date = np.array(Date)

Date = np.reshape()
# print([arr[1] for arr in Date])

# medelvärde
Food = np.array(df.iloc[:, 1])
F_mean = Food.mean()

Sleep = np.array(df.iloc[:, 2])
Sl_mean = Sleep.mean()

School = np.array(df.iloc[:, 3])
Sc_mean = School.mean()


# medel för varje dag

