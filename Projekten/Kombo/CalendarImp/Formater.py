import datetime
import numpy as np
list = [['23/12','24/12', "25/12", "26/12", "27/12"], ["30/12", "31/12", "1/1","2/1", "3/1"]]
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year
yearList = []
for i, weekDates in enumerate(list):
    weekYearList = []
    for i2, date in enumerate(weekDates):
        if int(date.split("/")[1])>=currentMonth:
            weekYearList.append(currentYear)
        else:
            weekYearList.append(currentYear+1)
    yearList.append(weekYearList)

print(list)
print(yearList)

