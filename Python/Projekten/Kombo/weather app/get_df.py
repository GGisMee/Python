# att fixa
# 
import os
import geocoder
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
import sys
# print(f"{sys.path[0]}/date.txt")
# os.path.join(sys.path[0], "filename") funkar bra för lokal folder

def same_dir(name):
    return os.path.join(sys.path[0], name)

def get_df():
    now_v = datetime.now().date()
    try:
        f = open(same_dir("date.txt"), "r")
        print("hello")
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
    link = f"https://api.open-meteo.com/v1/forecast?latitude={pos[0]}&longitude={pos[1]}&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m,windgusts_10m,winddirection_10m&windspeed_unit=ms&past_days=7&timezone=auto"
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
    for i in range(336):
        l_list = []
        for el in df:
            l_list.append(el[i])
        reformated_df = np.vstack((reformated_df, l_list))
    reformated_df = reformated_df[1:]
    df = pd.DataFrame(reformated_df, columns=np.array(df_uf.index))
    #print(df)

    file_path = os.path.join(sys.path[0], 'mydata.csv')
    df.to_csv(file_path, index=True)

    return df
df = get_df()
print(df)