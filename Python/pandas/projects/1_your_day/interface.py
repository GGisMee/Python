from tkinter import *
from PIL import Image, ImageTk
def submittion_func():
    print("submitted")
    submission_frame.pack_forget()
    # Show the new screen frame
    after_frame.pack()


window = Tk()
geometry = 800
window.geometry(f"{geometry}x{geometry}")

submission_frame = Frame(window)
submission_frame.pack()

scale_frame = Frame(submission_frame, background="blue")
scale_frame.pack()
l = ["Food", "Sleep", "School", "Mood"]
for i in range(0,4):
    scale = Scale(  scale_frame, 
                from_=0,
                to=10,
                length=geometry/2,
                width=geometry/40,
                resolution=0.1,
                orient=HORIZONTAL, # horizontal funkar med
                font=("Consolas", 20),
                #showvalue= 0, # hides current value
                troughcolor="#b4bdcc",
                fg="black",
                bg="#ebebeb"
                )
    scale.grid(column=1, row=i)

    label = Label(scale_frame, text=l[i], font=("Consolas", 20))
    label.grid(column=0, row=i)
button = Button(submission_frame, text="Submit", font=("Consolas", 20), width=10, height=1, command=submittion_func)
button.pack()


# after frame, when done with submittion
after_frame = Frame(window)
label = Label(after_frame, text="Nice")
label.pack()




image = Image.open("Python/pandas/projects/1_your_day/check_bok.png")

# Scale the image to 50% of its original size
new_width = int(geometry/4)
new_height = int(geometry/4)
image = image.resize((new_width, new_height))

# Convert the image to a Tkinter PhotoImage
photo = ImageTk.PhotoImage(image)
# resize the image


# Scale the photo object down by a factor
photo_label = Label(after_frame, image=photo)
photo_label.pack()

window.mainloop()