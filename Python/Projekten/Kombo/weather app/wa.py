# att fixa
# 
import os
import geocoder
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime

# chmod u+r date.txt **used to fix with allowens
# chmod u=r,go= date.txt ** to reset if necessary
def get_df():
    now_v = datetime.now().date()
    try:
        f = open("date.txt", "r")
        if str(f.readline()) == str(now_v):
            print("unchanged")
            df = pd.read_csv("mydata.csv")
            return df
    except FileNotFoundError:
        print("error: file not found")
        
    f = open("date.txt", "w")
    f.write(str(now_v))
    print("changed to", now_v)

    pos = geocoder.ip("me").latlng
    pos = np.round(pos, decimals=2)
    print(pos)
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
    print(length)
    reformated_df = np.arange(len(df))
    print()
    for i in range(336):
        l_list = []
        for el in df:
            l_list.append(el[i])
        reformated_df = np.vstack((reformated_df, l_list))
    reformated_df = reformated_df[1:]
    df = pd.DataFrame(reformated_df, columns=np.array(df_uf.index))
    print(df)

    df.to_csv('mydata.csv', index=True)

    return df
get_df()