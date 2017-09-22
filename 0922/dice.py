from time import sleep
import random
import ev3dev.fonts as fonts
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *

ts = ev3.TouchSensor()

lcd = Screen()

while True:
    if (ts.is_pressed):
        lcd_str = str(random.randint(1, 6))
        lcd.clear()
        lcd.draw.text((60,60), lcd_str, font = fonts.load('luBS18'))
        lcd.update()
        sleep(1)
