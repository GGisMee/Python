from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import pandas as pd
import os
import numpy as np
from datetime import datetime
import datetime as dt_a
from tkinter.ttk import Notebook
from sys import path


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import calendar


def vec(func, arr):
    return (np.array(list(map(func, arr))))


df = pd.read_csv(f"{path[0]}/mydata.csv", index_col='ID')
s_df_s = pd.read_csv(f"{path[0]}/status_df.csv", index_col='ID')
s_df = np.array(s_df_s)[0]

# för att skriva >< kan man använda knappen till vänster om 1

window = Tk()
geometry = 800
window.geometry(f"{geometry}x{geometry}")
window.title("Your Day")

# icon = PhotoImage(file="Python/pandas/projects/your_day/final/day.png") # ikon över bilden, kräver att 
#* fix so it shows
window.iconbitmap(f"{path[0]}/day.ico")

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
        # print(df)
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_path, 'mydata.csv')
        df.to_csv(file_path, index=True)

        # print(s_df_s, "\n")
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
            image = Image.open("Python/Projekten/Kombo/your_day/final/alr_done.png")
        else:
            image = Image.open("Python/Projekten/Kombo/your_day/final/check_bok.png")

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
            # print(x_axeln)

            # print("\n\n")
            # print(mean_list_tot)
            # felet just nu är att x_axeln ger 0001-01-01 på de som inte är fulla, den måste tas bort nu
            # kanske en while loop som kör näst närmaste till inga 0001-01-01 finns kvar och om den är samma så skriver den bara samma
            # print(mean_list_tot)

        # print(x_axeln, mean_list_tot)
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
def week_month_all_3():
    global week_month_all_frame
    week_month_all_frame = Frame(window)
    pass
    #* insert week_mont_all

    def get_mean(df):
        F_mean = np.array(df["Food"]).mean()
        Sl_mean = np.array(df["Sleep"]).mean()
        Sc_mean = np.array(df["School"]).mean()
        M_mean = np.array(df["Mood"]).mean()
        return F_mean, Sl_mean, Sc_mean, M_mean


    date = np.array(df["Date"])
    ldate = datetime.strptime(date[-1], '%Y-%m-%d')

    # get the week
    for i,element in list(enumerate(reversed(date)))[1:]:
        element2 = datetime.strptime(element, '%Y-%m-%d')
        if ((ldate - element2).days) >= 7:
            break
    i_of_first = np.where(date == element)[0][0]
    which_date_week = date[i_of_first:]
    df_week = df[df['Date'].isin(which_date_week)]

    # get the month
    for i,element in list(enumerate(reversed(date)))[1:]:
        element2 = datetime.strptime(element, '%Y-%m-%d')
        if ((ldate - element2).days) >= 30:
            break
    i_of_first2 = np.where(date == element)[0][0]
    which_date_month = date[i_of_first2:]
    df_month = df[df['Date'].isin(which_date_month)]

    # all
    df_all = df

    # print(df_week)
    # print()
    # print(df_month)
    # print()
    # print(df_all)
    df_all = get_mean(df_all)
    df_month = get_mean(df_month)
    df_week = get_mean(df_week)

    x = np.arange(len(df_all))
    width = 0.25

    fig, ax = plt.subplots(figsize=(6, 4), dpi=50)

    ax.bar(x - width, df_all, width, label='All')
    ax.bar(x, df_month, width, label='Month')
    ax.bar(x + width, df_week, width, label='Week')


    ax.set_xlabel('Grade')
    ax.set_ylabel('Value')
    ax.set_title('Grouped Bar Chart')

    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=week_month_all_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
def box_all_4():
    global box_all_frame
    box_all_frame = Frame(window)
    n_df = (np.array(df)[:,2:])
    # print(n_df)

    # Set up the figure and subplots
    fig, axs = plt.subplots(figsize=(8, 6), dpi=40)

    # Create the boxplot
    axs.boxplot(n_df, labels=['Food', 'Sleep', 'School', 'Mood'])

    # Add some padding to the plot
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    canvas = FigureCanvasTkAgg(fig, master=box_all_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
def value_of_day_all_5():
    global value_of_day_frame
    value_of_day_frame = Frame(window)
    # fix date formater
    # print(df["Daytype"])
    ordered_day = np.array([0,0,0,0])
    for i in range(1,8):
        one_day_all_data = (np.array(df.loc[df["Daytype"] == i]))[:,2:]
        # print(one_day_all_data, "ddd")
        day_food_mean = one_day_all_data[:, 0].mean()
        day_sleep_mean = one_day_all_data[:, 1].mean()
        day_school_mean = one_day_all_data[:, 2].mean()
        day_mood_mean = one_day_all_data[:, 3].mean()
        ordered_day = np.vstack((ordered_day, [day_food_mean, day_sleep_mean, day_school_mean, day_mood_mean]))
    ordered_day = ordered_day[1:]

    # re orders them to be all average food for all days in one list
    food_od = ordered_day[:,0]
    sleep_od = ordered_day[:,1]
    school_od = ordered_day[:,2]
    mood_od = ordered_day[:,3]
    names = ["M", "T", "W", "T", "F", "S", "W"]

    # print(food_od)

    fig, axs = plt.subplots(2, 2, figsize=(8, 6), dpi=50)

    # print(names[:len(food_od)])

    # Create the four bar plots
    axs[0, 0].bar(np.arange(len(food_od)), food_od, tick_label=names, color="r")
    axs[0, 0].set_title('Food')
    axs[0, 1].bar(np.arange(len(sleep_od)), sleep_od, tick_label=names, color="g")
    axs[0, 1].set_title('Sleep')
    axs[1, 0].bar(np.arange(len(school_od)), school_od, tick_label=names, color="b")
    axs[1, 0].set_title('School')
    axs[1, 1].bar(np.arange(len(mood_od)), mood_od, tick_label=names,color="y")
    axs[1, 1].set_title('Mood')



    # Add some padding between subplots
    plt.subplots_adjust(hspace=0.4)

    # Show the figure
    canvas = FigureCanvasTkAgg(fig, master=value_of_day_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
def calendar_all_6():
    global calendar_all_frame
    global datetime_obj, marked_dates, frame_pack

    calendar_all_frame = Frame(window)
    marked_dates = list(df["Date"])
    datetime_obj = datetime.now()
    calendar_frame = Frame(calendar_all_frame)
    calendar_frame.pack()
    frame_pack = []

    def forward():
        global datetime_obj
        if datetime_obj.month == 12:
            datetime_obj = datetime_obj.replace(year=datetime_obj.year + 1, month=1)
        else:
            datetime_obj = datetime_obj.replace(month=datetime_obj.month + 1)
        for_back(datetime_obj)
    def backward():
        global datetime_obj
        if datetime_obj.month == 1:
            datetime_obj = datetime_obj.replace(year=datetime_obj.year - 1, month=12)
        else:
            datetime_obj = datetime_obj.replace(month=datetime_obj.month - 1)
        for_back(datetime_obj)

    def for_back(datetime_obj):
        # print(datetime_obj.month)
        frame_pack.pop().pack_forget()
        create_calendar(datetime_obj)

    # indicator labels
    indication_label = Label(calendar_frame, text="Year-Month",  font=("Helvetica",13, "bold"))
    indication_label.pack()


    # knapparna
    button_frame = Frame(calendar_frame)
    button_frame.pack()
    back_button = Button(button_frame, text="back", bg="green", command=backward)
    back_button.grid(column=0,row=0)
    forward_button = Button(button_frame, text="forward", bg="yellow", command=forward)
    forward_button.grid(column=1,row=0)

    def create_calendar(datetime_obj):
        month = datetime_obj.month
        year = datetime_obj.year
        cal = calendar.monthcalendar(year, month)

        indication_label.config(text=(f"{year} {calendar.month_name[month]}"))

        dates_frame = Frame(calendar_frame)
        dates_frame.pack()
        frame_pack.append(dates_frame)
        # print(cal)
        # Veckorna försig
        for i, week in enumerate(cal):
            # print("new week: ", i)
            # dagarna försig
            for i2, day in enumerate(week):
                # print(year, month, day)
                if not day:
                    # om den veckodagen inte finns hoppas den över t.ex. 2023-7-0
                    continue
                else:
                    date = datetime(year, month, day)
                if date.strftime('%Y-%m-%d') in marked_dates:
                    # Svart bakgrund
                    frame = Frame(dates_frame, width=20, height=20, bg='#b5b5b5')
                    frame.pack_propagate(False)
                    label = Label(frame, text=day, bg='#b5b5b5', font=("Helvetica",13))
                    # print(label)
                else:
                    frame = Frame(dates_frame, width=20, height=20, bg='#dedede')
                    frame.pack_propagate(False)
                    label = Label(frame, text=day, bg='#dedede', font=("Helvetica",13))
                label.pack()
                frame.grid(row=i, column=i2)
    create_calendar(datetime_obj)



# baren med val av sidor
Val_bar = Notebook(window)    

# Skapar allt
inp_page_1()
grouped_graph_all_2()
week_month_all_3()
box_all_4()
value_of_day_all_5()
calendar_all_6()

# sub for submittion, in inp_page_1
Val_bar.add(sub_notebook_frame, text="Submission")
Val_bar.add(grouped_graph_main_frame, text="grouped graph")
Val_bar.add(week_month_all_frame, text="Week Month All")
Val_bar.add(box_all_frame, text="Box All")
Val_bar.add(value_of_day_frame, text="Value of day")
Val_bar.add(calendar_all_frame, text="Calendar")
Val_bar.pack()

# Label(tab2, text="This is in tab 2", width=50, height=25).pack()
window.mainloop()