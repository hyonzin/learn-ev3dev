#!/usr/bin/env python3
import ev3dev.fonts as fonts
from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
ts = TouchSensor()
count=0
state=True

while True:
    for i in range(0, 20):
        if state and ts.is_pressed:
            state = False
            count+=1
        elif not state and not ts.is_pressed:
            state = True
        sleep(0.05)

    lcd_str = str(count)

    lcd.clear()
    lcd.draw.text((60,60), lcd_str, font = fonts.load('luBS24'))
    lcd.update()
