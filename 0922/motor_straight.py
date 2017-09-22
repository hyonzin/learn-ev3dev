#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

mL = LargeMotor('outC')
mR = LargeMotor('outB')

mL.run_to_rel_pos(position_sp=720, speed_sp=450, stop_action="brake")
mR.run_to_rel_pos(position_sp=720, speed_sp=450, stop_action="brake")

mL.wait_while('running')
mR.wait_while('running')

sleep(1)

mL.run_to_rel_pos(position_sp=-720, speed_sp=450)
mR.run_to_rel_pos(position_sp=-720, speed_sp=450)

mL.wait_while('running')
mR.wait_while('running')

sleep(1)

mL.run_timed(time_sp=1000, speed_sp=450)
mR.run_timed(time_sp=1000, speed_sp=450)

mL.wait_while('running')
mR.wait_while('running')
