# 68__labels
from tkinter import *
Window = Tk()
Window.geometry("400x400")
label = Label(  master=Window, 
                text="Hello World", # om texten ökas tvingökas width
                font=("Arial", 40, "bold"), 
                fg="green", 
                bg="beige",
                relief=RAISED,
                borderwidth=10,
                bd=10,
                padx=20,
                pady=10, # kan ses som (min y)
                # image= photo,
                # compound="bottom",


                ) 
# label.pack() # implementerar labeln i window
label.place(x=100, y=100) # speciell placering



Window.mainloop() 