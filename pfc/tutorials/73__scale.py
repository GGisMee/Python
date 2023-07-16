# 73__scale
from tkinter import *
window = Tk()

def submit_func():
    print("the temp is, "+ str(scale.get())+" degrees C")

scale = Scale(  window, 
                from_=100, 
                to=0,
                length=600,
                width=10,
                orient=VERTICAL, # horizontal funkar med
                font=("Consolas", 20),
                tickinterval=10,
                #showvalue= 0, # hides current value
                troughcolor="lightblue",
                fg="orange",
                bg="gray"
                )

button = Button(window, text="submit", command=submit_func)

scale.set(43) # start value

def def_pack_func(*items):
    items = list(items)
    for i in items:
        i.pack()

def_pack_func(scale, button)
window.mainloop()