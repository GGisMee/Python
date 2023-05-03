import os
import pandas as pd
import time
import numpy as np
# create a sample DataFrame

import time
current_year = time.localtime().tm_year
current_month = time.localtime().tm_mon
current_day = time.localtime().tm_mday
current_type_of_day = time.localtime().tm_wday # alltså typ idag är det måndag, torsdag, söndag eller annat


compact = [current_year, current_month, current_day, current_type_of_day, current_type_of_day]
df = pd.DataFrame({'ID':[0],'Time':[compact],'Food':[0], 'Sleep': [0], 'School':[0]})

# create a new pair of columns using the assign() method
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'mydata.csv')
df.to_csv(file_path, index=False)
