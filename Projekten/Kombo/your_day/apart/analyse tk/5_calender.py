import pandas as pd
from datetime import datetime
import numpy as np
import calendar
from tkinter import *
from dateutil.relativedelta import relativedelta

#* idea have with year view as well maybe gradient white to black depending on use
global datetime_obj, marked_dates, frame_pack

df = pd.read_csv("Python/pandas/projects/your_day/final/mydata.csv", index_col='ID')
marked_dates = list(df["Date"])
window = Tk()
window.geometry("400x400")
datetime_obj = datetime.now()
calendar_frame = Frame(window)
calendar_frame.pack()
frame_pack = []

def forward():
    global datetime_obj
    if datetime_obj.month == 12:
        datetime_obj = datetime_obj.replace(year=datetime_obj.year + 1, month=1)
    else:
        datetime_obj = datetime_obj.replace(month=datetime_obj.month + 1)
    for_back(datetime_obj)
def backward():
    global datetime_obj
    if datetime_obj.month == 1:
        datetime_obj = datetime_obj.replace(year=datetime_obj.year - 1, month=12)
    else:
        datetime_obj = datetime_obj.replace(month=datetime_obj.month - 1)
    for_back(datetime_obj)

def for_back(datetime_obj):
    # print(datetime_obj.month)
    frame_pack.pop().pack_forget()
    create_calendar(datetime_obj)

# indicator labels
indication_label = Label(calendar_frame, text="Year-Month",  font=("Helvetica",13, "bold"))
indication_label.pack()


# knapparna
button_frame = Frame(calendar_frame)
button_frame.pack()
back_button = Button(button_frame, text="back", bg="green", command=backward)
back_button.grid(column=0,row=0)
forward_button = Button(button_frame, text="forward", bg="yellow", command=forward)
forward_button.grid(column=1,row=0)

def create_calendar(datetime_obj):
    month = datetime_obj.month
    year = datetime_obj.year
    cal = calendar.monthcalendar(year, month)

    indication_label.config(text=(f"{year} {calendar.month_name[month]}"))

    dates_frame = Frame(calendar_frame)
    dates_frame.pack()
    frame_pack.append(dates_frame)
    # print(cal)
    # Veckorna försig
    for i, week in enumerate(cal):
        # print("new week: ", i)
        # dagarna försig
        for i2, day in enumerate(week):
            # print(year, month, day)
            if not day:
                # om den veckodagen inte finns hoppas den över t.ex. 2023-7-0
                continue
            else:
                date = datetime(year, month, day)
            if date.strftime('%Y-%m-%d') in marked_dates:
                # Svart bakgrund
                frame = Frame(dates_frame, width=20, height=20, bg='#b5b5b5')
                frame.pack_propagate(False)
                label = Label(frame, text=day, bg='#b5b5b5', font=("Helvetica",13))
                # print(label)
            else:
                frame = Frame(dates_frame, width=20, height=20, bg='#dedede')
                frame.pack_propagate(False)
                label = Label(frame, text=day, bg='#dedede', font=("Helvetica",13))
            label.pack()
            frame.grid(row=i, column=i2)
    print("done")
    window.mainloop()
create_calendar(datetime_obj)