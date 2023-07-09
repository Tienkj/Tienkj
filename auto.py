import pyautogui
import time

for number in range(10000):
    formatted_number = str(number).zfill(4)
    pyautogui.typewrite(formatted_number)
    pyautogui.press('enter')
    time.sleep(10)
