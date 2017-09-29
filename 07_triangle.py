from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')
ts = TouchSensor()
gy = GyroSensor()
gy.mode = 'GYRO-ANG'

initial_angle = gy.value()
constant = 10
max_speed = 999
min_speed= -999
degree = 120
go_position = 1000
go_speed = 500
rotate_speed = 100
turn_count = 1

start_angle = current_angle = gy.value()

while not ts.is_pressed:
    # Go straight
    mL.run_to_rel_pos(position_sp=go_position, speed_sp=go_speed, stop_action='hold')
    mR.run_to_rel_pos(position_sp=go_position, speed_sp=go_speed, stop_action='hold')
    mL.wait_while('running')
    mR.wait_while('running')

    mL.run_forever(speed_sp= degree)
    mR.run_forever(speed_sp=-degree)

    # Turn
    finish_angle = start_angle + degree*turn_count;

    while (degree > 0 and current_angle < finish_angle) \
            or (degree < 0 and current_angle > finish_angle):
        current_angle = gy.value()
        #print(str(current_angle) + " " + gy.units)

    mL.stop(stop_action="hold")
    mR.stop(stop_action="hold")
    turn_count+=1
