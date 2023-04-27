import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

# förändra en kolumn med info från annan

df.loc[df['Type 1'] == 'Fire', 'Type 2'] = 'Flamer'
# i detta fallet ej df = ... pga (=) tecknet över
print(df)

# reset
df = pd.read_csv("pokemon_data.csv")

df.loc[df['Attack'] > 60, ['Generation', 'Legendary']] = [2, True]
# förändring av 2

print(df)