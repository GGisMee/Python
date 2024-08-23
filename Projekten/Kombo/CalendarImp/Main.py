from playwright.sync_api import sync_playwright
import time
from Navigator import insert
from Grabber import getData 
from icalendar import Calendar, Event, vCalAddress, vText
import datetime
startWeek: int = 34
numWeeks: int = 2
klass = "2201"

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    page.wait_for_load_state("networkidle")
    return page, browser

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
    for i, day in enumerate(dataSet):
        for i2, activity in enumerate(day):
            
            # event = Event()
            startTime = activity[0]
            endTime = activity[1]
            activityName = activity[2]
            activityTeacher = activity[3]
            activityRoom = activity[4]
            # event.add('name', activityName)
            # event['location'] = vText(f'Sal {activityRoom}')
            # event.add('teacher', activityTeacher)
            print( startTime, endTime, yearList[i][i2], daySet[i][i2])


    

with sync_playwright() as playwright:
    page, browser = start(playwright)
    insert(page, info = r"placeholder='Klass'",text=f"TE V{klass}")
    daySet, dataSet = getData(page, startWeek, numWeeks)
    FormatToICal(daySet, dataSet)
    page.close()