from ev3dev.ev3 import *
from time import sleep

btn = Button()

def change(changed_buttons):
    print('These buttons changed state: ' + str(changed_buttons))

btn.on_change = change

while True:
    btn.process()
    sleep(0.01)
