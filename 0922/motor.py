from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('outB')

m.run_to_rel_pos(position_sp=60, speed_sp=100, stop_action='hold')
sleep(1)

m.run_to_rel_pos(position_sp=60, speed_sp=100, stop_action='brake')
sleep(1)

m.run_to_rel_pos(position_sp=60, speed_sp=100, stop_action='coast')
sleep(1)


m.run_timed(time_sp=1000, speed_sp=-100)
print("set speed (speed_sp) = " + str(m.speed_sp))
print("actual speed = " + str(m.speed))
sleep(1)
print("actual speed = " + str(m.speed))
sleep(1)

m.run_timed(time_sp=1000, speed_sp=100)
print("set speed (speed_sp) = " + str(m.speed_sp))
print("actual speed = " + str(m.speed))
sleep(1)
print("actual speed = " + str(m.speed))
sleep(1)

m.run_timed(time_sp=3000, speed_sp=250, stop_action='brake')
Sound.beep()
m.wait_while('running')
Sound.beep()

170 380
