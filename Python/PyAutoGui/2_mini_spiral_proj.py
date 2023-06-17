import pyautogui as pag
import time
import numpy as np
time.sleep(1)
pos = [90, 172]
width_length = 200
print(pag.position())

pag.moveTo(pos[0], pos[1], 1)
pag.click()
in_val = 10


# method 1
for i in range(round(width_length/(in_val*2))):
    pag.dragRel(width_length, 0, button="left")
    pag.dragRel(0, width_length, button="left")
    width_length-=in_val
    pag.dragRel(-width_length, 0, button="left")
    pag.dragRel(0, -width_length, button="left")
    width_length-=in_val
    time.sleep(1)
else:
    pag.mouseUp()


# method 2
# for i in range(round(width_length/(in_val*2))):
#     pag.mouseDown(pag.position()[0], pag.position()[1], button="left")
#     pag.moveRel(width_length, 0)
#     pag.moveRel(0, width_length)
#     width_length-=in_val
#     pag.moveRel(-width_length, 0)
#     pag.moveRel(0, -width_length)
#     width_length-=in_val
# else:
#     pag.mouseUp()
exit()

