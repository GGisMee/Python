import tkinter as tk
from datetime import datetime 
import pandas as pd
import sys
import numpy as np

df = pd.read_csv(f"{sys.path[0]}/records.csv",index_col="ID")
print(df.sort_values(df["Score"]))
exit()

window = tk.Tk()
now = datetime.now()
today = now.strftime("%Y-%m-%d")
print(today)
exit()


window.mainloop()