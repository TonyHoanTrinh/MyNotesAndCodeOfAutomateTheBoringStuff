#! /usr/bin/env python3
import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))

print(pyautogui.pixelMatchesColor(50, 200, (18, 18, 18)) )

