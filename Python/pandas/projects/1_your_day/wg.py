import tkinter as tk

root = tk.Tk()
root.geometry("200x200")
# create a frame that will fill the entire interface
frame = tk.Frame(root)

frame.pack(fill=tk.BOTH, expand=True)

# create a widget and center it within the frame
widget = tk.Label(frame, text="Hello, World!")
widget.place(anchor="center", relx=0.5, rely=0.5)

root.mainloop()
