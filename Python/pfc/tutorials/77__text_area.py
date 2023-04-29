# 77__text_area
from tkinter import *
window = Tk()
txt_area = Text(window, bg="light yellow", font=("Ink Free", 20), width=20, height=8, padx=10, pady=10)
txt_area.pack()

def btn():
    inp = txt_area.get("1.0", END)
    print(inp)


btn = Button(window, command=btn, text="Submit")
btn.pack()
window.mainloop()