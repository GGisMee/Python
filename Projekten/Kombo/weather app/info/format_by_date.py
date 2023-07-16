import numpy as np
import pandas as pd
from datetime import datetime
def format_date(time_values, grouping_of_data="1h"):

    if grouping_of_data == "1h":
        for i, el in enumerate(time_values):
            time_values[i] = np.array([time_values[i]])
        return time_values, []

    # pos_date = time_values[0] # första tidsvärdet hämtas för att ge en startpunkt och grupera dem
    ind_arr = np.zeros(2) # arr för alla index skapas
    pos_date = time_values[0]
    # print("\n",pos_date,"\n")
    smhdwmo = ([1, 60, 3600, 86400, 604800, 18748800][(np.where(np.array(["s", "m", "h", "d", "w", "mo"]) == grouping_of_data[-1:])[0][0])])
    grouping_of_data = int(grouping_of_data[:-1])
    #print(len(time_values))
    for i, element in enumerate(time_values): # tidsvärden försig
        if ((element-pos_date).total_seconds()) >= grouping_of_data*smhdwmo: # om tidsvärdenas timmskillnad ex 4 är större eller lika med 4 kommer de delas in i en grupp
            i_obj = [int(np.where(time_values==pos_date)[0][0]), int(i-1)] # värdena memoreras

        elif i == len(time_values)-1:
            i_obj = (int(np.where(time_values==pos_date)[0][0]), int(i)) # om sista värdet körs som inte är lika stort som timmskillnad kommer det ändå gruperas
        else:
            continue
        # print(x_obj)
        pos_date = element
        ind_arr = np.vstack((ind_arr, i_obj))
    del pos_date
    ind_arr = ind_arr[1:]
    date_arr = []
    for el in ind_arr:
        part_dates = time_values[int(el[0]): int(el[1]+1)]
        date_arr.append(part_dates)
    #print(pos_date)
    return date_arr, ind_arr

#tv = np.array([datetime(2023, 6, 15, 0, 0), datetime(2023, 6, 15, 1, 0), datetime(2023, 6, 15, 2, 0), datetime(2023, 6, 15, 3, 0), datetime(2023, 6, 15, 4, 0), datetime(2023, 6, 15, 5, 0), datetime(2023, 6, 15, 6, 0), datetime(2023, 6, 15, 7, 0), datetime(2023, 6, 15, 8, 0), datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 11, 0), datetime(2023, 6, 15, 12, 0), datetime(2023, 6, 15, 13, 0), datetime(2023, 6, 15, 14, 0), datetime(2023, 6, 15, 15, 0), datetime(2023, 6, 15, 16, 0), datetime(2023, 6, 15, 17, 0), datetime(2023, 6, 15, 18, 0), datetime(2023, 6, 15, 19, 0), datetime(2023, 6, 15, 20, 0), datetime(2023, 6, 15, 21, 0), datetime(2023, 6, 15, 22, 0), datetime(2023, 6, 15, 23, 0)])
#print(format_date(tv, "1h"))
