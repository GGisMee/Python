# 75__messagebox
from tkinter import *
from tkinter import messagebox

def click():
    try:
        inp = int(entrybox.get())
    except ValueError:
        print("must be number")
        return
        
    
    
    if inp == 1:
    # för information
        messagebox.showinfo(title="This is an info message box", message="This is a simple message")
    elif inp == 2:
    # för varning
        messagebox.showwarning(title="Warning", message="This is a simple warning")

    # show error
    elif inp == 3:
        messagebox.showerror(title="Something went wrong", message="This is a big problem")

    # Usr input
    elif inp == 4:
        # gå vidare eller bakåt
        if messagebox.askokcancel(title="Do you understand?", message="Click ok to continue"):
            print("You accepted. often continue")
        else:
            print("Often go back, ")
    elif inp == 5:
        # retry eller bakåt
        while messagebox.askretrycancel(title="Do you understand?", message="Click retry to retry, else break"):
            print("you retry, click called")
        else:
            print("Often go back, ")

    elif inp == 6:
        # ja eller nej
        if messagebox.askyesno(title="Do you understand?", message="Do you agree, disagree?"):
            print("nice to know")
        else:
            print("sad")

    elif inp == 7:
        msgba = messagebox.askyesnocancel(title="Do you understand?", message="Do you like to code?", icon ="info") # ikånen kan ändras här
        if msgba == True:
            print("nice that you like it")
        elif msgba == False:
            print("Thats bad")
        else:
            print("you dodged the question")
            
    else:
        return

        


window = Tk()

entrybox = Entry(window)
entrybox.pack()

btn = Button(window, command=click, text="click me!")
btn.pack()

window.mainloop()