# 85__progress_bar
from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    while (download < GB):
        time.sleep(0.1)
        bar['value'] += 1
        download+=1
        percent.set(str(int((download/GB)*100))+"%")
        texttask.set(str(download)+"/"+str(GB) + " GB completed")
        window.update_idletasks()
        

window = Tk()

percent = StringVar()
percent.set("0%")

texttask = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

procentlabel = Label(window, textvariable=percent).pack()
tasklabel = Label(window, textvariable=texttask).pack()

btn = Button(window, text="download", command=start).pack()

window.mainloop()