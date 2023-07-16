# 80__menubar
from tkinter import *

def openFile():
    print("I opened it")

def saveFile():
    print("File has been saved")


window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
# här lägger vi till menubaren som ett specifikt element i window

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
# val element

fileMenu.add_command(label="open", command=openFile)
fileMenu.add_command(label="save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="exit", command=quit)
# nu gör vi en dropp meny på menybaren

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
# val element

editMenu.add_command(label="Control c for save")
editMenu.add_command(label="Control x for clip")
editMenu.add_separator()
editMenu.add_command(label="Control v for paste")

window.mainloop()