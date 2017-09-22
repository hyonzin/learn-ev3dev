#!/usr/bin/env python3
import ev3dev.fonts as fonts
from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
ts = TouchSensor()
count=0

while True:
    if ts.is_pressed:
        count+=1
        lcd_str = str(count)

        lcd.clear()
        lcd.draw.text((60,60), lcd_str, font = fonts.load('luBS24'))
        lcd.update()
        sleep(0.1)
