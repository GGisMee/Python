import tkinter as tk
import time
import threading

window = tk.Tk()
while 1 != 0:
    def wfunc(event):
        print("w")
    def sfunc(event):
        print("s")

    window.bind("<w>", wfunc)
    window.bind("<s>", sfunc)
    time.sleep(0.01)
    window.update()
window.mainloop()