from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
s = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=s)
driver.get(r"https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")

time.sleep(10)

input_field = driver.find_element(By.ID, "8b52b100ec2383d2e66bb1c0541e87c8")  # Ersätt 'INPUT_RUTANS_ID' med det faktiska ID:t eller annan selektor
# Skriv in "2201" i rutan
input_field.send_keys("2201")

time.sleep(10)
driver.close()