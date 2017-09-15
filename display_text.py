from ev3dev.ev3 import *
from time import sleep

lcd = Screen()
lcd.draw.rectangle((0,0,177,40), fill='black')
lcd.draw.text((48,13), 'Hello, world.', fill='white')

my_string = 'This text is black'
print(lcd.draw.textsize(my_string))
lcd.draw.text((36,80), my_string)
lcd.update()
sleep(5000)
