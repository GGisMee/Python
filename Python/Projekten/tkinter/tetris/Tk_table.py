from TkTable import Table
import tkinter as tk
import numpy as np
import pandas as pd
window = tk.Tk()
ti = pd.DataFrame({'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']})
ti2 = [[0,1], ["hello", "where"], ["indigo", "orange"]]


t = Table(window)
t.populate(ti, titles=1, id=1)

window.mainloop()