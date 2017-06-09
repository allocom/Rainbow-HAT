Rainbow Hat Python Library
==========================

This library wraps the ws281x python driver for RainbowHat, handling conversion of X/Y coordinates to pixel index
and exposing the basic methods you need to set pixels and update RainbowHat.


Installing
----------

**PIP**

    sudo pip install rainbowhat

**GitHub**

    sudo ./setup.py install


Usage
-----

Just import rainbowhat, then all you need is:

* rainbowhat.set_pixel( x, y, red, green, blue ) - Set a pixel in the buffer to the specified colour
* rainbowhat.show - Update RainbowHat with the current buffer
* rainbowhat.clear - Turn off all the pixels in the buffer and update RainbowHat

Rainbow pHAT
------------

For use with the pHAT version type this in at the top of your file to set the board mode:

* rainbow.set_layout(rainbow.PHAT)

See the examples for more advanced usage.
