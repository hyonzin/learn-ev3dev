#!/usr/bin/env python3

from hyonzin.ev3 import Ev3;

robot = Ev3()

initial_angle = robot.gy.value()

while not robot.ts.is_pressed:
    robot.show_text(robot.gy.value() - initial_angle)
