# 74__listbox

def submit():
    choice = str(listbox.get(listbox.curselection()))
    # från innehåll ta objekt med nyckel någon av 1,2,3,4,5
    print("You have ordered a "+choice)

nr = 5
def add():
    global nr
    nr += 1
    if str(entry_box.get())+"" != "":
        listbox.insert(listbox.size(), entry_box.get()) # istället för listbox.size() skulle nr kunna användas
    listbox.config(height=listbox.size())
    entry_box.delete(first=0, last=END)

def delete():
    try:
        listbox.delete(listbox.curselection())
    except:
        print("you must select an item to delete")
    listbox.config(height=listbox.size())

from tkinter import *
window = Tk()

listbox = Listbox(window, bg="#fafafa",
                    font=("Constantia", 20),
                    width=12,
                    height=5)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Taco")
listbox.insert(3, "Hamburger")
listbox.insert(4, "Kebab")
listbox.insert(5, "Hotdog")

listbox.config(height=listbox.size())
# metod för att ändra storleken till minimum

entry_box = Entry(window)
entry_box.pack()


submit_button = Button(window, text="submit", command=submit)
submit_button.pack()
add_button = Button(window, text="add", command=add)
add_button.pack()
del_button = Button(window, text="del", command=delete)
del_button.pack()

window.mainloop()