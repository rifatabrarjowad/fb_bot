#pip install PyAutoGUI
#import pyautogui
#import time
#while True:
    #time.sleep(1)
  #  pyautogui.typewrite('noman vaiya kmn achn :) ')
  #  pyautogui.press('enter')



#pip install PyAutoGUI
import pyautogui
import time
while True:
    time.sleep(4)
    while True:
        # Python3 code to iterate over a list
        list = ["hi", "hum"]

        # Getting length of list
        length = len(list)
        i = 0

        # Iterating using while loop

        while i < length:
             pyautogui.typewrite(list[i])
             pyautogui.press('enter')
             i += 1
