import pandas as pd
from printing import prints
df = pd.read_csv("pokemon_data.csv")

prints(df.sort_values("Name"), ascending=False)

prints(df.sort_values(["Name", "HP"], ascending=[1, 0]))
# sorterar som separata listor, uppstigande i namn, nedstigande i HP