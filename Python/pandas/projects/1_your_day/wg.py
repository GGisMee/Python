import tkinter as tk

root = tk.Tk()

# create a frame that will fill the entire interface
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# create a widget and center it within the frame
widget = tk.Label(frame, text="Hello, World!")
widget.pack(side=tk.TOP, anchor=tk.CENTER)

root.mainloop()
