from ev3dev.ev3 import *
from math import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')
ts = TouchSensor()
gy = GyroSensor()
gy.mode = 'GYRO-ANG'
us = UltrasonicSensor()
us.mode='US-DIST-CM'

go_speed = 500
rotate_speed = 50

initial_angle = gy.value()
short_distance = 200

def limit_speed(speed):
    max_speed = 999
    min_speed= -999
    return min(max(speed, min_speed), max_speed)

def turn_to(angle):
    start_angle = current_angle = gy.value()

    if angle - current_angle > 0:
        mL.run_forever(speed_sp= rotate_speed)
        mR.run_forever(speed_sp=-rotate_speed)
    else:
        mL.run_forever(speed_sp=-rotate_speed)
        mR.run_forever(speed_sp= rotate_speed)

    while not ts.is_pressed \
            and ((angle > start_angle and angle > current_angle) \
            or   (angle < start_angle and angle < current_angle)):
        current_angle = gy.value()

def go(depth, distance=short_distance):
    moved_distance=0

    while not ts.is_pressed and moved_distance < distance:
        mL.run_forever(speed_sp=limit_speed(go_speed))
        mR.run_forever(speed_sp=limit_speed(go_speed))

        current_angle = gy.value()
        if us.value() < 400:
            turn_to(current_angle+90)

            go(depth=depth+1)
            turn_to(current_angle)
            go(depth=depth+1)
            turn_to(current_angle-90)
            go(depth=depth+1)
            turn_to(current_angle)

        moved_distance += 1

while not ts.is_pressed:
    go(depth=0, distance=1)

mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
