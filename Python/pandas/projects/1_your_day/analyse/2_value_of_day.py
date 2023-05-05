import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

# fix date formater
# print(df["Daytype"])
ordered_day = np.array([0,0,0,0])
for i in range(1,8):
    one_day_all_data = (np.array(df.loc[df["Daytype"] == i]))[:,2:]
    print(one_day_all_data, "ddd")
    day_food_mean = one_day_all_data[:, 0].mean()
    day_sleep_mean = one_day_all_data[:, 1].mean()
    day_school_mean = one_day_all_data[:, 2].mean()
    day_mood_mean = one_day_all_data[:, 3].mean()
    ordered_day = np.vstack((ordered_day, [day_food_mean, day_sleep_mean, day_school_mean, day_mood_mean]))
ordered_day = ordered_day[1:]
print(ordered_day)