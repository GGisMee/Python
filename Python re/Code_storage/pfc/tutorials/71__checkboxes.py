# 71__checkbox
from tkinter import *
window = Tk()

def display():

    if x.get() == 1:
        print("You agree")
    else:
        print("You disagree")

x = IntVar()

check_button = Checkbutton( window, 
                            text="I agree to something",
                            font=("Arial", 20),
                            fg="gray",
                            bg="#00FF00",
                            activebackground="#00FF00",
                            activeforeground="black",
                            variable=x,
                            onvalue=1,
                            offvalue=2,
                            command=display,
                            padx=25,
                            pady=10,
                            
                            )
check_button.pack()


window.mainloop()