from playwright.sync_api import sync_playwright
import time
def run(playwright):
    # Start a new browser session
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Open the desired website
    page.goto("https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Replace with the actual URL
    time.sleep(2)
    # Insert 2201 into the input field
    page.click("input[placeholder='Klass']")
    page.fill("input[placeholder='Klass']", "TE V2201")  # Replace with the actual selector
    #time.sleep(1)
    page.click("input[placeholder='Klass']")

    page.wait_for_timeout(1000)
    page.press("input[class='w-text w-block']", "Enter")  # Replace with the actual selector

    page.wait_for_timeout(5000)
    #time.sleep(4)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
