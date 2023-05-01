# måste använda 
# pip install pyautogui 
# # först
import pyautogui
import time
def func():
    while True:    
        pyautogui.press('a')
        time.sleep(1)
        pyautogui.press("d")

time.sleep(5)
func()