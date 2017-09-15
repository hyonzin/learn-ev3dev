from ev3dev.ev3 import *
from time import sleep
from PIL import Image

lcd = Screen()
bomb_image = Image.open('pics/Bomb.bmp')
boom_image = Image.open('pics/Boom.bmp')

sec = 10

while True:
    if sec >= 0:
        lcd.draw.text((40,120), str(sec))
        lcd.update()
        sleep(1)

        if sec > 0:
            lcd.image.paste(bomb_image, (0, 0))
        else:
            lcd.image.paste(boom_image, (0, 0))
        lcd.update()
        sleep(1)

        sec -= 1
