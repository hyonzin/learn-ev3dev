#!/usr/bin/env python3
import ev3dev.fonts as fonts
from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
ts = TouchSensor()
count=0

while True:
    for i in range(0, 10):
        if ts.is_pressed:
            count+=1
        sleep(0.1)

    lcd_str = str(count)

    lcd.clear()
    lcd.draw.text((60,60), lcd_str, font = fonts.load('luBS24'))
    lcd.update()
