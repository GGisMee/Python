import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

import re
# re = regular expression
# new_df = df.loc[df["Type 1"].str.contains('Fire|Grass', regex=True)]


new_df = df.loc[df["Name"].str.contains('^pi[a-z]*', flags=re.I , regex=True)]

 
print(new_df)
