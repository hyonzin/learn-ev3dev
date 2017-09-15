from ev3dev.ev3 import *
from time import sleep

btn = Button()

while True:
    print(btn.buttons_pressed)
    if btn.check_buttons(buttons=['left', 'right']):
        exit()
    sleep(1)

