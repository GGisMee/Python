import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 

def get_mean(df):
    F_mean = np.array(df["Food"]).mean()
    Sl_mean = np.array(df["Sleep"]).mean()
    Sc_mean = np.array(df["School"]).mean()
    M_mean = np.array(df["Mood"]).mean()
    return F_mean, Sl_mean, Sc_mean, M_mean


df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')


date = np.array(df["Date"])
ldate = datetime.strptime(date[-1], '%Y-%m-%d')

# get the week
for i,element in list(enumerate(reversed(date)))[1:]:
    element2 = datetime.strptime(element, '%Y-%m-%d')
    if ((ldate - element2).days) >= 7:
        break
i_of_first = np.where(date == element)[0][0]
which_date_week = date[i_of_first:]
df_week = df[df['Date'].isin(which_date_week)]

# get the month
for i,element in list(enumerate(reversed(date)))[1:]:
    element2 = datetime.strptime(element, '%Y-%m-%d')
    if ((ldate - element2).days) >= 30:
        break
i_of_first2 = np.where(date == element)[0][0]
which_date_month = date[i_of_first2:]
df_month = df[df['Date'].isin(which_date_month)]

# all
df_all = df

# print(df_week)
# print()
# print(df_month)
# print()
# print(df_all)
df_all = get_mean(df_all)
df_month = get_mean(df_month)
df_week = get_mean(df_week)

x = np.arange(len(df_all))
width = 0.25

fig, ax = plt.subplots(figsize=(6, 4))

ax.bar(x - width, df_all, width, label='All')
ax.bar(x, df_month, width, label='Month')
ax.bar(x + width, df_week, width, label='Week')


ax.set_xlabel('Grade')
ax.set_ylabel('Value')
ax.set_title('Grouped Bar Chart')

ax.legend()

# Show the figure
plt.show()
