#!/usr/bin/env python3
from ev3dev.ev3 import *

lcd = Screen()

# Connect Pixy camera
pixy = Sensor(address='in3')
assert pixy.connected, "Connecting PixyCam"

# Set mode
pixy.mode = 'SIG1'

buttons = Button()
while not buttons.any():
    lcd.clear()
    if pixy.value(0) != 0:  # Object with SIG1 detected
        print("found!")
        x = pixy.value(1)
        y = pixy.value(2)
        w = pixy.value(3)
        h = pixy.value(4)
        dx = int(w / 2)  # Half of the width of the rectangle
        dy = int(h / 2)  # Half of the height of the rectangle
        xa = x - int(w / 2)
        ya = y + int(h / 2)
        xb = x + int(w / 2)  # X-coordinate of bottom-right corner
        yb = y - int(h / 2)  # Y-coordinate of the bottom-right corner
        lcd.draw.rectangle([(xa, yb), (xb, yb)], fill='black')
        lcd.update()
    else:
        print("not found")