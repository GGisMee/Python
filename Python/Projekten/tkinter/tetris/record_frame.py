import tkinter as tk
from datetime import datetime 
import pandas as pd
import sys
import numpy as np
global df
from Table import Table
df = pd.read_csv(f"{sys.path[0]}/records.csv",index_col="ID")

def add(Name, Score, Time):
    df.loc[len(df)] = [str(Name), str(Score), str(Time)]



df = df.sort_values(by=['Score'])
window = tk.Tk()
now = datetime.now()
today = now.strftime("%Y-%m-%d")
exit()


window.mainloop()