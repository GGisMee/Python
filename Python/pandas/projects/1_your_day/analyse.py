import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

# del 1 graf över alla värden (kan välja om specifikt senaste 30 eller så)
Food = np.array(df["Food"])
Sleep = np.array(df["Sleep"])
School = np.array(df["School"])
x = np.arange(0, len(df))
plt.title("Your day")
plt.xlabel("Day")
plt.ylabel("Grade")
plt.plot(x,Food, "ro-",  label="Food", linewidth=3)
plt.plot(x,Sleep, "go-",  label="Sleep", linewidth=3)
plt.plot(x,School, "bo-",  label="School", linewidth=3)
plt.legend()
# plt.show()


# Date formater
Date = np.array(df.iloc[:, 0])
Date2 = [[]]
for i in range(len(Date)):
    Date[i] = np.fromstring(Date[i][1:-1], dtype=int, sep=",")
Date = np.array(Date)
Date2 = np.array([0,0,0,0])
for i,element in enumerate(Date):
    l = np.array(1)
    for i,element in enumerate(Date[i]):
        l = np.hstack((l, element))
    l = l[1:]
    Date2 = np.vstack((Date2, l))
Date = Date2[1:]
# Medel per dag
for i in range(1,7):
    true = np.where(Date[:,3] == i, True, False)
    List_of_that_day = Date[true]
    for i2, element in enumerate(List_of_that_day):
        element = str(element.tolist())
        print(element)
        print(df.index[df['Date'] == element][0])
        exit()
        print(df.loc[df['Date'] == element])
        

    


# medelvärde
F_mean = np.array(df.iloc[:, 1]).mean()
Sl_mean = np.array(df.iloc[:, 2]).mean()
Sc_mean = np.array(df.iloc[:, 3]).mean()


# medel för varje dag

