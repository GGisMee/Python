from playwright.sync_api import sync_playwright
import time

from Navigator import insert, insert_and_choose_in_list
from sys import path
dir = path[0]

startWeek: int= 36
numWeeks: int = 3

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    page.wait_for_load_state("networkidle")
    return page, browser


def scrape_calendar(page, dir):

    page_text = page.inner_text('body')
    print(page_text)

    # Skriv clipboard-data till en textfil
    with open(f"{dir}/output2.txt", 'w') as file:
        file.write(page_text)

    
        



with sync_playwright() as playwright:
    page, browser = start(playwright)
    insert(page, info = r"placeholder='Klass'",text="TE V2201")
    print(1)
    insert_and_choose_in_list(page, info = r"placeholder='Vecka'",text=str(startWeek), list_info="w-menu-item")
    time.sleep(0.1)
    scrape_calendar(page, dir)
    time.sleep(10)
    page.close()
    