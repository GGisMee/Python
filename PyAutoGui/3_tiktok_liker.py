import pyautogui as pag
import time
import numpy as np

pag.moveTo(449, 692)
pag.click()
for i in range(6):
    pag.moveTo(741, 729)
    pag.click()
    pag.moveTo(449, 692)
    pag.doubleClick()
    time.sleep(3)