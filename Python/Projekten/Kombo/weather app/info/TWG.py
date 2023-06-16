import os
import geocoder
import requests
import json

import sys

import pandas as pd
import numpy as np
from datetime import datetime


import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def format_date(time_values, grouping_of_data="1h"):

    if grouping_of_data == "1h":
        for i, el in enumerate(time_values):
            time_values[i] = np.array([time_values[i]])
        return time_values, []

    # pos_date = time_values[0] # första tidsvärdet hämtas för att ge en startpunkt och grupera dem
    ind_arr = np.zeros(2) # arr för alla index skapas
    pos_date = time_values[0]
    # print("\n",pos_date,"\n")
    smhdwmo = ([1, 60, 3600, 86400, 604800, 18748800][(np.where(np.array(["s", "m", "h", "d", "w", "mo"]) == grouping_of_data[-1:])[0][0])])
    grouping_of_data = int(grouping_of_data[:-1])
    #print(len(time_values))
    for i, element in enumerate(time_values): # tidsvärden försig
        if ((element-pos_date).total_seconds()) >= grouping_of_data*smhdwmo: # om tidsvärdenas timmskillnad ex 4 är större eller lika med 4 kommer de delas in i en grupp
            i_obj = [int(np.where(time_values==pos_date)[0][0]), int(i-1)] # värdena memoreras

        elif i == len(time_values)-1:
            i_obj = (int(np.where(time_values==pos_date)[0][0]), int(i)) # om sista värdet körs som inte är lika stort som timmskillnad kommer det ändå gruperas
        else:
            continue
        # print(x_obj)
        pos_date = element
        ind_arr = np.vstack((ind_arr, i_obj))
    del pos_date
    ind_arr = ind_arr[1:]
    date_arr = []
    for el in ind_arr:
        part_dates = time_values[int(el[0]): int(el[1]+1)]
        date_arr.append(part_dates)
    #print(pos_date)
    return date_arr, ind_arr



# print(f"{sys.path[0]}/date.txt")
# os.path.join(sys.path[0], "filename") funkar bra för lokal folder

def same_dir(name):
    return os.path.join(sys.path[0], name)

def get_df():
    now_v = datetime.now().date()
    try:
        f = open(same_dir("date.txt"), "r")
        # print("hello")
        if str(f.readline()) == str(now_v):
            print("unchanged")
            df = pd.read_csv(same_dir("mydata.csv"))
            return df
    except FileNotFoundError:
        print("error: file not found")
        
    f = open(same_dir("date.txt"), "w")
    f.write(str(now_v))
    print("changed to", now_v)
    pos = geocoder.ip("me").latlng
    pos = np.round(pos, decimals=2)
    # länken till api
    link = f"https://api.open-meteo.com/v1/forecast?latitude={pos[0]}&longitude={pos[1]}&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m,windgusts_10m,winddirection_10m&windspeed_unit=ms&timezone=auto"
    response = requests.get(link)
    if (response.status_code) == 200:
        response_data = response.text
    else:
        print("Error:", response.status_code)
    # print(response_data)
    data = json.loads(response_data)
    df_uf = pd.DataFrame(data)
    #print(df)

    # tar bort onödiga indikatorer

    df = np.array(df_uf["hourly"])
    length = len(df[0])
    #print(length)
    reformated_df = np.arange(len(df))
    #print()
    for i in range(len(df[0])):
        l_list = []
        for el in df:
            l_list.append(el[i])
        reformated_df = np.vstack((reformated_df, l_list))
    reformated_df = reformated_df[1:]
    df = pd.DataFrame(reformated_df, columns=np.array(df_uf.index))
    #print(df)
    df.index.name = "ID"
    file_path = os.path.join(sys.path[0], 'mydata.csv')
    df.to_csv(file_path, index=True)

    return df
df = get_df()
# print(df)



#!----------------------------------------------------------------------------------------

#!----------------------------------------------------------------------------------------

night_v: bool = False
run_data: list = ["1w", 2, "1h", night_v]
choice: str = "1w"

def forget_f():
    temp_canvas_f.forget()
    canvas_f.forget()

def change_f(dec_val, default=0):
    global night_v, run_data, choice
    choice = dec_val
    forget_f()
    if default == 1:
        print("halleluja")
        run(view_part="1w", label_view=3, grouping_of_data="1h", night=night_v)
        return
    if dec_val == "1d": 
        run(view_part="1d", label_view=1, grouping_of_data="1h", night=night_v)

    if dec_val == "2d":
        run(view_part="2d", label_view=1, grouping_of_data="1h", night=night_v)

    if dec_val == "4d":
        run(view_part="4d", label_view=1, grouping_of_data="1h", night=night_v)

    if dec_val == "6d":
        run(view_part="6d", label_view=2, grouping_of_data="1h", night=night_v)

    if dec_val == "1w":
        run(view_part="1w", label_view=2, grouping_of_data="1h", night=night_v)

    if dec_val == "1w 1d":
        run(view_part="1w", label_view=1, grouping_of_data="1d", night=night_v)
 

           
        
def night_command():
    global night_v
    night_v = night_cb_v.get()
    if choice == "1w" and night_v:
        change_f(choice, 1)
        return
    change_f(choice)
window = tk.Tk()

window.title("TWG")

night_cb_v = tk.IntVar()
content_f = tk.Frame(window)
content_f.pack()

input_f = tk.Frame(content_f)
input_f.pack()

night_fr = tk.Frame(input_f)
night_fr.grid(row=0, columnspan=6)

night_l = tk.Label(night_fr, text="Natt:")
night_l.grid(column=0)

night_cb = tk.Checkbutton(night_fr, command=night_command, variable=night_cb_v)
night_cb.grid(column=1, row=0)

btn_1d = tk.Button(input_f, text="1d", command=lambda: change_f("1d"))
btn_1d.grid(column=0, row=1)

btn_2d = tk.Button(input_f, text="2d", command=lambda: change_f("2d"))
btn_2d.grid(column=1, row=1)

btn_4d = tk.Button(input_f, text="4d", command=lambda: change_f("4d"))
btn_4d.grid(column=2, row=1)

btn_6d = tk.Button(input_f, text="6d", command=lambda: change_f("6d"))
btn_6d.grid(column=3, row=1)

btn_1w = tk.Button(input_f, text="1w", command=lambda: change_f("1w"))
btn_1w.grid(column=4, row=1)

btn_1w_mean = tk.Button(input_f, text="1w mean", command=lambda: change_f("1w 1d"))
btn_1w_mean.grid(column=5, row=1)


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
#print("now: ",now)




def run(view_part, label_view, grouping_of_data, night=False):
    temp_graph(view_part, label_view, grouping_of_data, night)
    wind_graph(view_part, label_view, grouping_of_data, night)
    window.update()
    


def temp_graph(view_part, label_view, grouping_of_data, night):
    global temp_canvas_f, now, unf_now
    temp_canvas_f = tk.Frame(content_f, width=400, height= 400)
    temp_canvas_f.pack()

    df_l_temp = df.drop(['windspeed_10m','windgusts_10m','winddirection_10m', 'relativehumidity_2m'], axis=1)
    df_l_temp["precipitation"] = np.array(df_l_temp["precipitation"])/10
    df_l_temp["cloudcover"] = np.array(df_l_temp["cloudcover"])/10

    
    # print("\n\n\n",time_values, "\n\n\n")
    time_values = np.vectorize(lambda element:datetime.strptime(element, "%Y-%m-%dT%H:%M"))(np.array(df_l_temp["time"])) # tidsvärdena hämtas och ordnas till datetime.datetime format
    time_values = format_date(time_values, view_part)[0][0]
    #print(time_values)

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
    #print("\n"*2,date_arr)

    x_arr = np.zeros(1)
    for element in date_arr:
        if element[0].hour == element[-1].hour:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}")))
        else:
            x_arr = np.hstack((x_arr, (f"{element[0].day}/{element[0].hour}-{element[-1].hour}")))
        #print(int(element[0].day),now[0],"\n", int(element[0].hour),now[1],element[-1].hour,int(element[0].hour)<=now[1]<=element[-1].hour, "\n\n")
        if int(element[0].day) == now[0] and int(element[0].hour)<=now[1]<=element[-1].hour and (night or now[1] < 23):
            print("hallelulia")
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
    #print(now_point)
    # exit()
    fig, axs = plt.subplots(figsize=(17, 6), dpi=50)
    axs.set_xticks(range(len(x_arr))[::label_view])
    axs.set_xticklabels(x_arr[::label_view])
    
    plt.xticks(rotation=45)

    plt.grid(True)

    day_labeling = (np.vectorize(lambda str: str.split("/")[0])(x_arr))
    # print(day_labeling)
    each_and_every = (round((len(day_labeling))/len(np.unique(day_labeling))))

    ax2 = axs.secondary_xaxis('top')
    ax2.set_xticks(range(len((day_labeling)))[round(each_and_every/2)::each_and_every])
    ax2.set_xticklabels((np.array(["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag","Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"])[unf_now.weekday()+np.arange(len(np.unique(day_labeling)))]))
    

    ax3 = axs.secondary_xaxis('top')
    ax3.tick_params(axis='x', which='both', pad=17)
    ax3.set_xticks(range(len((day_labeling)))[round(each_and_every/2)::each_and_every])
    ax3.set_xticklabels(np.unique(day_labeling))
    



    axs.set_yticks(np.arange(np.amin(mean_arr), np.amax(mean_arr), 1))
    axs.set_title("Temperatur och Vind Graf")
    axs.set_ylabel("Nivå")
    axs.set_xlabel("Tid")
    axs.plot(x_arr,mean_arr[0],  label="Temperatur", linewidth=3)
    axs.plot(x_arr,mean_arr[1],  label="Molnighet", linewidth=3)
    axs.plot(x_arr,mean_arr[2],  label="Regn", linewidth=3)
    #print(np.amax(mean_arr))
    if ((night or now[1] < 23)):
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
    #! 23 tas inte fixa i formateringen. kör med viewpart 1d och grouping of data 1h så märks det att 23:00 saknas
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
        if int(element[0].day) == now[0] and int(element[0].hour)<=now[1]<=element[-1].hour and (night or now[1] < 23):
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
    fig, axs = plt.subplots(figsize=(17, 6), dpi=50)
    axs.set_xticks(range(len(x_arr))[::label_view])
    axs.tick_params(axis='x', which='both', pad=17)
    axs.set_xticklabels(x_arr[::label_view])
    plt.xticks(rotation=45)

    plt.grid(True)

    day_labeling = (np.vectorize(lambda str: str.split("/")[0])(x_arr)) # tar ut dagen ur x_arr värdet
    each_and_every = (round((len(day_labeling))/len(np.unique(day_labeling)))) # hittar antalet värden mellan varje dag

    ax2 = axs.secondary_xaxis('top')
    ax2.set_xticks(range(len((day_labeling)))[round(each_and_every/2)::each_and_every])
    ax2.set_xticklabels((np.array(["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag","Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"])[unf_now.weekday()+np.arange(len(np.unique(day_labeling)))]))

    #print(unf_now.weekday()+np.arange(len(np.unique(day_labeling))))
    
    
    ax3 = axs.secondary_xaxis('top')
    ax3.tick_params(axis='x', which='both', pad=17)
    ax3.set_xticks(range(len((day_labeling)))[round(each_and_every/2)::each_and_every])
    ax3.set_xticklabels(np.unique(day_labeling))
    
    
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
    

      #print(f"\n\nd:{el}")
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
    axs4 = axs.secondary_xaxis("bottom")
    axs4.set_xticks(np.arange(len(direction_str_list))[::label_view])
    axs4.set_xticklabels(direction_str_list[::label_view])

    # print("\n"*4,x_arr.tolist())
    # print("\n"*2,mean_arr.tolist(), "\n"*4)

    axs.set_ylabel("Nivå")
    axs.set_xlabel("Tid")
    axs.plot(x_arr,mean_arr[0],  label="Vindby", linewidth=3)
    axs.plot(x_arr,mean_arr[1],  label="Normal Vind", linewidth=3)
    if ((night or now[1] < 23)):
        axs.plot([now_point, now_point], [0, np.amax(mean_arr[0:2])], color="red", linewidth=2,linestyle="dashed")

     # de kommer visas korrekt
    axs.legend()
    canvas = FigureCanvasTkAgg(fig, master=canvas_f)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
run(view_part="1w", label_view=2, grouping_of_data="1h", night=night_v)


window.mainloop()