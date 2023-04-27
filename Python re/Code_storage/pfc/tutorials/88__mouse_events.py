# 88__mouse_events
from tkinter import *

x,y = -1, -1
window = Tk()
window.geometry("400x400")

def lfunc(event):
    print("You clicked left at "+str(event.x)+ " "+ str(event.y))
def rfunc(event):
    print("You clicked right at "+str(event.x)+ " "+ str(event.y))
    
def enter(event):
    print("You entered at "+str(event.x)+ " "+ str(event.y))

def motion(event):
    global x, y
    if x == -1: 
        x = int(event.x)
        y = int(event.y)
        return (x,y)
    else:
        xlabel.config(text=int(event.x)-x)
        ylabel.config(text=y-int(event.y))
        x = int(event.x)
        y = int(event.y)
        
        


window.bind("<Button-1>", lfunc)
window.bind("<Button-3>", rfunc)
window.bind("<Enter>", enter) # var man på nytt öppnar bilden
window.bind("<Motion>", motion) # var man på nytt öppnar bilden

frame = Frame(window, width=100, height=20)
frame.place(x=180, y=0)

xlabel = Label(frame, font=("Arial", 20))
xlabel.grid(row=0, column=0)
ylabel = Label(frame, font=("Arial", 20))
ylabel.grid(row=0, column=1)


window.mainloop()