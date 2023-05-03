import pandas as pd
import os
import numpy as np

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata.csv", index_col='ID')

Date = np.array(df.iloc[:, 0])
print(np.array(Date[-1]))