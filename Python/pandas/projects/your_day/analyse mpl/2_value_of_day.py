import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')

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

# re orders them to be all average food for all days in one list
food_od = ordered_day[:,0]
sleep_od = ordered_day[:,1]
school_od = ordered_day[:,2]
mood_od = ordered_day[:,3]
names = ["M", "T", "W", "T", "F", "S", "W"]



print(food_od)

fig, axs = plt.subplots(2, 2, figsize=(8, 6))

print(names[:len(food_od)])

# Create the four bar plots
axs[0, 0].bar(np.arange(len(food_od)), food_od, tick_label=names, color="r")
axs[0, 0].set_title('Food')
axs[0, 1].bar(np.arange(len(sleep_od)), sleep_od, tick_label=names, color="g")
axs[0, 1].set_title('Sleep')
axs[1, 0].bar(np.arange(len(school_od)), school_od, tick_label=names, color="b")
axs[1, 0].set_title('School')
axs[1, 1].bar(np.arange(len(mood_od)), mood_od, tick_label=names,color="y")
axs[1, 1].set_title('Mood')



# Add some padding between subplots
plt.subplots_adjust(hspace=0.4)

# Show the figure
plt.show()