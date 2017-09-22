#!/usr/bin/env python3
from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

mL.run_to_rel_pos(position_sp=2200, speed_sp=100, stop_action="hold")
mR.run_to_rel_pos(position_sp=2200, speed_sp=100, stop_action="hold")
