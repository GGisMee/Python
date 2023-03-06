import pandas as pd
from printing import prints

# df = pd.read_csv("pokemon_data.csv")
# istället
dfs = pd.read_csv("pokemon_data.csv")

new_df = pd.DataFrame(columns=dfs.columns)
def part():
    global new_df
    i = 0
    for df in pd.read_csv("pokemon_data.csv", chunksize=5):
        i+=1
        print()
        print(f"CHUNK DF {i}")
        print()
        # nu är df bara 5 rader

        if i==5:
            return
        
part()
