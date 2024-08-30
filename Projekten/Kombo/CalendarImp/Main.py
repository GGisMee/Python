from playwright.sync_api import sync_playwright
from Formater import FormatToICal
from Navigator import insert
from Grabber import getData 

#! fixa fel med skumma aktiveten vecka 5
startWeek: int = 5
year: int = 2025
numWeeks: int = None
endWeek: int = 10
klass = "2201"

if ("s" in klass) or ("S" in klass):
    klass = f"TES V{klass}"
    klass = klass.replace('s', 'S')
else:
    klass = f"TE V{klass}"

if not numWeeks:
    if endWeek < startWeek:
        endWeek+=52
    numWeeks = endWeek-startWeek+1   
else:
    endWeek = startWeek+numWeeks-1 
print(f'Imputed weeks: {startWeek} - {endWeek}')

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    page.wait_for_load_state("networkidle")
    return page, browser 

with sync_playwright() as playwright:
    page, browser = start(playwright)
    insert(page, info = r"placeholder='Klass'",text=klass)
    daySet, dataSet = getData(page, startWeek, numWeeks, year = year)
    FormatToICal(daySet, dataSet)
    page.close()
    print("Successfully ran through program")
    print(f"Weeks {startWeek}-{endWeek} scraped")