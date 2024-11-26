import pyautogui
import time
import random

time.sleep(5)




for i in range(1000000000):
    pyautogui.write('###')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 's')
    number = random.randint(1, 350)
    time.sleep(number)
