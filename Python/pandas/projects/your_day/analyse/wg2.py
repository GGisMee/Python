import tkinter as tk

root = tk.Tk()

# Create a frame
frame = tk.Frame(root, width=200, height=200, bg="blue")
frame.pack()

# Create a label inside the frame
label = tk.Label(frame, text="Hello World!")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
