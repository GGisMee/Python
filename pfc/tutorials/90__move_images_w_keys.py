# 90__move_images_w_keys
inp = input()
if inp == 0:

    from tkinter import *
    window = Tk()
    geometry = 500
    window.geometry(f"{geometry}x{geometry}")


    def wfunc(event):
        label.place(x=label.winfo_x(), y=label.winfo_y()-10)
        print(event.keysym)
    def sfunc(event):
        print(event.keysym)
        label.place(x=label.winfo_x(), y=label.winfo_y()+10)
    def afunc(event):
        label.place(x=label.winfo_x()-10, y=label.winfo_y())
        print(event.keysym)
    def dfunc(event):
        label.place(x=label.winfo_x()+10, y=label.winfo_y())
        print(event.keysym)

    window.bind("<w>", wfunc)
    window.bind("<s>", sfunc)
    window.bind("<a>", afunc)
    window.bind("<d>", dfunc)


    myimage = PhotoImage(file="/Users/gustavgamstedt/Desktop/Hemma_folder/programmering/Python (kopia)/Code_storage/pfc/till_library/racecar.png")
    label = Label(window, image=myimage)
    label.place(x=0,y=0)
   
else:

    from tkinter import *
    window = Tk()
    geometry = 500
    window.geometry(f"{geometry}x{geometry}")
    
    def wfunc(event):
        canvas.move(myimage, 0, -10)
        print(event.keysym)
    def sfunc(event):
        canvas.move(myimage, 0, 10)
        print(event.keysym)
    def afunc(event):
        canvas.move(myimage, -10, 0)
        print(event.keysym)
    def dfunc(event):
        canvas.move(myimage, 10, 0)
        print(event.keysym)

    window.bind("<w>", wfunc)
    window.bind("<s>", sfunc)
    window.bind("<a>", afunc)
    window.bind("<d>", dfunc)


    canvas = Canvas(window, width=500, height=500,bg="black")
    canvas.pack()

    photoimage = PhotoImage(file="/Users/gustavgamstedt/Desktop/Hemma_folder/programmering/Python (kopia)/Code_storage/pfc/till_library/racecar.png")
    myimage = canvas.create_image(0,0, image=photoimage, anchor=NW)

    window.mainloop()

