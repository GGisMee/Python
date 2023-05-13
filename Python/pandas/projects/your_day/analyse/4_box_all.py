import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')
n_df = np.sort(np.array(df)[:,2:])
print(n_df)
print("\n", len(n_df))
# namnen
Food= np.array(df["Food"])
Sleep = np.array(df["Sleep"])
School = np.array(df["School"])
Mood = np.array(df["Mood"])

F_mean = Food.mean()
Sl_mean = Sleep.mean()
Sc_mean = School.mean()
M_mean = Mood.mean()




# Set up the figure and subplots
fig, axs = plt.subplots(figsize=(8, 6))

# Create the boxplot
axs.boxplot(n_df, labels=['Food', 'Sleep', 'School', 'Mood'])

# Add some padding to the plot
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Show the plot
plt.show()

