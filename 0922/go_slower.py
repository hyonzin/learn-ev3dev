from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

us = UltrasonicSensor()
assert us.connected, "Connect a single US sonsor to any sensor port"
ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"

us.mode='US-DIST-CM'
units = us.units

MAX_SPEED = 1000
start_speed = 1000
multi_us_val = 3
e = 50 # (mm)

while not ts.value():
    cur_speed = min(MAX_SPEED,
                    start_speed,
                    max((us.value() - e) * multi_us_val, 0))
    # print(str(cur_speed) + " " + units)

    mL.run_forever(speed_sp = cur_speed)
    mR.run_forever(speed_sp = cur_speed)
