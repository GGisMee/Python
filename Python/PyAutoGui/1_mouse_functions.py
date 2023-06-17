import pyautogui as pag
import time
# Give time
# time.sleep(3)

print((pag.size())) # ger skärmstorleken
print(pag.position()) # muspekarens plats

# rör musen
#pag.moveTo(100, 100, 3) # till [100, 100] på 3 sek

# Rör musen relativt till position som den befann sig på
#pag.moveRel(100, 100, 0.5)

# klick, [100,100], gör det 2 ggr i 3 sek med höger knappen
# pag.click(100, 100, 2, 3, button="right")
# finns även pag. rightclick, leftclick, doubleclick, tripleclick

# skrolla
# pag.scroll(3) # skrolla uppåt 3 klick, -3 för nedåt
time.sleep(2)
# Musen trycker ned/upp musen på en koordinat
pag.mouseDown(100, 100, button="left")
pag.mouseUp()


