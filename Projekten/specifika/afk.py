import pyautogui
import tkinter as tk
import threading
import time
next_time_between=60

def strt_fn():
    global on
    on = True
    pause_event.set()
    print("on")


def pause_fn():
    global on
    on = False
    print("off")
    pause_event.clear()


def time_between_fn(value):
    global next_time_between
    next_time_between = int(value)

time_between = 10
on = True
pause_event = threading.Event()


def main_func():
    global time_between
    while True:
        for i in range(time_between):
            if on:
                label.config(text=time_between-1 - i)
                window.update_idletasks()
                time.sleep(1)
            else:
                pause_event.wait()
        pyautogui.keyDown('a')
        time.sleep(0.5)
        pyautogui.keyUp('a')
        pyautogui.keyDown('d')
        time.sleep(0.5)
        pyautogui.keyUp('d')
        time_between = next_time_between

window = tk.Tk()
sp_frame = tk.Frame(window)
sp_frame.pack()

strt_btn = tk.Button(sp_frame, text="Start", font=("Arial"), bg="gray", command=strt_fn)
strt_btn.grid(row=0, column=0)

pause_btn = tk.Button(sp_frame, text="Pause", font=("Arial"), bg="gray", command=pause_fn)
pause_btn.grid(row=0, column=1)

scale_frame = tk.Frame(window)
scale_frame.pack()

scale = tk.Scale(scale_frame, from_=100,to=2, length=300,orient="horizontal", tickinterval=1, command = time_between_fn)
scale.grid(column=0, row=0)

label_frame = tk.Frame(window)
label_frame.pack()
label = tk.Label(label_frame, font=("Arial", 300, "bold"))
label.pack()

window.geometry("400x400")
main_t = threading.Thread(target=main_func)
main_t.start()

window.mainloop()
