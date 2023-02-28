import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

# Alla översta prints(df.columns)
prints(df.columns)
prints(df.Name)