# 69__buttons
from tkinter import *
window = Tk()
window.geometry("400x400")
count = 0
photo = PhotoImage()

def click():
    global count, button
    count += 1
    print("hello, you clicked the button "+ str(count))
    button.config(text=("Click me! "+str(count)))

button = Button(    master=window,
                    text="Click me! "+str(count),
                    command=click, # onclick...
                    font=("Comic Sans", 30),
                    fg="gray",
                    bg="black",
                    activebackground="white",
                    activeforeground="green",
                    state=ACTIVE, #disabled för att stänga av buttonen
                    )
button.pack()

window.mainloop()