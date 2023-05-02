import pandas as pd
# tar datan till dokumentet
df = pd.read_csv("pokemon_data.csv")
df_excel = pd.read_excel("pokemon_data.xlsx")
df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t")

print(df.head(2)) # visar 2 högsta raderna
print(df_excel.tail(2)) # visar 2 lägsta raderna
