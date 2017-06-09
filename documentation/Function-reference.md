<!--
---
title: Rainbow HAT-pHAT Python Function Reference
handle: rainbow-hat-python-function-reference
type: tutorial
summary: A comprehensive list of functions from the Rainbow pHAT/HAT python library.
author: Phil Howard
products: [rainbow-hat]
tags: [Rainbow HAT, Raspberry Pi, Python, Reference, Programming]
images: [images/tba.png]
difficulty: Beginner
-->
#Rainbow HAT Function Reference

Note: all of the functions detailed below are applicable to the Rainbow pHAT, but please check the next section for important information.

```python
rotation( 90 )
```

Set the rotation of your Rainbow HAT's output, can be one of 0, 90, 180 or 270 degrees.

```python
brightness( 0.5 )
```

Set the global brightness of Rainbow HAT. This defaults to 0.2 to save your eyes, but can be anywhere from 0.0 to 1.0.

```python
clear()
```

Clears the buffer, setting all pixels to RGB 0,0,0. This won't update RainbowHAT until you call `show()`

```python
off()
```

Clears the buffer and updates Rainbow HAT immediately by calling clear, and then show for you.

```python
set_pixel(x, y, r, g, b)
```

Sets the pixel at x,y to colour r,g,b. The x and y values should be between 0 and 7, and r, g, b between 0 and 255. The actual brightness value displayed will depend upon the global brightness.

```python
get_pixel(x, y)
```

Returns the colour of the pixel at x, y as a tuple of 3 items from 0 to 255.

```python
set_pixels(pixels)
```

Accepts a 2d list of pixels of dimensions 8:8 ( [[0]*8]*8 ). Can be used to set the whole buffer in one go from a numpy array.

```python
get_pixels()
```

Gets the whole pixel buffer as a 2d list of dimensions 8:8.


```python
show()
```

Updates the Rainbow HAT with the current buffer. The buffer contains all pixel data that you have drawn with the set_pixel or set_pixels methods.

```python
set_layout(rainbow.HAT)
```

Enforces the pixel mapping required for the Rainbow HAT. This is the default, so in nnormal circumstances only needed if you need to reset the layout after using the Rainbow pHAT. 

#Rainbow pHAT Function Reference

```python
set_layout(rainbow.PHAT)
```

Enforces the pixel mapping required for the Rainbow pHAT. It must be called at the start of your routine for pixel coordinates to be handled correctly.

```python
rotation( 180 )
```

Set the rotation of your Rainbow pHAT's output. 180 will invert the display, i.e set the origin in the bottom right corner, looking at the PCB with the header at the top. O will reset the origin. It is not possible to swap the x and y axis.

```python
set_pixel(x, y, r, g, b)
```

Sets the pixel at x,y to colour r,g,b. The x value should be between 0 and 7, the y value should be between 0 and 3. r, g, b must be between 0 and 255. The actual brightness value displayed will depend upon the global brightness.

Note that for compatibility with Rainbow HAT y values between 4 and 7 will be accepted but wrap around the range. In other words they are technically acceptable but should be avoided when writing programs designed for the pHAT.

All other functions detailed in the HAT sections are otherwise valid and identical.
