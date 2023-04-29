# 93__clock_program
from tkinter import *
from time import *
window = Tk()

time_box = Frame(window, bg="black")
time_box.pack()

time_label = Label(time_box, font=("Arial", 50), fg="#00ff00", bg="black")
time_label.pack()

def update():
    time_string = strftime(":%M:%S")

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    if strftime("%p") == "PM":
        time_string = str(int(strftime("%I"))+12)+time_string
    else:
        strftime("%I")+time_string
    time_label.config(text=time_string)

    time_label.after(1000, update) # rekursiv funktion
    # updaterar och förändrar sig själv

day_label = Label(time_box, font=("Ink Free", 25), bg="black", fg="lightgray")
day_label.pack()

date_label = Label(time_box, font=("Comic Sans", 30), bg="black", fg="lightgray")
date_label.pack()

while True:
    update()
    sleep(1)
    window. update()

window.mainloop()