from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep
from PIL import Image

lcd = Screen()
bomb_image = Image.open('pics/Bomb.bmp')
boom_image = Image.open('pics/Boom.bmp')

sec = 10

while True:
    if sec >= 0:
        lcd.clear()
        lcd.draw.text((30,110), str(sec), font = fonts.load('luBS24'))
        lcd.update()
        sleep(1)

        lcd.clear()
        if sec > 0:
            lcd.image.paste(bomb_image, (0, 0))
        else:
            lcd.image.paste(boom_image, (0, 0))
        lcd.update()
        sleep(1)

        sec -= 1
