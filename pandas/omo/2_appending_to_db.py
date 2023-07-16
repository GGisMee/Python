import pandas as pd
import os
df = pd.read_csv("Python/pandas/omo/mydata.csv", index_col='ID')
print(df)
df.loc[len(df)] = [3, 8, 5]
print(df)

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path, 'my_new_df.csv')
df.to_csv(file_path, index=True)
