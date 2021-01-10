#! /usr/bin/env python3

import pyautogui
print(pyautogui.size())
width, height = pyautogui.size()

# Moves to absolute position
for i in range(10):
    pyautogui.moveTo(100, 100, duration = 0.25)
    pyautogui.moveTo(200, 100, duration = 0.25)
    pyautogui.moveTo(200, 200, duration = 0.25)
    pyautogui.moveTo(100, 200, duration = 0.25)

# Moves to relative position
for i in range(10):
    pyautogui.moveRel(100, 0, duration = 0.25)
    pyautogui.moveRel(0, 100, duration = 0.25)
    pyautogui.moveRel(-100, 0, duration = 0.25)
    pyautogui.moveRel(0, -100, duration = 0.25)

# Getting the Mouse Position
print(pyautogui.position())

# Clicking the mouse
pyautogui.click(10, 5)
pyautogui.click(200, 300, button = 'right')
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()

# Scrolling the Mouse
pyautogui.scroll(200)
for i in range(200):
    numbers = numbers + str(i) + '\n'

pyperclip.copy(numbers)
