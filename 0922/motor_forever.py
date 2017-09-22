from ev3dev.ev3 import *
from time import sleep

m = LargeMotor('outB')

m.run_forever(speed_sp=100)
sleep(5)
m.stop(stop_action="coast")
sleep(2)

m.run_forever()
sleep(3)
m.stop()
sleep(2)
