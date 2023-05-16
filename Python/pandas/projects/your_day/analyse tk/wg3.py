import tkinter as tk

root = tk.Tk()


checkbox = tk.Checkbutton(root, text="Checkbox")
checkbox.select()
checkbox.pack()

root.mainloop()
w