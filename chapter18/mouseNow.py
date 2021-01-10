#! /usr/bin/env python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        # Get and print the mouse coordiantes.
        x, y = pyautogui.position()
        print(x , y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end = '')
except KeyboardInterrupt:
    print('\nDone.')
    print(positionStr, end ='')
    print('\b' * len(positionStr), end ='', flush = True)
