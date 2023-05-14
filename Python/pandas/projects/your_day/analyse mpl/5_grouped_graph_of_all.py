import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
#<>

def to_mean(arr):
    global df
    # print()
    new_arr = np.array([0,0,0,0])
    for part in arr:
        arr_part = np.array(df[df['Date'].isin(part)])[:,2:]
        arr_part = np.transpose(arr_part)
        # print(arr_part, "\n")
        arr_part = np.array(list(map(lambda element: np.mean(element), arr_part)))
        new_arr = np.vstack((new_arr, arr_part))
    new_arr = new_arr[1:]
    # print(new_arr)
    return new_arr

# input = int(input("Write the groupation: "))
input = 2
df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')

Date = np.array(df["Date"])
arr_date = Date
Date = (list(map(lambda element:datetime.strptime(element, '%Y-%m-%d'), Date)))
# print(Date)
last = 0
# array with the indexes of the devided information
ind_arr = np.array([0,0])
for i,element in enumerate(Date): # ! error i denna fixa, grupperar fel med sista, ex [6,6] även om [6, 7] går i gruppering 2
    error = # skriver så du minns
    # print(Date[last]-element)
    if (element-Date[last]).days >= 0.5*(input): # om skillnaden i dagar är större än ett halvt tidsinterval
        ind_arr = np.vstack((ind_arr, [last, i-1]))
        print(np.vstack((last, i-1)))
        last = i
    elif (element-Date[last]).days >= (input-1): # -1 pga index
        ind_arr = np.vstack((ind_arr, [last, i]))
        # print(np.vstack((last, i)))
        last = i+1
ind_arr = ind_arr[1:]
print(ind_arr)
# print(ind_arr)
# print()

# makes the index array into an actual array with dates 
fixed_arr = np.array(np.arange(input))
for i, element in list(enumerate(ind_arr)):
    print(fixed_arr, arr_date[element[0]:element[1]+1])
    if len(arr_date[element[0]:element[1]+1]) != input:
        break
    fixed_arr = np.vstack((fixed_arr, arr_date[element[0]:element[1]+1]))
fixed_arr = fixed_arr[1:]
# print(fixed_arr)
mean_arr = to_mean(fixed_arr)

# för att få dem i ordning efter typ alltså Food list, Sleep list... istället för vecka 1 list, vecka 2 list 
mean_arr = np.transpose(mean_arr)
# print(mean_arr)

x = np.arange(0, len(mean_arr[0]))*input
plt.title("Your day")
plt.xlabel("Day")
plt.ylabel("Grade")
plt.plot(x,mean_arr[0], "ro-",  label="Food", linewidth=3)
plt.plot(x,mean_arr[1], "go-",  label="Sleep", linewidth=3)
plt.plot(x,mean_arr[2], "bo-",  label="School", linewidth=3)
plt.plot(x,mean_arr[3], "yo-",  label="Mood", linewidth=3)
plt.xticks(x) # de kommer visas korrekt
plt.legend()
plt.show()