from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Starta webbläsaren med Selenium
chrome_options = Options()
#chrome_options.add_argument("--profile-directory=Profile 5")
chrome_options.add_argument("--user-data-dir=/Users/gustavgamstedt/Library/Application Support/Google/Chrome")
driver = webdriver.Chrome() # "/usr/local/bin/chromedriver"

# Gå till webbsidan
#driver.get(r"https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")



time.sleep(30)
# Avsluta webbläsaren
driver.quit()
