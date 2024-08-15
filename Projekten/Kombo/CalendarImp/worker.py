from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("star")
# Starta en ny webbläsarsession
chrome_options = Options()
# chrome_options.add_argument("--disable-popup-blocking")  # Inaktivera popup-blockering
# chrome_options.add_argument("--disable-infobars")  # Inaktivera infobars som säger att Chrome inte är standard
# chrome_options.add_argument("--disable-infobars")  # Inaktivera infobars som säger att Chrome inte är standard
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome()  # Använd 'webdriver.Firefox()' om du använder Firefox

# Gå till webbsidan
driver.get(r"https://web.skola24.se/timetable/timetable-viewer/industritekniska.skola24.se/Hitachigymnasiet%20i%20V%C3%A4ster%C3%A5s/")  # Ersätt med den faktiska URL:en

time.sleep(10)
# Hitta rutan där du ska skriva in "2201"
input_field = driver.find_element(By.ID, "6c1d3027c0e51849cb99badbaf1cdffb")  # Ersätt 'INPUT_RUTANS_ID' med det faktiska ID:t eller annan selektor

# Skriv in "2201" i rutan
input_field.send_keys("2201")

# Om aktivering kräver att du trycker på 'Enter' eller klickar på en knapp:
input_field.send_keys(Keys.RETURN)  # Används om det ska tryckas på 'Enter'
# eller
# submit_button = driver.find_element(By.ID, "BUTTON_ID")  # Ersätt 'BUTTON_ID' med knappens ID
# submit_button.click()

# Vänta en kort stund för att kalendern ska laddas (justera vid behov)
time.sleep(2)

# Nu kan du fortsätta med att hämta kalenderdata
# Exempel: Hämta alla händelser som har en viss klass
# events = driver.find_elements(By.CLASS_NAME, "event-class")  # Ersätt 'event-class' med rätt klass

# for event in events:
#     title = event.find_element(By.TAG_NAME, "h2").text
#     date = event.find_element(By.CLASS_NAME, "date-class").text
#     print(f"Title: {title}, Date: {date}")

# # Avsluta webbläsaren
# driver.quit()
print("done")