import numpy as np
import time
from Navigator import insert_and_choose_in_list
def scrape_calendar(page):
    # Pause execution briefly to avoid overwhelming the server or triggering anti-scraping measures
    time.sleep(0.1)

    # Select all text elements on the page and convert them into a numpy array
    text_elements = np.array(page.query_selector_all('text'))

    line_elements = np.array(page.query_selector_all('line'))
    leftXOutline = int(line_elements[0].get_attribute("x2"))
    rightXOutline = int(line_elements[-1].get_attribute("x1"))
    Step = (rightXOutline-leftXOutline)/5
    
    # Removes all elements before Fredag
    try:
        index = next(i for i, elem in enumerate(text_elements) if "Fredag" in elem.text_content())
    except StopIteration: 
        print("Loaded incorrectly, run again")
    Days = [str(el.text_content()).split(" ")[1] for el in text_elements[index-4:index+1]]
    text_elements = text_elements[index+1:]

    # # Removes empty elements
    text_elements = np.array([elem for elem in text_elements if elem.text_content()])
    
    DevidedList = []
    # # Divide the remaining text elements into 5 weekly lists
    for i in range(5):
        WeekList = []
        # Calculate the minimum and maximum x-coordinate values for the current week
        minX = Step * i + leftXOutline
        maxX = Step * (i + 1) + leftXOutline
        # Add elements to the current week list if their x-coordinate falls within the days range
        for el in text_elements:
            if minX < np.int16(el.get_attribute("x")) < maxX:
                WeekList.append(el)
                
        DevidedList.append(WeekList)
    
    TotalWeekList = []
    for i2,WeekList in enumerate(DevidedList):
        WeekList = np.array(WeekList)
        Dates = np.array([el for el in WeekList if ":" in el.text_content()])
        if (len(Dates) % 2) == 1:
            print(f"Activity with same startdate, causing issue skipping day {Days[i2]}")
            del Days[i2]
            continue #! problem, det finns enbart ett 12:10 på onsdagen v 38 som SVA och SVE delar 
        YDates = np.array([np.int16(el.get_attribute("y")) for el in Dates])


        WeekListNoDates = WeekList[~np.isin(WeekList, Dates)]

        TextDates = np.array([el.text_content() for el in Dates])

        # I pair the dates up in two so that they are split into when they happen.
        PairedTextDates = [TextDates[i:i+2] for i in range(0, len(TextDates), 2)]
        PairedYDates = list([YDates[i:i+2] for i in range(0, len(YDates), 2)])
    
        Text = [el.text_content() for el in WeekListNoDates]
        TextY = [np.int16(el.get_attribute("y")) for el in WeekListNoDates]

        IndexList = [next((i for i, (start, end) in enumerate(PairedYDates) if start <= element <= end), None) for element in TextY]

        StructuredLectures = np.array(PairedTextDates).tolist()
        for TextIndex, DatesIndex in enumerate(IndexList):
            if Text[TextIndex][0:3] == Text[TextIndex][3:6]:
                Text[TextIndex] = Text[TextIndex][3:]
            StructuredLectures[DatesIndex].append(Text[TextIndex])
        for i, lecture in enumerate(StructuredLectures):
            while len(lecture) < 5:
                StructuredLectures[i].append("")
            while len(lecture) > 5:
                part = lecture[0:5]
                del StructuredLectures[i][2:5]
                StructuredLectures.insert(i+1, part)
        TotalWeekList.append(StructuredLectures)
    return Days, TotalWeekList
        

def getData(page, startWeek, NumWeek: int = 1):
    dataSet = []
    daySet = []
    extraYearValue = 0
    extraWeekValue = 0
    for i in range(NumWeek):
        ChosenWeek = i+startWeek-extraWeekValue
        if ChosenWeek >= 53:
            extraWeekValue -= 52
            ChosenWeek-=52
            extraYearValue+=1
        if ChosenWeek > 52:
            pass
        insert_and_choose_in_list(page, info = r"placeholder='Vecka'",text=ChosenWeek, list_info="w-menu-item", extraYearValue=extraYearValue)
        page.wait_for_timeout(100)
        Days, WeekData = scrape_calendar(page)
        dataSet.append(WeekData)
        daySet.append(Days)
    return daySet, dataSet