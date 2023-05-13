import pandas as pd
from datetime import datetime
import numpy as np
import calendar
from tkinter import *
from dateutil.relativedelta import relativedelta
global datetime_obj, marked_dates

df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')
marked_dates = list(df["Date"])
window = Tk()
window.geometry("400x400")
datetime_obj = datetime.now()
calender_frame = Frame(window)
calender_frame.pack()

def forward():
    global datetime_obj
    datetime_obj = datetime_obj+relativedelta(month=1)
    print("forward", datetime_obj)
    create_calendar(datetime_obj)
def backward():
    global datetime_obj
    datetime_obj = (datetime_obj-relativedelta(month=1))
    print("backward", datetime_obj)
    create_calendar(datetime_obj)


# knapparna
button_frame = Frame(calender_frame)
button_frame.pack()
back_button = Button(button_frame, text="back", bg="green", command=backward)
back_button.grid(column=0,row=0)
forward_button = Button(button_frame, text="forward", bg="yellow", command=forward)
forward_button.grid(column=1,row=0)

def create_calendar(datetime_obj):
    month = datetime_obj.month
    year = datetime_obj.year

    cal = calendar.monthcalendar(year, month)
    #! Nuvarande månaden byt sen

    dates_frame = Frame(calender_frame)
    dates_frame.pack()

    # Veckorna försig
    for i, week in enumerate(cal):
        # print("new week: ", i)
        # dagarna försig
        for i2, day in enumerate(week):
            # print(year, month, day)
            try:
               date = datetime(year, month, day)
            except ValueError:
                break
            if date.strftime('%Y-%m-%d') in marked_dates:
                # Hintergrundfarbe auf schwarz ändern
                frame = Frame(dates_frame, width=20, height=20, bg='#b5b5b5')
                frame.pack_propagate(False)
                label = Label(frame, text=day, bg='#b5b5b5')
                # print(label)
            else:
                frame = Frame(dates_frame, width=20, height=20, bg='#dedede')
                frame.pack_propagate(False)
                label = Label(frame, text=day, bg='#dedede')
            label.pack()
            frame.grid(row=i, column=i2)
    print("done")
    window.mainloop()
create_calendar(datetime_obj)