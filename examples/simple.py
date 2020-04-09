#!/usr/bin/env python

import time

import rainbowhat as rainbow


print("""Simple

Turns each pixel on in turn and updates the display.

If you're using a Rainbow HAT and only half the screen lights up,
edit this example and  change 'rainbow.AUTO' to 'rainbow.HAT' below.
""")

rainbow.set_layout(rainbow.AUTO)
rainbow.rotation(0)
rainbow.brightness(0.3)
#rainbow.brightness(1.0)
width,height=rainbow.get_shape()


for y in range(height):
  for x in range(width):
    rainbow.set_pixel(x,y,255,255,255)
    rainbow.show()
    time.sleep(0.05)
time.sleep(100)
