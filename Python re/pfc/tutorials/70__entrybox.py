# 70__entrybox

# entry widget = textbox that accepts a singe line of user input


class console():
    log = print

from tkinter import *
window = Tk()

def submit():
    username = entry.get()
    console.log("submiting, UN: " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)
    # från str del 0 till slut

def bs():
    sum
    
    entry.delete(len(entry.get())-1, END)

def DLW():
    numerate = 0
    rn = (entry.get())
    rrn = rn[::-1]
    for i in rrn:
        numerate += 1
        if i == " ":
            break
    print(numerate, len(rn))
    final = len(rn)-numerate
    print(final)
    entry.delete(final, END)

entry = Entry(  master=window,
                font=("Arial", 20),
                bg="gray",
                fg="#00FF00",
                #show="*", # visas istället, bra för password
                
                )
entry.pack(side=LEFT)

submintbtn = Button(window, 
                    text="Submit", 
                    command=submit)
submintbtn.pack(side=RIGHT)

delbtn = Button(window, 
                    text="delete", 
                    command=delete)
delbtn.pack(side=RIGHT)

bsbtn = Button(window, 
                    text="Backspace", 
                    command=bs)
bsbtn.pack(side=RIGHT)

lastword_btn_del = Button(window, 
                    text="Del last word", 
                    command=DLW)
lastword_btn_del.pack(side=RIGHT)

window.mainloop()