import tkinter as tk
import pandas as pd
from datetime import datetime
import numpy as np
import calendar
from tkinter import Tk, Label



marked_dates = ['2022-01-01','2023-05-15', '2023-05-20', '2023-05-25']
def create_calendar(year, month, marked_dates):
    #! Nuvarande månaden byt sen
    year = datetime.now().year
    month = datetime.now().month
    cal = calendar.monthcalendar(year, month)
    
    # Skapar fönster
    root = Tk()
    
    # Schleife über die Tage im Kalender
    for i, week in enumerate(cal):
        print("new week: ", i)
        for i2, day in enumerate(week):
            # Überprüfen, ob der Tag in der markierten Datenliste enthalten ist
            print(year, month, day)
            try:
               date = datetime(year, month, day)
            except ValueError:
                break
            if date.strftime('%Y-%m-%d') in marked_dates:
                # Hintergrundfarbe auf schwarz ändern
                label = Label(root, text=day, bg='black', fg='white')
                print(label)
            else:
                label = Label(root, text=day)
            label.grid(row=i, column=i2)
    
    root.mainloop()
create_calendar(year="", month="", marked_dates=marked_dates)