# 82__new_windows
from tkinter import *

def create_top_window():
    new_window = Toplevel()
    # toplevel är en nytt fönster öven andra fönster
    # Som är länkat till det undre fönstret
    # alltså finns ett sammanband t.ex. avslut av bottom leder till avslut av top

def create_ind_window():
    new_window = Tk()
    # detta leder till ett oberoende fönster 
    window.destroy()
    # detta förstör gamla fönstret
window = Tk()



Button(window, text="Create new  ind window", command=create_ind_window).pack() 
Button(window, text="Create new top window", command=create_top_window).pack() 

window.mainloop()