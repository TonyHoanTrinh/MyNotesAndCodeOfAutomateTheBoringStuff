#! /usr/bin/env python3
# send2trash doesn't permanently deletes files and folders but sends them to the trash first
import send2trash
baconFile = open('blue.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('blue.txt')

