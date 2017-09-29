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

def turn(degree):
    degree = degree*0.95

    mL.run_forever(speed_sp= rotate_speed)
    mR.run_forever(speed_sp=-rotate_speed)

    start_angle = current_angle = gy.value()
    finish_angle = start_angle + degree;

    while (degree > 0 and current_angle < finish_angle) \
            or (degree < 0 and current_angle > finish_angle):
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

        if us.value() < 200:
            turn_right()
            go()
            turn_left()
            go()
            turn_left()
            go()
            turn_right()

        moved_distance += 1

while not ts.is_pressed:
    go(1)

mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
