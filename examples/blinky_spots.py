#!/usr/bin/env python

import rainbowhat as rainbow
import time, colorsys
import numpy as np
import random

rainbow.brightness(0.4)

def make_gaussian(fwhm, x0, y0):
	x = np.arange(0, 8, 1, float)
	y = x[:, np.newaxis]
	fwhm = fwhm
	gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
	return gauss

while True:
	x0 = random.random() * 8
	y0 = random.random() * 8
	h = random.random()
	for z in range(1,5)[::-1] + range(1,10):
		fwhm = 5.0/z
		gauss = make_gaussian(fwhm, x0, y0)
		for y in range(8):
			for x in range(8):
				s = 0.8
				v = gauss[x,y]
				rgb = colorsys.hsv_to_rgb(h, s, v)
				r = int(rgb[0]*255.0)
				g = int(rgb[1]*255.0)
				b = int(rgb[2]*255.0)
				rainbow.set_pixel(x, y, r, g, b)
		rainbow.show()
		time.sleep(0.01)
