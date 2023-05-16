import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from vec import vec

# input = int(input("Write the groupation: "))
input = 3
df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')
Date = np.vectorize(lambda element:datetime.strptime(element, '%Y-%m-%d'))(np.array(df.sort_index()["Date"]))
day_date = np.vectorize(lambda element: element.day)(Date)
# print(day_date)
# print()

start_day = Date[0]
# print(Date)
ind_arr = np.array([0,0])
for i,element in enumerate(Date):
    if (element-start_day).days > input-1:
        # print(np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i-1])[0])))
        # print(ind_arr)
        ind_arr = np.vstack((ind_arr, np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i-1])[0]))))
        # print("new startvar", element)
        start_day = element
    if i == len(Date)-1:
        ind_arr = np.vstack((ind_arr, np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i])[0]))))

ind_arr = ind_arr[1:]
# print(ind_arr)
# print("\n\n")
list_of_formated_dates = np.array(np.zeros(input))
for el in ind_arr:
    list = Date[el[0]:el[1]+1]
    list = np.pad(list, (0,(input-(len(Date[el[0]:el[1]])+1))), mode="constant")
    list[np.where(list==0)] = datetime(1,1,1)
    list = vec(lambda el2: el2.strftime("%Y-%m-%d"), list)
    list_of_formated_dates = np.vstack((list_of_formated_dates, list))
list_of_formated_dates = list_of_formated_dates[1:]
# print("\n\n")
# print(list_of_formated_dates)
# print("\n\n")

mean_list_tot = np.zeros(4)
for el in list_of_formated_dates:
    list = np.transpose(np.array(df[df['Date'].isin(el)])[:,2:])
    mean_list = vec(lambda el2: np.mean(el2), list)
    # print(mean_list, "\n")
    mean_list_tot = np.vstack((mean_list_tot, mean_list))
mean_list_tot = np.transpose(mean_list_tot[1:])
# print("\n\n")
# print(list_of_formated_dates)

# felet just nu är att x_axeln ger 0001-01-01 på de som inte är fulla, den måste tas bort nu
# kanske en while loop som kör näst närmaste till inga 0001-01-01 finns kvar och om den är samma så skriver den bara samma


# print()
# för x axeln
x_axel = (vec(lambda el: f"{el[0]} - {el[-1]}", list_of_formated_dates))
# print(x_axel)

plt.title("Your day")
plt.xlabel("Day")
plt.ylabel("Grade")
plt.plot(x_axel,mean_list_tot[0], "ro-",  label="Food", linewidth=3)
plt.plot(x_axel,mean_list_tot[1], "go-",  label="Sleep", linewidth=3)
plt.plot(x_axel,mean_list_tot[2], "bo-",  label="School", linewidth=3)
plt.plot(x_axel,mean_list_tot[3], "yo-",  label="Mood", linewidth=3)
plt.xticks(x_axel) # de kommer visas korrekt
plt.legend()
plt.show()

