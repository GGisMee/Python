import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

# Alla översta prints(df.columns)
# prints(df.columns)

# Alla data i en kolumn
prints(df["Name"][0:8]) # i detta fallet 0 till 8
prints(df[["Name", "HP", "Type 1"]][0:8]) # i detta fallet 0 till 8
# flera samtidigt ^

# Alla data i en rad, index locate
prints(df.iloc[1:4,1],3) # i detta faller rad 1 till 4 och bara info från första kolumn
#             [rad, kolumn]
# df.loc, locate
prints(df.loc[df["Type 1"] == "Fire"],3)



# iterrera över alla
for index, row in df.iterrows():
    if 10<index<20: 
        print(index, row["Name"])

prints(df.describe())
