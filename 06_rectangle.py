from hyonzin.ev3 import *

robot = Ev3()

initial_angle = robot.gy.value()
constant = 10
max_speed = 999
min_speed= -999

while not robot.ts.is_pressed:
    robot.go(position_sp=1000)
    robot.rotate(degree=90)
