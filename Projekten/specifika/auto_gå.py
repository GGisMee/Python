# måste använda 
# pip install pyautogui 
# # först
import pyautogui
import tkinter as tk
import threading

def strt_fn():
    global on
    print("on")
    on=True

def pause_fn():
    global on
    print("off")
    on=False


on = True


window = tk.Tk()
inp_thread = tk.Frame(window)
inp_thread.pack()

strt_btn = tk.Button(inp_thread, text="Start", font = ("Arial"), bg="gray", command=strt_fn)
strt_btn.grid(row=0, column=0)

pause_btn = tk.Button(inp_thread, text="Pause", font = ("Arial"), bg="gray", command = pause_fn)
pause_btn.grid(row=0, column=1)

label_frame = tk.Frame(window)
label_frame.pack()
label = tk.Label(label_frame, font=("Arial", 300, "bold"))
label.pack()
import time
def main_func():
    while on:   
        for i in range(60):
            label.config(text=59-i)
            window.update_idletasks()
            time.sleep(1) 
        pyautogui.keyDown('a')
        time.sleep(0.5)
        pyautogui.keyUp('a')
        pyautogui.keyDown("d")
        time.sleep(0.5)
        pyautogui.keyUp('d')

time.sleep(5)
window.geometry("400x400")
main_t = threading.Thread(target=main_func)
main_t.start()



window.mainloop()