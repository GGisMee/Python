from tkinter import *
from PIL import Image, ImageTk
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


window = Tk()
window.geometry("500x500")

HEIGHT = 500
canvas = Canvas(window, width=400, height=400)
canvas.pack()
og_catpic = Image.open("cat2.png")
edited_catpic=og_catpic.resize((450, 350))
print(edited_catpic)
photo_imaged = ImageTk.PhotoImage(edited_catpic)
obj = canvas.create_image(0, 0, image=photo_imaged)
window.update_idletasks()

window.mainloop()