# from selenium import webdriver
# website = "https://github.com/"
# path = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome("Projekten/Kombo/CalendarImp")
# driver.get(website)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

website = "https://github.com/"
path = "/usr/local/bin/chromedriver"

# Set Chrome options if needed
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run headlessly

# Initialize the Chrome driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the website
driver.get(website)


time.sleep(5)

# input_field = driver.find_element(By.ID, "8b52b100ec2383d2e66bb1c0541e87c8")  # Ersätt 'INPUT_RUTANS_ID' med det faktiska ID:t eller annan selektor
# Skriv in "2201" i rutan
input_field = driver.find_element(By.CSS_SELECTOR, "col-12.my-0.mb-3.mb-md-0.flex-auto.form-control.f4-mktg.width-full.rounded-md-right-0")



""


input_field.click()

