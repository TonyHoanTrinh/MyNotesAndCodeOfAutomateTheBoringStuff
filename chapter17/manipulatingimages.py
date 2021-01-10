#! /usr/bin/env python3

from PIL import Image
# Opening an image from a directory
catIm = Image.open('zophie.png')
# Attributes of the image object
print(catIm.size)
width, height = catIm.size
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
# Saves a new version of the picture
catIm.save('zophie.jpg')

# Creating a blank image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')
