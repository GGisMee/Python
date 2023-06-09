import geocoder
import pandas as pd
import numpy as np
import requests
import json
# pos = geocoder.ip("me").latlng
# pos = np.round(pos, decimals=2)
# print(pos)
# # länken till api
# link = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{pos[1]}/lat/{pos[0]}/data.json"
# response = requests.get(link)
# if (response.status_code) == 200:
#     data = response.json()
# else:
#     print("Error:", response.status_code)



df = pd.read_json("Python/Projekten/Kombo/weather app/file.json", orient="index")
print(df)