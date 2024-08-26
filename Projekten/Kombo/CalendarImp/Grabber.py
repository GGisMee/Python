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
        maxX = Step * (i + 1) + leftXOutline-2
        # Add elements to the current week list if their x-coordinate falls within the days range
        for el in text_elements:
            if minX < np.int16(el.get_attribute("x")) < maxX:
                WeekList.append(el)
                
        DevidedList.append(WeekList)
    
    TotalWeekList = []
    for i2,WeekList in enumerate(DevidedList):
        WeekList = np.array(WeekList)
        Dates = np.array([el for el in WeekList if ":" in el.text_content()])
        if len(Dates) % 2 == 1:
            print('Error. Uneven amount of hours for the activities') #! problem, det finns enbart ett 12:10 på onsdagen v 38 som SVA och SVE delar 
            exit()
        YDates = np.array([np.int16(el.get_attribute("y")) for el in Dates])
        XDates = np.array([np.int16(el.get_attribute("x")) for el in Dates])


        WeekListNoDates = WeekList[~np.isin(WeekList, Dates)]

        TextDates = np.array([el.text_content() for el in Dates])

        # I pair the dates up in two so that they are split into when they happen.
        PairedTextDates = [TextDates[i:i+2] for i in range(0, len(TextDates), 2)]
        PairedYDates = list([YDates[i:i+2] for i in range(0, len(YDates), 2)])
        PairedXDates = list([XDates[i:i+2] for i in range(0, len(XDates), 2)])
    
        Text = [el.text_content() for el in WeekListNoDates]
        TextYList = [np.int16(el.get_attribute("y")) for el in WeekListNoDates]
        TextXList = [np.int16(el.get_attribute("x")) for el in WeekListNoDates]

        IndexList = []

        for i, TextY in enumerate(TextYList):
            FontValue = str(WeekListNoDates[i].get_attribute("style"))
            TextEl = Text[i]
            FontValue = FontValue.split(";")[0].replace("font-size: ","").replace("px", "")
            WeekList[i].text_content()
            widthValue = round(len(TextEl)*0.6*int(FontValue))
            TextX = TextXList[i]+widthValue
            #print(widthValue)

            index = None
            for i2, (startY, endY) in enumerate(PairedYDates):
                startX = PairedXDates[i2][0]
                endX = PairedXDates[i2][1]
                if startY <= TextY <= endY and startX <= TextX<= endX: # antaglig anledning är att det är salen som automatiskt hamnar utanför endX
                    Index = i2
                    break
            IndexList.append(Index)
             # kan nog göras genom att använda en approximation av hur många pixlar som ska läggas till.
        #! problem på torsdag 12/9 att den tänker att Aktivitet skolfoto tillhör svenskan eftersom den är innanför svenskans y ramar.
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
        

def getData(page, startWeek, NumWeeks: int = None, stopWeek:int = None):
    dataSet = []
    daySet = []
    WeekList = []
    VarWeek = startWeek
    if stopWeek:
        while VarWeek != stopWeek+1:
            WeekList.append(VarWeek)
            VarWeek += 1
            if VarWeek == 53:
                VarWeek -= 52
    elif NumWeeks:
        for i in range(NumWeeks):
            weekNum = startWeek+i
            if weekNum>52:
                WeekList.append(weekNum-52)
            else:
                WeekList.append(weekNum)

    for weekNum in WeekList:
        insert_and_choose_in_list(page, info = r"placeholder='Vecka'",text=weekNum, list_info="w-menu-item")
        page.wait_for_timeout(100)
        Days, WeekData = scrape_calendar(page)
        dataSet.append(WeekData)
        daySet.append(Days)
    return daySet, dataSet