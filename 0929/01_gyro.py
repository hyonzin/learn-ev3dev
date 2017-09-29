#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

gy = GyroSensor()
assert gy.connected, "Connect a single gyro sensor to any sensor port"
ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"

gy.mode = 'GYRO-ANG'

units = gy.units

while not ts.value():
    angle = gy.value()
    print(str(angle) + " " + units)
    Sound.tone(1000+angle*10, 1000).wait()
    sleep(0.5)

Sound.beep()
