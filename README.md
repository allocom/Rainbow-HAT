# Rainbow-HAT
32/64 LED HAT for Raspberry Pi

![Rainbow HAT/pHAT](rainbow-hat-logo.png)

Available from ALLO.com:

### Important Notice

Because Rainbow HAT uses the PWM hardware, which is also how your Raspberry Pi generates analog audio, you may see random colour patterns and flickering.

If this happens, you should add the following to your `/boot/config.txt`:

```
hdmi_force_hotplug=1
```

Sound will work fine using speakers on, for example, an HDMI TV, but you will not be able to use your Pi's 3.5mm audio jack in conjunction with Rainbow HAT.

### `rainbowhat` Python Library & Examples

Here you'll find everything you need to start lighting up your Rainbow HAT or pHAT using python.

Python users should probably ignore most of this repository and just:


```bash
sudo apt-get install python-pip python-dev
```
**Install from Github clone**

```
git clone https://github.com/allocom/rainbow-hat
cd rainbow-hat/
sudo apt-get install python-dev python-setuptools
cd library/rpi-ws281x
sudo python setup.py install
cd ../..
cd library/RainbowHat
sudo python setup.py install
cd ../..
```

Then proceed to [examples](examples).

Notes:

 -rainbow-hat tested with Volumio  & max2play images.
 -rainboa-hat compatible with unicorn-hat python library and examples.

*****************************************************************************

