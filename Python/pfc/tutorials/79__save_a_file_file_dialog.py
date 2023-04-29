# 79__save_a_file_file_dialog
from tkinter import *
from tkinter import filedialog
window = Tk()

def saveFile():
    file = filedialog.asksaveasfile(
        defaultextension=".txt", 
        filetypes=(("Text file", ".txt"), 
        ("Html file", ".html"),
        ("All file", ".*"),
        
        )
    )
    filetxt = str(text.get(1.0, END))
    file.write(filetxt)
    file.close


text = Text(window)
text.pack()

btn = Button(window, text="save", command=saveFile,)
btn.pack()


window.mainloop()