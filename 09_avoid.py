from ev3dev.ev3 import *
from math import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')
ts = TouchSensor()
gy = GyroSensor()
gy.mode = 'GYRO-ANG'
us = UltrasonicSensor()
us.mode='US-DIST-CM'

constant = 10
max_speed = 999
min_speed= -999
degree = 90
go_position = 1000
go_speed = 100
rotate_speed = 100

initial_angle = gy.value()
moved_distance = 0
rotated_degree = 0
cosine_distance = 0

def limit_speed(speed):
    return min(max(speed, min_speed), max_speed)

while not ts.is_pressed:

    mL.run_forever(speed_sp=limit_speed(go_speed - (gy.value() - initial_angle) * constant))
    mR.run_forever(speed_sp=limit_speed(go_speed + (gy.value() - initial_angle) * constant))

    while us.value() < 20:
        mL.run_forever(speed_sp=limit_speed(rotate_speed))
        mR.run_forever(speed_sp=limit_speed(-rotate_speed))

    moved_distance += 1
    rotated_degree = gy.value() - initial_angle
    if rotated_degree > 0:
        cosine_distance += cos(rotated_degree)

    print("moved:"+str(moved_distance)+", cos:"+str(cosine_distance))

mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
