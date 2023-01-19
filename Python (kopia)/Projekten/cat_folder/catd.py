from tkinter import *

window = Tk()
window.geometry("500x500")

HEIGHT = 500
canvas = Canvas(window)
canvas.pack()
og_catpic = Image.open("/Users/gustavgamstedt/Desktop/Hemma_folder/programmering/Python (kopia)/Projekten/cat_folder/cat{self.cat_nr}.png")
edited_catpic=og_catpic.resize((450, 350))

photo_image = PhotoImage(file=edited_catpic)
obj = canvas.create_image(0, HEIGHT-100, image=photo_image)
window.update_idletasks()

window.mainloop()