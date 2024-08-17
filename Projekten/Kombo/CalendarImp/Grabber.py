from sys import path
import numpy as np
dir = path[0]

# Skriv clipboard-data till en textfil
with open(f"{dir}/output.txt", 'r') as file:
    page_text = file.read()
rows = page_text.split('\n')

# Further split each row into columns
data = [row.split(',') for row in rows]
#print(data)
for i,row in enumerate(data):
    if "Fredag" in row[0]:
        data = data[i+1:-2]
        break
times = []
for i,row in enumerate(data):
    if ":" in row[0]:
        times = data[i:]
        data = data[:i]
        break

new_times = []
for i, row in enumerate(times):
    if i%2 == 0:
        new_times.append([times[i], times[i+1]])
print(new_times)