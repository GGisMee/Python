import os
import pandas as pd

# create a sample DataFrame

df = pd.DataFrame({'ID':[0],'Food':[0], 'Sleep': [0], 'School':[0]})

# create a new pair of columns using the assign() method
dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'mydata.csv')
df.to_csv(file_path, index=False)
