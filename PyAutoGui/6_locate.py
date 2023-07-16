import pyautogui as pag
import time
import sys
from PIL import Image
location1 = f"{sys.path[0]}/bilder/yt.png"
location2 = f"{sys.path[0]}/bilder/razer.png"
location3 = f"{sys.path[0]}/bilder/title.png"
location4 = f"{sys.path[0]}/bilder/code.png"

print(location4)
# image = Image.open(location3)
# image.show()
# exit()
pos = None
while pos == None:
    pos = (pag.locateOnScreen(location4, grayscale=False, confidence=0.9))
    time.sleep(1)
pag.moveTo(pos[1], pos[2])
time.sleep(2)
pag.moveTo(pos[2], pos[3])


#pag.locateOnScreen()