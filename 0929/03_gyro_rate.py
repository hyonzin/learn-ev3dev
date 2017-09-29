#!/usr/bin/env python3

from hyonzin.ev3 import Ev3;

robot = Ev3()

while not robot.ts.is_pressed:
    robot.show_text(robot.gy.value())
