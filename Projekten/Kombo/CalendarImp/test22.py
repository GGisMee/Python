from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("start")
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

url = 'https://www.amazon.com'

driver.get(url)

time.sleep(3)

driver.find_element(by=By.XPATH, value='//*[@id="twotabsearchtextbox"]').send_keys('smartwatch')

time.sleep(1)

driver.find_element(by=By.XPATH, value='//*[@id="nav-search-submit-button"]').click()

time.sleep(5)

driver.close()

print("end")