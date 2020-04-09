#!/usr/bin/env python

from time import sleep

import rainbowhat as rainbow


print("""ASCII Pic

You should see a scrolling image, defined in the below variable ASCIIPIC.

If the smiley looks sad, change the rotation from 0 to 180.
""")


rainbow.set_layout(rainbow.AUTO)
#rainbow.set_layout(rainbow.HAT)
rainbow.rotation(0)
rainbow.brightness(0.5)
width,height=rainbow.get_shape()

# Every line needs to be exactly 8 characters
# but you can have as many lines as you like.
ASCIIPIC = [
     "  X  X  "
    ,"        "
    ,"X      X"
    ," XXXXXX "
    ,"        "
    ,"        "
    ,"        "
    ]
i = -1

def step():
    global i
    i = 0 if i>=100*len(ASCIIPIC) else i+1 # avoid overflow
    for h in range(height):
        for w in range(width):
            hPos = (i+h) % len(ASCIIPIC)
            chr = ASCIIPIC[hPos][w]
            if chr == ' ':
                rainbow.set_pixel(w, h, 0, 0, 0)
            else:
                rainbow.set_pixel(w, h, 255, 0, 0)
    rainbow.show()

while True:
    step()
    sleep(0.2)
