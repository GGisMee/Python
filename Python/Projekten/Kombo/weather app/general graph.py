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
view_part: str # 1h exempelvis
label_view: int # var ... label syns
grouping_of_data: str # timmar som de grupperas i för att lättare analysera data som hänger ihop typ medeltemp över en dag
df = pd.read_csv("Python/Projekten/Kombo/weather app/mydata.csv", index_col="ID") # df hämtas

content_f = tk.Frame(window)
content_f.pack()

input_f = tk.Frame(content_f)
input_f.pack()





def run(view_part, label_view, grouping_of_data, night=False):
    # temp_graph(view_part, label_view, grouping_of_data, night)
    wind_graph(view_part, label_view, grouping_of_data, night)


def temp_graph(view_part, label_view, grouping_of_data, night):
    global temp_canvas_f
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
    print(time_values)
    date_arr = format_date(time_values, grouping_of_data)[0]

    x_arr = np.zeros(1)
    for element in date_arr:
        if element[0].hour == element[-1].hour:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}")))
        else:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}-{element[-1].hour}")))
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
    fig, axs = plt.subplots(figsize=(20, 10), dpi=50)
    axs.set_xticks(range(len(x_arr))[::label_view])
    axs.set_xticklabels(x_arr[::label_view])
    plt.xticks(rotation=45)

    plt.grid(True)

    day_labeling = (np.vectorize(lambda str: str.split("/")[0])(x_arr))
    print(day_labeling)
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

     # de kommer visas korrekt
    axs.legend()

    canvas = FigureCanvasTkAgg(fig, master=temp_canvas_f)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.update()

def wind_graph(view_part, label_view, grouping_of_data, night):
    global canvas_f
    canvas_f = tk.Frame(content_f, width=400, height= 400)
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
    print(time_values)
    date_arr = format_date(time_values, grouping_of_data)[0]

    x_arr = np.zeros(1)
    for element in date_arr:
        if element[0].hour == element[-1].hour:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}")))
        else:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}-{element[-1].hour}")))
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
    fig, axs = plt.subplots(figsize=(20, 10), dpi=50)
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

    normal_wind = np.array(mean_arr.tolist()[0])
    high_wind = np.array(mean_arr.tolist()[1])
    print(x_arr)
    plt.fill_between(x_arr, normal_wind, high_wind, color='gray', alpha=0.5)

    axs.set_title("Temperature Weather graph")
    axs.set_ylabel("Level")
    axs.set_xlabel("Time")
    axs.plot(x_arr,mean_arr[0],  label="1", linewidth=3)
    axs.plot(x_arr,mean_arr[1],  label="2", linewidth=3)

     # de kommer visas korrekt
    axs.legend()

    canvas = FigureCanvasTkAgg(fig, master=canvas_f)
    canvas.draw()
    canvas.get_tk_widget().pack()
    window.update()

run(view_part="1w", label_view=2, grouping_of_data="2h", night=True)


window.mainloop()