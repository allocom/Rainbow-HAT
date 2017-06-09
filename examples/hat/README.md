Rainbow HAT Examples
====================

The examples in this folder must be run with `sudo`, like so:

    sudo ./clock.py

or

    sudo python clock.py


The examples in this folder are intended for the Rainbow HAT and have not been designed for the pHAT geometry. Feel free to give it a try and move them up inside the main examples folder if you are successful making them work adequately with both boards.

clock.py
--------

Uses `graphics.py` and shows how you can, but probably shouldn't, display an analogue clock on Rainbow HAT!

graphics.py
-----------

Used by clock.py

eve.py
------

Monitors the usb bus and displays a checkmark when a new device is detected.

matrix.py
---------

Knock, knock, Neo.

show_png.py
-----------

Shows how you can open and display a PNG image file (here lofi.png), great for sprite animations.

**Requirements:**

    sudo pip install pillow
