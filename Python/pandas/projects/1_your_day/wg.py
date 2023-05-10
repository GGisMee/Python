# 83__window_tabs
from tkinter import *
from tkinter import ttk # ger notebook

window = Tk()
notebook = ttk.Notebook(window) # windget som styr samling av windows/displayer

tab1 = Frame(notebook) # ny ram för notebook
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True,fill="both") 
# expan = kan fylla oanvänd plats
# fill = fyller utrymmet i x och y led, annars skriv bara "x" eller "y"

Label(tab1, text="This is in tab 1", width=50, height=25).pack()
Label(tab2, text="This is in tab 2", width=50, height=25).pack()


window.mainloop()