import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

## spara och skapa en ny
df.to_csv("modified.csv", index=False)
df.to_excel("modified.csv", index = False) # index visar vilket nummer på i vilken rad
df.to_csv("modified.txt", index="False", sep="\t")

