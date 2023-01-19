from tkinter import *

window = Tk()
window.geometry("500x500")


canvas = Canvas(window)
canvas.pack()

photo_image = PhotoImage(file="cat folder/cat1.png")
obj = canvas.create_image(0,0, image=photo_image, anchor=NW)

window.mainloop()