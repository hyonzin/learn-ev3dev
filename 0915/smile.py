from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
smile = True
while True:
    lcd.clear()

    lcd.draw.ellipse((20, 20, 60, 60))
    lcd.draw.ellipse((118, 20, 158, 60))

    if smile:
        lcd.draw.arc((40, 80, 138, 100), 0, 180)
    else:
        lcd.draw.arc((40, 80, 138, 100), 180, 360)

    smile = not smile
    lcd.update()
    sleep(1)



