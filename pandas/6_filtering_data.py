import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

# två olika typer (&,| krävs i panda) ej (and eller or)
fil_df = df.loc[(df['Type 1']== "Grass") & (df['Type 2']) & (df['HP'] > 80)]
print(fil_df.head(5))