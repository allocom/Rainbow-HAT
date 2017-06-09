#!/usr/bin/env python

import math
import time

import rainbowhat as rainbow


print("""Rainbow

Displays a beautiful rainbow across your HAT/pHAT :D

If you're using a Rainbow HAT and only half the screen lights up, 
edit this example and  change 'rainbow.AUTO' to 'rainbow.HAT' below.
""")

#rainbow.set_layout(rainbow.AUTO)
rainbow.set_layout(rainbow.HAT)
rainbow.rotation(0)
rainbow.brightness(0.5)
width,height=rainbow.get_shape()


print("Reticulating splines")
time.sleep(.5)
print("Enabled rainbow poop module!")
time.sleep(.5)
print("Pooping rainbows...")

i = 0.0
offset = 30
while True:
        i = i + 0.3
        for y in range(height):
                for x in range(width):
                        r = 0
                        g = 0
                        r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                        g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                        b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                        r = max(0, min(255, r + offset))
                        g = max(0, min(255, g + offset))
                        b = max(0, min(255, b + offset))
                        rainbow.set_pixel(x,y,int(r),int(g),int(b))
        rainbow.show()
        time.sleep(0.01)
