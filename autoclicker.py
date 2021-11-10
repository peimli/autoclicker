import pyautogui
import time
 
def klikk(): 
    time.sleep(1)     
    pyautogui.click()
 
def a():
    for i in range(50): 
        klikk()
 
a()