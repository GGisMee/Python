import pandas as pd
import os
import numpy as np
df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')


import time
current_year = time.gmtime().tm_year
current_month = time.gmtime().tm_mon
current_day = time.gmtime().tm_mday
current_type_of_day = time.localtime().tm_wday # alltså typ idag är det måndag, torsdag, söndag eller annat
compact = [current_year, current_month, current_day, current_type_of_day]
# print(compact)

# fixa att df.iloc[-1,0] alltså sista datumet blir lista. Därefter jämföre med datumet idag och avsluta eller fortsätt
last = np.fromstring(df.iloc[-1][0][1:-1], dtype=int, sep=",")
# print(df.iloc[-1][0][1:-1])
# print(last, compact, np.array_equal(last, compact))

if np.array_equal(np.array(last), compact):
    print("today")
    exit()
    
print("Scale 1-10")
inp1_food = input("Food: ")
inp2_sleep = input("Sleep: ")
inp3_school = input("School: ")

df.loc[len(df)] = [compact, inp1_food, inp2_sleep, inp3_school]
print(df)
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'mydata.csv')
df.to_csv(file_path, index=True)


