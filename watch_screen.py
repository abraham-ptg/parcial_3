import pyautogui
import time
from new_screenshot import take_screenshot

def move_cursor(data):

    x_percent = 50
    y_percent = 40

    screen_width, screen_height = pyautogui.size()

    x = int(screen_width * (x_percent / 100))
    y = int(screen_height * (y_percent / 100))
    
    take_screenshot("before")

    pyautogui.click(x, y)
    pyautogui.press("enter")
    pyautogui.press("tab")
    
    for nombre in data["nombres"]:
        pyautogui.typewrite(nombre)
        pyautogui.press("enter")
    
    pyautogui.press("tab")
    pyautogui.typewrite(str(data["suma"]))
    pyautogui.press("tab")
    pyautogui.press("space")

    take_screenshot("during")

    pyautogui.press("tab")
    #pyautogui.press("enter")
    time.sleep(5)
    take_screenshot("after")

    return