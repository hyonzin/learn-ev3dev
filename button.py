from ev3dev.ev3 import *
from time import sleep

btn = Button()

while True:
    if btn.any():
        print(btn.process())
        exit()
    else:
        sleep(0.01)
