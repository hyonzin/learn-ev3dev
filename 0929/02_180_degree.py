#!/usr/bin/env python3

from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

gy = GyroSensor()
assert gy.connected, "Connect a single gyro sensor to any sensor port"
ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"

gy.mode = 'GYRO-ANG'

units = gy.units

mL.run_forever(speed_sp=50)
mR.run_forever(speed_sp=-50)

start_angle = current_angle = gy.value()
finish_angle = start_angle + 180;

while current_angle < finish_angle:
    current_angle = gy.value()
    print(str(current_angle) + " " + units)

mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
