from hyonzin.ev3 import *

robot = Ev3()

initial_angle = robot.gy.value()
constant = 10
max_speed = 999
min_speed= -999

while not robot.ts.is_pressed:
    robot.mL.run_forever(speed_sp=min(max(100 - (robot.gy.value() - initial_angle) * constant, min_speed), max_speed))
    robot.mR.run_forever(speed_sp=min(max(100 + (robot.gy.value() - initial_angle) * constant, min_speed), max_speed))

robot.mL.stop(stop_action="hold")
robot.mR.stop(stop_action="hold")
