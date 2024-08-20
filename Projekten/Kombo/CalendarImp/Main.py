from playwright.sync_api import sync_playwright
import time
from Navigator import insert, insert_and_choose_in_list
from sys import path
import numpy as np

dir = path[0]

startWeek: int = 35
numWeeks: int = 3

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    page.wait_for_load_state("networkidle")
    return page, browser



def scrape_calendar(page, dir):
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

    text_elements = text_elements[index+1:]

    print(1)
    # # Removes empty elements
    text_elements = np.array([elem for elem in text_elements if elem.text_content()])
    
    DevidedList = []
    # # Divide the remaining text elements into 5 weekly lists
    for i in range(5):
        WeekList = []
        # Calculate the minimum and maximum x-coordinate values for the current week
        minX = Step * i + leftXOutline #! Skulle behöva göra den här dynamisk eftersom den ändras efter device.
        maxX = Step * (i + 1) + leftXOutline
        # Add elements to the current week list if their x-coordinate falls within the days range
        if i == 3:
            pass
            #print(minX, maxX)
        for el in text_elements:
            if minX < np.int16(el.get_attribute("x")) < maxX:
                if i == 3:
                    pass
                    
                WeekList.append(el)
                
        DevidedList.append(WeekList)
    
    print(2)
    for WeekList in DevidedList:
        WeekList = np.array(WeekList)
        Dates = np.array([el for el in WeekList if ":" in el.text_content()])
        YDates = np.array([np.int16(el.get_attribute("y")) for el in Dates])
        #IndexSortedYDates = np.argsort(YDates) #! problem med argsort då den förstör när två aktiviteter överlappar.


        print([el.text_content() for el in Dates])
        #YDates = YDates[IndexSortedYDates]
        #Dates = Dates[IndexSortedYDates]
        WeekListNoDates = WeekList[~np.isin(WeekList, Dates)]
        
        XDates = np.array([np.int16(el.get_attribute("x")) for el in Dates])


        TextDates = np.array([el.text_content() for el in Dates])
        # I pair the dates up in two so that they are split into when they happen.
        PairedTextDates = [TextDates[i:i+2] for i in range(0, len(TextDates), 2)]
        PairedYDates = list([YDates[i:i+2] for i in range(0, len(YDates), 2)])
        PairedXDates = list([XDates[i:i+2] for i in range(0, len(XDates), 2)])
    
        Text = [el.text_content() for el in WeekListNoDates]
        TextY = [np.int16(el.get_attribute("y")) for el in WeekListNoDates]
        
        IndexList = [next((i for i, (start, end) in enumerate(PairedYDates) if start <= element <= end), None) for element in TextY]
        StructuredLectures = np.array(PairedTextDates).tolist()
        print(3)
        for TextIndex, DatesIndex in enumerate(IndexList):
            if Text[TextIndex][0:3] == Text[TextIndex][3:6]:
                Text[TextIndex][0:3]
            StructuredLectures[DatesIndex].append(Text[TextIndex])
        print(StructuredLectures)
        #print(StructuredLectures)
        #* Att göra  
        # Dela upp dem som består av två ex SVESVE och SVASVA i två stycken.
        # Ta bort repetering alltså SVESVE...
        # Fixa att lunch är för kort med 2

        
    


with sync_playwright() as playwright:
    page, browser = start(playwright)
    insert(page, info = r"placeholder='Klass'",text="TE V2201")
    insert_and_choose_in_list(page, info = r"placeholder='Vecka'",text=str(startWeek), list_info="w-menu-item")
    page.wait_for_timeout(100)
    scrape_calendar(page, dir)
    page.close()