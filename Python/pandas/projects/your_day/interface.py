from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import os
import numpy as np
from datetime import datetime
import datetime as dt_a
from tkinter.ttk import Notebook


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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
def inp_page_1():   
    global sub_notebook_frame 
    def upload(list_of_input, store_variable):
        global df
        global time_until_next
        global s_df
        


        # Format the date
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        daytype = int(now.strftime("%w"))
        if daytype == 0: daytype = 7
        # ger tids skillnaden mellan senaste dagen och idag
        time_diff = datetime.strptime(today, "%Y-%m-%d")- datetime.strptime(np.array(df["Date"])[-1], "%Y-%m-%d")

        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + dt_a.timedelta(days=1)
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
        now = datetime.now()
        # ger tids skillnaden mellan senaste dagen och idag

        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + dt_a.timedelta(days=1)
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
def grouped_graph_all_2():
    global grouped_graph_main_frame
    grouped_graph_main_frame = Frame(window)

    # om någon av de övre alternativ knapparna trycks på
    def b_fixed(inp):
        global graph_frame
        try:
            graph_frame_l.pop(-1).pack_forget()
        except IndexError:
            print("err")
            return 1
        prod_graph(inp)
        return 0


    # när man submittar ett nummer i gruppering
    def submittion_b():
        global graph_frame
        inp = (inp_t.get())
        try:
            inp = int(inp)
        except ValueError:
            print("Not right class, must be number")
            return 1
        graph_frame_l.pop(-1).pack_forget()
        prod_graph(inp)
        return 0

    inp_frame = Frame(grouped_graph_main_frame)
    inp_frame.pack()
    top_frame = Frame(inp_frame)
    top_frame.pack()
    inp_t = Entry(top_frame)
    inp_t.grid(row=0, column=0)
    but_t = Button(top_frame, text="Submit", command=submittion_b)
    but_t.grid(row=0,column=1)
    graph_frame_l = []
    down_frame = Frame(inp_frame)
    down_frame.pack()
    choices_intervals = ["Day","Half week", "Week","2 Week", "Month", "4 Month"]
    choices_numbs = [1,3,7,14,30,120]
    for i,el in enumerate(choices_intervals):
        n = (choices_numbs[i])
        b = Button(down_frame, text=el, command=lambda n=n:b_fixed(n))
        b.grid(row=0, column=i)
    del choices_numbs, choices_intervals

    # input = int(input("Write the groupation: "))
    def prod_graph(inp):
        graph_frame = Frame(grouped_graph_main_frame)
        graph_frame.pack()
        graph_frame_l.append(graph_frame)
        if inp == 1:
            x_axeln = np.vectorize(lambda element: element.day)(np.vectorize(lambda element:datetime.strptime(element, '%Y-%m-%d'))(np.array(df.sort_index()["Date"])))
            Food = np.array(df["Food"])
            Sleep = np.array(df["Sleep"])
            School = np.array(df["School"])
            Mood = np.array(df["Mood"])
            mean_list_tot = [Food, Sleep, School, Mood]

        else:
            Date = np.vectorize(lambda element:datetime.strptime(element, '%Y-%m-%d'))(np.array(df.sort_index()["Date"]))
            day_date = np.vectorize(lambda element: element.day)(Date)
            # print(day_date)
            # print()

            start_day = Date[0]
            # print(Date)
            ind_arr = np.array([0,0])
            for i,element in enumerate(Date):
                if (element-start_day).days > inp-1:
                    # print(np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i-1])[0])))
                    # print(ind_arr)
                    ind_arr = np.vstack((ind_arr, np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i-1])[0]))))
                    # print("new startvar", element)
                    start_day = element
                if i == len(Date)-1:
                    ind_arr = np.vstack((ind_arr, np.hstack((np.where(Date==start_day)[0], np.where(Date==Date[i])[0]))))

            ind_arr = ind_arr[1:]
            # print(ind_arr)
            # print("\n\n")
            list_of_formated_dates = np.array(np.zeros(inp))
            for el in ind_arr:
                list = Date[el[0]:el[1]+1]
                list = np.pad(list, (0,(inp-(len(Date[el[0]:el[1]])+1))), mode="constant")
                list[np.where(list==0)] = datetime(1,1,1)
                list = np.vectorize(lambda el2: el2.strftime("%Y-%m-%d"))(list)
                list_of_formated_dates = np.vstack((list_of_formated_dates, list))
            list_of_formated_dates = list_of_formated_dates[1:]
            # print("\n\n")
            # print(list_of_formated_dates)
            # print("\n\n")

            mean_list_tot = np.zeros(4)
            x_axeln = np.array(0)
            # print(list_of_formated_dates, "\n")
            for el in list_of_formated_dates:
                x_obj: str
                el1 = datetime.strptime(el[0], '%Y-%m-%d').day
                el2 = datetime.strptime(el[-1], '%Y-%m-%d').day
                l = len(el)
                while el2 == 1:
                    l-=1
                    el2 = datetime.strptime(el[l], '%Y-%m-%d').day
                # print(el1, el2)
                if el1 == el2:
                    x_obj = el1
                else:
                    x_obj = f"{el1}-{el2}"
                x_axeln = np.vstack((x_axeln, x_obj))
                list = np.transpose(np.array(df[df['Date'].isin(el)])[:,2:])
                mean_list = np.mean(list, axis=1)
                # print(mean_list)
                mean_list_tot = np.vstack((mean_list_tot, mean_list))
            mean_list_tot = np.transpose(mean_list_tot[1:])
            x_axeln = x_axeln.reshape((1,-1))[0][1:]
            print(x_axeln)

            # print("\n\n")
            # print(mean_list_tot)
            # felet just nu är att x_axeln ger 0001-01-01 på de som inte är fulla, den måste tas bort nu
            # kanske en while loop som kör näst närmaste till inga 0001-01-01 finns kvar och om den är samma så skriver den bara samma
            # print(mean_list_tot)

        print(x_axeln, mean_list_tot)
            # för x axeln
        fig, axs = plt.subplots(figsize=(8, 6), dpi=50)
            # print(mean_list_tot)
        axs.set_title("Your day")
        axs.set_ylabel("Days")
        axs.set_xlabel("Grade")
        axs.plot(x_axeln,mean_list_tot[0], "ro-",  label="Food", linewidth=3)
        axs.plot(x_axeln,mean_list_tot[1], "go-",  label="Sleep", linewidth=3)
        axs.plot(x_axeln,mean_list_tot[2], "bo-",  label="School", linewidth=3)
        axs.plot(x_axeln,mean_list_tot[3], "yo-",  label="Mood", linewidth=3)
        axs.set_xticks(x_axeln) # de kommer visas korrekt
        axs.legend()

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        graph_frame.update()
    prod_graph(7)
    # Run the Tkinter event loop
def week_month_all_3():
    pass
    #* insert week_mont_all


# baren med val av sidor
Val_bar = Notebook(window)    

# Skapar allt
inp_page_1()
grouped_graph_all_2()





# sub for submittion, in inp_page_1
Val_bar.add(sub_notebook_frame, text="Submittion")
Val_bar.add(grouped_graph_main_frame, text="grouped graph")

Val_bar.pack(expand=True,fill="both") 
# Label(tab2, text="This is in tab 2", width=50, height=25).pack()


window.mainloop()