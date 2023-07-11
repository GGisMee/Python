import tkinter as tk
from datetime import datetime 
import pandas as pd
import sys
import numpy as np
global df
from Table import Table

window = tk.Tk()

def show_table(Name):
    global window
    df = pd.read_csv(f"{sys.path[0]}/records.csv",index_col="ID")

    def add(Name, Score):
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        df.loc[len(df)] = [str(Name), Score, str(today)]




    add(Name, 300)
    table = Table(window)
    table.populate(df.sort_values(by=['Score'], ascending=False), fill_same=True, id=True)

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
