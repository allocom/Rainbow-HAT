#!/usr/bin/env python

import rainbowhat as rainbow
import time, colorsys
import numpy as np

rainbow.set_layout(rainbow.AUTO)
rainbow.brightness(0.5)

def make_gaussian(fwhm):
	x = np.arange(0, 8, 1, float)
	y = x[:, np.newaxis]
	x0, y0 = 3.5, 3.5
	fwhm = fwhm
	gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
	return gauss

while True:
	fwhm = 5
	gauss = make_gaussian(fwhm)
	for y in range(8):
		for x in range(8):
			h = 0.1
			s = 1.0
			v = gauss[x,y]
			rgb = colorsys.hsv_to_rgb(h, s, v)
			r = int(rgb[0]*255.0)
			g = int(rgb[1]*255.0)
			b = int(rgb[2]*255.0)
			rainbow.set_pixel(x, y, r, g, b)
	rainbow.show()
	time.sleep(0.005)
