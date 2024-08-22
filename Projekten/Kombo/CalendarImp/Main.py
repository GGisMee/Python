from playwright.sync_api import sync_playwright
import time
from Navigator import insert, insert_and_choose_in_list
from sys import path
import numpy as np
from Grabber import getData 

startWeek: int = 37
numWeeks: int = 1
klass = "2201"

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    page.wait_for_load_state("networkidle")
    return page, browser

def FormatToICal(daySet:list, dataSet:list):
    print(daySet, dataSet)

    

with sync_playwright() as playwright:
    page, browser = start(playwright)
    insert(page, info = r"placeholder='Klass'",text=f"TE V{klass}")
    daySet, dataSet = getData(page, startWeek, numWeeks)
    FormatToICal(daySet, dataSet)
    page.close()