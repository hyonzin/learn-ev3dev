from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('outB')

m.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action='hold')

sleep(10)
