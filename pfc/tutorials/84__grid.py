# 84__grid
from tkinter import *
from tkinter import Grid
window = Tk()

entry = Entry(window, )

titleLabel = Label(window, text="Enter your info:", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)
firstNameLabel = Label(window, text="add first name:", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window, ).grid(row=1, column=1)

lastNameLabel = Label(window, text="add last name:", bg="yellow").grid(row=2, column=0)
lastNameEntry = Entry(window, ).grid(row=2, column=1)

EmailLabel = Label(window, text="add email:", bg="green", width=30).grid(row=3, column=0)
EmailEntry = Entry(window, ).grid(row=3, column=1)

btn = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()