import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

print(df.head(5))


# method 1
# df["Total"] = (df["HP"] + df["Attack"] + df["Defense"] + 
#                df["Sp. Atk"] + df["Sp. Def"] + df["Speed"])
# Skapar en ny datakolumn med totalen för alla dessa

# method 2:
df['Total'] = df.iloc[:,4:10].sum(axis=1) 
    # axis = 1 för horizontell addition
prints((df.head(5))["Total"])

# omplacering
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:-2]] 
prints((df.head(5)))

df = df.drop(columns=["Total"])
# raderar Totalen

