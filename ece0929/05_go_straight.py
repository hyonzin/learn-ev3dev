from hyonzin.ev3 import *

robot = Ev3()


initial_angle = robot.gy.value()
constant = 10

while not robot.ts.is_pressed:
    robot.mL.run_forever(speed_sp=100 + (robot.gy.value() - initial_angle) * constant)
    robot.mR.run_forever(speed_sp=100 + (robot.gy.value() - initial_angle) * constant)

robot.mL.stop(stop_action="hold")
robot.mR.stop(stop_action="hold")
