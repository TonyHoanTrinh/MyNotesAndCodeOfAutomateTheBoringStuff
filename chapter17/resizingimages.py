#! /usr/bin/env python3

from PIL import Image

# Resizing Images
catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height/2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# Rotating and Flipping Images
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand = True).save('rotated6_expanded.png')

# Mirror Flip
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

