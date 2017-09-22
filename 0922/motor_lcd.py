import random
import math
import ev3dev.fonts as fonts
from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('outB')
lcd = Screen()
i=0

while True:
    i+=1
    m_speed = math.sin(i*0.1) * 1000
    m.run_forever(speed_sp=m_speed)

    print("actual speed = " + str(m.speed))

    lcd_str = "speed: " + str(m.speed)
    lcd.clear()
    lcd.draw.text((60,60), lcd_str, font = fonts.load('luBS18'))
    lcd.update()
    sleep(0.1)
