import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

df_d = df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
# print(df_d) # för varje typ hittas ett medelvärde på defense i sjunkande ordning

df_s = df.groupby(['Type 1']).sum()
df_c = (df.groupby(['Type 1', 'Type 2']).count())['#']
# visar tot av typ 1 med specifikation av en viss typ 2 

print(df_c)