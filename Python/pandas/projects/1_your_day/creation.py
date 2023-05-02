import os
import pandas as pd
import time
# create a sample DataFrame

import time
current_year = time.gmtime().tm_year
current_month = time.gmtime().tm_mon
current_day = time.gmtime().tm_mday
compact = [current_year, current_month, current_day]

df = pd.DataFrame({'ID':[0],'Time':[compact],'Food':[0], 'Sleep': [0], 'School':[0]})

# create a new pair of columns using the assign() method
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'mydata.csv')
df.to_csv(file_path, index=False)
