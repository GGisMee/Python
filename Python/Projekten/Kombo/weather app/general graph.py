import os
import pandas as pd
import numpy as np
import sys
from datetime import datetime

import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from format_by_date import format_date



window = tk.Tk()

content_f = tk.Frame(window)
content_f.pack()

input_f = tk.Frame(content_f)
input_f.pack()

btn_1h = tk.Button(input_f, text="1h")
btn_1h.grid(column=0, row=0)

btn_2h = tk.Button(input_f, text="2h")
btn_2h.grid(column=1, row=0)

btn_1d = tk.Button(input_f, text="1d")
btn_1d.grid(column=2, row=0)

btn_2d = tk.Button(input_f, text="2d")
btn_2d.grid(column=3, row=0)

btn_1w = tk.Button(input_f, text="1w")
btn_1w.grid(column=4, row=0)


view_part: str # 1h exempelvis
label_view: int # var ... label syns
grouping_of_data: str # timmar som de grupperas i för att lättare analysera data som hänger ihop typ medeltemp över en dag
df = pd.read_csv("Python/Projekten/Kombo/weather app/mydata.csv", index_col="ID") # df hämtas

df_time = df["time"]
unf_now = datetime.now()
now = [int(unf_now.day)]
if (int(unf_now.strftime("%M"))>=30):
    now.append(int(unf_now.hour+1))
else:
    now.append(int(unf_now.hour))
print("now: ",now)




def run(view_part, label_view, grouping_of_data, night=False):
    temp_graph(view_part, label_view, grouping_of_data, night)
    wind_graph(view_part, label_view, grouping_of_data, night)
    window.update()


def temp_graph(view_part, label_view, grouping_of_data, night):
    global temp_canvas_f, now
    temp_canvas_f = tk.Frame(content_f, width=400, height= 400)
    temp_canvas_f.pack()

    df_l_temp = df.drop(['windspeed_10m','windgusts_10m','winddirection_10m', 'relativehumidity_2m'], axis=1)
    df_l_temp["precipitation"] = np.array(df_l_temp["precipitation"])/10
    df_l_temp["cloudcover"] = np.array(df_l_temp["cloudcover"])/10


    # print("\n\n\n",time_values, "\n\n\n")
    time_values = np.vectorize(lambda element:datetime.strptime(element, "%Y-%m-%dT%H:%M"))(np.array(df_l_temp["time"])) # tidsvärdena hämtas och ordnas till datetime.datetime format

    time_values = format_date(time_values, view_part)[0][0]
    dates = np.zeros(1)
    if not night:
        for i in time_values:
            if i.hour >= 7 and i.hour <= 22:
                dates = np.hstack((dates, i))
        time_values = dates[1:]
    try:
        time_values[0]
    except IndexError:
        exit("Error: time_value array empty, Line 42")
    #print(time_values)
    date_arr = format_date(time_values, grouping_of_data)[0]

    x_arr = np.zeros(1)
    for element in date_arr:
        if element[0].hour == element[-1].hour:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}")))
        else:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}-{element[-1].hour}")))
        if int(element[0].day) == now[0] and int(element[0].hour)<=now[1]<=element[-1].hour:
            now_point = x_arr[np.where(x_arr == x_arr[-1])[0]][0]
    x_arr = x_arr[1:]
    mean_arr = (np.zeros(len(np.array(df_l_temp.iloc[0])[1:])))
    for el in date_arr:
        l_list = []
        for el2 in el:
            if el2 != 0:
                el2 = el2.isoformat()[:-3]
                l_list.append(np.array(df_l_temp[df_l_temp['time'] == str(el2)]))
        l_list = np.array(list(map(lambda el: el[0],(l_list))))[:,1:]
        mean_arr = np.vstack((mean_arr, np.mean(l_list, axis=0)))
    mean_arr = np.transpose(mean_arr[1:])
    #print(mean_arr)
    # print(np.array(x_arr))

    # exit()
    fig, axs = plt.subplots(figsize=(15, 6), dpi=50)
    axs.set_xticks(range(len(x_arr))[::label_view])
    axs.set_xticklabels(x_arr[::label_view])
    plt.xticks(rotation=45)

    plt.grid(True)

    day_labeling = (np.vectorize(lambda str: str.split("/")[0])(x_arr))
    # print(day_labeling)
    each_and_every = (round((len(day_labeling))/len(np.unique(day_labeling))))
    ax2 = axs.secondary_xaxis('top')
    ax2.set_xticks(range(len((day_labeling)))[round(each_and_every/2)::each_and_every])
    ax2.set_xticklabels(np.unique(day_labeling))
    



    axs.set_yticks(np.arange(np.amin(mean_arr), np.amax(mean_arr), 1))
    axs.set_title("Temperature Weather graph")
    axs.set_ylabel("Level")
    axs.set_xlabel("Time")
    axs.plot(x_arr,mean_arr[0],  label="1", linewidth=3)
    axs.plot(x_arr,mean_arr[1],  label="2", linewidth=3)
    axs.plot(x_arr,mean_arr[2],  label="3", linewidth=3)
    print(np.amax(mean_arr))
    axs.plot([now_point, now_point], [0, np.amax(mean_arr)], color="red", linewidth=2,linestyle="dashed")

     # de kommer visas korrekt
    axs.legend()

    canvas = FigureCanvasTkAgg(fig, master=temp_canvas_f)
    canvas.draw()
    canvas.get_tk_widget().pack()

def wind_graph(view_part, label_view, grouping_of_data, night):
    global canvas_f
    canvas_f = tk.Frame(content_f, width=400, height= 400, bg="blue")
    canvas_f.pack()

    df_l_wind = df.drop(['temperature_2m', 'relativehumidity_2m','precipitation','cloudcover'], axis=1)


    # print("\n\n\n",time_values, "\n\n\n")
    time_values = np.vectorize(lambda element:datetime.strptime(element, "%Y-%m-%dT%H:%M"))(np.array(df_l_wind["time"])) # tidsvärdena hämtas och ordnas till datetime.datetime format

    time_values = format_date(time_values, view_part)[0][0]
    dates = np.zeros(1)
    if not night:
        for i in time_values:
            if i.hour >= 7 and i.hour <= 22:
                dates = np.hstack((dates, i))
        time_values = dates[1:]
    try:
        time_values[0]
    except IndexError:
        exit("Error: time_value array empty, Line 42")
    #print(time_values)
    date_arr = format_date(time_values, grouping_of_data)[0]

    x_arr = np.zeros(1)
    for element in date_arr:
        if element[0].hour == element[-1].hour:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}")))
        else:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}-{element[-1].hour}")))
        if int(element[0].day) == now[0] and int(element[0].hour)<=now[1]<=element[-1].hour:
            now_point = x_arr[np.where(x_arr == x_arr[-1])[0]][0]
    x_arr = x_arr[1:]
    mean_arr = (np.zeros(len(np.array(df_l_wind.iloc[0])[1:])))
    for el in date_arr:
        l_list = []
        for el2 in el:
            if el2 != 0:
                el2 = el2.isoformat()[:-3]
                l_list.append(np.array(df_l_wind[df_l_wind['time'] == str(el2)]))
        l_list = np.array(list(map(lambda el: el[0],(l_list))))[:,1:]
        mean_arr = np.vstack((mean_arr, np.mean(l_list, axis=0)))
    mean_arr = np.transpose(mean_arr[1:])
    #print(mean_arr)
    # print(np.array(x_arr))

    # exit()
    fig, axs = plt.subplots(figsize=(15, 6), dpi=50)
    axs.set_xticks(range(len(x_arr))[::label_view])
    axs.tick_params(axis='x', which='both', pad=17)
    axs.set_xticklabels(x_arr[::label_view])
    plt.xticks(rotation=45)

    plt.grid(True)

    day_labeling = (np.vectorize(lambda str: str.split("/")[0])(x_arr)) # tar ut dagen ur x_arr värdet
    each_and_every = (round((len(day_labeling))/len(np.unique(day_labeling)))) # hittar antalet värden mellan varje dag
    ax2 = axs.secondary_xaxis('top')
    ax2.set_xticks(range(len((day_labeling)))[round(each_and_every/2)::each_and_every])
    ax2.set_xticklabels(np.unique(day_labeling))

    axs.set_yticks(np.arange(np.amin(mean_arr), np.amax(mean_arr), 1))

    normal_wind = np.array(mean_arr.tolist()[0])
    high_wind = np.array(mean_arr.tolist()[1])
    deg = np.array(mean_arr.tolist()[2])
    #print(x_arr)
    plt.fill_between(x_arr, normal_wind, high_wind, color='gray', alpha=0.5)

    direction_def: list = ["N", "O", "S", "W"]
    direction_str_list: list = []
    for i, el in enumerate(deg):
      direction_num_list: list = []
    

      print(f"\n\nd:{el}")
      for extent in range(4):
        # print(extent*90, (extent+1)*90)
        if (extent*90<=el<=(extent+1)*90):
          if (extent*90<=el<(extent+1)*90-60):
            direction_num_list.append(extent)
          elif (extent*90+30<=el<=(extent+1)*90-30):
            direction_num_list.append(extent)
            added_extent = extent+1
            if added_extent == 4: added_extent=0
            direction_num_list.append(added_extent)
          elif (extent*90+60<=el<=(extent+1)*90):
            added_extent = extent+1
            if added_extent == 4: added_extent=0
            direction_num_list.append(added_extent)
          #print(direction_num_list)

          #print(direction_num_list)
          if 0 in direction_num_list:
            #print(direction_num_list.index(0))
            direction_num_list.insert(0,direction_num_list.pop((direction_num_list.index(0))))
            #print(direction_num_list)
          elif 2 in direction_num_list:
            #print(direction_num_list.index(2))
            direction_num_list.insert(0,direction_num_list.pop((direction_num_list.index(2))))
            #print(direction_num_list)
          to_str = "".join((np.array(direction_def)[direction_num_list]).tolist())
          direction_str_list.append(to_str)
          # print(el, direction_str_list[-1])
    del direction_def, direction_num_list
    direction_str_list = np.array(direction_str_list)
    axs3 = axs.secondary_xaxis("bottom")
    axs3.set_xticks(np.arange(len(direction_str_list))[::label_view])
    axs3.set_xticklabels(direction_str_list[::label_view])

    # print("\n"*4,x_arr.tolist())
    # print("\n"*2,mean_arr.tolist(), "\n"*4)

    axs.set_title("Temperature Weather graph")
    axs.set_ylabel("Level")
    axs.set_xlabel("Time")
    axs.plot(x_arr,mean_arr[0],  label="1", linewidth=3)
    axs.plot(x_arr,mean_arr[1],  label="2", linewidth=3)
    axs.plot([now_point, now_point], [0, np.amax(mean_arr[0:2])], color="red", linewidth=2,linestyle="dashed")

     # de kommer visas korrekt
    axs.legend()
    canvas = FigureCanvasTkAgg(fig, master=canvas_f)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
run(view_part="1w", label_view=2, grouping_of_data="1h", night=True)


window.mainloop()