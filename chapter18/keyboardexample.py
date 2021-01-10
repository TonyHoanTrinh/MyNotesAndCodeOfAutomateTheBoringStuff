#! /usr/bin/env python3

import pyautogui
pyautogui.click(140, 120, button = "left")
pyautogui.typewrite('Hello world!')

# Keynames
print(pyautogui.KEYBOARD_KEYS)
pyautogui.typewrite(['a','b', 'left','left', 'X', 'Y'])

# Pressing and Releasing the Keyboard
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
