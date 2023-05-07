import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("Python/pandas/projects/1_your_day/mydata_ext.csv", index_col='ID')

Date = np.array(df["Date"])
Date = reversed(list(map(lambda element:datetime.strptime(element, '%Y-%m-%d'), Date)))
last = Date[0]
# array with the indexes of the 
ind_arr = np.array()

for i in Date:
    i+=1