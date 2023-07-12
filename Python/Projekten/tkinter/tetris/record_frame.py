import tkinter as tk
from datetime import datetime 
import pandas as pd
import sys
import numpy as np
global df
from TkTable import Table

window = tk.Tk()

def show_table(Name):
    df = pd.read_csv(f"{sys.path[0]}/records.csv",index_col="ID")

    def add(Name, Score):
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        df.loc[len(df)] = [str(Name), Score, str(today)]



    add(Name, 1100)
    table = Table(window)
    titles = pd.DataFrame({1:["Name, Score"]})
    modified_df = df.sort_values(by=['Score'], ascending=False)[:9]
    table.populate(modified_df,fill=True, fill_same=False, titles=True)
    df.to_csv(f'{sys.path[0]}/records.csv', index=True)

def test_button(entry, entry_button):
    if entry.get() == "":
        return
    entry.forget()
    entry_button.forget()


    show_table(entry.get())

def start():
    entry = tk.Entry(window)
    entry.pack(anchor="center")
    entry_button = tk.Button(window, command=lambda: test_button(entry, entry_button))
    entry_button.pack()
start()

window.mainloop()
