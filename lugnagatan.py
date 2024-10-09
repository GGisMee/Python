from playwright.sync_api import sync_playwright
import numpy as np

def start(playwright):
    """Creates the browser and opens the website and returns it"""
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.compass-group.se/restauranger-och-menyer/foodandco/lugna-gatan/")
    page.wait_for_load_state("networkidle")
    return page, browser 

def getData():
    "https://www.compass-group.se/menuapi/feed/json?costNumber=6417&language=sv"
    div_content = page.locator("div.manual-menu.compass-rich-text").all_text_contents()
    print(div_content)
    #print(np.array(div_content.split(',')))


with sync_playwright() as playwright:
    page, browser = start(playwright)
    getData()