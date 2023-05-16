from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import os
import numpy as np
import datetime
from tkinter.ttk import Notebook
def vec(func, arr):
    return (np.array(list(map(func, arr))))

df = pd.read_csv("Python/pandas/projects/your_day/mydata.csv", index_col='ID')
s_df_s = pd.read_csv("Python/pandas/projects/your_day/status_df.csv", index_col='ID')
s_df = np.array(s_df_s)[0]

# för att skriva >< kan man använda knappen till vänster om 1

window = Tk()
geometry = 800
window.geometry(f"{geometry}x{geometry}")


time_until_next: str
done_today: bool



# inlämning av data sidan
def interface1():   
    global sub_notebook_frame 
    def upload(list_of_input, store_variable):
        global df
        global time_until_next
        global s_df
        


        # Format the date
        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d")
        daytype = int(now.strftime("%w"))
        if daytype == 0: daytype = 7
        # ger tids skillnaden mellan senaste dagen och idag
        time_diff = datetime.datetime.strptime(today, "%Y-%m-%d")- datetime.datetime.strptime(np.array(df["Date"])[-1], "%Y-%m-%d")

        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        time_diff2 = tomorrow - now
        total_seconds = int(time_diff2.total_seconds())
        hours = (total_seconds // 3600)
        minutes = ((total_seconds % 3600) // 60)
        seconds = (total_seconds % 60)
        time_until_next = f"{hours}:{minutes}:{seconds}"
        if time_diff.days == 0:
            return 1

        if any(not isinstance(x, (int, float)) or x > 10 for x in list_of_input):
            print("Error: not number or to high/low")
            exit()
        for i,el in enumerate(store_variable):
            if not el.get():
                list_of_input[i] = None
        store_variable = (vec(lambda x: x.get(), store_variable))

        df.loc[len(df)] = [today,daytype, list_of_input[0], list_of_input[1], list_of_input[2], list_of_input[3]]
        print(df)
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_path, 'mydata.csv')
        df.to_csv(file_path, index=True)

        print(s_df_s, "\n")
        s_df_s.loc[0] = store_variable
        file_path2 = os.path.join(dir_path, 'status_df.csv')
        s_df_s.to_csv(file_path2, index=True)
        return 0


    def submittion_func():
        global done_today

        submission_frame.pack_forget()
        done_today =  upload(list(map(lambda x: x.get(), list_of_scale)), store_variable)
        print(f"\n  -----  done_today:{done_today}  ----  \n")
        # weiter arbeiten
        if not done_today:
            print("submitted")
        after_frame_func()
        # Show the new screen frame
        
        
    def update_label(text_to_description):
        now = datetime.datetime.now()
        # ger tids skillnaden mellan senaste dagen och idag

        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        time_diff2 = tomorrow - now
        total_seconds = int(time_diff2.total_seconds())

        hours = str(total_seconds // 3600)
        minutes = str((total_seconds % 3600) // 60)
        seconds = str(total_seconds % 60)

        
        if int(hours) < 10:
            hours = "0"+hours
        if int(minutes) < 10:
            minutes = "0"+minutes
        if int(seconds) < 10:
            seconds = "0"+seconds

        time_until_next = f"{hours}:{minutes}:{seconds}"
        if done_today:
            text2 = f"Your submission has already accepted, \nnext submittion may be sent in: {time_until_next}"
        else:
            text2 = f"Your submission has accepted, \nnext submittion may be sent in: {time_until_next}"

        text_to_description.config(text=text2)
        text_to_description.after(1000, update_label, text_to_description)



    
    sub_notebook_frame = Frame(window)
    
    submission_frame = Frame(sub_notebook_frame)
    scale_frame = Frame(submission_frame, background="#ebebeb")
    scale_frame.pack()
    l = ["Food", "Sleep", "School", "Mood"]
    list_of_scale = []
    store_variable = []
    for i in range(0,4):
        scale = Scale(scale_frame, 
                    from_=0,
                    to=10,
                    length=geometry/2,
                    width=geometry/40,
                    resolution=0.5,
                    orient=HORIZONTAL, # horizontal funkar med
                    font=("Consolas", 20),
                    #showvalue= 0, # hides current value
                    troughcolor="#b4bdcc",
                    fg="black",
                    bg="#ebebeb"
                    )
        checkbox_val = BooleanVar(value=str(s_df[i]))
        cb = Checkbutton(scale_frame, variable=checkbox_val)
        cb.grid(column=1, row=i)
        store_variable.append(checkbox_val)
        


        scale.grid(column=2, row=i,)
        list_of_scale.append(scale)


        label = Label(scale_frame, text=l[i], font=("Consolas", 20))
        label.grid(column=0, row=i)
    button = Button(submission_frame, text="Submit", font=("Consolas", 20), width=10, height=1, command=submittion_func)
    button.pack()
    submission_frame.pack()


    # after frame, when done with submittion
    def after_frame_func():
        after_frame = Frame(sub_notebook_frame)
        after_frame.pack(fill=BOTH, expand=True)
        in_after_frame = Frame(after_frame, width=400, height=400, bg="#ebebeb")
        in_after_frame.place(anchor="center", relx=.5, rely=.5)
        if done_today:
            image = Image.open("Python/pandas/projects/your_day/alr_done.png")
        else:
            image = Image.open("Python/pandas/projects/your_day/check_bok.png")

        # Scale the image to 50% of its original size
        new_width = int(geometry/4)
        new_height = int(geometry/4)
        image = image.resize((new_width, new_height))

        # Convert the image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)
        # resize the image


        # Scale the photo object down by a factor
        photo_label = Label(in_after_frame, image=photo)
        photo_label.image = photo
        photo_label.pack()
        subtext: str
        if done_today:
            subtext = "Already submitted"
            text2 = f"Your submission has already been accepted, \nnext submittion may be sent in: {time_until_next}"
        else:
            subtext = "Submitted"
            text2 = f"Your submission has been accepted, \nnext submittion may be sent in: {time_until_next}"

        label_beneath_photo = Label(in_after_frame, text=subtext, font=("Consolas", 30, "bold"), width=15, height=1)
        label_beneath_photo.pack()
        text_to_description = Label(in_after_frame, 
                                    text=text2, 
                                    font=("Consolas", 20, "normal"), width=100, height=2) # fixa så den wrappar kanske genom wraplength
        text_to_description.pack()
        text_to_description.after(1000, update_label(text_to_description))
        
Val_bar = Notebook(window)    
interface1()



# baren med val av sidor

Val_bar.add(sub_notebook_frame, text="Submittion")
Val_bar.pack(expand=True,fill="both") 
# Label(tab2, text="This is in tab 2", width=50, height=25).pack()


window.mainloop()