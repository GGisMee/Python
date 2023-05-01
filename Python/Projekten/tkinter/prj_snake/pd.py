import pandas as pd


df = pd.read_csv('Python (kopia)/Projekten/prj_snake/storage.csv')
print(df["#"])
max = int(df['#'].max())
new_row = pd.DataFrame({'#':[max+1], 'length':[2], 'time':[3]})
print(new_row)
df = pd.concat([df,new_row], ignore_index=False, axis=0, join='outer')
print(df)
try:    
    df = df.drop(columns=["Unnamed: 0"])
except KeyError:
    pass
df.to_csv('Python (kopia)/Projekten/prj_snake/storage.csv')
