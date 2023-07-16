import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
df = pd.read_csv("Python/Projekten/Kombo/your_day/final/mydata.csv", index_col='ID')

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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


window = Tk()
inp_frame = Frame(window)
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
    graph_frame = Frame(window)
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
        print(Date)
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
        #print(x_axeln)

        # print("\n\n")
        # print(mean_list_tot)
        # felet just nu är att x_axeln ger 0001-01-01 på de som inte är fulla, den måste tas bort nu
        # kanske en while loop som kör näst närmaste till inga 0001-01-01 finns kvar och om den är samma så skriver den bara samma
        # print(mean_list_tot)

    #print(x_axeln, mean_list_tot)
        # för x axeln
    fig, axs = plt.subplots(figsize=(8, 6), dpi=50)
    print(mean_list_tot)
    print(x_axeln)
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
window.mainloop()