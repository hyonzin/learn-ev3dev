from ev3dev.ev3 import *
from time import sleep
from threading import Thread
ts = TouchSensor()

assert ts.connected, "connect touch sensor"

def playtone():
    for j in range(10):
        Sound.tone(1000, 200).wait()
        sleep(0.5)

t = Thread(target=playtone)

t.start()

for i in range(5):
    while ts.value() == 0:
        sleep(0.01)
    while ts.value() == 1:
        sleep(0.01)

Sound.beep()
