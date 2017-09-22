#!/usr/bin/env python3
from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

def go_straight():
    mL.run_to_rel_pos(position_sp=1200, speed_sp=450)
    mR.run_to_rel_pos(position_sp=1200, speed_sp=450)

def turn_right():
    mL.run_to_rel_pos(position_sp=160, speed_sp=450)
    mR.run_to_rel_pos(position_sp=-160, speed_sp=450)

def wait():
    mL.wait_while('running')
    mR.wait_while('running')

for i in range(0,4):
    go_straight()
    wait()
    turn_right()
    wait()
