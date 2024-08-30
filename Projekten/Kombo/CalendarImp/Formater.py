from icalendar import Calendar, Event, vCalAddress, vText
import datetime
import os
import sys
def getYearList(daySet:list):
    # gets a list with the right year
    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year
    yearList = []
    for weekDates in daySet:
        weekYearList = []
        for date in weekDates:
            if int(date.split("/")[1])>=currentMonth:
                weekYearList.append(currentYear)
            else:
                weekYearList.append(currentYear+1)
        yearList.append(weekYearList)
    return yearList

def FormatToICal(daySet:list, dataSet:list):
    cal = Calendar()
    cal.add('version', '2.0')
    yearList = getYearList(daySet)
    # Fixa så åren fungerar som de ska och även att den fungerar med flera veckor eftersom det blev någon bugg nu.
    for i, WeekData in enumerate(dataSet):
        for i2, dayData in enumerate(WeekData):
            for i3, activity in enumerate(dayData):
                event = Event()
                startTime = str(activity[0]).split(":")
                endTime = str(activity[1]).split(":")
                activityName = activity[2]
                activityTeacher = activity[3]
                activityRoom = activity[4]
                event.add('summary', activityName)
                event['location'] = vText(f'Sal {activityRoom}')
                event.add('description', f"lärare: {activityTeacher}")

                date = str(daySet[i][i2]).split("/")
                event.add('dtstart', datetime.datetime(int(yearList[i][i2]), int(date[1]), int(date[0]), int(startTime[0]), int(startTime[1])))
                event.add('dtend', datetime.datetime(int(yearList[i][i2]), int(date[1]), int(date[0]), int(endTime[0]), int(endTime[1])))
                cal.add_component(event)
                
                #print(startTime, endTime, yearList[i][i2], daySet[i][i2])
    f = open(os.path.join(sys.path[0], 'calendar.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()