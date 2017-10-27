from ev3dev.ev3 import *
from time import sleep
from threading import Thread
ts = TouchSensor()

assert ts.connected, "connect touch sensor"

def playtone():
    global run
    while run:
        Sound.tone(1000, 200).wait()
        sleep(0.5)

global run
run = True

t = Thread(target=playtone)
t.start()

for i in range(5):
    while ts.value() == 0:
        sleep(0.01)
    while ts.value() == 1:
        sleep(0.01)

Sound.beep()
run = False
