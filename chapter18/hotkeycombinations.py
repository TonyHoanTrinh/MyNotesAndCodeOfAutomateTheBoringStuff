#! /usr/bin/env python3

import pyautogui, time

pyautogui.hotkey('ctrl', 'c')

def commentAfterDelay():
    pyautogui.click(100, 100)
    pyautogui.typewrite('In IDLE, Ctrl-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('ctrl', '3')

commentAfterDelay()
