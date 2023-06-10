# att fixa
# 
import os
import geocoder
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime

now_v = datetime.now().date()
f = open("Python/Projekten/Kombo/weather app/date.txt", "r")
if str(f.readline()) != str(now_v):
    f = open("Python/Projekten/Kombo/weather app/date.txt", "w")
    f.write(str(now_v))
    print("changed to", now_v)
else:
    print("unchanged")
del f
        

exit()
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
df = pd.DataFrame(data)
#print(df)

# tar bort onödiga indikatorer

df_hour = np.array(df["hourly"])
length = len(df_hour[0])
print(length)
reformated_df = np.arange(len(df_hour))
print()
for i in range(336):
    l_list = []
    for el in df_hour:
        l_list.append(el[i])
    reformated_df = np.vstack((reformated_df, l_list))
reformated_df = reformated_df[1:]
#print(reformated_df)
#print(np.array(df.index))

df_new = pd.DataFrame(reformated_df, columns=np.array(df.index))
print(df_new)




# dir_path = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(dir_path, 'mydata2.csv')
# df_new.to_csv(file_path, index=True)


# file_path2 = os.path.join(dir_path, 'mydata2.csv')
# df_new.to_csv(file_path2, index=True)
