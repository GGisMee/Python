import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

# del 1 graf över alla värden (kan välja om specifikt senaste 30 eller så)
Food = np.array(df["Food"])
Sleep = np.array(df["Sleep"])
School = np.array(df["School"])
Mood = np.array(df["Mood"])
x = np.arange(0, len(df))
plt.title("Your day")
plt.xlabel("Day")
plt.ylabel("Grade")
plt.plot(x,Food, "ro-",  label="Food", linewidth=3)
plt.plot(x,Sleep, "go-",  label="Sleep", linewidth=3)
plt.plot(x,School, "bo-",  label="School", linewidth=3)
plt.plot(x,Mood, "yo-",  label="Mood", linewidth=3)
plt.legend()
plt.show()