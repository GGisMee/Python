# 72__radio_buttons
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]
window = Tk()

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton( master=window, 
                                text=food[i], 
                                variable=x, 
                                value=i, # value delar upp
                                padx=25,
                                pady=2,
                                )

    radio_button.pack(anchor="w") # hamnar väster / west
window.mainloop()