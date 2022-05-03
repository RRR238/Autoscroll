import time

import pyautogui

speed = input("How fast you want to scroll ?")
sleep = input("How long sleep between scrollings ?")
start = input("After how many secs. you want to start ?")

time.sleep(int(start))

while True:
    pyautogui.scroll(int(speed))
    pyautogui.time.sleep(int(sleep))


