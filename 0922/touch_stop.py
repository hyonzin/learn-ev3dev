#!/usr/bin/env python3
from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

ts = TouchSensor()

mL.run_forever(speed_sp=1000)
mR.run_forever(speed_sp=1000)

while True:
    if ts.is_pressed:
        mL.stop(stop_action="hold")
        mR.stop(stop_action="hold")
        break

