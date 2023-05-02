import pandas as pd
import os
import numpy as np
df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')


import time
current_year = time.gmtime().tm_year
current_month = time.gmtime().tm_mon
current_day = time.gmtime().tm_mday
compact = [current_year, current_month, current_day]

# fixa att df.iloc[-1,0] alltså sista datumet blir lista. Därefter jämföre med datumet idag och avsluta eller fortsätt


print(df.iloc[[-1]])
print("Scale 1-10")
inp1_food = input("Food: ")
inp2_sleep = input("Sleep: ")
inp3_school = input("School: ")

df.loc[len(df)] = [inp1_food, inp2_sleep, inp3_school]
print(df)
