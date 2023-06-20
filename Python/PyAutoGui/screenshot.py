import pyautogui as pag
import time
import numpy as np
l = []
for i in range(2):
    time.sleep(4)
    l.append(pag.position())
    print(pag.position())
l = np.array(l)
l[1] = l[1]-l[0]
l = np.vectorize(lambda x:x)(l)

print((l[0][0], l[0][1], l[1][0], l[1][1]))
pag.screenshot("pic.png", region=(l[0][0], l[0][1], l[1][0], l[1][1]))
