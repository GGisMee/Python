import pandas as pd
from datetime import datetime
import numpy as np
import calendar
from tkinter import *

df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')
marked_dates = list(df["Date"])
window = Tk()
window.geometry("400x400")
c_year = datetime.now().year
c_month = datetime.now().month

def create_calendar(year, month, marked_dates):
    cal = calendar.monthcalendar(year, month)
    #! Nuvarande månaden byt sen
    
    
    cal_frame = Frame(window)
    cal_frame.pack()

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
                frame = Frame(cal_frame, width=20, height=20, bg='#b5b5b5')
                frame.pack_propagate(False)
                label = Label(frame, text=day, bg='#b5b5b5')
                print(label)
            else:
                frame = Frame(cal_frame, width=20, height=20, bg='#dedede')
                frame.pack_propagate(False)
                label = Label(frame, text=day, bg='#dedede')
            label.pack()
            frame.grid(row=i, column=i2)
    print("done")
    window.mainloop()
create_calendar(year=c_year, month=c_month, marked_dates=marked_dates)