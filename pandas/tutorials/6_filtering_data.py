import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

# två olika typer (&,| krävs i panda) ej (and eller or)
fil_df = df.loc[(df['Type 1']== "Grass") & (df['Type 2'] == "Poison") & (df['HP'] > 70)]
fil_df = fil_df.reset_index(drop=True, inplace=True) # gör en ny indexskala, 
#drop gör att gamla index tas bort 
#
print(fil_df)

mega_df = df.loc[~df["Name"].str.contains('Mega')]
print(mega_df) # ~ ger not