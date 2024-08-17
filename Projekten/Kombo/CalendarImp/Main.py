from playwright.sync_api import sync_playwright
import time

from Navigator import insert, insert_and_choose_in_list
from sys import path

import numpy as np
dir = path[0]

startWeek: int= 37
numWeeks: int = 3

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    page.wait_for_load_state("networkidle")
    return page, browser



def scrape_calendar(page, dir):
    # page_text = page.inner_text('body')
    # print(page_text)

    # # Skriv clipboard-data till en textfil
    # with open(f"{dir}/output2.txt", 'w') as file:
    #     file.write(page_text)

    # rätt sätt: gruppera alla olika textvärden. Ta deras x och y värden och gruppera därefter dem i vilken dag dem är och sen i lektioner

    # style="font-size: 14px; font-family: &quot;Open Sans&quot;; fill: rgb(0, 0, 0); pointer-events: none;"
    time.sleep(0.1)
    text_elements = np.array(page.query_selector_all('text'))
    #print(text_elements)
    indexList = []
    for i,el in enumerate(text_elements):
        if "Fredag" in el.text_content():
            text_elements = text_elements[i+1:]
            break
    for i,el in enumerate(text_elements):
        if "" == el.text_content():
            indexList.append(i)
    text_elements = np.delete(text_elements, indexList)

    #print([el.text_content() for el in text_elements])


    DevidedList = []
    for i in range(5):
        WeekList = []
        minX = 221*i+39
        maxX = 221*(i+1)+39
        for el in text_elements:
            if minX < int(el.get_attribute("x")) < maxX:
                WeekList.append(el)
                #print(el)
       #print("\n")
        #print(WeekList, "\n")
        DevidedList.append(WeekList)




with sync_playwright() as playwright:
    page, browser = start(playwright)
    insert(page, info = r"placeholder='Klass'",text="TE V2201")
    insert_and_choose_in_list(page, info = r"placeholder='Vecka'",text=str(startWeek), list_info="w-menu-item")
    page.wait_for_timeout(100)
    scrape_calendar(page, dir)
    time.sleep(1000)
    page.close()