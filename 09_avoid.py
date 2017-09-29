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
rotate_speed = 100

initial_angle = gy.value()
moved_distance = 0
rotated_degree = 0
cosine_distance = 0

def limit_speed(speed):
    max_speed = 999
    min_speed= -999
    return min(max(speed, min_speed), max_speed)

while not ts.is_pressed:

    mL.run_forever(speed_sp=limit_speed(go_speed))
    mR.run_forever(speed_sp=limit_speed(go_speed))

    while us.value() < 200:
        mL.run_forever(speed_sp=limit_speed(rotate_speed))
        mR.run_forever(speed_sp=limit_speed(-rotate_speed))

    moved_distance += 1
    rotated_degree = gy.value() - initial_angle
    if rotated_degree > 0:
        cosine_distance += cos(rotated_degree)

    print("moved:"+str(moved_distance)+", cos:"+str(cosine_distance)+", us:"+str(us.value()))

mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
