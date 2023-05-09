from tkinter import *
from PIL import Image, ImageTk
def submittion_func():
    print("submitted")
    submission_frame.pack_forget()
    # Show the new screen frame
    after_frame.pack(fill=BOTH, expand=True)


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
in_after_frame = Frame(after_frame, width=400, height=400, bg="blue")
in_after_frame.place(anchor="center", relx=.5, rely=.5)




image = Image.open("Python/pandas/projects/1_your_day/check_bok.png")

# Scale the image to 50% of its original size
new_width = int(geometry/4)
new_height = int(geometry/4)
image = image.resize((new_width, new_height))

# Convert the image to a Tkinter PhotoImage
photo = ImageTk.PhotoImage(image)
# resize the image


# Scale the photo object down by a factor
photo_label = Label(in_after_frame, image=photo)
photo_label.pack()
label_beneath_photo = Label(in_after_frame, text="Submitted", font=("Consolas", 30, "bold"), width=10, height=1)
label_beneath_photo.pack()
text_to_description = Label(in_after_frame, 
                            text=f"Your submission has been accepted, next submittion may be sent in: ", 
                            font=("Consolas", 20, "normal"), width=100, height=2) # fixa så den wrappar kanske genom wraplength
text_to_description.pack()
window.mainloop()