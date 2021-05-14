import pyautogui
import time
while True:
    time.sleep(4)
    while True:
        # Python3 code to iterate over a listba

        list = ["baba ", " kmn acho "]

        # Getting length of list
        length = len(list)
        i = 0

        # Iterating using while loop

        while i < length:
             pyautogui.typewrite(list[i])
             pyautogui.press('enter')
             i += 1