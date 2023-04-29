# 78__open_a_file_file_dialog
from tkinter import *
from tkinter import filedialog
window = Tk()

def openFile():
    fp = filedialog.askopenfilename(     initialdir="C:\\Users\\Administrator\\OneDrive - ABB Gymnasiet\\Programmeringen är i denna foldern\\Python (kopia)\Code_storage\\pfc\\tutorials",
                                        title="Open file",
                                        filetypes= (("text files", ".txt"), ("all files", "*.*")),
                                        )
    # välj en fil, inital directory = var den ska börja, vad som visas
    print(fp)
    file = open(fp, "rt")
    print(file.read())
    file.close()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()