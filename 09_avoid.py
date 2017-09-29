from ev3dev.ev3 import *
from math import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')
ts = TouchSensor()
gy = GyroSensor()
gy.mode = 'GYRO-ANG'
us = UltrasonicSensor()
us.mode='US-DIST-CM'

go_speed = 100
rotate_speed = 50

initial_angle = gy.value()
short_distance = 100

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

    while (angle > start_angle and angle > current_angle) \
            or (angle < start_angle and angle < current_angle):
        current_angle = gy.value()

def turn(angle):
    angle = angle*0.95

    mL.run_forever(speed_sp= rotate_speed)
    mR.run_forever(speed_sp=-rotate_speed)

    start_angle = current_angle = gy.value()
    finish_angle = start_angle + angle;

    while (angle > 0 and current_angle < finish_angle) \
            or (angle < 0 and current_angle > finish_angle):
        current_angle = gy.value()

    mL.stop(stop_action="hold")
    mR.stop(stop_action="hold")

def turn_right():
    turn(90)

def turn_left():
    turn(-90)

def go(distance = short_distance):
    moved_distance=0

    while moved_distance < distance:
        mL.run_forever(speed_sp=limit_speed(go_speed))
        mR.run_forever(speed_sp=limit_speed(go_speed))

        current_angle = gy.value()
        if us.value() < 200:
            turn_to(current_angle+90)
            go()
            turn_to(current_angle)
            go()
            turn_to(current_angle-90)
            go()
            turn_to(current_angle)

        moved_distance += 1

while not ts.is_pressed:
    go(1)

mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
