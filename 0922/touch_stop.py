#!/usr/bin/env python3
from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

ts = TouchSensor()

mL.run_forever()
mR.run_forever()

while True:
    if ts.value() == 1:
        mL.stop(stop_action="hold")
        mR.stop(stop_action="hold")
        break

