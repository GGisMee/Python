import pandas as pd
import os
import numpy as np
import datetime
#<>
df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

# Format the date
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d")
daytype = int(now.strftime("%w"))
if daytype == 0: daytype = 7
# ger tids skillnaden mellan senaste dagen och idag
time_diff = datetime.datetime.strptime(today, "%Y-%m-%d")- datetime.datetime.strptime(np.array(df["Date"])[-1], "%Y-%m-%d")
if time_diff.days == 0:
    tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    time_diff2 = tomorrow - now
    total_seconds = int(time_diff2.total_seconds())
    hours = (total_seconds // 3600)
    minutes = ((total_seconds % 3600) // 60)
    seconds = (total_seconds % 60)
    print("You have already logged your day, please come back tomorrow if you have the time")
    print(f"You can try again in {hours}:{minutes}:{seconds}")
    exit()


print("Scale 1-10")
inp1_food = input("Food: ")
inp2_sleep = input("Sleep: ")
inp3_school = input("School: ")
inp4_mood = input("Mood: ")
my_list = [4, 10, 2.4, 4]

if any(not isinstance(x, (int, float)) or x > 10 for x in my_list):
    print("Error: not number or to high/low")
    exit()

df.loc[len(df)] = [today,daytype, inp1_food, inp2_sleep, inp3_school, inp4_mood]
print(df)
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'mydata.csv')
df.to_csv(file_path, index=True)


