import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

# medelvärde
F_mean = np.array(df["Food"]).mean()
Sl_mean = np.array(df["Sleep"]).mean()
Sc_mean = np.array(df["School"]).mean()
M_mean = np.array(df["Mood"]).mean()