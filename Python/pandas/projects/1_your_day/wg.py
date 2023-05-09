from tkinter import *

root = Tk()

# create a menu
menu = Menu(root)
menu.add_command(label="Item 1")
menu.add_command(label="Item 2")
menu.add_command(label="Item 3")

# create a menubutton to display the menu
menubutton = Menubutton(root, text="Menu", menu=menu)
menubutton.pack()

root.mainloop()
