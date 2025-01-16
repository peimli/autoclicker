import pyautogui
import time
import threading
import keyboard 


stop_flag = False

def klikk(): 
    pyautogui.click()

def a():
    global stop_flag
    while not stop_flag:
        klikk()
        time.sleep(0.000000000000000000001)  

def start_stop_clicking():
    global stop_flag
    if stop_flag:  
        stop_flag = False
        threading.Thread(target=a, daemon=True).start()
        print("Started clicking...")
    else:  
        stop_flag = True
        print("Stopped clicking.")


keyboard.add_hotkey('s', start_stop_clicking)

print("Press 's' to start/stop clicking.")


keyboard.wait()
