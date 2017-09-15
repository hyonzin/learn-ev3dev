from ev3dev.ev3 import *
from time import sleep
from PIL import Image
lcd = Screen()
logo = Image.open('pics/Bomb.bmp')
lcd.image.paste(logo, (0, 0))
lcd.update()
sleep(5)
