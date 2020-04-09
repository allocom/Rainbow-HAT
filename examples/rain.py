#!/usr/bin/env python

import rainbowhat as rainbow
import time, colorsys
import random

rainbow.set_layout(rainbow.AUTO)
rainbow.brightness(0.5)
width,height=rainbow.get_shape()

m = [[0 for i in range(8)] for i in range(8)]

while True:
	if 1 in m[-1]:
		top = [0.5 * i for i in m[-1]]
	elif 0.5 in m[-1]:
		top = [0] * 8
	else:
		top = [random.randint(0,1) for i in range(2)] + [0,0,0,0,0,0]
		random.shuffle(top)
		for i in range(len(top)):
			if top[i] == 1 and top[i-1] == 1:
				top[i] = 0
	m.append(top)
	del m[0]
	for x in range(width):
		for y in range(height):
			h = 0.6
			s = 0.6
			v = m[x][y] * 0.8
			rgb = colorsys.hsv_to_rgb(h, s, v)
			r = int(rgb[0]*255.0)
			g = int(rgb[1]*255.0)
			b = int(rgb[2]*255.0)
			rainbow.set_pixel(y, x, r, g, b)
	rainbow.show()
	time.sleep(0.075)
