#!/usr/bin/env python

import rainbowhat as rainbow
import time, colorsys
import numpy as np

rainbow.brightness(0.5)
rainbow.rotation(270)

def make_gaussian(fwhm):
        x = np.arange(0, 8, 1, float)
        y = x[:, np.newaxis]
        x0, y0 = 3.5, 3.5
        fwhm = fwhm
        gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
        return gauss

heart = [[0,0,0,0,0,0,0,0],
         [0,1,1,0,0,1,1,0],
         [1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1],
         [0,1,1,1,1,1,1,0],
         [0,0,1,1,1,1,0,0],
         [0,0,0,1,1,0,0,0],
         [0,0,0,0,0,0,0,0]]

heart = np.array(heart) * make_gaussian(7.5)

while True:
	for i in 2*(range(1,11)[::-1]+range(1,10)):
		for y in range(8):
			for x in range(8):
				h = 0.0
				s = 1.0
				v = heart[x,y] / float(i)
				rgb = colorsys.hsv_to_rgb(h, s, v)
				r = int(rgb[0]*255.0)
				g = int(rgb[1]*255.0)
				b = int(rgb[2]*255.0)
				rainbow.set_pixel(x, y, r, g, b)
		rainbow.show()
		time.sleep(0.005)
	time.sleep(0.5)
