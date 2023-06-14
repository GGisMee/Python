import numpy as np
import pandas as pd
from datetime import datetime
def format_date(time_values, grouping_of_data="1h"):
    # pos_date = time_values[0] # första tidsvärdet hämtas för att ge en startpunkt och grupera dem
    ind_arr = np.zeros(2) # arr för alla index skapas
    pos_date = time_values[0]
    # print("\n",pos_date,"\n")
    smhdwmo = ([1, 60, 3600, 86400, 604800, 18748800][(np.where(np.array(["s", "m", "h", "d", "w", "mo"]) == grouping_of_data[-1:])[0][0])])
    grouping_of_data = int(grouping_of_data[:-1])
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
    ind_arr = ind_arr[1:]
    date_arr = []
    for el in ind_arr:
        part_dates = time_values[int(el[0]): int(el[1]+1)]
        date_arr.append(part_dates)
    print(pos_date)
    return date_arr, ind_arr