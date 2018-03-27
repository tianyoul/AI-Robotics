#!/usr/bin/env python3
from ev3dev.ev3 import *

lcd = Screen()

# Connect Pixy camera
pixy = Sensor(address = 'in2')
assert pixy.connected, "Connecting PixyCam"

print('good1\n')

# Connect TouchSensor
ts = TouchSensor(address = 'in4')
assert ts.connected, "Connecting TouchSensor"

print('good2\n')

# Set mode
pixy.mode = 'ALL'

print('good3\n')

while not ts.value():
  lcd.clear()
  if pixy.value(0) != 0:  # Object with SIG1 detected
    x = pixy.value(1) 
    y = pixy.value(2)
    w = pixy.value(3)
    h = pixy.value(4)
    dx = int(w/2)       # Half of the width of the rectangle
    dy = int(h/2)       # Half of the height of the rectangle
    xb = x + int(w/2)   # X-coordinate of bottom-right corner
    yb = y - int(h/2)   # Y-coordinate of the bottom-right corner
    lcd.draw.rectangle((xa,ya,xb,yb), fill='black')
    lcd.update()